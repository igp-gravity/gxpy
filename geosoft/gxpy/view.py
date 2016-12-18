#TODO review grd class to clean-up files like map class does.

import numpy as np

import geosoft
import geosoft.gxapi as gxapi
from . import map as gxmap
from . import vv as gxvv
from . import ipj as gxipj
from . import utility as gxu

__version__ = geosoft.__version__

def _(s):
    return s

class VIEWException(Exception):
    """
    Exceptions from this module.

    .. versionadded:: 9.2
    """
    pass

MODE_READ = gxapi.MVIEW_READ
MODE_WRITENEW = gxapi.MVIEW_WRITENEW
MODE_WRITEOLD = gxapi.MVIEW_WRITEOLD
SMOOTH_NONE = gxapi.MVIEW_SMOOTH_NEAREST
SMOOTH_CUBIC = gxapi.MVIEW_SMOOTH_CUBIC
SMOOTH_AKIMA = gxapi.MVIEW_SMOOTH_AKIMA
TILE_RECTANGULAR = gxapi.MVIEW_TILE_RECTANGULAR
TILE_DIAGONAL = gxapi.MVIEW_TILE_DIAGONAL
TILE_TRIANGULAR = gxapi.MVIEW_TILE_TRIANGULAR
TILE_RANDOM = gxapi.MVIEW_TILE_RANDOM

_def_group = "_default_group_"

# spatial data structures
class Point:
    def __enter__(self):
        return self

    def __exit__(self, xtype, xvalue, xtraceback):
        self.__del__()

    def __del__(self):
        pass

    def __repr__(self):
        return "{}({})".format(self.__class__, self.__dict__)

    def __str__(self):
        return "({}, {}, {})".format(self.x, self.y, self.z)

    def __init__(self, x, y, z=0.0):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    def __add__(self, p):
        if type(p) is Point:
            return Point(self.x + p.x, self.y + p.y, self.z + p.z)
        else:
            v = float(p)
            return Point(self.x + v, self.y + v, self.z + v)

    def __sub__(self, p):
        if type(p) is Point:
            return Point(self.x - p.x, self.y - p.y, self.z - p.z)
        else:
            v = float(p)
            return Point(self.x - v, self.y - v, self.z - v)

    def __neg__(self):
        return Point(-self.x, -self.y, -self.z)

    def __mul__(self, p):
        if type(p) is Point:
            return Point(self.x * p.x, self.y * p.y, self.z * p.z)
        else:
            v = float(p)
            return Point(self.x * v, self.y * v, self.z * v)

    def __truediv__(self, p):
        if type(p) is Point:
            return Point(self.x / p.x, self.y / p.y, self.z / p.z)
        else:
            v = float(p)
            return Point(self.x / v, self.y / v, self.z / v)

    def xy(self):
        """ Return (x, y) of a point"""
        return (self.x, self.y)

    def xyz(self):
        """ Return (x, y, z) of a point"""
        return (self.x, self.y, self.z)


class PPoint:
    """
    Poly-Point class.
    """

    def __init__(self, xyznp, z=0.0):
        """
        Create a PPoint from numpy array
        :param xyz: numpy array shape (n, 2) or (n, 3)
        :param z:   constant z value for (n, 2) data, ignored for (n, 3) data
        """

        self.xyz = np.zeros(xyznp.shape[0]*3, dtype=np.float).reshape((xyznp.shape[0], 3))
        self.xyz[:, 0] = xyznp[:,0]
        self.xyz[:, 1] = xyznp[:,1]
        if xyznp.shape[1] > 2:
            self.xyz[:, 2] = xyznp[:, 2]
        else:
            self.xyz[:, 2] = z

    @classmethod
    def from_list(cls, xyzlist, z=0.0):
        return cls(np.array(xyzlist, dtype=np.float), z)

    def __add__(self, p):
        if type(p) is PPoint:
            return PPoint(self.xyz + p.xyz)
        if type(p) is Point:
            return PPoint(self.xyz + (p.x, p.y, p.z))
        return PPoint(self.xyz + p)

    def __sub__(self, p):
        if type(p) is PPoint:
            return PPoint(self.xyz - p.xyz)
        if type(p) is Point:
            return PPoint(self.xyz - (p.x, p.y, p.z))
        return PPoint(self.xyz - p)

    def __neg__(self):
        return PPoint(self.xyz * -1.0)

    def __mul__(self, p):
        if type(p) is PPoint:
            return PPoint(self.xyz * p.xyz)
        if type(p) is Point:
            return PPoint(self.xyz * (p.x, p.y, p.z))
        return PPoint(self.xyz * p)

    def __truediv__(self, p):
        if type(p) is PPoint:
            return PPoint(self.xyz / p.xyz)
        if type(p) is Point:
            return PPoint(self.xyz / (p.x, p.y, p.z))
        return PPoint(self.xyz / p)

class GXview:
    """
    Geosoft view class.

    .. versionadded:: 9.2
    """

    _view = None

    def __enter__(self):
        return self

    def __exit__(self, xtype, xvalue, xtraceback):
        self.__del__()

    def __del__(self):

        if self._view:

            # remove the default group if it is empty

            if self._view.is_group_empty(_def_group):
                self._view.delete_group(_def_group)
            self._view = None

    def __repr__(self):
        return "{}({})".format(self.__class__, self.__dict__)

    def __str__(self):
        return self._filename

    def __init__(self, viewname="_default_view_", gmap=None, mode=MODE_WRITENEW):

        # temporary map for the view
        if gmap is None:
            self._map = gxmap.GXmap.new()
        else:
            self._map = gmap
        self._viewname = viewname
        self._view = gxapi.GXMVIEW.create(self._map._map, self._viewname, mode)

        # start a default group
        self._view.start_group("_default_group_", gxapi.MVIEW_GROUP_NEW)

        # intitialize pen
        self._init_pen_attributes()

    def _line_style(self, ls):
        self._view.line_style(ls[0], ls[1])

    def _init_pen_attributes(self):

        # set the default pen characteristics, initializes pen dictionaries

        def setpen(att, fn, setting):
            fn(setting)
            self.pen[att] = setting
            self.pen_fn[att] = fn

        self.pen = {}
        self.pen_fn = {}
        setpen('line_color', self._view.line_color, gxapi.C_BLACK)
        setpen('line_thick', self._view.line_thick, 0.1)
        setpen('line_smooth',self._view.line_smooth, SMOOTH_NONE)
        setpen('line_style', self._line_style, (0, 1.0))
        setpen('fill_color', self._view.fill_color, gxapi.C_TRANSPARENT)
        setpen('pat_number', self._view.pat_number, 0)
        setpen('pat_angle', self._view.pat_angle, 0.0)
        setpen('pat_density', self._view.pat_density, 1.0)
        setpen('pat_size', self._view.pat_size, 5.0)
        setpen('pat_style', self._view.pat_style, TILE_RECTANGULAR)
        setpen('pat_thick', self._view.pat_thick, 0.1)

    def map(self):
        """
        :return: name of the map that contains this view

        .. versionadded:: 9.2
        """
        return self._map

    def viewname(self):
        """
        :return: name of the view contains this view

        .. versionadded:: 9.2
        """
        return self._viewname

    def mapname(self):
        """
        :return: name of the map that contains this view

        .. versionadded:: 9.2
        """
        return self._map.filename()

    def set_pen(self, pen=None):
        """
        Set the current drawing pen attributes
        :param pen: dictionary of pen attrbutes and settings, if None, set to default

        .. versionadded:: 9.2
        """

        if pen is None:
            self._init_pen_attributes()

        else:
            for att, setting in pen.items():
                if self.pen[att] != setting:
                    self.pen_fn[att](setting)
                    self.pen[att] = setting

    def get_pen(self):
        """
        Return a dictionary of the current pen settings.

        .. versionadded:: 9.2
        """
        return self.pen

    def group(self, name, append=False):
        """
        Start a new named group in a view.  Drawing functions that follow will be rendered into this group.

        :param name:    name of the group
        :param append:  True to append to the group should it exist

        .. versionadded:: 9.2
        """

    # drawing to a plane

    def xy_line(self, p1, p2):
        """
        Draw a line on the current plane
        :param p1:  Point starting
        :param p2:  Point end

        .. versionadded:: 9.2
        """

        self._view.line(p1.x, p1.y, p2.x, p2.y)

    def xy_poly_line(self, pp, close=False):
        """
        Draw a polyline the current plane
        :param pline: PPoint
        :param close: if True, draw a polygon, default is a polyline

        .. versionadded:: 9.2
        """

        if close:
            self._view.poly_line(gxapi.MVIEW_DRAW_POLYGON,
                                 gxvv.GXvv.vv_np(pp.xyz[:,0])._vv,
                                 gxvv.GXvv.vv_np(pp.xyz[:,1])._vv)
        else:
            self._view.poly_line(gxapi.MVIEW_DRAW_POLYLINE,
                                 gxvv.GXvv.vv_np(pp.xyz[:, 0])._vv,
                                 gxvv.GXvv.vv_np(pp.xyz[:, 1])._vv)

    def xy_rectangle(self, p1, p2):
        """
        Draw a 2D rectangle on the current plane
        :param p1:  Point starting
        :param p2:  Point diagonal

        .. versionadded:: 9.2
        """

        self._view.rectangle(p1.x, p1.y, p2.x, p2.y)
