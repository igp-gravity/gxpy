"""
Geosoft grids.

.. note::

    Regression tests provide usage examples: `Tests <https://github.com/GeosoftInc/gxpy/blob/master/geosoft/gxpy/tests/test_grd.py>`_

"""
import os
import numpy as np
import math

import geosoft
import geosoft.gxapi as gxapi
from . import gx as gx
from . import coordinate_system as gxcs
from . import vv as gxvv
from . import utility as gxu

__version__ = geosoft.__version__

def _t(s):
    return geosoft.gxpy.system.translate(s)


class GRDException(Exception):
    """
    Exceptions from this module.

    .. versionadded:: 9.1
    """
    pass


def name_parts(name):
    """
    Return folder, undecorated file name + ext, file root, ext, decorations.

    If extension is not specified, ".grd" assumed

    For example:

    .. code::

        >>> import geosoft.gxpy.grd as gxgrd
        >>> namep = gxgrd.name_parts("f:/someFolder/name.grd(GRD;TYPE=SHORT)")
        >>> print(namep)
        ('f:/someFolder/','name.grd','name','.grd','(GRD;TYPE=SHORT)')

    .. versionadded:: 9.1
    """

    path = os.path.abspath(name)
    fn = os.path.dirname(path)
    root, ext = os.path.splitext(os.path.basename(path))

    if '(' in ext:
        ext, dec = ext.split('(')
        if ')' in dec:
            dec = dec.split(')')[0]
    else:
        dec = ''

    if not ext:
        if (not dec) or (dec[:3].upper() == 'GRD'):
            ext = '.grd.'
    name = root + ext

    return fn, name, root, ext, dec


def decorate_name(name, decorations=''):
    """
    Properly decorate a grid name.

    :param name:        file name
    :param decorations: file decorations, semicolon delimited
    :returns:           decorated file name

    .. versionadded:: 9.1
    """

    root, ext = os.path.splitext(name)
    dec = decorations.strip()
    if dec:
        d = decorations.lstrip('(')
        end = d.rfind(')')
        if end != -1:
            d = d[:end]
        ext = ext.split('(')[0]
        return root + ext + '(' + d + ')'
    else:
        if ext.lower() == '.grd':
            return root + ext + '(GRD)'
        else:
            return name


def delete_files(file_name):
    """
    Delete all files associates with this grid name.
    :param file_name:

    .. versionadded:: 9.2
    """

    def df(fn):
        try:
            os.remove(fn)
        except OSError as e:
            pass

    if file_name is not None:

        fn = name_parts(file_name)
        file_name = os.path.join(fn[0], fn[1])
        ext = fn[3]
        df(file_name)
        df(file_name + '.gi')
        df(file_name + '.xml')

        # remove shaded files associated with this grid
        file_s = os.path.join(fn[0], fn[1].replace('.', '_')) + '_s.grd'
        df(file_s)
        df(file_s + '.gi')
        df(file_s + '.xml')


        # hgd files
        if ext == '.hgd':
            for i in range(16):
                df(file_name + str(i))

# constants
FILE_READ = 0
FILE_READWRITE = 1     # file exists, but can change properties
FILE_NEW = 2

class GXgrd():
    """
    Grid and image class.

    Instance constructors:

        ======== =============================
        'open()' open an existing grid/image
        'new()'  create a new grid/image
        ======== =============================

    .. versionadded:: 9.1
    """

    gc = None
    _delete_files = False
    _file_name = None

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._close()

    def _close(self, pop=True):

        def df(fn):
            try:
                os.remove(fn)
            except OSError as e:
                pass

        if self._open:

            if self._delete_files:

                self._img = None
                delete_files(self._file_name)

            elif self._hgd:
                # an HGD memory grid was made, save it to an HGD file
                gxapi.GXHGD.h_create_img(self._img, decorate_name(self._file_name, 'HGD'))

            self._hpg = None
            self._img = None
            if pop:
                gx.pop_resource(self._open)
            self._open = None

    def __repr__(self):
        return "{}({})".format(self.__class__, self.__dict__)

    def __str__(self):
        if self._file_name is None:
            return '__memory__'
        else:
            return self.file_name_decorated

    def __init__(self, file_name=None, dtype=None, mode=None, kx=1, dim=None, overwrite=False):

        self._delete_files = False
        self._readonly = False
        self._hpg = None
        self._decoration = ''

        # When working with very large grids (gigabyte+), the
        # file system cannot always keep up with closing/caching and re-opening the
        # grid. Though this is actually a system problem, we deal with this problem by attempting
        # to open a grid three times before raising an error.

        # rebuild a clean file name
        self._hgd = False
        if (file_name is None) or (len(file_name.strip()) == 0):
            self._file_name = None
        else:
            path, file_name, root, ext, self._decoration = name_parts(file_name)
            self._file_name = os.path.join(path, file_name)

            if mode == FILE_NEW:
                # special case - HGD file, must work with a memory grid, save to HGD at end
                if ext.lower() == '.hgd':
                    self._hgd = True

        self._img = None
        if (self._file_name is None):
            self._img = gxapi.GXIMG.create(gxu.gx_dtype(dtype), kx, dim[0], dim[1])

        elif mode == FILE_NEW:
            if not overwrite:
                if os.path.isfile(self.file_name):
                    raise GRDException(_t('Cannot overwrite existing grid {}'.format(self.file_name)))
            if self._hgd:
                # for HGD grids, make a memory grid, which will be saved to an HGD on closing
                self._img = gxapi.GXIMG.create(gxu.gx_dtype(dtype), kx, dim[0], dim[1])
            else:
                self._img = gxapi.GXIMG.create_new_file(gxu.gx_dtype(dtype), kx, dim[0], dim[1], self.file_name_decorated)

        elif mode == FILE_READ:
            self._img = gxapi.GXIMG.create_file(gxu.gx_dtype(dtype), self.file_name_decorated, gxapi.IMG_FILE_READONLY)
            self._readonly = True

        else:
            self._img = gxapi.GXIMG.create_file(gxu.gx_dtype(dtype), self.file_name_decorated, gxapi.IMG_FILE_READORWRITE)

        self._open = gx.track_resource(self.__class__.__name__, self._file_name)

    @classmethod
    def open(cls, file_name, dtype=None, mode=None):
        """
        Open an existing grid file.

        :param file_name:    name of the grid file
        :param dtype:       numpy data type
        :param mode:        open mode:

            =================  ================================================
            FILE_READ          only read the file, properties cannot be changed
            FILE_READWRITE     grid stays the same, but properties may change
            =================  ================================================

        .. versionadded:: 9.1
        """

        if mode is None:
            mode = FILE_READ
        grd = cls(file_name, dtype=dtype, mode=mode)

        return grd

    @classmethod
    def new(cls, file_name=None, properties={}, overwrite=False):
        """
        Create a new grid file.

        :param file_name:   name of the grid file, None or '' for a memory grid
        :param properties:  dictionary of grid properties
        :param overwrite:   True to overwrite existing file

        .. versionadded:: 9.1
        """

        # set basic grid properties
        dtype = properties.get('dtype', None)
        nx = properties.get('nx', 0)
        ny = properties.get('ny', 0)
        if (nx <= 0) or (ny <= 0):
            raise GRDException(_t('Grid dimension ({},{}) must be > 0').format(nx, ny))

        grd = cls(file_name, dtype=dtype, mode=FILE_NEW, dim=(nx, ny), overwrite=overwrite)
        grd.set_properties(properties)

        return grd

    @classmethod
    def copy(cls, grd, file_name, dtype=None, overwrite=False):
        """
        Create a new GXgrd instance as a copy of an existing grid.

        :param grd:         grid instance to save as a new grid
        :param file_name:   name of the new grid (file with optional decorations)
        :param dtype:       numpy data type, None to use type of the parent grid
        :param overwrite:   True to overwrite if the file exists, False to no overwrite.

        .. versionadded:: 9.2
        """

        p = grd.properties()
        if dtype:
            p['dtype'] = dtype

        path0, base_file0, root0, ext0, dec0 = name_parts(grd.file_name_decorated)
        path1, base_file1, root1, ext1, dec1 = name_parts(file_name)
        if not ext1:
            ext1 = ext0
        if (ext1 == ext0) and not dec1:
            dec1 = dec0
        file_name = decorate_name(os.path.join(path1, root1) + ext1, dec1)

        copy = GXgrd.new(file_name, p, overwrite=overwrite)
        grd._img.copy(copy._img)

        return copy

    @classmethod
    def index_window(cls, grd, name=None, x0=0, y0=0, nx=None, ny=None, overwrite=False):
        """
        Create a windowed instance of a grid.
        
        :param grd:         gxpy.grd.GXgrd instance
        :param name:        name for the windowed_grid, default is constructed from input grid
        :param x0:          integer index of the first X point
        :param y0:          integer index of the first Y point
        :param nx:          number of points in x
        :param ny:          number of points in y
        :param overwrite:   True to overwrite existing file

        .. versionadded:: 9.2
        """

        gnx = grd.nx
        gny = grd.ny
        if nx is None:
            nx = gnx - x0
        if ny is None:
            ny = gny - y0
        mx = x0 + nx
        my = y0 + ny
        if ((x0 >= gnx) or (y0 >= gny) or
                (x0 < 0) or (y0 < 0) or
                (nx <= 0) or (ny <= 0) or
                (mx > gnx) or (my > gny)):
            raise GRDException(_t('Window x0,y0,mx,my({},{},{},{}) out of bounds ({},{})').format(x0, y0, mx, my, gnx, gny))

        if name is None:
            path, file_name, root, ext, dec = name_parts(grd.file_name_decorated)
            name = '{}_({},{})({},{}){}'.format(root, x0, y0, nx, ny, ext)
            name = decorate_name(name, dec)

        # create new grid
        p = grd.properties()
        p['nx'] = nx
        p['ny'] = ny
        if grd.rot == 0.0:
            p['x0'] = grd.x0 + grd.dx * x0
            p['y0'] = grd.y0 + grd.dy * y0
        else:
            dx = grd.dx * x0
            dy = grd.dy * y0
            cos = math.cos(math.radians(grd.rot))
            sin = math.sin(math.radians(grd.rot))
            p['x0'] = grd.x0 - dx * cos - dy * sin
            p['y0'] = grd.y0 - dy * cos + dx * sin

        wgd = cls.new(name, p, overwrite=True)
        wpg = wgd._geth_pg()
        wpg.copy_subset(grd._geth_pg(), 0, 0, y0, x0, ny, nx)

        return wgd

    @classmethod
    def from_data_array(cls, data, file_name, properties={}):
        """
        Create grid from a 2D numpy array.

        :param data:        2D numpy data array, must be 2D
        :param file_name:   name of the file
        :return:            GXgrd instance

        .. versionadded:: 9.1
        """

        ny, nx = data.shape
        properties['nx'] = nx
        properties['ny'] = ny
        properties['dtype'] = data.dtype
        grd = cls.new(file_name, properties=properties)
        grd.write_rows(data)
        return grd

    def delete_files(self, delete=True):
        """
        Delete the files associated with this grid when deleting the grid object.
        Note that files are not deleted until all references to this object are
        deleted and garbage collection is performed.

        :param delete: set to False to reverse a previous delete request

        .. versionadded:: 9.1
        """
        self._delete_files = delete

    def close(self):
        self._close()

    @property
    def dtype(self):
        """
        :return: numpy data type for the grid

        .. versionadded:: 9.2
        """
        return gxu.dtype_gx(self._img.e_type())

    @property
    def nx(self):
        """
        :return: grid x dimension

        .. versionadded:: 9.2
        """
        return self._img.nx()

    @property
    def ny(self):
        """
        :return: grid y dimension

        .. versionadded:: 9.2
        """
        return self._img.ny()

    @property
    def x0(self):
        """
        :return: grid origin x location

        .. versionadded:: 9.2
        """
        return self._img.query_double(gxapi.IMG_QUERY_rXO)

    @property
    def y0(self):
        """
        :return: grid origin y location

        .. versionadded:: 9.2
        """
        return self._img.query_double(gxapi.IMG_QUERY_rYO)

    @property
    def dx(self):
        """
        :return: separation between grid points in the grid x direction

        .. versionadded:: 9.2
        """
        return self._img.query_double(gxapi.IMG_QUERY_rDX)

    @property
    def dy(self):
        """
        :return: separation between grid points in the grid y direction

        .. versionadded:: 9.2
        """
        return self._img.query_double(gxapi.IMG_QUERY_rDY)

    @property
    def rot(self):
        """
        :return: grid rotation angle, degrees azimuth
        
        Note that grid rotations in the gxapi GXIMG are degrees clockwise, which is the opposite of
        degree azimuth, used here.  All horizontal plane anles in the Python gxpy module are degrees
        azimuth for consistency.

        .. versionadded:: 9.2
        """
        return -self._img.query_double(gxapi.IMG_QUERY_rROT)

    @property
    def file_name(self):
        """
        :return: grid file name without decorations

        .. versionadded:: 9.2
        """
        return self._file_name

    @property
    def file_name_decorated(self):
        """
        :return: grid file name with decorations

        .. versionadded:: 9.2
        """
        return decorate_name(self.file_name, self._decoration)


    @property
    def name(self):
        basename = os.path.basename(self.file_name)
        return os.path.splitext(basename)[0]


    @property
    def gridtype(self):
        """
        :return: grid type (ie. 'GRD" or 'HGD')

        .. versionadded:: 9.2
        """
        _, _, _, ext, dec = name_parts(self._file_name)
        if len(dec) > 0:
            return dec.split(';')[0]
        else:
            return ext[1:].upper()

    @property
    def decoration(self):
        """
        :return: grid descriptive decoration

        .. versionadded:: 9.2
        """
        return self._decoration

    @property
    def cs(self):
        """
        :return: grid coordinate system as a GXcs.

        .. versionadded:: 9.2
        """
        cs = gxcs.GXcs()
        self._img.get_ipj(cs.gxipj)
        return gxcs.GXcs(cs)

    def properties(self):
        """
        Get the grid properties dictionary

        :return: dictionary of all grid properties

        .. versionadded:: 9.1
        """

        properties = {}
        properties['nx'] = self.nx
        properties['ny'] = self.ny
        properties['x0'] = self.x0
        properties['y0'] = self.y0
        properties['dx'] = self.dx
        properties['dy'] = self.dy
        properties['rot'] = self.rot
        properties['dtype'] = self.dtype
        properties['file_name'] = self.file_name
        properties['gridtype'] = self.gridtype
        properties['decoration'] = self._decoration
        properties['cs'] = self.cs

        return properties

    @x0.setter
    def x0(self, v):
        self._img.set_info(self.dx, self.dy, v, self.y0, -self.rot)

    @y0.setter
    def y0(self, v):
        self._img.set_info(self.dx, self.dy, self.x0, v, -self.rot)

    @dx.setter
    def dx(self, v):
        self._img.set_info(v, self.dy, self.x0, self.y0, -self.rot)

    @dy.setter
    def dy(self, v):
        self._img.set_info(self.dx, v, self.x0, self.y0, -self.rot)

    @rot.setter
    def rot(self, v):
        self._img.set_info(self.dx, self.dy, self.x0, self.y0, -v)

    @cs.setter
    def cs(self, cs):
        if not isinstance(cs, gxcs.GXcs):
            cs = gxcs.GXcs(cs)
        self._img.set_ipj(cs.gxipj)

    def set_properties(self, properties):
        """
        Set grid properties from a properties dict.  Settable property keys are:

            ===== ============================================
            'x0'  grid X origin location (default 0.0)
            'y0'  grid Y origin location (0.0)
            'dx'  grid X point separation (1.0)
            'dy'  grid Y point separation (1.0)
            'rot' grid rotation angle in degrees azimuth (0.0)
            'cs'  coordinate system (unchanged)
            ===== ============================================

        Not all keys need be passed, though typically one will get the properties from
        the grid and modify those that need to change and pass the properties back.

        :param properties: properties dictionary

        .. versionadded:: 9.1
        """

        if self._readonly:
            raise GRDException(_t('{} opened as read-only, cannot set properties.').format(self.file_name_decorated))

        dx = properties.get('dx', 1.0)
        dy = properties.get('dy', dx)
        self._img.set_info(dx, dy,
                           properties.get('x0', 0.0),
                           properties.get('y0', 0.0),
                           -properties.get('rot', 0.0))
        cs = properties.get('cs', None)
        if cs is not None:
            if not isinstance(cs, gxcs.GXcs):
                cs = gxcs.GXcs(cs)
            self._img.set_ipj(cs.gxipj)

    def _geth_pg(self):
        """Get an hpg for the grid, adding the handle to the class so it does not get destroyed."""
        if self._hpg is None:
            self._hpg = self._img.geth_pg()
        return self._hpg

    def write_rows(self, data, ix0=0, iy0=0, order=1):
        """
        Write data to a grid by rows.

        :param data:    array of data to write
        :param ix0:     grid X index of first point
        :param iy0:     grid Y index of first point, top index if writing rows top to bottom
        :param order:   1: bottom to top; -1: top to bottom

        .. versionadded:: 9.1
        """

        ny, nx = data.shape
        iy = iy0
        dtype = self.dtype
        for i in range(ny):
            self._img.write_y(iy, ix0, 0, gxvv.GXvv(data[i, :], dtype=dtype)._vv)
            iy += order

    def read_rows(self, ix0=0, iy0=0):
        """

        :param ix0:
        :param iy0:
        :return:

        .. versionadded:: 9.1
        """

    @staticmethod
    def name_parts(name):
        """

        .. deprecated:: use name_parts()
        """
        return name_parts(name)

    @staticmethod
    def decorate_name(name, decorations=''):
        """

        .. deprecated:: ise name_parts()
        """
        return decorate_name(name, decorations)

    def indexWindow(self, name, x0=0, y0=0, nx=None, ny=None):
        """

         .. deprecated:: use index_window()
        """
        return self.index_window(name, x0, y0, nx, ny)

    def extent_2d(self):
        """
        Return the 2D extent of the grid on the grid plane
        :return: (min_x, min_y, max_x, max_y)

        .. versionadded:: 9.2
        """
        cosine = math.cos(math.radians(self.rot))
        sine = math.sin(math.radians(self.rot))
        width = (self.nx - 1) * self.dx
        height = (self.ny - 1) * self.dy
        xy0 = (self.x0, self.y0)
        xy1 = (self.x0 + width * cosine, self.y0 - width * sine)
        xy2 = (xy1[0] + height * sine, xy1[1] + height * cosine)
        xy3 = (self.x0 + height * sine, self.y0 + height * cosine)

        return min(xy0[0], xy1[0], xy2[0], xy3[0]),\
               min(xy0[1], xy1[1], xy2[1], xy3[1]),\
               max(xy0[0], xy1[0], xy2[0], xy3[0]),\
               max(xy0[1], xy1[1], xy2[1], xy3[1])

    def extent_3d(self):
        """
        Return the 3D extent of the grid in the base coordinate system.
        :return: ((min_x, min_y, min_z), (max_x, max_y, max_z))

        .. versionadded:: 9.2
        """

        ex2d = self.extent_2d()
        cs = self.cs
        xyz0 = cs.xyz_from_oriented((ex2d[0], ex2d[1], 0.0))
        xyz1 = cs.xyz_from_oriented((ex2d[2], ex2d[1], 0.0))
        xyz2 = cs.xyz_from_oriented((ex2d[2], ex2d[3], 0.0))
        xyz3 = cs.xyz_from_oriented((ex2d[0], ex2d[3], 0.0))

        return min(xyz0[0], xyz1[0], xyz2[0], xyz3[0]),\
               min(xyz0[1], xyz1[1], xyz2[1], xyz3[1]),\
               min(xyz0[2], xyz1[2], xyz2[2], xyz3[2]),\
               max(xyz0[0], xyz1[0], xyz2[0], xyz3[0]),\
               max(xyz0[1], xyz1[1], xyz2[1], xyz3[1]),\
               max(xyz0[2], xyz1[2], xyz2[2], xyz3[2])


# grid utilities
def array_locations(properties, z=0.):
    """
    Create an array of (x,y,z) points for a grid defined by properties
    :param properties:  grid properties
    :return:            array of points, shaped (ny, nx, 3)

    .. versionadded:: 9.1
    """

    nx = properties.get('nx')
    ny = properties.get('ny')
    dx = properties.get('dx')
    dy = properties.get('dy', dx)
    offset = np.array([properties.get('x0', 0.), properties.get('y0', 0.), z])
    loc = np.zeros((ny, nx, 3))
    loc[:, :, 0:2] = np.mgrid[0: (nx - 0.5) * dx: dx, 0: (ny - 0.5) * dy: dy].swapaxes(0, 2)

    return loc + offset


def gridMosaic(mosaic, gridList, typeDecoration='', report=None):
    """
    Combine a set of grids into a single grid.  Raises an error if the resulting grid is too large.

    :param mosaic:          name of the output grid, returned.  Decorate with '(HGD)' to get an HGD
    :param gridList:        list of input grid names
    :param typeDecoration:  decoration for input grids if not default
    :param report:          string reporting function, report=print to print progress
    :return:                GXgrd instance, must be closed with a call to close().

    .. versionadded:: 9.1
    """

    def props(gn, repro=None):
        with GXgrd.open(gn) as g:
            if repro:
                g._img.create_projected2(repro[0], repro[1])
            p = g.properties()
            return p

    def dimension(glist):

        def dimg(g, repro=None):
            p = props(g, repro)
            x0 = p.get('x0')
            y0 = p.get('y0')
            xM = x0 + (p.get('nx') - 1) * p.get('dx')
            yM = y0 + (p.get('ny') - 1) * p.get('dy')
            ipj = p.get('cs').gxipj
            cell = p.get('dx')
            return x0, y0, xM, yM, (ipj, cell)

        def ndim(x0, xM, dX):
            return int((xM - x0 + dX / 2.0) / dX) + 1

        x0, y0, xM, yM, repro = dimg(glist[0])
        for g in glist[1:]:
            xx0, yy0, xxM, yyM, r = dimg(g, repro)
            if xx0 < x0:
                x0 = xx0
            if yy0 < y0:
                y0 = yy0
            if xxM > xM:
                xM = xxM
            if yyM > yM:
                yM = yyM

        # calculate new grid dimension
        p = props(glist[0])
        nX = ndim(x0, xM, p.get('dx'))
        nY = ndim(y0, yM, p.get('dy'))

        return x0, y0, nX, nY, xM, yM

    def locate(x0, y0, p):

        dx = p.get('dx')
        dy = p.get('dy')
        dsx = round((p.get('x0') - x0) / dx)
        dsy = round((p.get('y0') - y0) / dy)

        return dsx, dsy

    def paste(gn, mpg):
        with GXgrd.open(gn) as g:
            p = g.properties()
            nX = p.get('nx')
            nY = p.get('ny')
            gpg = g._geth_pg()
            destx, desty = locate(x0, y0, p)
            if report:
                report('    +{} nx,ny({},{})'.format(g, nX, nY))
                report('     Copy ({},{}) -> ({},{}) of ({},{})'.format(nX, nY, destx, desty, mnx, mny))
            mpg.copy_subset(gpg, desty, destx, 0, 0, nY, nX)
            return

    if len(gridList) == 0:
        raise GRDException(_t('At least one grid is required'))

    # create list of grids, all matching on coordinate system of first grid
    grids = []
    for i in range(len(gridList)):
        grids.append(decorate_name(gridList[i], typeDecoration))

    # output grid
    x0, y0, nX, nY, xm, ym = dimension(grids)
    p = props(grids[0])
    p['x0'] = x0
    p['y0'] = y0
    p['nx'] = nX
    p['ny'] = nY
    if report is not None:
        report('')
        report('Mosaic: dim({},{}) x({},{}) y({},{}), cell({})...'.format(nX, nY, x0, xm, y0, ym, p.get('dx')))
    master = GXgrd.new(mosaic, p)
    if report:
        report('Memory image ready ({}) dim({},{}) x0,y0({},{})'.format(master, master.nx, master.ny,
                                                                        master.x0, master.y0))

    # paste grids onto master
    mnx = master.nx
    mny = master.ny
    mpg = master._geth_pg()
    for g in grids:
        paste(g, mpg)

    if report:
        report('Mosaic completed: {}'.format(mosaic))

    return master


def gridBool(g1, g2, joinedGrid, opt=1, size=3, olap=1):
    """

    :param g1,g2:   GXgrd of grids to merge
    :param new:     new output grid, overwritten if it exists
    :param opt:     logic to use on overlap points, default 1 (OR):

        === ============================================
        0   AND, both grids must have valid value
        1   OR, either grid has a valid value
        2   XOR, same as OR, except overlap is dummied
        === ============================================

    :param size:    size of the output grid, default is minimum size

        === ==========================================
        0   minimum size - dummy regions clipped
        1   size to grid 1
        2   size to grid 2
        3   size to maximum including both grids
        === ==========================================

    :param olap:    what to do with overlapping valid points, default uses grid 1

        === ==========================================
        0   average points
        1   use grid 1
        2   use grid 2
        === ==========================================

    :returns:       GXgrd instance of the merged output grid, must be closed with a call to close().

    .. versionadded:: 9.1
    """

    close_g1 = close_g2 = False
    if isinstance(g1, str):
        g1 = GXgrd.open(g1)
        close_g1 = True
    if isinstance(g2, str):
        g2 = GXgrd.open(g2)
        close_g2 = True

    gxapi.GXIMU.grid_bool(g1._img, g2._img, joinedGrid, opt, size, olap)

    if close_g1:
        g1.close()
    if close_g2:
        g2.close()

    return GXgrd.open(joinedGrid)
