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
class GXVOXD:
    """
    GXVOXD class.

    `GXVOX` Display object.
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapVOXD(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXVOXD`
        
        :returns: A null `GXVOXD`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of `GXVOXD` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of `GXVOXD`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def create(cls, vox, table, zone, contour):
        """
        Create a new `GXVOXD`

        **Note:**

        Fails if the `GXVOX` object is NOT thematic.
        (See the `create_thematic` function.)
        """
        ret_val = gxapi_cy.WrapVOXD.create(GXContext._get_tls_geo(), vox._wrapper, table.encode(), zone, contour)
        return GXVOXD(ret_val)



    @classmethod
    def create_itr(cls, vox, itr):
        """
        Create a new `GXVOXD` with our own `GXITR`

        **Note:**

        Fails if the `GXVOX` object is thematic.
        (See the `create_thematic` function.)
        """
        ret_val = gxapi_cy.WrapVOXD.create_itr(GXContext._get_tls_geo(), vox._wrapper, itr._wrapper)
        return GXVOXD(ret_val)



    @classmethod
    def create_thematic(cls, vox):
        """
        Create a new `GXVOXD` for a thematic `GXVOX` object.

        **Note:**

        A thematic voxel is one where the stored integer values
        represent indices into an internally stored `GXTPAT` object.
        Thematic voxels contain their own color definitions, and
        normal numerical operations, such as applying ITRs for display,
        are not valid.
        
        To determine if a `GXVOX` object is thematic, use the
        `is_thematic` function.
        
        Fails if the `GXVOX` object is NOT thematic.
        """
        ret_val = gxapi_cy.WrapVOXD.create_thematic(GXContext._get_tls_geo(), vox._wrapper)
        return GXVOXD(ret_val)




    def is_thematic(self):
        """
        Is this a thematic voxel?

        **Note:**

        A thematic voxel is one where the stored integer values
        represent indices into an internally stored `GXTPAT` object.
        Thematic voxels contain their own color definitions, and
        normal numerical operations, such as applying ITRs for display,
        are not valid.
        """
        ret_val = self._wrapper.is_thematic()
        return ret_val




    def get_thematic_info(self, tpat, vv):
        """
        Get a copy of a thematic voxel's `GXTPAT` object and a `GXVV` containing the current display selections.
        """
        self._wrapper.get_thematic_info(tpat._wrapper, vv._wrapper)
        




    def set_thematic_selection(self, vv):
        """
        Get a copy of a thematic voxel's `GXTPAT` object and a `GXVV` containing the current display selections.
        """
        self._wrapper.set_thematic_selection(vv._wrapper)
        






    def get_draw_controls(self, box, trans, min_x, min_y, min_z, max_x, max_y, max_z):
        """
        Get the draw controls
        """
        box.value, trans.value, min_x.value, min_y.value, min_z.value, max_x.value, max_y.value, max_z.value = self._wrapper.get_draw_controls(box.value, trans.value, min_x.value, min_y.value, min_z.value, max_x.value, max_y.value, max_z.value)
        




    def get_name(self, name):
        """
        Gets the file name of the voxel.
        """
        name.value = self._wrapper.get_name(name.value.encode())
        




    def get_itr(self, itr):
        """
        Get the `GXITR` of the `GXVOXD`
        """
        self._wrapper.get_itr(itr._wrapper)
        




    def get_shell_controls(self, min, max):
        """
        Get the shell controls
        """
        min.value, max.value = self._wrapper.get_shell_controls(min.value, max.value)
        




    def set_draw_controls(self, box, trans, min_x, min_y, min_z, max_x, max_y, max_z):
        """
        Set the draw controls
        """
        self._wrapper.set_draw_controls(box, trans, min_x, min_y, min_z, max_x, max_y, max_z)
        




    def set_itr(self, itr):
        """
        Set the `GXITR` of the `GXVOXD`
        """
        self._wrapper.set_itr(itr._wrapper)
        




    def set_shell_controls(self, min, max):
        """
        Set the shell controls
        """
        self._wrapper.set_shell_controls(min, max)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer