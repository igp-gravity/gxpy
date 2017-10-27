### extends 'class_empty.py'
### block ClassImports
# NOTICE: Do not edit anything here, it is generated code
from typing import NewType
from . import gxapi_cy
from geosoft.gxapi import GXContext, float_ref, int_ref, str_ref


### endblock ClassImports

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXACQUIRE:
    """
    GXACQUIRE class.

    This class is used to import acQuire data. It uses the
    public acQuire API.
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapACQUIRE(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXACQUIRE`
        
        :returns: A null `GXACQUIRE`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of `GXACQUIRE` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of `GXACQUIRE`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def create(cls):
        """
        Create an acQuire object
        """
        ret_val = gxapi_cy.WrapACQUIRE.create(GXContext._get_tls_geo())
        return GXACQUIRE(ret_val)




    def delete_empty_chan(self, db):
        """
        Delete empty channels
        """
        self._wrapper.delete_empty_chan(db._wrapper)
        






    def import_hole(self, proj, dir, para, geo_vv, delete, convert):
        """
        Import Drillhole data acQuire database into a GDB

        **Note:**

        Point data and polygon data are saved into Dnnn lines in GDB,
        nnn representing incremental number starting from 0
        """
        ret_val = self._wrapper.import_hole(proj.encode(), dir.encode(), para.encode(), geo_vv._wrapper, delete, convert)
        return ret_val




    def import_point(self, db, para, convert):
        """
        Import Point Sample data acQuire database into a GDB

        **Note:**

        Data existing in the receiving GDB file will be over-written.
        Point data and polygon data are saved into Dnnn lines in GDB,
        nnn representing incremental number starting from 0
        """
        ret_val = self._wrapper.import_point(db._wrapper, para.encode(), convert)
        return ret_val




    def selection_tool(self, selection_file, mode):
        """
        Run the acQuire Selection Tool.

        **Note:**

        The selection file will be loaded (if present) and then
        the user can make selections then the selections are saved
        back in the selection file.
        """
        ret_val = self._wrapper.selection_tool(selection_file.encode(), mode)
        return ret_val





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer