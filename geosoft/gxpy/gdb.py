"""
Geosoft databases for line-oriented spatial data.

:Classes:

    ==================== =========================
    :class:`Geosoft_gdb` Geosoft line database
    :class:`Line`        line handling
    :class:`Channel`     channel handling
    ==================== =========================

.. seealso:: :mod:`geosoft.gxapi.GXGB`, :mod:`geosoft.gxapi.GXEDB`, 
             :mod:`geosoft.gxapi.GXDBREAD`, :mod:`geosoft.gxapi.GXDBWRITE`

.. note::

    Regression tests provide usage examples: `Tests <https://github.com/GeosoftInc/gxpy/blob/master/geosoft/gxpy/tests/test_gdb.py>`_

"""
from enum import Enum
import os
import sys
import math
import numpy as np

import geosoft
import geosoft.gxapi as gxapi
from . import vv as gxvv
from . import va as gxva
from . import utility as gxu
from . import gx as gx
from . import coordinate_system as gxcs
from . import metadata as gxmeta
from . import map as gxmap
from . import view as gxview

__version__ = geosoft.__version__

def _t(s):
    return geosoft.gxpy.system.translate(s)

# Constants

LINE_TYPE_NORMAL = gxapi.DB_LINE_TYPE_NORMAL #:
LINE_TYPE_BASE = gxapi.DB_LINE_TYPE_BASE #:
LINE_TYPE_TIE = gxapi.DB_LINE_TYPE_TIE #:
LINE_TYPE_TEST = gxapi.DB_LINE_TYPE_TEST #:
LINE_TYPE_TREND = gxapi.DB_LINE_TYPE_TREND  #:
LINE_TYPE_SPECIAL = gxapi.DB_LINE_TYPE_SPECIAL  #:
LINE_TYPE_RANDOM = gxapi.DB_LINE_TYPE_RANDOM  #:

LINE_CATEGORY_FLIGHT = gxapi.DB_CATEGORY_LINE_FLIGHT #:
LINE_CATEGORY_GROUP = gxapi.DB_CATEGORY_LINE_GROUP #:
LINE_CATEGORY_NORMAL = gxapi.DB_CATEGORY_LINE_NORMAL #:

FORMAT_NORMAL = gxapi.DB_CHAN_FORMAT_NORMAL #:
FORMAT_EXP = gxapi.DB_CHAN_FORMAT_EXP #:
FORMAT_TIME = gxapi.DB_CHAN_FORMAT_TIME #:
FORMAT_DATE = gxapi.DB_CHAN_FORMAT_DATE #:
FORMAT_GEOGR = gxapi.DB_CHAN_FORMAT_GEOGR #:
FORMAT_SIGDIG = gxapi.DB_CHAN_FORMAT_SIGDIG #:
FORMAT_HEX = gxapi.DB_CHAN_FORMAT_HEX #:

CHAN_ALL = None     #:
CHAN_NORMAL = 0     #:
CHAN_ARRAY = 1      #:
CHAN_DISPLAYED = 2  #:

SYMB_LINE_NORMAL = gxapi.DB_CATEGORY_LINE_NORMAL #:
SYMB_LINE_FLIGHT = gxapi.DB_CATEGORY_LINE_FLIGHT #:
SYMB_LINE_GROUP = gxapi.DB_CATEGORY_LINE_GROUP #:

SELECT_INCLUDE = gxapi.DB_LINE_SELECT_INCLUDE #:
SELECT_EXCLUDE = gxapi.DB_LINE_SELECT_EXCLUDE #:

COMP_NONE = gxapi.DB_COMP_NONE #:
COMP_SPEED = gxapi.DB_COMP_SPEED #:
COMP_SIZE = gxapi.DB_COMP_SIZE #:

READ_REMOVE_DUMMYROWS = 1 #:
READ_REMOVE_DUMMYCOLUMNS = 2 #:

SYMBOL_LOCK_NONE = gxapi.DB_LOCK_NONE #:
SYMBOL_LOCK_READ = gxapi.DB_LOCK_READONLY #:
SYMBOL_LOCK_WRITE = gxapi.DB_LOCK_READWRITE #:

DRAW_AS_POINTS = 0 #:
DRAW_AS_LINES = 1 #:

class GdbException(Exception):
    """
    Exceptions from :mod:`geosoft.gxpy.gdb`.

    .. versionadded:: 9.1
    """
    pass

def _gdb_name(name):
    name = name.strip()
    nameExt = os.path.splitext(name)
    if nameExt[1].lower() == '.gdb':
        return name
    else:
        return os.path.normpath(name + ".gdb")


def _va_width(data):
    if len(data.shape) == 1:
        width = 1
    elif len(data.shape) == 2:
        width = data.shape[1]
    else:
        raise GdbException(_t("Only one or two-dimensional data allowed."))
    return width

def is_valid_line_name(name):
    """
    Return True if this is a valid line name.

    See also :func:`create_line_name`

    .. versionadded:: 9.3
    """
    name = str(name)
    try:
        int(name)
        return False
    except ValueError:
        return bool(gxapi.GXDB.is_line_name(name))

def create_line_name(number=0, type=LINE_TYPE_NORMAL, version=0):
    """
    Returns a valid database line name constructed from the component parts.

    :param number:  line number, or a string, default is 0
    :param type:    one of LINE_TYPE constants, default is LINE_TYPE_NORMAL
    :param version: version number, default is 0

    :return:        string line name

    Line name strings are constructed using the line naming convention as in the following:

        ====== =======================================
        L10.4  LINE_TYPE_NORMAL, number 10, version 4
        B10.4  LINE_TYPE_BASE, number 10, version 4
        D10.4  LINE_TYPE_RANDOM, number 10, version 4
        P10.4  LINE_TYPE_SPECIAL, number 10, version 4
        T10.4  LINE_TYPE_TIE, number 10, version 4
        S10.4  LINE_TYPE_TEST, number 10, version 4
        R10.4  LINE_TYPE_TREND, number 10, version 4
        ====== =======================================

    .. versionadded:: 9.3
    """
    sr = gxapi.str_ref()
    gxapi.GXDB.set_line_name2(str(number), type, version, sr)
    return sr.value

def delete_files(file_name):
    """
    Delete all files associates with this database name.

    :param file_name:   name of the database

    .. versionadded:: 9.3
    """

    def df(fn):
        try:
            os.remove(fn)
        except OSError as e:
            pass

    if file_name is not None:

        path = _gdb_name(file_name)
        fn = os.path.dirname(path)
        root, ext = os.path.splitext(os.path.basename(path))

        if ext.lower() != '.gdb':
            raise GdbException(_t('File is not a Geosoft database file (no gdb extension): {}'.format(file_name)))

        df(file_name)
        df(file_name + '.xml')


class Geosoft_gdb:
    """
    Class to work with Geosoft databases. This class wraps many of the functions found in 
    :class:`geosoft.gxapi.GXDB`.

    :Constructors:
     
        =============== =========================================================================
        :meth:`open`    open an existing file, or if not specified open/lock the current database
        :meth:`new`     create a new database
        =============== =========================================================================

    **Some typical programming patterns**

    Python Oasis extension opens and reads through all data in the current database:

    .. code::

        import os,sys
        import numpy as np
        import gxpy.gx as gxp
        import gxpy.gdb as gxdb

        # open the current database in the open project
        gdb = gxdb.Geosoft_gdb.open()
        for line in gdb.list_lines():

            npd,ch,fid = gdb.read_line(line)
            # npd is a 2D numpy array to all data in this line.
            # ch is a list of the channels, one channel for each column in npd.
            # Array channels are expanded with channel names "name[0]", "name[1]" ...
            # fid is a tuple (start,increment) fiducial, which will be the minimum start and smallest increment.

            # ... do something with the data in npd ...

    External Python program to open and read through all data in a database:

    .. code::

        import os,sys
        import numpy as np
        import gxpy.gx as gx
        import gxpy.gdb as gxdb

        # initalize the gx environment - required for external programs.
        gxp = gx.GXpy()
    
        # open a database
        gdb = gxdb.Geosoft_gdb.open('test.gdb')
        for line in gdb.list_lines():

            npd,ch,fid = gdb.read_line(line)
            # npd is a 2D numpy array to all data in this line.
            # ch is a list of the channels, one channel for each column in npd.
            # Array channels are expanded with channel names "name[0]", "name[1]" ...
            # fid is a tuple (start,increment) fiducial, which will be the minimum start and smallest increment.

            # ... do something with the data in npd ...

    The following creates a new channel that is the distance from the origin to the X,Y,Z location of every point.

    .. code::

        ...
        gdb = gxdb.Geosoft_gdb.open('test.gdb')
        for line in gdb.list_lines():

            npd,ch,fid = gdb.read_line(line, channels=['X','Y','Z'])

            npd = np.square(npd)
            distance_from_origin = np.sqrt(npd[0] + npd[1] + npd[2])

            gdb.write_channel(line, 'distance', distance_from_origin, fid)

    .. versionadded:: 9.1

    .. versionchanged:: 9.3 float numpy arrays use np.nan for dummies so dummy filtering no longer necessary.

    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.__del__()

    def __del__(self):
        if hasattr(self, '_close'):
            self._close()

    def _close(self, pop=True):
        if hasattr(self, '_open'):
            if self._open:
                if self._db:
                    if self._edb is not None:
                        if self._edb.is_locked():
                            self._edb.un_lock()
                        self._edb = None

                    if self._xmlmetadata_changed:
                        with open(self._file_name + '.xml', 'w+') as f:
                            f.write(gxu.xml_from_dict(self._xmlmetadata))
                        self._db.sync()

                    self._db = None

                self._file_name = None
                if pop:
                    gx.pop_resource(self._open)
                self._open = None


    def __repr__(self):
        return "{}({})".format(self.__class__, self.__dict__)

    def __str__(self):
        return os.path.basename(self._file_name)

    def __init__(self):
        self._lst = gxapi.GXLST.create(2000)
        self._sr = gxapi.str_ref()
        self._file_name = None
        self._db = None
        self._edb = None
        self._xmlmetadata = None
        self._xmlmetadata_changed = False
        self._xmlmetadata_root = ''

        self._open = gx.track_resource(self.__class__.__name__, self._file_name)


    @classmethod
    def open(cls, name=None):
        """
        Open an existing database.

        :param name:    name of the database, default is the current project database
        :returns:       :class:`Geosoft_gdb` instance

        .. versionadded:: 9.1
        """

        gdb = cls()

        if name is None:
            gdb._edb = gxapi.GXEDB.current()
            gdb._db = gxapi.GXEDB.lock(gdb._edb)
        else:
            gdb._edb = None
            gdb._db = gxapi.GXDB.open(_gdb_name(name), 'SUPER', '')

        gxapi.GXDB.get_name(gdb._db, gxapi.DB_NAME_FILE, gdb._sr)
        gdb._file_name = os.path.normpath(gdb._sr.value)

        return gdb

    @classmethod
    def new(cls, name, maxLines=500, maxChannels=200, maxBlobs=0, pageSize=1024,
            comp=None, overwrite=False):
        """
        Create a new database.

        :param name:        database name
        :param maxLines:    maximum number of lines, default 500
        :param maxChannels: maximum number of channels, default 200
        :param maxBlobs:    maximum number of blobs, default lines*channels+20
        :param comp:        compression:

                            | COMP_NONE
                            | COMP_SPEED (default)
                            | COMP_SIZE
        :param overwrite:   `True` to overwrite existing database. Default is `False`, GdbException if file exists.
        :param pageSize:    page size (default is 1024), which limits the amount of compressed data that can be stored
                            in a single channel on a line. The maximum compressed data size for a channel will be this
                            number * 65534 (default 1024 * 65534 = 64 MB of compressed data). This will be forced to
                            a power of 2 between 64 and 4096, which would allow for a maximum of 256 MB compressed
                            data per channel per line.
                            
        :returns:           :class:`Geosoft_gdb` instance

        .. versionadded:: 9.1

        .. versionchanged:: 9.3
            added parameter `overwrite=False`
        """
        maxLines = max(10, maxLines)
        maxChannels = max(25, maxChannels)
        minBlobs = maxChannels * maxLines + 20
        maxBlobs = max(minBlobs, maxBlobs)
        if not comp:
            comp = COMP_SPEED

        # validate pageSize:
        ps = 64
        while ps < pageSize:
            ps *= 2
            if ps > 4096:
                raise GdbException(_t('Page size cannot be larger than 4096 (256 MB per line-channel).'))
        pageSize = ps

        name = _gdb_name(name)

        if not overwrite and os.path.isfile(name):
            raise GdbException(_t('Cannot overwrite existing database \'{}\''.format(name)))

        gxapi.GXDB.create_comp(name,
                               maxLines, maxChannels, maxBlobs, 10, 100,
                               'SUPER', '',
                               pageSize, comp)
        return cls.open(name)

    def commit(self):
        """
        Commit database changes.

        .. versionadded:: 9.1
        """
        self._db.commit()

    def discard(self):
        """
        Discard database changes.

        .. versionadded:: 9.1
        """
        self._db.discard()

    # ============================================================================
    # internal helper functions

    def _exist_symb(self, symb, symb_type):
        """
        Check if a symbol exists of the required type.
        
        :param symb:        symbol name, number or instance
        :param symb_type:   one of DB_SYMB_TYPE
        :returns:           `True` if the symbol exists and is the expected symbol type, `False` otherwise

        .. versionadded:: 9.1
        """

        if isinstance(symb, str):
            return self._db.exist_symb(symb, symb_type)
        elif isinstance(symb, int):
            return self._db.valid_symb(symb, symb_type)
        elif isinstance(symb, Line) and (symb_type == gxapi.DB_SYMB_LINE):
            return True
        elif isinstance(symb, Channel) and (symb_type == gxapi.DB_SYMB_CHAN):
            return True
        return False

    # ============================================================================
    # Information

    @property
    def gxdb(self):
        """The :class:`geosoft.gxapi.GXDB` instance handle"""
        return self._db

    @property
    def xyz_channels(self):
        """
        The currently identified (x, y, z) channels.  Methods that work on spatial locations will use these
        channels for locating the data at each fiducial of the data.  Can be set using a tuple of two or
        three strings.  For example:
        
        .. code::
        
            gdb.xyz_channels = ('Easting', 'Northing')
            gdb.xyz_channels = ('Easting', 'Northing', 'Elevation')
            
        .. versionadded:: 9.2
        """
        sr = gxapi.str_ref()
        self.gxdb.get_xyz_chan(0, sr)
        x = sr.value
        self.gxdb.get_xyz_chan(1, sr)
        y = sr.value
        self.gxdb.get_xyz_chan(2, sr)
        z = sr.value
        if not self.is_channel(x):
            x = None
        if not self.is_channel(y):
            y = None
        if not self.is_channel(z):
            z = None
        return (x, y, z)

    @xyz_channels.setter
    def xyz_channels(self, xyz):

        if len(xyz) >= 3:
            x, y, z = xyz
            self.is_channel(z, True)
        else:
            x, y = xyz
            z = None
            self.is_channel(x, True)
            self.is_channel(y, True)

        self.gxdb.set_xyz_chan(0, x)
        self.gxdb.set_xyz_chan(1, y)
        if z:
            self.gxdb.set_xyz_chan(2, z)

    def _init_xmlmetadata(self):
        if not self._xmlmetadata:
            self._xmlmetadata = gxu.geosoft_metadata(self._file_name)
        self._xmlmetadata_root = tuple(self._xmlmetadata.items())[0][0]

    @property
    def metadata(self):
        """
        Return the database XML metadata as a dictionary.  Can be set, in which case
        the dictionary items passed will be added to, or replace existing XML metadata.

        .. versionadded:: 9.2
        """
        self._init_xmlmetadata()
        return self._xmlmetadata[self._xmlmetadata_root]

    @metadata.setter
    def metadata(self, meta):
        self._init_xmlmetadata()
        self._xmlmetadata[self._xmlmetadata_root] = gxu.merge_dict(self._xmlmetadata[self._xmlmetadata_root], meta)
        self._xmlmetadata_changed = True

    def get_gx_metadata(self):
        """
        Return the database Geosoft metadata as a Geosoft :class:`geosoft.gxpy.metadata.Metadata` instance.

        The internal database metadata is used to store various database properties that are not intended
        to be part of the exposed dataset metadata exposed by the :attr:metadata property.

        If you wish to add your own metadata to the internal properties you can use the
        :mod:geosoft.gxpy.metadata module to add metadata and save it to the database using
        :func:geosoft.gxapi.GXDB.set_meta.

        .. versionadded:: 9.3
        """
        gxm = gxapi.GXMETA.create()
        self.gxdb.get_meta(gxm)
        return gxmeta.Metadata(gxm)

    def update_gxmeta(self, meta, replace=False):
        """
        Update the database Geosoft metadata as a Geosoft :class:`geosoft.gxpy.metadata.Metadata` instance.

        :param meta:    the new metadata as a :class:`geosoft.gxpy.Metadata` instance
        :param relace:  True to replace all database metadata.


        .. versionadded:: 9.3
        """
        gxm = gxapi.GXMETA.create()
        self.gxdb.get_meta(gxm)
        return gxmeta.Metadata(gxm)

    @property
    def file_name(self):
        """Database file name."""
        return os.path.abspath(self._file_name)

    @property
    def coordinate_system(self):
        """
        Coordinate system of the current :meth:`xyz_channels`.
        Can be set from any :class:`geosoft.gxpy.coordinate_system.Coordinate_system` constructor.

        .. versionchanged:: 9.3
            added setter
        """
        try:
            x, y, z = self.xyz_channels
            ipj = gxapi.GXIPJ.create()
            self.gxdb.get_ipj(self.channel_name_symb(x)[1], ipj)
            return gxcs.Coordinate_system(ipj)

        except GdbException:
            return gxcs.Coordinate_system()

    @coordinate_system.setter
    def coordinate_system(self, cs):
        if not isinstance(cs, gxcs.Coordinate_system):
            cs = gxcs.Coordinate_system(cs)
        x, y, z = self.xyz_channels
        self.gxdb.set_ipj(self.channel_name_symb(x)[1], self.channel_name_symb(y)[1], cs.gxipj)
        x, _, z = self.xyz_channels
        if z:
            z = Channel(self, z)
            if not z.unit_of_measure:
                z.unit_of_measure = Channel(self, x).unit_of_measure

    @property
    def max_blobs(self):
        """maximum blobs allowed"""
        return self._db.get_info(gxapi.DB_INFO_BLOBS_MAX)

    @property
    def max_lines(self):
        """maximum number of lines allowed"""
        return self._db.get_info(gxapi.DB_INFO_LINES_MAX)

    @property
    def max_channels(self):
        """maximum number of channels allowed"""
        return self._db.get_info(gxapi.DB_INFO_CHANS_MAX)

    @property
    def used_blobs(self):
        """number of blobs used"""
        return self._db.get_info(gxapi.DB_INFO_BLOBS_USED)

    @property
    def used_lines(self):
        """number of lines used"""
        return self._db.get_info(gxapi.DB_INFO_LINES_USED)

    @property
    def used_channels(self):
        """number of channels used"""
        return self._db.get_info(gxapi.DB_INFO_CHANS_USED)

    @property
    def max_compressed_channel_bytes(self):
        """maximum compressed data per channel per line in bytes"""
        ps = self._db.get_info(gxapi.DB_INFO_PAGE_SIZE)
        return  ps * 65534

    @property
    def number_of_blocks(self):
        """number of blocks"""
        return self._db.get_info(gxapi.DB_INFO_DATA_SIZE)

    @property
    def lost_blocks(self):
        """lost blocks that might be freed"""
        return self._db.get_info(gxapi.DB_INFO_LOST_SIZE)

    @property
    def free_blocks(self):
        """number of free blocks"""
        return self._db.get_info(gxapi.DB_INFO_FREE_SIZE)

    @property
    def compression(self):
        """database compression setting"""
        return self._db.get_info(gxapi.DB_INFO_COMP_LEVEL)

    @property
    def pages_for_blobs(self):
        """pages consumed by blobs"""
        try:
            return self._db.get_info(gxapi.DB_INFO_BLOB_SIZE)
        except gxapi.GXError:
            return 0

    @property
    def db_size_kb(self):
        """database size in kb"""
        return self._db.get_info(gxapi.DB_INFO_FILE_SIZE)

    @property
    def index_size_kb(self):
        """index size in kb"""
        return self._db.get_info(gxapi.DB_INFO_INDEX_SIZE)

    @property
    def max_block_size_bytes(self):
        """maximum block size in bytes"""
        return self._db.get_info(gxapi.DB_INFO_MAX_BLOCK_SIZE)

    @property
    def data_has_changed(self):
        """`True` if data has changed"""
        return self._db.get_info(gxapi.DB_INFO_CHANGESLOST)

    def is_line(self, line, raise_err=False):
        """
        Returns `True` if the named line exists in the database.

        :param line: line name
        :param raise_err: True to raise an error if it does not exist

        .. versionadded:: 9.1
        """

        exist = self._db.find_symb(str(line), gxapi.DB_SYMB_LINE) != gxapi.NULLSYMB
        if raise_err and not exist:
            raise GdbException(_t('"{}" is not a line in the database'.format(line)))
        return exist

    def is_channel(self, chan, raise_err=False):
        """
        Returns `True` if the channel name exists in the database.

        :param chan: channel name
        :param raise_err: True to raise an error if it does not exist

        .. versionadded:: 9.1
        """
        exist = self._db.find_chan(chan) != gxapi.NULLSYMB
        if raise_err and not exist:
            raise GdbException(_t('"{}" is not a channel in the database'.format(chan)))
        return exist

    def extent_xyz(self):
        """ 
        Return the spatial extent of all selected data in the database.
        
        :returns:   (xmin, ymin, zmin, xmax, ymax, zmax)
        
        .. versionadded:: 9.2
        """

        def expand(_min, _max, data):
            if np.isnan(data).all():
                return _min, _max
            mdata = np.nanmin(data)
            if _min is None:
                _min = mdata
                _max = np.nanmax(data)
                return _min, _max
            if mdata < _min:
                _min = mdata
                return _min, _max
            mdata = np.nanmax(data)
            if mdata > _max:
                _max = mdata
            return _min, _max

        xmin = xmax = ymin = ymax = zmin = zmax = None
        lines = self.lines()
        if len(lines):
            xyz = self.xyz_channels
            if None in xyz:
                if None in xyz[0:2]:
                    return (xmin, ymin, zmin, xmax, ymax, zmax)
                xyz = xyz[0:2]

            for l in lines:
                data = self.read_line(l, channels=xyz)[0]
                xmin, xmax = expand(xmin, xmax, data[:, 0])
                ymin, ymax = expand(ymin, ymax, data[:, 1])
                if data.shape[1] > 2:
                    zmin, zmax = expand(zmin, zmax, data[:, 2])

        return (xmin, ymin, zmin, xmax, ymax, zmax)

    def _get(self, s, fn):
        self._lock_read(s)
        try:
            v = fn(s)
        finally:
            self._unlock(s)
        return v


    def _set(self, s, fn, v):
        self._lock_write(s)
        try:
            fn(s, v)
        finally:
            self._unlock(s)

    def line_name_symb(self, line, create=False):
        """
        Return line name, symbol

        :param line:    line name, or symbol number
        :param create:  `True` to create a line if one does not exist
        :returns:       line name, symbol
        :raises:        GdbException if line not found or cannot be created

        .. versionadded:: 9.1
        """

        if isinstance(line, Line):
            return line.name, line.symbol

        elif isinstance(line, str):
            if (self._exist_symb(line, gxapi.DB_SYMB_LINE)):
                symb = self._db.find_symb(line, gxapi.DB_SYMB_LINE)
                return line, symb
            if create:
                return line, self.new_line(line)
            else:
                raise GdbException(_t('Line \'{}\' not found'.format(line)))
        else:
            self._db.get_symb_name(line, self._sr)
            return self._sr.value, line



    def channel_name_symb(self, chan):
        """
        Return channel name, symbol

        :param chan:    channel name, or symbol number or Channel instance
        :returns:       line name, symbol, returns ('',-1) if invalid
        :raises:        GdbException if channel does not exist

        .. versionadded:: 9.1
        """

        if isinstance(chan, Channel):
            return chan.name, chan.symbol
        if isinstance(chan, str):
            symb = self._db.find_symb(chan, gxapi.DB_SYMB_CHAN)
            if symb == -1:
                raise GdbException(_t('Channel \'{}\' not found'.format(chan)))
            return chan, symb

        if not self._exist_symb(chan, gxapi.DB_SYMB_CHAN):
            raise GdbException(_t('Channel symbol \'{}\' not found'.format(chan)))
        self._db.get_symb_name(chan, self._sr)
        return self._sr.value, chan

    def channel_width(self, channel):
        """
        Channel array width, 1 for normal channels, >1 for VA channels.

        :param channel: channel symbol or name
        :returns:       array dimension, 1 for non-array channels

        .. versionadded:: 9.1
        """
        return self._get(self.channel_name_symb(channel)[1], self._db.get_col_va)

    def list_channels(self, chan=None):
        """
        Return a dict of channels in the database.

        :param chan: channel filter, default CHAN_ALL:

            =============== ============================
            CHAN_ALL        all channels, normal and VA
            CHAN_NORMAL     normal channels only
            CHAN_ARRAY      VA channels only
            =============== ============================

        :returns:   dictionary {channel_names: channel_symbols}

        .. versionadded:: 9.1
        """

        def cleanChannelsDct():
            """ returns list without any temporaty VA sliced channels """
            self._db.chan_lst(self._lst)
            _dct = gxu.dict_from_lst(self._lst)
            dct = {}
            for k in _dct:
                if '[' in k:
                    continue
                dct[k] = _dct.get(k)
            return dct

        if chan == CHAN_ALL:
            dct = cleanChannelsDct()

        else:
            self._db.array_lst(self._lst)
            va = gxu.dict_from_lst(self._lst)
            if chan == CHAN_ARRAY:
                dct = va
            else:
                # filter VA channels out of the list
                all = cleanChannelsDct()
                va = list(va)
                dct = {}
                for k in all:
                    if not(k in va):
                        dct[k] = all.get(k)

        # convert symbol strings to ints
        for k in dct:
            dct[k] = int(dct.get(k))

        return dct

    def lines(self, select=True):
        """
        .. deprecated:: 9.2 use list_lines()
        """
        return self.list_lines(select)

    def list_lines(self, select=True):
        """
        List of lines in the database, returned as a {name: symbol} dictionary
        
        :param select=True: `True` to return selected lines, `False` to return all lines
        :returns:           dictionary (line name: symbol)

        .. versionadded:: 9.1
        """
        if select:
            self._db.selected_line_lst(self._lst)
        else:
            self._db.line_lst(self._lst)
        dct = gxu.dict_from_lst(self._lst)
        for k in dct:
            dct[k] = int(dct.get(k))
        return dct

    def line_details(self, line):
        """
        Return dictionary of line details

        :param line:    channel name or symbol
        :returns:       dictionary:

            =========== ==============================================================
            Key         Meaning
            =========== ==============================================================
            name        line name
            symbol      line symbol
            type        line type, one of gxapi.DB_LINE_TYPE
            category    one of SYMB_LINE
            date        date of the line
            number      numeric line number
            flight      flight number
            version     line version number
            groupclass  class name for grouped lines, None if not a grouped line
            =========== ==============================================================

        .. versionadded:: 9.1
        """

        def get_detail(fn):
            try:
                fn(ls, self._sr)
                return self._sr.value
            except geosoft.gxapi.GXAPIError:
                return ''

        ln, ls = self.line_name_symb(line)
        detail = {}
        self._lock_read(ls)

        try:
            detail['name'] = ln
            detail['symbol'] = ls
            detail['category'] = self._db.line_category(ls)
            detail['date'] = self._db.line_date(ls)
            detail['flight'] = self._db.line_flight(ls)
            detail['number'] = self._db.line_number(ls)
            detail['version'] = self._db.line_version(ls)
            detail['type'] = self._db.line_type(ls)
            if self._db.line_category(ls) == gxapi.DB_CATEGORY_LINE_GROUP:
                detail['groupclass'] = get_detail(self._db.get_group_class)
            else:
                detail['groupclass'] = None

        finally:
            self._unlock(ls)

        return detail

    def channel_details(self, channel):
        """
        Return dictionary of channel details

        :param channel: channel name or symbol
        :returns:       dictionary:

            ======= ==============================================================
            Key     Meaning
            ======= ==============================================================
            name    channel name
            symbol  channel symbol
            class   class name
            format  format, one of gxapi.DB_CHAN_FORMAT constants
            width   display width in characters
            decimal decimal places to display
            unit    measurement unit
            label   channel label, which can be different from the channel name
            protect protection: 0 can be modified; 1 protected from modification
            columns number data columns, 1 for normal channels, n for VA channels
            type    data type, one of gxapi.DB_CATEGORY_CHAN constants
            ======= ==============================================================

        .. versionadded:: 9.1
        """

        def get_detail(fn):
            fn(cs, self._sr)
            return self._sr.value

        cn, cs = self.channel_name_symb(channel)
        detail = {}
        self._lock_read(cs)

        try:
            detail['name'] = cn
            detail['symbol'] = cs
            detail['class'] = get_detail(self._db.get_chan_class)
            detail['format'] = self._db.get_chan_format(cs)
            detail['width'] = self._db.get_chan_width(cs)
            detail['decimal'] = self._db.get_chan_decimal(cs)
            detail['unit'] = get_detail(self._db.get_chan_unit)
            detail['label'] = get_detail(self._db.get_chan_label)
            detail['protect'] = self._db.get_chan_protect(cs)
            detail['array'] = self.channel_width(cs)
            detail['type'] = self._db.get_chan_type(cs)

        finally:
            self._unlock(cs)

        return detail

    def set_channel_details(self, channel, detail):
        """
        Set/change channel details from dictionary

        :param channel: channel name or symbol
        :param detail:  dictionary, see chan_details

        .. versionadded:: 9.1
        """

        def set_detail(what, fn):
            det = detail.get(what)
            if det is not None:
                fn(cs, det)

        cs = self.channel_name_symb(channel)[1]
        self._lock_write(cs)

        try:
            set_detail('class', self._db.set_chan_class)
            set_detail('format', self._db.set_chan_format)
            set_detail('width', self._db.set_chan_width)
            set_detail('decimal', self._db.set_chan_decimal)
            set_detail('unit', self._db.set_chan_unit)
            set_detail('label', self._db.set_chan_label)

            protect = detail.get('protect')
            if protect is not None:
                self._db.set_chan_protect(cs, protect)

        finally:
            self._unlock(cs)

    def channel_dtype(self, channel):
        """
        Returns channel numpy dtype

        :param channel: channel name or symbol
        :returns:       numpy dtype

        .. versionadded:: 9.1
        """
        return gxu.dtype_gx(self._db.get_chan_type(self.channel_name_symb(channel)[1]))

    def channel_fid(self, line, channel):
        """
        Return the fiducial of a line, channel

        :param line:    line name, symbol or Line
        :param channel: channel name, symbol or channel
        :returns:       (start,increment)
        """
        ls = self.line_name_symb(line)[1]
        cs = self.channel_name_symb(channel)[1]
        self._lock_read(cs)

        try:
            fidStart = self._db.get_fid_start(ls, cs)
            fidIncr = self._db.get_fid_incr(ls, cs)

        finally:
            self._unlock(cs)

        return (fidStart, fidIncr)

    # ========================================================================================
    # management

    def new_channel(self, name, dtype=np.float64, array=1, dup=None, details=None):
        """
        Return a channel symbol, create if it does not exist.

        :param name:        channel name
        :param dtype:       numpy dtype (ie. np.int64)
        :param array:       array columns (default is 1)
        :param dup:         duplicate properties of this channel (name, symbol, channel)
        :param details:     dictionary containing channel details, see channel_details()

        :returns:           channel symbol

        Examples:

        .. code::

            symb = gdb.newChan('X')
            symb = gdb.newChan('X', dtype=np.float64, details={'decimal':4})

        .. versionadded:: 9.1

        .. versionchanged:: 9.3
            added support for duplication an existing channel via dup=
        """

        symb = self._db.find_symb(name, gxapi.DB_SYMB_CHAN)
        if array < 1:
            array = 1
        if symb == gxapi.NULLSYMB:
            if dup:
                symb = self._db.dup_symb_no_lock(self.channel_name_symb(dup)[1], name)
            else:
                symb = self._db.create_symb_ex(name,
                                               gxapi.DB_SYMB_CHAN,
                                               gxapi.DB_OWN_SHARED,
                                               gxu.gx_dtype(dtype),
                                               array)

        if details:
            self.set_channel_details(symb, details)
        elif not dup:
            self.set_channel_details(symb, {'width': 12, 'decimal': 2})

        return symb

    def new_line(self, line, linetype=None, group=None, dup=None):
        """
        Create a new line symbol.  If line exists an error is raised.

        :param line:        line name
        :param linetype:    line type for creating a new line, ignored if group defines

                                ================= =========================================
                                SYMB_LINE_NORMAL  normal lines, name is a string
                                SYMB_LINE_FLIGHT  flight lines, first letter is line type
                                ================= =========================================

        :param group:       group name for a grouped class
        :param dup:         duplicate from an existing line (name, symbol of Line)

        :returns:           line symbol

        .. seealso:: function :func:`create_line_name` to create a valid line name.

        .. versionadded:: 9.1
        """

        if not is_valid_line_name(line):
            raise GdbException(_t('Invalid line name \'{}\'. Use create_line_name() to create a valid name.'.format(line)))

        symb = self._db.find_symb(line, gxapi.DB_SYMB_LINE)
        if symb != gxapi.NULLSYMB:
            raise GdbException(('Cannot create existing line \'{}\''.format(line)))

        if dup:
            dup_symb = self.line_name_symb(dup)[1]
            symb = self._db.dup_line_symb(dup_symb, line)
        else:
            if group:
                linetype = SYMB_LINE_GROUP
            elif not linetype:
                linetype = SYMB_LINE_NORMAL
            symb = self._db.create_symb_ex(line,
                                       gxapi.DB_SYMB_LINE,
                                       gxapi.DB_OWN_SHARED,
                                       linetype,
                                       0)
            if group:
                Line(self, symb).group = group

        return symb

    def delete_channel(self, channels):
        """
        Delete channel(s) by name or symbol.

        :param channels: channel name or symbol, or a list of channel names or symbols

        .. versionadded:: 9.1
        """

        if isinstance(channels, str) or isinstance(channels, int):
            channels = [channels]

        protected_channels = []

        for s in channels:

            try:
                c = Channel(self, s)
                if c.protect:
                    protected_channels.append(c.name)
                else:
                    c.delete()
            except GdbException:
                continue

        if len(protected_channels):
            raise GdbException(_t('Cannot delete protected channels: {}'.format(protected_channels)))

    def delete_line(self, lines):
        """
        Delete line(s) by name or symbol.

        :param lines: line name/symbol, or a list of names/symbols

        .. versionadded:: 9.1
        """

        if isinstance(lines, str) or isinstance(lines, int):
            lines = [lines]

        for s in lines:

            try:
                ln, ls = self.line_name_symb(s)
            except GdbException:
                continue

            self._unlock(ls)
            self._lock_write(ls)
            self._db.delete_symb(ls)

    def select_lines(self, selection='', select=True):
        """
        Change selected state of a line, or group of lines
        
        :param selection:   string representing selection, comma-delimit multiple selections, or provide a list
                            of selections.
        :param select=True: `True` to select, `False` to deselect

        "L99:800" will select all lines of type "L" in range 99 through 800.

        | Use a "T" prefix for Tie lines.
        | Use an "F" prefix to specify lines of a specific flight.
        |    For example, "F10" would select all lines of flight 10.
        | Use an empty string ("") to select/deselect ALL lines.

        Invalid line names are ignored.

        .. versionadded:: 9.1

        """

        if isinstance(selection, str):
            selection = selection.split(',')

        for s in selection:
            if select:
                self._db.select(s, gxapi.DB_LINE_SELECT_INCLUDE)
            else:
                self._db.select(s, gxapi.DB_LINE_SELECT_EXCLUDE)

    # =====================================================================================
    # reading and writing

    def _sorted_chan_list(self):

        ch = list(self.list_channels())
        ch.sort(key=str.lower)
        channels = []

        # put x,y,z at the front
        xch = self._db.get_xyz_chan_symb(gxapi.DB_CHAN_X)
        if xch != -1:
            nX, sX = self.channel_name_symb(xch)
            channels.append(nX)
        else:
            nX = ''

        ych = self._db.get_xyz_chan_symb(gxapi.DB_CHAN_Y)
        if ych != -1:
            nY, sY = self.channel_name_symb(ych)
            channels.append(nY)
        else:
            nY = ''

        zch = self._db.get_xyz_chan_symb(gxapi.DB_CHAN_Z)
        if zch != -1:
            nZ, sZ = self.channel_name_symb(zch)
            channels.append(nZ)
        else:
            nZ = ''

        for c in ch:
            if (c == nX) or (c == nY) or (c == nZ):
                continue
            channels.append(c)

        return channels

    def _expand_chan_list(self, channels):
        """ expand VA channels and return lists of names, symbols and types"""

        chNames = []
        chSymbs = []
        cType = []
        for c in channels:
            cn, cs = self.channel_name_symb(c)
            w = self.channel_width(cs)
            if w == 1:
                chNames.append(cn)
                chSymbs.append(cs)
                cType.append(self._db.get_chan_type(cs))
            else:
                for i in range(w):
                    ccn, ccs = self.channel_name_symb("{}[{}]".format(cn, i))
                    chNames.append(ccn)
                    chSymbs.append(ccs)
                    cType.append(self._db.get_chan_type(cs))

        return chNames, chSymbs, cType

    def _lock_read(self, s):
        try:
            self._db.lock_symb(s, SYMBOL_LOCK_READ, gxapi.DB_WAIT_INFINITY)
        except GdbException:
            raise GdbException(_t('Cannot read lock symbol {}'.format(s)))

    def _lock_write(self, s):
        try:
            self._db.lock_symb(s, SYMBOL_LOCK_WRITE, gxapi.DB_WAIT_INFINITY)
        except GdbException:
            raise GdbException(_t('Cannot write lock symbol {}'.format(s)))

    def _unlock(self, s):
        if self._db.get_symb_lock(s) != SYMBOL_LOCK_NONE:
            self._db.un_lock_symb(s)

    def unlock_all(self):
        """
        Unlock all locked symbols.

        .. versionadded:: 9.3
        """
        self._db.un_lock_all_symb()

    def read_channel_vv(self, line, channel, dtype=None):
        """
        Read data from a single channel, return in a vv.

        :param line:    line name or symbol
        :param channel: channel name or symbol
        :param dtype:   type wanted, default same as the channel data

        :returns:       vv

        .. versionadded:: 9.2
        """

        ln, ls = self.line_name_symb(line, create=True)
        cn, cs = self.channel_name_symb(channel)

        if self.channel_width(cs) != 1:
            raise GdbException(_t("Cannot read a VA channel into a VV."))

        if dtype is None:
            dtype = self.channel_dtype(cs)
        vv = gxvv.GXvv(dtype=dtype)
        self._lock_read(cs)
        try:
            self._db.get_chan_vv(ls, cs, vv.gxvv)
        finally:
            self._unlock(cs)

        vv.unit_of_measure = Channel(self, cs).unit_of_measure

        return vv


    def read_channel_va(self, line, channel, dtype=None):
        """
        Read VA data from a single channel, return in a va.

        :param line:    line name or symbol
        :param channel: channel name or symbol
        :param dtype:   type wanted, default same as the channel data

        :returns:       va

        .. versionadded:: 9.2
        """

        ln, ls = self.line_name_symb(line, create=True)
        cn, cs = self.channel_name_symb(channel)

        if dtype is None:
            dtype = self.channel_dtype(cs)
        w = self.channel_width(cs)
        va = gxva.GXva(width=w, dtype=dtype)
        self._lock_read(cs)
        try:
            self._db.get_chan_va(ls, cs, va.gxva)
        finally:
            self._unlock(cs)

        va.unit_of_measure = Channel(self, cs).unit_of_measure

        return va

    def read_channel(self, line, channel, dtype=None):
        """
        Read data from a single channel.

        :param line:    line name or symbol
        :param channel: channel name or symbol
        :param dtype:   type wanted, default same as the channel data

        :returns:       numpy data, fid (start, increment)

        For dtype=np.float, dummy values will be np.nan. For integer types dummy values will be the
        Geosoft dummy values.

        .. versionadded:: 9.1
        """

        if self.channel_width(channel) == 1:
            vv = self.read_channel_vv(line, channel, dtype)
            return vv.get_data(vv.dtype)[0], vv.fid

        else:
            va = self.read_channel_va(line, channel, dtype)
            return va.get_data(va.dtype)[0], va.fid

    def read_line_vv(self, line, channels=None, dtype=None, fid=None, common_fid=False):
        """
        Read a line of data into VVs stored in a dictionary by channel.

        :param line:        line to read, string or symbol number
        :param channels:    list of channels, strings or symbol number.  If empty, read all channels
        :param dtype:       numpy data type for the array, default np.float64 for multi-channel data,
                            data type for single channel data. Use "<Unnn" for string type.
        :param common_fid:  `True` to resample all channels to a common fiducial
        :param fid:         required fid (start, increment), ignored if `common_fid=False`.
                            if `common_fid=True` and fid= is not defined, use the smallest common fid.
        :returns:           list of tuples [(channel_name, vv), ...]

        If a requested channel is a VA, it is with channel names 'name[0]', 'name[1]', etc.

        Examples:

        .. code::

            # npd - returned numpy array shape (n, number of channels)
            # ch  - list of returned channels names, array channels expanded to array[0], array[1], ...
            # fid - tuple (fidStart,fidIncrement), channels resampled as necessary

            data = gdb.read_line_vv('L100')                           # read all channels in line "L100"
            data = gdb.read_line_vv(681)                              # read all channels in line symbol 681
            data = gdb.read_line_vv('L100','X')                       # read channel 'X' from line 'L100'
            data = gdb.read_line_vv('L100',2135)                      # read channel symbol 2135 from 'L100"
            data = gdb.read_line_vv('L100',channels=['X','Y','Z'])    # read a list of channels to (n,3) array
            data = gdb.read_line_vv('L100','X',np.int32)              # read channel 'X' into integer array

        .. versionadded:: 9.2
        """

        ln, ls = self.line_name_symb(line)

        # default all channels, sorted, X,Y,Z first
        if channels is None:
            channels = self._sorted_chan_list()

        else:
            if (type(channels) is str) or (type(channels) is int):
                channels = [channels]

        # make up channel list, expanding VA channels
        chNames, chSymb, cType = self._expand_chan_list(channels)

        if dtype is None:
            dtype = np.float64

        # read the data into vv
        chvv = []
        for c in chNames:
            cs = self._db.find_symb(c, gxapi.DB_SYMB_CHAN)
            vv = self.read_channel_vv(ls, cs, dtype=dtype)
            chvv.append((c, vv))

        # resample?
        if common_fid:

            # determine fiducial range from data
            start = gxapi.GS_R8MX
            incr = gxapi.GS_R8MX
            fend = gxapi.GS_R8MN

            for vv in chvv:
                if vv[1].length > 0:
                    fd = vv[1].fid
                    if fd[0] != gxapi.rDUMMY:
                        if fd[0] < start:
                            start = fd[0]
                        if fd[1] < incr:
                            incr = fd[1]
                        dend = start + incr * (vv[1].length - 1)
                        if dend > fend:
                            fend = dend

            if fid is None:
                if start == gxapi.GS_R8MX:
                    fid = (0.0, 1.0)
                else:
                    fid = (start, incr)

            if start == gxapi.GS_R8MX:
                nvd = 0
            else:
                nvd = math.ceil(max((fend - fid[0] - sys.float_info.epsilon), 0) / fid[1]) + 1
            for vv in chvv:
                vv[1].refid(fid, nvd)

        return chvv

    def readLine(self, *args, **kwargs):
        """
        .. deprecated:: 9.2 use read_line() 
        """
        return self.read_line(*args, **kwargs)

    def read_line(self, line, channels=None, dtype=None, fid=None, dummy=None):
        """
        Read a line of data into a numpy array.

        :param line:        line to read, string or symbol number
        :param channels:    list of channels, strings or symbol number.  If empty, read all channels
        :param dtype:       numpy data type for the array, default np.float64 for multi-channel data,
                            data type for single channel data. Use "<Unnn" for string type.
        :param fid:         required fiducial as tuple (start,incr), default smallest in data
        :param dummy:       dummy_handling for multi-channel read, default leaves dummies in place.:

            ======================== ===================================================
            READ_REMOVE_DUMMYROWS    remove rows with dummies, fiducials lose meaning
            READ_REMOVE_DUMMYCOLUMNS remove columns with dummies
            ======================== ===================================================

        :returns:   2D numpy array shape(records,channels), list of channel names, (fidStart,fidIncr)
        :raises:    GdbException if first channel requested is empty

        VA channels are expanded by element with channel names name[0], name[1], etc.

        Empty

        Examples:

        .. code::

            # npd - returned numpy array shape (n, number of channels)
            # ch  - list of returned channels names, array channels expanded to array[0], array[1], ...
            # fid - tuple (fidStart,fidIncrement), channels resampled as necessary

            npd,ch,fid = gdb.read_line('L100')                           # read all channels in line "L100"
            npd,ch,fid = gdb.read_line(681)                              # read all channels in line symbol 681
            npd,ch,fid = gdb.read_line('L100','X')                       # read channel 'X' from line 'L100'
            npd,ch,fid = gdb.read_line('L100',2135)                      # read channel symbol 2135 from 'L100"
            npd,ch,fid = gdb.read_line('L100',channels=['X','Y','Z'])    # read a list of channels to (n,3) array
            npd,ch,fid = gdb.read_line('L100','X',np.int32)              # read channel 'X' into integer array

        .. versionadded:: 9.1
        """

        # get VVs of data, resampled to a common fid
        data = self.read_line_vv(line, channels, dtype, fid, common_fid=True)
        if len(data) == 0:
            return np.array([]), [], (0.0, 1.0)
        nvd = data[0][1].length
        fid = data[0][1].fid
        nCh = len(data)

        # move data to numpy array
        npd = np.empty((nvd, nCh), dtype=dtype)
        if npd.dtype == np.float32 or npd.dtype == np.float64:
            dummy_value = np.nan
        else:
            dummy_value = gxu.gx_dummy(npd.dtype)
        chNames = []
        for chvv in data:
            vv = chvv[1]
            if vv.length > 0:
                npd[:, len(chNames)] = vv.get_data(dtype=npd.dtype)[0]
            else:
                npd[:, len(chNames)].fill(dummy_value)
            chNames.append(chvv[0])

        # dummy handling
        if dummy:
            if dummy == READ_REMOVE_DUMMYCOLUMNS:
                n_ok = 0

                # shift data and channel names to remove columns containing a dummy
                for i in range(nCh):
                    if np.isnan(dummy_value):
                        if np.isnan(npd[:, i]).any():
                            continue
                    elif dummy_value in npd[:, i]:
                        continue
                    if n_ok != i:
                        npd[:, n_ok] = npd[:, i]
                        chNames[n_ok] = chNames[i]
                    n_ok += 1
                if n_ok != nCh:
                    npd = npd[:, 0:n_ok]
                    chNames = chNames[0:n_ok]

            elif dummy == READ_REMOVE_DUMMYROWS:

                if np.isnan(dummy_value):
                    mask = np.apply_along_axis(lambda a: not (np.isnan(a).any()), 1, npd)
                else:
                    mask = np.apply_along_axis(lambda a: not (dummy_value in a), 1, npd)
                npd = npd[mask, :]
                fid = (0.0, 1.0)

            else:
                raise GdbException(_t('Unrecognized dummy={}').format(dummy))

        return npd, chNames, fid

    def write_channel_vv(self, line, channel, vv):
        """
        Write data to a single channel.

        :param line:    line name or symbol
        :param channel: channel name or symbol
        :param vv:      vv data to write

        .. versionadded:: 9.2
        """

        ln, ls = self.line_name_symb(line, create=True)

        try:
            cn, cs = self.channel_name_symb(channel)

        except GdbException:
            if type(channel) is str:
                cs = self.new_channel(channel, vv.dtype)
            else:
                raise

        self._lock_write(cs)
        try:
            self._db.put_chan_vv(ls, cs, vv.gxvv)
        finally:
            self._unlock(cs)

        if vv.unit_of_measure:
            Channel(self, cs).unit_of_measure = vv.unit_of_measure

    def write_channel_va(self, line, channel, va):
        """
        Write VA data to a single channel.

        :param line:    line name or symbol
        :param channel: channel name or symbol
        :param va:      va data to write

        .. versionadded:: 9.2
        """

        ln, ls = self.line_name_symb(line, create=True)

        try:
            cn, cs = self.channel_name_symb(channel)

        except GdbException:
            if type(channel) is str:
                cs = self.new_channel(channel, va.dtype, array=va.width)
            else:
                raise

        self._lock_write(cs)
        try:
            self._db.put_chan_va(ls, cs, va.gxva)
        finally:
            self._unlock(cs)

        if va.unit_of_measure:
            Channel(self, cs).unit_of_measure = va.unit_of_measure

    def writeDataChan(self, *args, **kwargs):
        """
        .. deprecated:: 9.2 use :meth:`write_channel`
        """
        self.write_channel(*args, **kwargs)

    def write_channel(self, line, channel, data, fid=(0.0, 1.0), unit_of_measure=None):
        """
        Write data to a single channel.

        :param line:            line name or symbol
        :param channel:         channel name or symbol
        :param data:            numpy array (2D for VA channel), or a list
        :param fid:             tuple (fid start, increment), default (0.0,1.0)
        :param unit_of_measure: data unit of measurement

        .. versionchanged:: 9.3 support for setting channel from a list

            added unit_of_measure

        .. versionadded:: 9.1
        """

        ln, ls = self.line_name_symb(line, create=True)

        if isinstance(channel, str):
            cn = channel
            cs = self.new_channel(channel, data.dtype, array=_va_width(data))
        else:
            cn, cs = self.channel_name_symb(channel)
            

        if not isinstance(data, np.ndarray):
            data = np.array(data)

        if _va_width(data) == 0:
            # no data to write
            return

        w = self.channel_width(cs)
        if w != _va_width(data):
            raise GdbException(
                _t("Array data width {} does not fit into channel '{}' with width {}").
                format(_va_width(data), cn, w))

        # 1D channel
        if w == 1:

            # get a VV of the data
            vv = gxvv.GXvv(data, fid=fid)

            self._lock_write(cs)
            try:
                self._db.put_chan_vv(ls, cs, vv.gxvv)
            finally:
                self._unlock(cs)

        else:

            # get a VA of the data
            va = gxva.GXva(data, fid=fid)

            self._lock_write(cs)
            try:
                self._db.put_chan_va(ls, cs, va.gxva)
            finally:
                self._unlock(cs)

        if unit_of_measure:
            Channel(self, cs).unit_of_measure = unit_of_measure

    def write_line_vv(self, line, chan_data):
        """
        Write data to multiple channels in a line.  If no channel list is provided it assumes that the
        data is for all channels from the line, the compliment of read_line().

        :param line:        line to write to, name or symbol
        :param data:        numpy array shape (records,channels).  If single dimension, one channel.
                            Channels are created if they do not exist.  VA channels must exist.
        :param chan_data:   list of tuples [(channel_name, vv), ]

        .. note::

            chan_data may contain VA data, which is defined by slice (ie. name[0], name[4]...).
            If VA data is included the VA channels must already exist.

        .. versionadded:: 9.2
        """

        for chvv in chan_data:
            ch = chvv[0]
            vv = chvv[1]
            self.write_channel_vv(line, ch, vv)

    def write_line(self, line, data, channels=None, fid=(0.0, 1.0)):
        """
        Write data to a multiple channels in a line.  If no channel list is provided it assumes that the
        data is for all channels from the line, the compliment of read_line().

        :param line:        line to write to, name or symbol
        :param data:        numpy array shape (records,channels).  If single dimension, one channel
        :param channels:    channel name or symbol list, or a single name/symbol.  If a single name is specified
                            for multi-column data, a VA channel is assumed. If None, a sorted list of all channels
                            is assumed.
        :param fid:         option fid tuple (start, increment), default (0.0,1.0)

        .. versionadded:: 9.1
        """

        if type(channels) is str:
            self.write_channel(line, channels, data, fid=fid)

        else:

            if channels is None:
                channels = self._sorted_chan_list()

            if data.ndim == 1:
                data = data.reshape((-1, 1))

            # ensure data matches channels
            np_data = 0
            for chan in channels:
                try:
                    ch, cs = self.channel_name_symb(chan)
                    w = self.channel_width(cs)
                except GdbException:
                    w = 1
                np_data += w

            # channel - data mismatch
            if data.shape[1] != np_data:
                raise GdbException(_t('Data dimension ({}) does not match data required by channels ({}).').format(data.shape, channels))

            # all good, write the data
            np_index = 0
            for chan in channels:
                try:
                    ch, cs = self.channel_name_symb(chan)
                    w = self.channel_width(cs)
                except GdbException:
                    w = 1
                    cs = chan
                self.write_channel(line, cs, data[:, np_index: np_index + w], fid=fid)
                np_index += w

    def list_values(self, chan, max=1000, selected=True, dupl=50, progress=None, stop=None):
        """
        Build a list of unique values in a channel.  Uniqueness depends on the current display format for
        the field.

        :param chan:            channel to scan
        :param max=1000:        maximum values allowed, once this maximum is reached scanning stops
        :param selected=True:   `True` to scan only selected lines
        :param dupl:            Stop growing list after this many lines fail to grow the list, 0 scans all lines
        :param progress:        progress reporting function
        :param stop:            stop check function
        :returns:               list of values, represented as a string

        .. versionadded:: 9.1
        """

        lines = list(self.list_lines(select=selected))
        cn, cs = self.channel_name_symb(chan)
        details = self.channel_details(cs)
        dtype = np.dtype('<U{}'.format(details.get('width')))
        lines.sort(key=str.lower)
        set = []
        n = 0
        nset = -1
        ndup = 0
        for l in lines:

            try:
                d, c, f = self.read_line(l, cs, dtype=dtype)
            except GdbException:
                continue

            if d.shape[0] == 0:
                continue

            d = np.unique(d)
            set = np.append(set, d)
            set = np.unique(set)

            if set.shape[0] > max:
                break
            if dupl > 0:
                if (set.shape[0] == nset):
                    ndup += 1
                    if ndup > dupl:
                        break
                else:
                    ndup = 0
            nset = set.shape[0]

            n += 1
            if progress:
                progress('Scanning unique values in "{}", {}'.format(cn, str(l)), (n * 100.0) / len(lines))
            if stop:
                if stop():
                    return set.tolist()

        if set.shape[0] > max:
            set = set[:max]

        return set.tolist()

    def figure_map(self, file_name=None, title=None, draw=DRAW_AS_POINTS,
                   features=['SCALE', 'NEATLINE'], **kwargs):
        """
        Create a figure map file from selected lines in the database.

        :param file_name:       the name of the map, if None a default map is created.
        :param overwrite:       True to overwrite existing image file
        :param title:           Title added to the image
        :param style:           `DRAW_AS_POINTS` to draw a dot at each point (default). Long lines are decimated.
                                `DRAW_AS_LINES` to draw lines with a line label at each end.
        :param features:        list of features to place on the map, default is ('SCALE', 'NEATLINE')

                                    =========== =========================================
                                    'SCALE'     show a scale bar
                                    'NEATLINE'  draw a neat-line around the image
                                    'ANNOT_XY'  annotate map coordinates
                                    'ANNOT_LL'  annotate map Latitude, Longitude
                                    =========== =========================================

        :param kwargs:          passed to `geosoft.gxpy.map.Map.new`

        .. versionadded:: 9.3
        """

        # uppercase features, use a dict so we pop things we use and report error
        if isinstance(features, str):
            features = (features,)
        feature_list = {}
        if features is not None:
            for f in features:
                feature_list[f.upper()] = None
        features = list(feature_list.keys())

        # setup margins
        if not ('margins' in kwargs):

            bottom_margin = 1.0
            if title:
                bottom_margin += len(title.split('\n')) * 1.0
            if 'ALL' in feature_list or 'SCALE' in feature_list:
                bottom_margin += 1.2
            kwargs['margins'] = (1, 1, bottom_margin, 1)

        kwargs['coordinate_system'] = self.coordinate_system

        # work out some non-zero extents
        ex = self.extent_xyz()
        if not(ex[0] is None or ex[1] is None or ex[3] is None or ex[4] is None):

            mnx, mny, mxx, mxy = (ex[0], ex[1], ex[3], ex[4])
            dx = mxx - mnx
            dy = mxy - mny
            if dx == 0 and dy == 0:
                ex = (mnx - 50, mny - 50, mxx + 50, mxy + 50)
            else:
                if dx  < dy * 0.1:
                    d = dy * 0.05
                    mnx -= d
                    mxx += d
                elif dy < dx * 0.1:
                    d = dx * 0.05
                    mny -= d
                    mxy += d
                ex = (mnx, mny, mxx, mxy)

            gmap = gxmap.Map.figure(ex,
                                    file_name=file_name,
                                    features=features,
                                    title=title,
                                    **kwargs)

            x, y, _ = self.xyz_channels
            with gxview.View.open(gmap, "data") as v:
                for line in self.list_lines():
                    label = self.line_name_symb(line)[0]
                    xvv = self.read_channel_vv(line, x)
                    yvv = self.read_channel_vv(line, y)
                    gxapi.GXMVU.path_plot(v.gxview,
                                          xvv.gxvv, yvv.gxvv,
                                          label,
                                          gxapi.MVU_FLIGHT_LOCATE_END,
                                          67.5, 1,
                                          1, 1, 0)

        return gmap

class Channel:
    """
    Class to work with database channels.  Use constructor :meth:`Channel.new` to create a new channel.
    Use instance properties to work with channel properties.

    :param gdb:     database instance
    :param name:    channel name string, must exist - see new() to create a new channel

    .. versionadded:: 9.3
    """

    def _get(self, fn):
        self.gdb._lock_read(self._symb)
        try:
            return fn(self._symb)
        finally:
            self.gdb._unlock(self._symb)

    def _get_str(self, fn):
        self.gdb._lock_read(self._symb)
        try:
            fn(self._symb, self._sr)
            return self._sr.value
        finally:
            self.gdb._unlock(self._symb)

    def _set(self, fn, v):
        self.gdb._lock_write(self._symb)
        try:
            fn(self._symb, v)
        finally:
            self.gdb._unlock(self._symb)

    def __repr__(self):
        return "{}({})".format(self.__class__, self.__dict__)

    def __str__(self):
        return self.name

    def __init__(self, gdb, name):

        self.gdb = gdb
        name, self._symb = gdb.channel_name_symb(name)
        self._sr = gxapi.str_ref()

    @classmethod
    def new(cls, gdb, name, dtype=np.float64, array=1, dup=None, details=None, replace=False, unit_of_measure=None):
        """
        Create a new channel.

        :param gdb:             Geosoft_gdb instance
        :param name:            channel name
        :param dtype:           numpy data type, defaule np.float64
        :param array:           array size, default 1
        :param dup:             duplicate properties of this channal (name, symbol or Channel)
        :param details:         dictionary of other channel properties - see :meth:`Geosoft_gdb.set_channel_details`
        :param replace:         `True` to replace existing channel.  Existing channel information and data is lost.
                                default is `False`.
        :param unit_of_measure: unit of measurement of the data
        :return:        Channel instance
        """

        if gdb._exist_symb(name, gxapi.DB_SYMB_CHAN):
            if replace:
                gdb.delete_channel(name)
            else:
                raise GdbException(_t("Cannot replace existing channel '{}'".format(name)))
        symb = gdb.new_channel(name, dtype, array=array, dup=dup)
        if details:
            gdb.set_channel_details(symb, details)

        chan = cls(gdb, name)
        if unit_of_measure:
            chan.unit_of_measure = unit_of_measure

        return chan

    @property
    def name(self):
        """
        Channel name.

        .. versionadded:: 9.3
        """
        return self._get_str(self.gdb._db.get_chan_name)

    @name.setter
    def name(self, name):
        name = str(name)
        if name != self.name:
            if not self.gdb._db.is_chan_name(name):
                raise GdbException(_t('Invalid channel name \'{}\''.format(name)))
            if self.gdb._exist_symb(name, gxapi.DB_SYMB_CHAN):
                raise GdbException(_t('Cannot rename to an existing channel name \'{}\''.format(name)))
            self._set(self.gdb._db.set_chan_name, name)

    @property
    def symbol(self):
        """
        Channel symbol

        .. versionadded:: 9.3
        """
        return self._symb

    @property
    def array(self):
        """
        Array channel width, 1 for non-array channels

        .. versionadded:: 9.3
        """

        return self.gdb.channel_width(self._symb)

    @property
    def is_array(self):
        """
        `True` if this is an array channel

        .. versionadded:: 9.3
        """

        return bool(self.array > 1)

    @property
    def decimal(self):
        """
        Number of displayed decimal places, can be set.

        .. versionadded:: 9.3
        """

        return self.gdb._db.get_chan_decimal(self._symb)

    @decimal.setter
    def decimal(self, value):
        self._set(self.gdb._db.set_chan_decimal, value)

    @property
    def format(self):
        """
        Channel display format:

        ============= ========================================
        FORMAT_NORMAL normal decimal or integer format
        FORMAT_EXP    exponential
        FORMAT_TIME   geosoft time (HH:MM:SS.ssss)
        FORMAT_DATE   date (YYYY/MM/DD)
        FORMAT_GEOGR  geographic (deg.mm.ss.ssss)
        FORMAT_SIGDIG decimals is number of significant digits
        FORMAT_HEX    hexadecimal
        ============= ========================================

        .. versionadded:: 9.3
        """
        return self.gdb._db.get_chan_format(self._symb)

    @format.setter
    def format(self, value):
        self._set(self.gdb._db.set_chan_format, value)

    @property
    def label(self):
        """
        Channel label used in display graphics, normally the same as the channel name.
        Can be set.

        .. versionadded:: 9.3
        """
        self.gdb._db.get_chan_label(self._symb, self._sr)
        return self._sr.value

    @label.setter
    def label(self, value):
        self._set(self.gdb._db.set_chan_label, value)

    @property
    def type(self):
        """
        Geosoft data type.

        .. versionadded:: 9.3
        """
        return self.gdb._db.get_chan_type(self._symb)

    @property
    def unit_of_measure(self):
        """
        Unit of measure, can be set.

        .. versionadded:: 9.3
        """
        self.gdb._db.get_chan_unit(self._symb, self._sr)
        return self._sr.value

    @unit_of_measure.setter
    def unit_of_measure(self, value):
        self._set(self.gdb._db.set_chan_unit, value)

    @property
    def width(self):
        """
        Display window width in characters.
        Can be set.

        .. versionadded:: 9.3
        """
        return self.gdb._db.get_chan_width(self._symb)

    @width.setter
    def width(self, value):
        self._set(self.gdb._db.set_chan_width, value)

    @property
    def class_(self):
        """
        Class name to which this channel is associated.
        Can be set.

        .. versionadded:: 9.3
        """

        self.gdb._db.get_chan_class(self._symb, self._sr)
        return self._sr.value

    @class_.setter
    def class_(self, value):
        self._set(self.gdb._db.set_chan_class, value)

    @property
    def protect(self):
        """
        `True` if this channel is protected from modification.
        Can be set.

        .. versionadded:: 9.3
        """

        return bool(self.gdb._db.get_chan_protect(self._symb))

    @protect.setter
    def protect(self, value):
        if value:
            value = 1
        else:
            value = 0
        self._set(self.gdb._db.set_chan_protect, value)

    @property
    def locked(self):
        """
        True if symbol is locked.  Use property :any:`lock` to determine if read or write lock, or to
        set the lock.

        Setting to `False` unlocks the symbol.

        .. versionadded:: 9.3
        """
        return (self.lock != SYMBOL_LOCK_NONE)

    @locked.setter
    def locked(self, value):
        if not value:
            self.gdb._unlock(self._symb)
        else:
            raise GdbException(_t('Use property \'lock\' to set SYMBOL_READ or SYMBOL_WRITE lock.'))

    @property
    def lock(self):
        """
        Lock setting:

        | -1 unlocked (SYMBOL_LOCK_NONE)
        | 0 read-locked (SYMBOL_LOCK_READ)
        | 1 write-locked (SYMBOL_LOCK_WRITE)

        Can be set.

        .. versionadded 9.3
        """
        return self.gdb._db.get_symb_lock(self.symbol)

    @lock.setter
    def lock(self, value):
        if self.lock != value:
            self.gdb._unlock(self.symbol)
            self.gdb._db.lock_symb(self.symbol, value, gxapi.DB_WAIT_INFINITY)

    def delete(self):
        """
        Delete the channel and all associated data.  After calling this method this
        channel instance is no longer valid.

        .. versionadded:: 9.3
        """
        if self.protect:
            raise GdbException(_t("Cannot delete protected channel '{}'".format(self.name)))
        self.lock = SYMBOL_LOCK_WRITE
        self.gdb._db.delete_symb(self._symb)
        self._symb = gxapi.NULLSYMB

class Line:
    """
    Class to work with database lines.  Use constructor :meth:`Line.new` to create a new line.
    Use instance properties to work with line properties.

    :param gdb:     database instance
    :param name:    line name string, must exist - see new() to create a new line

    .. versionadded:: 9.3
    """

    def _get(self, fn):
        self.gdb._lock_read(self._symb)
        try:
            return fn(self._symb)
        finally:
            self.gdb._unlock(self._symb)

    def _get_str(self, fn):
        self.gdb._lock_read(self._symb)
        try:
            fn(self._symb, self._sr)
            return self._sr.value
        finally:
            self.gdb._unlock(self._symb)

    def _set(self, fn, v):
        self.gdb._lock_write(self._symb)
        try:
            fn(self._symb, v)
        finally:
            self.gdb._unlock(self._symb)

    def __repr__(self):
        return "{}({})".format(self.__class__, self.__dict__)

    def __str__(self):
        return self.name

    def __init__(self, gdb, name):

        self.gdb = gdb
        name, self._symb = gdb.line_name_symb(name)
        self._sr = gxapi.str_ref()

    @classmethod
    def new(cls, gdb, name, linetype=None, group=None, dup=None, replace=False):
        """
        Create a new line.

        :param name:        line name
        :param linetype:    line type for creating a new line, ignored if group defines

            ================= =========================================
            SYMB_LINE_NORMAL  normal lines, name is a string
            SYMB_LINE_FLIGHT  flight lines, first letter is line type
            ================= =========================================

        :param group:       group name for a grouped class
        :param dup:         duplicate properties of this line (name, symbol or Line).
        :param replace:     `True` to replace line if it exists. Default is `False` .
        :returns:           Line instance

        .. versionadded:: 9.3
        """

        if not is_valid_line_name(name):
            raise GdbException(_t('Invalid line name: {}'.format(name)))

        if gdb._exist_symb(name, gxapi.DB_SYMB_LINE):
            if replace:
                gdb.delete_line(name)
            else:
                raise GdbException(_t("Cannot replace existing line '{}'".format(name)))

        gdb.new_line(name, linetype, group=group, dup=dup)

        return cls(gdb, name)

    @property
    def name(self):
        """
        Line name, consistent with names constructed by :func:`create_line_name`.

        To change a line name change the type, number or version.

        .. versionadded:: 9.3
        """
        return self._get_str(self.gdb._db.get_symb_name)

    @property
    def symbol(self):
        """
        Line symbol

        .. versionadded:: 9.3
        """
        return self._symb

    @property
    def type(self):
        """
        Line type, which can be set:

        | LINE_TYPE_NORMAL
        | LINE_TYPE_BASE
        | LINE_TYPE_TIE
        | LINE_TYPE_TEST
        | LINE_TYPE_TREND
        | LINE_TYPE_SPECIAL
        | LINE_TYPE_RANDOM

        .. versionadded:: 9.3
        """
        return self._get(self.gdb._db.line_type)

    @type.setter
    def type(self, value):
        self._set(self.gdb._db.set_line_type, value)

    @property
    def category(self):
        """
        Line category, which can be set:

        | LINE_CATAGORY_FLIGHT
        | LINE_CATEGORY_GROUP
        | LINE_CATEGORY_NORMAL

        .. versionadded:: 9.3
        """
        return self._get(self.gdb._db.line_category)

    @property
    def date(self):
        """
        Line date. Can be set.

        .. versionadded:: 9.3
        """
        return self._get(self.gdb._db.line_date)

    @date.setter
    def date(self, value):
        self._set(self.gdb._db.set_line_date, value)

    @property
    def flight(self):
        """
        Line flight number (flight/cruise/survey event). Can be set.

        .. versionadded:: 9.3
        """
        return self._get(self.gdb._db.line_flight)
    
    @flight.setter
    def flight(self, value):
        self._set(self.gdb._db.set_line_flight, value)


    @property
    def number(self):
        """
        Line number. Can be set

        .. versionadded:: 9.3
        """
        return self._get(self.gdb._db.line_number)

    @number.setter
    def number(self, value):
        self._set(self.gdb._db.set_line_num, int(value))

    @property
    def version(self):
        """
        Line version number. Can be set.

        .. versionadded:: 9.3
        """
        return self._get(self.gdb._db.line_version)

    @version.setter
    def version(self, value):
        self._set(self.gdb._db.set_line_ver, value)

    @property
    def grouped(self):
        """
        True if this is a grouped line.

        .. versionadded:: 9.3
        """
        return self.category == LINE_CATEGORY_GROUP

    @property
    def group(self):
        """
        The lines group class name, '' for a group lines (LINE_CATEGORY_GROUP).
        Only works for lines that are part of a group.
        Can be set.

        .. versionadded:: 9.3
        """
        if self.category == LINE_CATEGORY_GROUP:
            return self._get_str(self.gdb._db.get_group_class)
        else:
            return None

    @group.setter
    def group(self, value):
        if self.category == LINE_CATEGORY_GROUP:
            self._set(self.gdb._db.set_group_class, value)
        else:
            raise GdbException(_t('Line \'{}\' is not a grouped line.'.format(self.name)))

    @property
    def selected(self):
        """True if this line is selected, can be set."""
        return self.gdb._db.get_line_selection(self._symb) == gxapi.DB_LINE_SELECT_INCLUDE

    @selected.setter
    def selected(self, value):
        if bool(value):
            self.gdb._db.set_line_selection(self._symb, gxapi.DB_LINE_SELECT_INCLUDE)
        else:
            self.gdb._db.set_line_selection(self._symb, gxapi.DB_LINE_SELECT_EXCLUDE)

    @property
    def locked(self):
        """
        True if symbol is locked.  Use property :any:`lock` to determine if read or write lock, or to
        set the lock.

        Setting to `False` unlocks the symbol.

        .. versionadded:: 9.3
        """
        return (self.lock != SYMBOL_LOCK_NONE)

    @locked.setter
    def locked(self, value):
        if not value:
            self.gdb._unlock(self._symb)
        else:
            raise GdbException(_t('Use property \'lock\' to set SYMBOL_READ or SYMBOL_WRITE lock.'))

    @property
    def lock(self):
        """
        Lock setting:

        | -1 unlocked (SYMBOL_LOCK_NONE)
        | 0 read-locked (SYMBOL_LOCK_READ)
        | 1 write-locked (SYMBOL_LOCK_WRITE)

        Can be set.

        .. versionadded 9.3
        """
        return self.gdb._db.get_symb_lock(self.symbol)

    @lock.setter
    def lock(self, value):
        if self.lock != value:
            self.gdb._unlock(self.symbol)
            self.gdb._db.lock_symb(self.symbol, value, gxapi.DB_WAIT_INFINITY)

    def delete(self):
        """
        Delete the line and all data associated with the line.  After calling this method this
        line instance is no longer valid.

        .. versionadded:: 9.3
        """
        self.gdb.delete_line(self.symbol)
        self._symb = gxapi.NULLSYMB

    #===========================================================================================
    # methods that work with line data

    def bearing(self):
        """
        Return bearing of a line based on location of the first and last point in the line.
        Returns None if the line is empty or first and last points are the same.

        .. versionadded:: 9.3
        """
        x, y, z = self.gdb.xyz_channels
        x = self.gdb.channel_name_symb(x)[1]
        y = self.gdb.channel_name_symb(y)[1]

        self.gdb._lock_read(x)
        self.gdb._lock_read(y)
        try:
            bearing = gxapi.GXDU.direction(self.gdb._db, self._symb, x, y)
        finally:
            self.gdb._unlock(y)
            self.gdb._unlock(x)

        self._set(self.gdb._db.set_line_bearing, bearing)
        if bearing == gxapi.rDUMMY:
            return None
        return bearing

