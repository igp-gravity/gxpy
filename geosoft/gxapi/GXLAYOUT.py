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
class GXLAYOUT:
    """
    GXLAYOUT class.

    Layout class for generic relative layout calculation
    
    The relative layout algorithm allows a logical organization of layout rectangles.
    You can set constraints with English-like semantics. For example:
    
    "Set the left side of rectangle 1 equal to the right side of rectangle 2 plus 10 pixels."
    "Set the bottom of rectangle 1 to 25 percent of the height of rectangle 2."
    "Move node 1 such that its bottom is equal to the top of rectangle 2 minus 10 pixels."
    
    The last constraint set would enjoy priority over any others as it would be
    the last one that would influence the rectangle calculations. See the notes for iSetConstraint
    for more details.
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapLAYOUT(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXLAYOUT`
        
        :returns: A null `GXLAYOUT`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of `GXLAYOUT` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of `GXLAYOUT`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous



    def calculate_rects(self, min_x, min_y, max_x, max_y):
        """
        Calculate new positions based on initial conditions and constraints

        **Note:**

        Use iGetRectangle to obtain the results for the other rectangles. Depending
        on the constraints set the parent rectangle may also change
        after the calculation (returned here for convenience).
        """
        min_x.value, min_y.value, max_x.value, max_y.value = self._wrapper.calculate_rects(min_x.value, min_y.value, max_x.value, max_y.value)
        




    def clear_all(self):
        """
        Remove all children and constraints from layout
        """
        self._wrapper.clear_all()
        




    def clear_constraints(self):
        """
        Remove all constraints from layout
        """
        self._wrapper.clear_constraints()
        



    @classmethod
    def create(cls, num, p2):
        """
        Creates a layout calculation object
        """
        ret_val = gxapi_cy.WrapLAYOUT.create(GXContext._get_tls_geo(), num, p2.encode())
        return GXLAYOUT(ret_val)






    def get_rectangle(self, rect, p3, p4, p5, p6):
        """
        Gets the current bounds for a rectangle or the parent layout
        """
        p3.value, p4.value, p5.value, p6.value = self._wrapper.get_rectangle(rect, p3.value, p4.value, p5.value, p6.value)
        




    def get_rect_name(self, rect, p3):
        """
        Gets an optional name the current info for a rectangle or the parent layout
        """
        p3.value = self._wrapper.get_rect_name(rect, p3.value.encode())
        




    def add_constraint(self, rect_from, p3, p4, p5, p6, p7):
        """
        Add a constraint between any two rectangles or to one with absolute positioning

        **Note:**

        Constraints can be applied between 2 rectangles in the layout, or to 1 rectangle with
        absolute positioning. Use the constraints to control left, right, bottom, top,
        width, height, or centering configurations. Examples:
        
        (ordered as rectangle from, constraint from, rectangle to, constraint to, offset modifier, multiplicative modifier)
        
        A, `LAYOUT_CONSTR_LEFT`, B, `LAYOUT_CONSTR_LEFT`, 0, 0, 1.0 		               Set left position of A equal to left pos of B
        A, `LAYOUT_CONSTR_LEFT`, B, `LAYOUT_CONSTR_RIGHT`, 0, 0, 1.0		               Set left pos of A equal to right of B
        
        The offset modifier is used for additive manipulation of constraints
        A, `LAYOUT_CONSTR_LEFT`, B, `LAYOUT_CONSTR_LEFT`, 10, 0, 1.0		               Set left pos of A equal to left of B, plus 10
        A, `LAYOUT_CONSTR_BOTTOM`, B, `LAYOUT_CONSTR_TOP`, -20, 0, 1.0	               Set bottom of A equal to top of B, minus 20
        
        Multiplicative manipulation of constraints
        A, `LAYOUT_CONSTR_WIDTH`, B, `LAYOUT_CONSTR_WIDTH`, 0, 0.5	                  Set the width of A equal to 0.5 times the width of B
        A, `LAYOUT_CONSTR_HEIGHT`, B, `LAYOUT_CONSTR_WIDTH`, 0, 1.2	                  Set the height of A equal to 1.2 times the width of B
        
        You can use BOTH the multiplicative and offset modifiers in conjunction (multiplicative gets precedence)
        A, `LAYOUT_CONSTR_WIDTH`, B, `LAYOUT_CONSTR_WIDTH`, 10, 0.5 	                  A(width) = (0.5 * B(width)) + 10
        A, `LAYOUT_CONSTR_LEFT`, B, `LAYOUT_CONSTR_WIDTH`, -20, 0.1	                  A(left) = (0.1 * B(width)) + (-20)
        
        If second node is -2, use absolute positioning
        A,`LAYOUT_CONSTR_LEFT`,-2,<ignored>,25,<ignored>,<ignored> 	               Position left of A at position 25
        A,`LAYOUT_CONSTR_WIDTH`,-2,<ignored>,30,<ignored>,<ignored>	               Set width of A to 30
        
        Use the MOVE constraints to move an entire window without resizing
        A, `LAYOUT_CONSTR_MOVEL`, B, `LAYOUT_CONSTR_LEFT`, 0, 0, 1.0	                  Move node A, align left with left side of B
        A, `LAYOUT_CONSTR_MOVEL`, B, `LAYOUT_CONSTR_RIGHT`, 0, 0, 1.0	               Move node A, align left with right side of B
        A, `LAYOUT_CONSTR_MOVET`, B, `LAYOUT_CONSTR_WIDTH`, 0, 0, 1.0	               Move node A, align bottom to position equal to width of B
        A, `LAYOUT_CONSTR_MOVER`, B, `LAYOUT_CONSTR_RIGHT`, 10, 1.1	                  Move node A, align right to 1.1*right of B, plus 10
        A, `LAYOUT_CONSTR_MOVEL`, NULL, 10, 0, 1.0	                                 Move node A, align left at position 10
        """
        ret_val = self._wrapper.add_constraint(rect_from, p3, p4, p5, p6, p7)
        return ret_val




    def add_rectangle(self, min_x, min_y, max_x, max_y):
        """
        Adds a rectangle as one of the layout's children (Higer.
        """
        ret_val = self._wrapper.add_rectangle(min_x, min_y, max_x, max_y)
        return ret_val




    def num_rectangles(self):
        """
        Returns the number of children in the list.
        """
        ret_val = self._wrapper.num_rectangles()
        return ret_val




    def set_rectangle(self, rect, p3, p4, p5, p6):
        """
        Sets the current bounds for a rectangle previously added to the layout
        """
        self._wrapper.set_rectangle(rect, p3, p4, p5, p6)
        




    def set_rectangle_name(self, rect, p3):
        """
        Sets an optional name the current info for a rectangle or the parent layout
        """
        self._wrapper.set_rectangle_name(rect, p3.encode())
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer