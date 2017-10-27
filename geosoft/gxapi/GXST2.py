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
class GXST2:
    """
    GXST2 class.

    Bi-variate statistics. The `GXST2` class accumulates statistics
    on two data vectors simultaneously in order to compute correlation
    information. Statistics are accumulated using the `data_vv` function.
    See also `GXST` (mono-variate statistics).
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapST2(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXST2`
        
        :returns: A null `GXST2`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of `GXST2` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of `GXST2`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def create(cls):
        """
        Creates a statistics object which is used to accumulate statistics.
        """
        ret_val = gxapi_cy.WrapST2.create(GXContext._get_tls_geo())
        return GXST2(ret_val)




    def data_vv(self, v_vx, v_vy):
        """
        Add all the values in VVx and VVy to `GXST2` object.
        """
        self._wrapper.data_vv(v_vx._wrapper, v_vy._wrapper)
        






    def items(self):
        """
        Gets Number of items
        """
        ret_val = self._wrapper.items()
        return ret_val




    def reset(self):
        """
        Resets the Statistics.
        """
        self._wrapper.reset()
        




    def get(self, id):
        """
        Gets correlation coeff. from the `GXST2` object.
        """
        ret_val = self._wrapper.get(id)
        return ret_val





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer