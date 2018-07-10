### extends 'class_empty.py'
### block ClassImports
# NOTICE: Do not edit anything here, it is generated code
from . import gxapi_cy
from geosoft.gxapi import GXContext, float_ref, int_ref, str_ref


### endblock ClassImports

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXMESHUTIL(gxapi_cy.WrapMESHUTIL):
    """
    GXMESHUTIL class.

    Mesh utility methods.
    """

    def __init__(self, handle=0):
        super().__init__(GXContext._get_tls_geo(), handle)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXMESHUTIL <geosoft.gxapi.GXMESHUTIL>`
        
        :returns: A null `GXMESHUTIL <geosoft.gxapi.GXMESHUTIL>`
        :rtype:   GXMESHUTIL
        """
        return GXMESHUTIL()

    def is_null(self):
        """
        Check if this is a null (undefined) instance
        
        :returns: True if this is a null (undefined) instance, False otherwise.
        :rtype:   bool
        """
        return self._internal_handle() == 0



# Miscellaneous


    @classmethod
    def clip_surface_with_grid(cls, inputSurfaceFile, inputSurface, gridFileName, outputSurfaceFile, outputSurfaceNameAbove, outputSurfaceNameBelow, surface_clip_mode):
        """
        Clip a Surface with a Grid
        
        :param inputSurfaceFile:        Input Geosurface file
        :param inputSurface:            Input Surface name within Geosurface file
        :param gridFileName:            Grid file name
        :param outputSurfaceFile:       Output Surface file
        :param outputSurfaceNameAbove:  Name of Surface Item above grid - required for mode=CLIP_ABOVE and CLIP_BOTH
        :param outputSurfaceNameBelow:  Name of Surface Item below grid - required for mode=CLIP_BELOW and CLIP_BOTH
        :param surface_clip_mode:       :ref:`SURFACE_CLIP_MODE`
        :type  inputSurfaceFile:        str
        :type  inputSurface:            str
        :type  gridFileName:            str
        :type  outputSurfaceFile:       str
        :type  outputSurfaceNameAbove:  str
        :type  outputSurfaceNameBelow:  str
        :type  surface_clip_mode:       int

        .. versionadded:: 9.5

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapMESHUTIL._clip_surface_with_grid(GXContext._get_tls_geo(), inputSurfaceFile.encode(), inputSurface.encode(), gridFileName.encode(), outputSurfaceFile.encode(), outputSurfaceNameAbove.encode(), outputSurfaceNameBelow.encode(), surface_clip_mode)
        



    @classmethod
    def clip_surface_with_extents(cls, inputSurfaceFile, inputSurface, outputSurfaceFile, min_x, max_x, min_y, max_y, min_z, max_z):
        """
        Clip a Surface with X,Y,Z extents
        
        :param inputSurfaceFile:   Input Geosurface file
        :param inputSurface:       Input Surface name within Geosurface file
        :param outputSurfaceFile:  Output Surface file
        :param min_x:              Min value of X
        :param max_x:              Max value of X
        :param min_y:              Min value of Y
        :param max_y:              Max value of Y
        :param min_z:              Min value of Z
        :param max_z:              Max value of Z
        :type  inputSurfaceFile:   str
        :type  inputSurface:       str
        :type  outputSurfaceFile:  str
        :type  min_x:              float
        :type  max_x:              float
        :type  min_y:              float
        :type  max_y:              float
        :type  min_z:              float
        :type  max_z:              float

        .. versionadded:: 9.5

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapMESHUTIL._clip_surface_with_extents(GXContext._get_tls_geo(), inputSurfaceFile.encode(), inputSurface.encode(), outputSurfaceFile.encode(), min_x, max_x, min_y, max_y, min_z, max_z)
        



    @classmethod
    def clip_surface_with_polygon2d(cls, inputSurfaceFile, inputSurface, polygonFile, outputSurfaceFile, maskInside):
        """
        Clip a Surface a specified Polygon file
        
        :param inputSurfaceFile:   Input Geosurface file
        :param inputSurface:       Input Surface name within Geosurface file
        :param polygonFile:        Polygon File
        :param outputSurfaceFile:  Output Surface file
        :param maskInside:         Set true if the values inside polygon are to be masked
        :type  inputSurfaceFile:   str
        :type  inputSurface:       str
        :type  polygonFile:        str
        :type  outputSurfaceFile:  str
        :type  maskInside:         bool

        .. versionadded:: 9.5

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapMESHUTIL._clip_surface_with_polygon2d(GXContext._get_tls_geo(), inputSurfaceFile.encode(), inputSurface.encode(), polygonFile.encode(), outputSurfaceFile.encode(), maskInside)
        



    @classmethod
    def compute_surface_union(cls, primarySurfaceFile, primarySurface, secondarySurfaceFile, secondarySurface, outputSurfaceFile, outputSurface):
        """
        Compute union of two surfaces
        
        :param primarySurfaceFile:    Primary Geosurface file
        :param primarySurface:        Primary Surface Name within Geosurface File
        :param secondarySurfaceFile:  Secondary Geosurface file
        :param secondarySurface:      Secondary Surface Name within Geosurface File
        :param outputSurfaceFile:     Output surface file
        :param outputSurface:         Output surface name
        :type  primarySurfaceFile:    str
        :type  primarySurface:        str
        :type  secondarySurfaceFile:  str
        :type  secondarySurface:      str
        :type  outputSurfaceFile:     str
        :type  outputSurface:         str

        .. versionadded:: 9.5

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapMESHUTIL._compute_surface_union(GXContext._get_tls_geo(), primarySurfaceFile.encode(), primarySurface.encode(), secondarySurfaceFile.encode(), secondarySurface.encode(), outputSurfaceFile.encode(), outputSurface.encode())
        



    @classmethod
    def compute_surface_clip(cls, primarySurfaceFile, primarySurface, secondarySurfaceFile, secondarySurface, outputSurfaceFile, outputSurface):
        """
        Clip a surface with another surface, and output the clipped surfaces
        
        :param primarySurfaceFile:    Primary Geosurface file
        :param primarySurface:        Primary Surface Name within Geosurface File
        :param secondarySurfaceFile:  Secondary Geosurface file
        :param secondarySurface:      Secondary Surface Name within Geosurface File
        :param outputSurfaceFile:     Output surface file
        :param outputSurface:         Output surface name
        :type  primarySurfaceFile:    str
        :type  primarySurface:        str
        :type  secondarySurfaceFile:  str
        :type  secondarySurface:      str
        :type  outputSurfaceFile:     str
        :type  outputSurface:         str

        .. versionadded:: 9.5

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapMESHUTIL._compute_surface_clip(GXContext._get_tls_geo(), primarySurfaceFile.encode(), primarySurface.encode(), secondarySurfaceFile.encode(), secondarySurface.encode(), outputSurfaceFile.encode(), outputSurface.encode())
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer