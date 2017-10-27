### extends 'class_empty.py'
### block ClassImports
# NOTICE: Do not edit anything here, it is generated code
from typing import NewType
from . import gxapi_cy
from geosoft.gxapi import GXContext, float_ref, int_ref, str_ref
from .GXIMG import GXIMG


### endblock ClassImports

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXRGRD:
    """
    GXRGRD class.

    The `GXRGRD` object is used as a storage place for the control
    parameters which the Rangrid (minimum curvature) program needs to execute. The
    Run_RGRD function executes the Rangrid program using the `GXRGRD` object.
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapRGRD(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXRGRD`
        
        :returns: A null `GXRGRD`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of `GXRGRD` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of `GXRGRD`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous



    def clear(self):
        """
        Clears all the parameters in a `GXRGRD` object

        **Note:**

        DLL name `clear`
        """
        self._wrapper.clear()
        



    @classmethod
    def create(cls):
        """
        Create a handle to a Rangrid object

        **Note:**

        The Rangrid object is initially empty. It will store the
        control file parameters which the Rangrid program needs
        to execute. Use the LoadParms_RGRD method to get the
        control file parameters into the `GXRGRD` object.
        """
        ret_val = gxapi_cy.WrapRGRD.create(GXContext._get_tls_geo())
        return GXRGRD(ret_val)



    @classmethod
    def create_img(cls, v_vx, v_vy, v_vz, ipj, ctl, grid):
        """
        Run Rangrid directly on XYZ `GXVV` data, output to an `GXIMG`.

        **Note:**

        If the grid file name is defined, the `GXIMG` is tied to a new output file.
        If the grid file name is not defined, the `GXIMG` is memory-based; not
        tied to a file.
        """
        ret_val = gxapi_cy.WrapRGRD.create_img(GXContext._get_tls_geo(), v_vx._wrapper, v_vy._wrapper, v_vz._wrapper, ipj._wrapper, ctl.encode(), grid.encode())
        return GXIMG(ret_val)






    def default(self, zchan, in_dat):
        """
        Set the defaults.
        """
        ret_val = self._wrapper.default(zchan.encode(), in_dat._wrapper)
        return ret_val




    def load_parms(self, file):
        """
        Retrieves a Rangrid object's control parameters from a file,
        or sets the parameters to default if the file doesn't exist.

        **Note:**

        If the control file name passed into this function is a file
        which does not exist, then the defaults for a Rangrid control
        file will be generated and put into the `GXRGRD` object.
        Otherwise, the control file's settings are retrieved from
        the file and loaded into the `GXRGRD` object.
        """
        ret_val = self._wrapper.load_parms(file.encode())
        return ret_val




    def run(self, in_dat, out_dat):
        """
        Executes the Rangrid program, using the input channel and
        output file parameters.
        """
        ret_val = self._wrapper.run(in_dat._wrapper, out_dat._wrapper)
        return ret_val



    @classmethod
    def run2(cls, db, x, y, z, ctl, grd):
        """
        Executes the Rangrid program directly on a database.
        """
        ret_val = gxapi_cy.WrapRGRD.run2(GXContext._get_tls_geo(), db._wrapper, x.encode(), y.encode(), z.encode(), ctl.encode(), grd.encode())
        return ret_val




    def save_parms(self, name):
        """
        Puts the Rangrid object's control parameters back into
        its control file.

        **Note:**

        If the control file did not previously exist, it will be
        created. Otherwise, the old file will be overwritten.
        """
        ret_val = self._wrapper.save_parms(name.encode())
        return ret_val



    @classmethod
    def run_vv(cls, v_vx, v_vy, v_vz, ipj, ctl, grd):
        """
        Executes the Rangrid program directly on input data VVs.
        """
        gxapi_cy.WrapRGRD.run_vv(GXContext._get_tls_geo(), v_vx._wrapper, v_vy._wrapper, v_vz._wrapper, ipj._wrapper, ctl.encode(), grd.encode())
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer