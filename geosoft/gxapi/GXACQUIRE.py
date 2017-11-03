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
class GXACQUIRE(gxapi_cy.WrapACQUIRE):
    """
    GXACQUIRE class.

    This class is used to import acQuire data. It uses the
    public acQuire API.
    """

    def __init__(self, handle=0):
        super().__init__(GXContext._get_tls_geo(), handle)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXACQUIRE <geosoft.gxapi.GXACQUIRE>`
        
        :returns: A null `GXACQUIRE <geosoft.gxapi.GXACQUIRE>`
        :rtype:   GXACQUIRE
        """
        return GXACQUIRE()

    def is_null(self):
        """
        Check if this is a null (undefined) instance
        
        :returns: True if this is a null (undefined) instance, False otherwise.
        :rtype:   bool
        """
        return self._internal_handle() == 0



# Miscellaneous


    @classmethod
    def create(cls):
        """
        Create an acQuire object
        

        :returns:    acQuire Object
        :rtype:      GXACQUIRE

        .. versionadded:: 6.0

        **License:** `Geosoft Desktop License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-GeosoftDesktopLicense>`_
        """
        ret_val = gxapi_cy.WrapACQUIRE._create(GXContext._get_tls_geo())
        return GXACQUIRE(ret_val)




    def delete_empty_chan(self, db):
        """
        Delete empty channels
        
        :param db:     Database
        :type  db:     GXDB

        .. versionadded:: 6.0

        **License:** `Geosoft Desktop License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-GeosoftDesktopLicense>`_
        """
        self._delete_empty_chan(db)
        






    def import_hole(self, proj, dir, para, geo_vv, delete, convert):
        """
        Import Drillhole data acQuire database into a GDB
        
        :param proj:     Project name
        :param dir:      Project directory
        :param para:     Parameter File
        :param geo_vv:   List of geology name database
        :param delete:   0: Write to existing databases (overwrite holes), 1: Delete existing databases.
        :param convert:  Convert Negatives (0,1)
        :type  proj:     str
        :type  dir:      str
        :type  para:     str
        :type  geo_vv:   GXVV
        :type  delete:   int
        :type  convert:  int

        :returns:        0 - Ok
                         1 - Error (Will not stop GX)
        :rtype:          int

        .. versionadded:: 6.0.1

        **License:** `Geosoft Desktop License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-GeosoftDesktopLicense>`_

        **Note:** Point data and polygon data are saved into Dnnn lines in GDB,
        nnn representing incremental number starting from 0
        """
        ret_val = self._import_hole(proj.encode(), dir.encode(), para.encode(), geo_vv, delete, convert)
        return ret_val




    def import_point(self, db, para, convert):
        """
        Import Point Sample data acQuire database into a GDB
        
        :param db:       Geosoft GDB
        :param para:     Parameter File
        :param convert:  Convert Negatives (0,1)
        :type  db:       GXDB
        :type  para:     str
        :type  convert:  int

        :returns:        0 - Ok
                         1 - Error (Will not stop GX)
        :rtype:          int

        .. versionadded:: 6.0.1

        **License:** `Geosoft Desktop License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-GeosoftDesktopLicense>`_

        **Note:** Data existing in the receiving GDB file will be over-written.
        Point data and polygon data are saved into Dnnn lines in GDB,
        nnn representing incremental number starting from 0
        """
        ret_val = self._import_point(db, para.encode(), convert)
        return ret_val




    def selection_tool(self, selection_file, mode):
        """
        Run the acQuire Selection Tool.
        
        :param selection_file:  Selection File Name
        :param mode:            :ref:`ACQUIRE_SEL`
        :type  selection_file:  str
        :type  mode:            int

        :returns:               0 - Ok
                                1 - if user cancels
        :rtype:                 int

        .. versionadded:: 6.0.1

        **License:** `Geosoft Desktop License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-GeosoftDesktopLicense>`_

        **Note:** The selection file will be loaded (if present) and then
        the user can make selections then the selections are saved
        back in the selection file.
        """
        ret_val = self._selection_tool(selection_file.encode(), mode)
        return ret_val





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer