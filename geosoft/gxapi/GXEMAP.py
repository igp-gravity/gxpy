### extends 'class_empty.py'
### block ClassImports
# NOTICE: Do not edit anything here, it is generated code
from typing import NewType
from . import gxapi_cy
from geosoft.gxapi import GXContext, float_ref, int_ref, str_ref
from .GXE3DV import GXE3DV
from .GXMAP import GXMAP


### endblock ClassImports

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXEMAP:
    """
    GXEMAP class.

    The `GXEMAP` class provides access to a map as displayed within
    Oasis montaj, but (usually) does not change data within the map itself.
    It performs functions such as setting the currently displayed area,
    or drawing "tracking" lines or boxes on the map (which are not
    part of the map itself).

    **Note:**

    To obtain access to the map itself, it is recommended practice
    to begin with an `GXEMAP` object, and use the `lock` function to
    lock the underlying map to prevent external changes. The returned
    `GXMAP` object (see `GXMAP`) may then be safely used to make changes to the map itself.
    
    `GXMAP` Redraw Rules:
    
        1. Redraws only occur at the end of the proccess (GX or SCRIPT) not during.
           You can safely call other GX's and the map will not redraw. If you need the
           map to redraw immediately use `redraw` instead.
        2. If the final GX calls `GXSYS.cancel_`, the map redraw is not done. If you
           need to force a redraw when the user hits cancel use the `redraw` function.
        3. You can set the redraw flag to `EMAP_REDRAW_YES` or `EMAP_REDRAW_NO` at any
            time using `set_redraw_flag`. This flag will only be looked at, when
            the last call to `un_lock` occurs and is ignored on a `GXSYS.cancel_`.
        4. `redraw` only works if the current map is not locked. It will do nothing
           if the map is locked.  Issue an `un_lock` before using this function.
    
    
    VIRTUAL `GXEMAP` SUPPORT
    
    These methods are only available when running in an external application.
    They allow the GX to open a `GXMAP` and then create a Virtual `GXEMAP` from that
    map. The GX can then call `make_current` and set the current `GXEMAP` so
    that code that follows sees this map as the current `GXMAP`.
    
    Supported methods on Virtual EMAPS are:
    
        | `current`
        | `current_no_activate`
        | `make_current`
        | `have_current`
        | `current_if_exists`
        | `GXMAP.current`
        | `lock`
        | `un_lock`
        | `is_locked`
        | `get_name`
        | `set_redraw_flag`
        | `redraw`
        | `loaded`
        | `load`
        | `load_no_activate`
        | `un_load_verify`
        | `un_load`
        | `create_virtual`
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapEMAP(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXEMAP`
        
        :returns: A null `GXEMAP`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of `GXEMAP` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of `GXEMAP`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Drag-and-drop methods



    def drop_map_clip_data(self, hglobal):
        """
        Drop Map clipboard data on this `GXEMAP`
        """
        self._wrapper.drop_map_clip_data(hglobal)
        




    def drag_drop_enabled(self):
        """
        Is drag-and-drop enabled for the map?
        """
        ret_val = self._wrapper.drag_drop_enabled()
        return ret_val




    def set_drag_drop_enabled(self, enable):
        """
        Set whether drag-and-drop is enabled for the map.
        """
        self._wrapper.set_drag_drop_enabled(enable)
        




# Drawing



    def copy_to_clip(self):
        """
        Copy entire map to clipboard.

        **Note:**

        Four objects are placed on the clipboard:
        
            1. Georefernce Text
            2. Bitmap of current window screen resolution
            3. EMF of current window screen resolution
            4. Entire map as a Geosoft View (go to view mode and hit paste). The coordinates are placed
               in the current view coordinates.
        """
        self._wrapper.copy_to_clip()
        




    def draw_line(self, min_x, min_y, max_x, max_y):
        """
        Draws a line on the current map.

        **Note:**

        Locations are in the current view user units.
        
        The line is temporary and will disappear on the next
        screen refresh.  This function is for you to provide
        interactive screen feedback to your user.
        """
        self._wrapper.draw_line(min_x, min_y, max_x, max_y)
        




    def draw_rect(self, min_x, min_y, max_x, max_y):
        """
        Draws a rect on the current map.

        **Note:**

        Locations are in the current view user units.
        
        The line is temporary and will disappear on the next
        screen refresh.  This function is for you to provide
        interactive screen feedback to your user.
        """
        self._wrapper.draw_rect(min_x, min_y, max_x, max_y)
        




    def draw_rect_3d(self, x, y, z, pix):
        """
        Plot a square symbol on a section view.

        **Note:**

        Plot a square symbol on a section view, but input 3D user coordinates
        
        The line is temporary and will disappear on the next
        screen refresh.  This function is for you to provide
        interactive screen feedback to your user.
        """
        self._wrapper.draw_rect_3d(x, y, z, pix)
        




    def get_display_area(self, min_x, min_y, max_x, max_y):
        """
        Get the area you are currently looking at.

        **Note:**

        Coordinates are based on the current view units.
        For 3D views this will return the full map extents.
        """
        min_x.value, min_y.value, max_x.value, max_y.value = self._wrapper.get_display_area(min_x.value, min_y.value, max_x.value, max_y.value)
        




    def get_display_area_raw(self, min_x, min_y, max_x, max_y):
        """
        Get the area you are currently looking at in raw map units

        **Note:**

        Coordinates are in millimeters.
        For 3D views this will return the full map extents.
        """
        min_x.value, min_y.value, max_x.value, max_y.value = self._wrapper.get_display_area_raw(min_x.value, min_y.value, max_x.value, max_y.value)
        




    def get_map_layout_props(self, snap_to_grid, snap_dist, view_grid, view_rulers, view_units, grid_red, grid_green, grid_blue):
        """
        Get the base layout view properties.

        **Note:**

        This affects the display units and other related properties for the base
        view of a map.
        """
        snap_to_grid.value, snap_dist.value, view_grid.value, view_rulers.value, view_units.value, grid_red.value, grid_green.value, grid_blue.value = self._wrapper.get_map_layout_props(snap_to_grid.value, snap_dist.value, view_grid.value, view_rulers.value, view_units.value, grid_red.value, grid_green.value, grid_blue.value)
        




    def get_map_snap(self, snap):
        """
        Get current snapping distance in MM
        """
        snap.value = self._wrapper.get_map_snap(snap.value)
        




    def get_window_state(self):
        """
        Retrieve the current state of the map window
        """
        ret_val = self._wrapper.get_window_state()
        return ret_val




    def set_display_area(self, min_x, min_y, max_x, max_y):
        """
        Set the area you wish to see.

        **Note:**

        Coordinates are based on the current view user units.
        The map is immediatly redrawn.
        """
        self._wrapper.set_display_area(min_x, min_y, max_x, max_y)
        




    def set_map_layout_props(self, snap_to_grid, snap_dist, view_grid, view_rulers, view_units, grid_red, grid_green, grid_blue):
        """
        Set the base layout view properties.

        **Note:**

        This affects the display units and other related properties for the base
        view of a map.
        """
        self._wrapper.set_map_layout_props(snap_to_grid, snap_dist, view_grid, view_rulers, view_units, grid_red, grid_green, grid_blue)
        




    def set_map_snap(self, snap):
        """
        Set current snapping distance in MM
        """
        self._wrapper.set_map_snap(snap)
        




    def set_window_state(self, state):
        """
        Changes the state of the map window
        """
        self._wrapper.set_window_state(state)
        




# General



    def packed_files(self):
        """
        The number of packed files in the map.
        """
        ret_val = self._wrapper.packed_files()
        return ret_val




    def activate_group(self, view_group):
        """
        Activates a group and associated tools.

        **Note:**

        Activating a group basically enters the edit mode associated
        with the type of group. E.g. a vector group will enable the
        edit toolbar for that gorup and an `GXAGG` will bring up the
        image color tool. Be sure to pass a combined name containing
        both the view name and the group separated by a "/" or "\\".
        """
        self._wrapper.activate_group(view_group.encode())
        




    def activate_view(self, view):
        """
        Activates a view and associated tools.
        """
        self._wrapper.activate_view(view.encode())
        



    @classmethod
    def current(cls):
        """
        This method returns the Current Edited map.
        """
        ret_val = gxapi_cy.WrapEMAP.current(GXContext._get_tls_geo())
        return GXEMAP(ret_val)



    @classmethod
    def current_no_activate(cls):
        """
        This method returns the Current Edited map.

        **Note:**

        This function acts just like `current` except that the document is not activated (brought to foreground) and no
        guarantee is given about which document is currently active.
        """
        ret_val = gxapi_cy.WrapEMAP.current_no_activate(GXContext._get_tls_geo())
        return GXEMAP(ret_val)



    @classmethod
    def current_if_exists(cls):
        """
        This method returns the Current Edited map.
        """
        ret_val = gxapi_cy.WrapEMAP.current_if_exists(GXContext._get_tls_geo())
        return GXEMAP(ret_val)






    def destroy_view(self, unload_flag):
        """
        Removes the view from the workspace.

        **Note:**

        Can only be run in interactive mode. After this call the
        `GXEMAP` object will become invalid. If this is the last view on
        the document and the document has been modified the map will be
        unloaded and optionally saved depending on the `EMAP_REMOVE`
        parameter.
        """
        self._wrapper.destroy_view(unload_flag)
        




    def font_lst(self, lst, which):
        """
        List all Windows and geosoft fonts.

        **Note:**

        To get TT and GFN fonts, call twice with the same list
        and `EMAP_FONT_TT`, then `EMAP_FONT_GFN`, or vice-versa to
        change order of listing.
        """
        self._wrapper.font_lst(lst._wrapper, which)
        




    def change_current_view(self, view):
        """
        Change the current working view.

        **Note:**

        This function operates on the current map.
        Unlike `set_current_view` this function's action
        survive the GX finishing.
        """
        ret_val = self._wrapper.change_current_view(view.encode())
        return ret_val




    def create_group_snapshot(self, lst):
        """
        Loads an `GXLST` with the current view/group names
        existing in a map. Typically used to track group
        changes that are about to occur.
        """
        ret_val = self._wrapper.create_group_snapshot(lst._wrapper)
        return ret_val




    def get_3d_view_name(self, name):
        """
        Get the name of a 3D view if the current view is 3D.
        """
        name.value = self._wrapper.get_3d_view_name(name.value.encode())
        




    def get_current_group(self, group):
        """
        Get the current group name.

        **Note:**

        This function operates on the current map.
        """
        group.value = self._wrapper.get_current_group(group.value.encode())
        




    def get_current_view(self, view):
        """
        Get the current view name.

        **Note:**

        This function operates on the current map.
        """
        view.value = self._wrapper.get_current_view(view.value.encode())
        



    @classmethod
    def get_maps_lst(cls, lst, path):
        """
        Load the file names of open maps into a `GXLST`.
        """
        ret_val = gxapi_cy.WrapEMAP.get_maps_lst(GXContext._get_tls_geo(), lst._wrapper, path)
        return ret_val




    def get_name(self, name):
        """
        Get the name of the map object of this `GXEMAP`.
        """
        name.value = self._wrapper.get_name(name.value.encode())
        



    @classmethod
    def have_current(cls):
        """
        This method returns whether a current map is loaded
        """
        ret_val = gxapi_cy.WrapEMAP.have_current(GXContext._get_tls_geo())
        return ret_val



    @classmethod
    def i_get_specified_map_name(cls, field, value, name):
        """
        Find a loaded map that has a setting in its reg.
        """
        ret_val, name.value = gxapi_cy.WrapEMAP.i_get_specified_map_name(GXContext._get_tls_geo(), field.encode(), value.encode(), name.value.encode())
        return ret_val




    def is_grid(self):
        """
        Is the map a grid map?
        """
        ret_val = self._wrapper.is_grid()
        return ret_val



    @classmethod
    def reload_grid(cls, name):
        """
        Reloads a grid document.

        **Note:**

        Use this method to reload (if loaded) a grid document if the file on disk changed.
        """
        gxapi_cy.WrapEMAP.reload_grid(GXContext._get_tls_geo(), name.encode())
        




    def is_3d_view(self):
        """
        Is the current view a 3D view.
        """
        ret_val = self._wrapper.is_3d_view()
        return ret_val




    def get_e_3dv(self):
        """
        Get an `GXE3DV` from the `GXEMAP`
        """
        ret_val = self._wrapper.get_e_3dv()
        return GXE3DV(ret_val)




    def is_locked(self):
        """
        Is this Map locked
        """
        ret_val = self._wrapper.is_locked()
        return ret_val



    @classmethod
    def loaded(cls, name):
        """
        Returns 1 if a map is loaded .
        """
        ret_val = gxapi_cy.WrapEMAP.loaded(GXContext._get_tls_geo(), name.encode())
        return ret_val




    def read_only(self):
        """
        Checks if a map is currently opened in a read-only mode.
        """
        ret_val = self._wrapper.read_only()
        return ret_val




    def get_window_position(self, left, top, right, bottom, state, is_floating):
        """
        Get the map window's position and dock state
        """
        left.value, top.value, right.value, bottom.value, state.value, is_floating.value = self._wrapper.get_window_position(left.value, top.value, right.value, bottom.value, state.value, is_floating.value)
        




    def set_window_position(self, left, top, right, bottom, state, is_floating):
        """
        Get the map window's position and dock state
        """
        self._wrapper.set_window_position(left, top, right, bottom, state, is_floating)
        




    def doubleize_group_snapshot(self, state):
        """
        The `GXLST` passed in must contain View\\Group strings in
        the Name field only. The function will compare with
        a more current `GXLST` and zoom the map to the new entry.

        **Note:**

        Typically this function is used in conjunction with
        CreateSnapshot_EMAP.
        """
        ret_val = self._wrapper.doubleize_group_snapshot(state._wrapper)
        return ret_val




    def set_current_view(self, view):
        """
        Set the current working view.

        **Note:**

        This function operates on the current map.
        It changes the view only during the execution of the
        GX. As soon as the GX terminates the view will revert
        to the original one.
        """
        ret_val = self._wrapper.set_current_view(view.encode())
        return ret_val




    def get_view_ipj(self, view, ipj):
        """
        Get a view's `GXIPJ`.

        **Note:**

        This function can be used to obtain a views coordinate system 
        without having to call `lock`. This could be an expensive operation
        that cause undesirable UX.
        """
        self._wrapper.get_view_ipj(view.encode(), ipj._wrapper)
        



    @classmethod
    def load(cls, name):
        """
        Loads maps into the editor.

        **Note:**

        The last map in the list will be the current map.
        
        Maps may already be loaded.
        
        Only the first file in the list may have a directory path.
        All other files in the list are assumed to be in the same
        directory as the first file.
        """
        ret_val = gxapi_cy.WrapEMAP.load(GXContext._get_tls_geo(), name.encode())
        return GXEMAP(ret_val)



    @classmethod
    def load_no_activate(cls, name):
        """
        Loads documents into the workspace

        **Note:**

        This function acts just like `load` except that the document(s) is not activated (brought to foreground) and no
        guarantee is given about which document is currently active.
        """
        ret_val = gxapi_cy.WrapEMAP.load_no_activate(GXContext._get_tls_geo(), name.encode())
        return GXEMAP(ret_val)



    @classmethod
    def load_with_view(cls, name, p2):
        """
        Load an `GXEMAP` with the view from a current `GXEMAP`.

        **Note:**

        Can only be run in interactive mode. Is used by
        dbsubset to create a new database with the same
        view as previously.
        """
        ret_val = gxapi_cy.WrapEMAP.load_with_view(GXContext._get_tls_geo(), name.encode(), p2._wrapper)
        return GXEMAP(ret_val)




    def lock(self):
        """
        This method locks the Edited map.

        **Note:**

        The Redraw flag is set to `EMAP_REDRAW_YES` when this functions is called.
        """
        ret_val = self._wrapper.lock()
        return GXMAP(ret_val)




    def make_current(self):
        """
        Makes this `GXEMAP` object the current active object to the user.
        """
        self._wrapper.make_current()
        




    def print_(self, entire_map, scale_to_fit, print_to_file, all_pages, centre, copies, first_page, last_page, scale_factor, overlap_size, offset_x, offset_y, file):
        """
        Print the current map to current printer.
        """
        self._wrapper.print_(entire_map, scale_to_fit, print_to_file, all_pages, centre, copies, first_page, last_page, scale_factor, overlap_size, offset_x, offset_y, file.encode())
        




    def redraw(self):
        """
        Redraw the map immediately.

        **Note:**

        Redraws the map immediately. Map must not be locked.
        """
        self._wrapper.redraw()
        




    def select_group(self, view_group):
        """
        Select a group.
        """
        self._wrapper.select_group(view_group.encode())
        




    def set_redraw_flag(self, redraw):
        """
        Set the redraw flag.

        **Note:**

        This function is generally used to prevent redrawing of
        the map, which normally occurs after the last `un_lock`
        call, in cases where it is known that no changes are being
        made to the map.
        
        Typical usage:
        
        ap = `lock`(EMap);
        etRedrawFlag_EMAP(EMap,`EMAP_REDRAW_NO`);
        
        Stuff....
        
        `un_lock`(Map);
        """
        self._wrapper.set_redraw_flag(redraw)
        



    @classmethod
    def un_load(cls, name):
        """
        Unloads a `GXMAP`.

        **Note:**

        If the `GXMAP` is not loaded, nothing happens.
        Same as `un_load_verify` with FALSE to prompt save.
        """
        gxapi_cy.WrapEMAP.un_load(GXContext._get_tls_geo(), name.encode())
        



    @classmethod
    def un_load_all(cls):
        """
        Unloads all opened maps
        """
        gxapi_cy.WrapEMAP.un_load_all(GXContext._get_tls_geo())
        



    @classmethod
    def un_load_verify(cls, name, prompt):
        """
        Unloads an edited map, optional prompt to save.

        **Note:**

        If the map is not loaded, nothing happens.
        If "FALSE", map is saved without a prompt.
        """
        gxapi_cy.WrapEMAP.un_load_verify(GXContext._get_tls_geo(), name.encode(), prompt)
        




    def un_lock(self):
        """
        This method unlocks the Edited map.
        """
        self._wrapper.un_lock()
        




# Input



    def get_cur_point(self, x, y):
        """
        Returns the coordinates of the currently selected point in view coordinates
        """
        x.value, y.value = self._wrapper.get_cur_point(x.value, y.value)
        




    def get_cur_point_mm(self, x, y):
        """
        Returns the coordinates of the currently selected point in mm on map
        """
        x.value, y.value = self._wrapper.get_cur_point_mm(x.value, y.value)
        




    def get_cursor(self, x, y):
        """
        Returns the coordinates of the last known cursor location
        """
        x.value, y.value = self._wrapper.get_cursor(x.value, y.value)
        




    def get_cursor_mm(self, x, y):
        """
        Returns the coordinates of the last known cursor location in mm on map.
        """
        x.value, y.value = self._wrapper.get_cursor_mm(x.value, y.value)
        




    def digitize(self, wa, img, digits, prompt, prefix, delim, newline):
        """
        Digitise points from the current map and place in a `GXWA`.

        **Note:**

        The command line will start to recieve digitized points
        from the mouse.  Whenever the left mouse button is
        pressed, the current view X,Y are placed on the workspace
        command line.  If a valid `GXIMG` is passed, the Z value is
        also placed on the command line.  If auto-newline is
        specified, the line is immediately placed into `GXWA`,
        otherwise the user has the oportunity to enter data
        before pressing Enter.
        
        Locations are in the current view user units
        """
        ret_val = self._wrapper.digitize(wa._wrapper, img._wrapper, digits, prompt.encode(), prefix.encode(), delim.encode(), newline)
        return ret_val




    def digitize2(self, vvx, vvy, vvz, img, prompt, newline):
        """
        Digitise points from the current map and place in VVs.

        **Note:**

        The command line will start to recieve digitized points
        from the mouse.  Whenever the left mouse button is
        pressed, the current view X,Y are placed on the workspace
        command line.  If a valid `GXIMG` is passed, the Z value is
        also placed on the command line.  If auto-newline is
        specified, the line is immediately placed into the VVs,
        otherwise the user has the oportunity to enter data
        before pressing Enter.
        
        Locations are in the current view user units
        """
        ret_val = self._wrapper.digitize2(vvx._wrapper, vvy._wrapper, vvz._wrapper, img._wrapper, prompt.encode(), newline)
        return ret_val




    def digitize_peaks(self, vvx, vvy, vvz, img, prompt, newline):
        """
        Digitise points from the current map and place in VVs.

        **Note:**

        Same as `digitize2`, but the closest peaks to the selected locations are
        returned instead of the selected location. The method chooses the highest value
        of the 8 surrounding points, the repeats this process until no higher value can
        be found in any of the 8 surrounding points. If there are two or more points with
        a higher value, it will just take the first one and continue, and this method will
        stall on flat areas as well (since no surrounding point is larger).
        """
        ret_val = self._wrapper.digitize_peaks(vvx._wrapper, vvy._wrapper, vvz._wrapper, img._wrapper, prompt.encode(), newline)
        return ret_val




    def digitize_polygon(self, vvx, vvy, vvz, img, prompt, newline, pixel_radius):
        """
        Same as iDigitze2_EMAP, but automatically close polygons.

        **Note:**

        This is the same as `digitize2`, except that it automatically
        detects, (except for the 2nd and 3rd points) when a selected location
        is within the entered number of pixels from the starting point. If yes,
        the polygon is assumed to be closed, and the operation is the same as
        the RMB "done" command, and the process returns 0.
        """
        ret_val = self._wrapper.digitize_polygon(vvx._wrapper, vvy._wrapper, vvz._wrapper, img._wrapper, prompt.encode(), newline, pixel_radius)
        return ret_val




    def get_box(self, str_val, min_x, min_y, max_x, max_y):
        """
        Returns the coordinates of a user selected box.
        """
        ret_val, min_x.value, min_y.value, max_x.value, max_y.value = self._wrapper.get_box(str_val.encode(), min_x.value, min_y.value, max_x.value, max_y.value)
        return ret_val




    def get_box2(self, str_val, x1, y1, x2, y2, x3, y3, x4, y4):
        """
        Returns the coordinates of a user selected box in a warped view.

        **Note:**

        If the data view has a rotational (or other) warp, then the
        `get_box` function returns only opposite diagonal points in the
        box, not enough info to determine the other two corners. This
        function returns the exact coordinates of all four corners, calculated
        from the pixel locations.
        """
        ret_val, x1.value, y1.value, x2.value, y2.value, x3.value, y3.value, x4.value, y4.value = self._wrapper.get_box2(str_val.encode(), x1.value, y1.value, x2.value, y2.value, x3.value, y3.value, x4.value, y4.value)
        return ret_val




    def get_grid(self, str_val, nx, ny, angle, x1, y1, x_len, y_len):
        """
        Position and size a grid on a map.

        **Note:**

        If the input angle is `rDUMMY`, an extra step is inserted
        for the user to define the angle by drawing a line
        with the mouse.
        The output primary axis angle will always be in the
        range -90 < angle <= 90. The grid origin is shifted to
        whichever corner necessary to make this possible, while keeping
        the secondary axis at 90 degrees greater than the primary (
        going counter-clockwise).
        The coordinates are returned in the current User projection
        (See `GXMVIEW.get_user_ipj` and `GXMVIEW.set_user_ipj`.)
        """
        ret_val, angle.value, x1.value, y1.value, x_len.value, y_len.value = self._wrapper.get_grid(str_val.encode(), nx, ny, angle.value, x1.value, y1.value, x_len.value, y_len.value)
        return ret_val




    def get_line(self, str_val, min_x, min_y, max_x, max_y):
        """
        Returns the end points of a line.

        **Note:**

        The coordinates are returned in the current User projection
        (See `GXMVIEW.get_user_ipj` and `GXMVIEW.set_user_ipj`.)
        """
        ret_val, min_x.value, min_y.value, max_x.value, max_y.value = self._wrapper.get_line(str_val.encode(), min_x.value, min_y.value, max_x.value, max_y.value)
        return ret_val




    def get_line_ex(self, str_val, min_x, min_y, max_x, max_y):
        """
        Returns the end points of a line.

        **Note:**

        The coordinates are returned in the current User projection
        (See `GXMVIEW.get_user_ipj` and `GXMVIEW.set_user_ipj`.)
        """
        ret_val, min_x.value, min_y.value, max_x.value, max_y.value = self._wrapper.get_line_ex(str_val.encode(), min_x.value, min_y.value, max_x.value, max_y.value)
        return ret_val




    def get_line_xyz(self, str_val, min_x, min_y, min_z, max_x, max_y, max_z):
        """
        Returns the end points of a line in X,Y and Z

        **Note:**

        The coordinates are returned in the current User projection
        (See `GXMVIEW.get_user_ipj` and `GXMVIEW.set_user_ipj`.)
        This is useful for digitizing a line in an oriented view and getting
        the true coordinates in (X, Y, Z) at the selected point on the view plane.
        """
        ret_val, min_x.value, min_y.value, min_z.value, max_x.value, max_y.value, max_z.value = self._wrapper.get_line_xyz(str_val.encode(), min_x.value, min_y.value, min_z.value, max_x.value, max_y.value, max_z.value)
        return ret_val




    def get_point(self, str_val, x, y):
        """
        Returns the coordinates of a user selected point.

        **Note:**

        This will wait for user to select a point.

        .. seealso::

            iTrackPoint, GetCurPoint, GetCursor
        """
        ret_val, x.value, y.value = self._wrapper.get_point(str_val.encode(), x.value, y.value)
        return ret_val




    def get_point_ex(self, str_val, x, y):
        """
        Returns the coordinates of a user selected point.

        **Note:**

        This will wait for user to select a point.

        .. seealso::

            iTrackPoint, GetCurPoint, GetCursor
        """
        ret_val, x.value, y.value = self._wrapper.get_point_ex(str_val.encode(), x.value, y.value)
        return ret_val




    def get_point_3d(self, str_val, x, y, z):
        """
        Returns the coordinates of a user selected point.

        **Note:**

        This will wait for user to select a point.

        .. seealso::

            iTrackPoint, GetCurPoint, GetCursor
        """
        ret_val, x.value, y.value, z.value = self._wrapper.get_point_3d(str_val.encode(), x.value, y.value, z.value)
        return ret_val




    def get_poly_line(self, str_val, v_vx, v_vy):
        """
        Returns a polyline.

        **Note:**

        The coordinates are returned in the current User projection
        (See `GXMVIEW.get_user_ipj` and `GXMVIEW.set_user_ipj`.)
        """
        ret_val = self._wrapper.get_poly_line(str_val.encode(), v_vx._wrapper, v_vy._wrapper)
        return ret_val




    def get_poly_line_xyz(self, str_val, v_vx, v_vy, v_vz):
        """
        Returns a polyline.

        **Note:**

        The coordinates are returned in the current User projection
        (See `GXMVIEW.get_user_ipj` and `GXMVIEW.set_user_ipj`.) In this version
        of the method X, Y and Z (depth) are returned. Initially created
        to deal with crooked sections.
        """
        ret_val = self._wrapper.get_poly_line_xyz(str_val.encode(), v_vx._wrapper, v_vy._wrapper, v_vz._wrapper)
        return ret_val




    def get_rect(self, str_val, min_x, min_y, max_x, max_y):
        """
        Returns the coordinates of a user selected box starting at a corner.

        **Note:**

        The coordinates are returned in the current User projection
        (See `GXMVIEW.get_user_ipj` and `GXMVIEW.set_user_ipj`.)
        If the user `GXIPJ` distorts the coordinates from being rectilinear
        (e.g. for a TriPlot graph), then care should be taken since the
        (Xmin, Ymin) and (Xmax, Ymax) values returned do not necessarily
        correspond to the lower-left and upper-right corners. In fact, the
        returned values are calculated by taking the starting (fixed) corner
        and the tracked (opposite) corner, and finding the min and max for
        X and Y among these two points. With a warped User projection, those
        two corner locations could easily be (Xmin, Ymax) and (Xmax, Ymin).
        This becomes quite important if you want to use the rectangle for a
        masking operation, because the "other" two corner's coordinates may
        need to be constructed based on a knowledge of the User projection,
        and may not be directly obtained from the returned X and Y min and
        max values. What appears to be a rectangle as seen on the map is not
        necessarily a rectangle in the User coordinates.
        """
        ret_val, min_x.value, min_y.value, max_x.value, max_y.value = self._wrapper.get_rect(str_val.encode(), min_x.value, min_y.value, max_x.value, max_y.value)
        return ret_val




    def track_point(self, flags, x, y):
        """
        Get point without prompt or cursor change with tracking
        """
        ret_val, x.value, y.value = self._wrapper.track_point(flags, x.value, y.value)
        return ret_val




# Map Viewport Mode Methods



    def get_aoi_area(self, min_x, min_y, max_x, max_y):
        """
        Get the area of interest.

        **Note:**

        Coordinates are based on the current view units.
        """
        min_x.value, min_y.value, max_x.value, max_y.value = self._wrapper.get_aoi_area(min_x.value, min_y.value, max_x.value, max_y.value)
        




    def set_aoi_area(self, min_x, min_y, max_x, max_y):
        """
        Set the area of interest.

        **Note:**

        Coordinates are based on the current view user units.
        The map is immediatly redrawn.
        """
        self._wrapper.set_aoi_area(min_x, min_y, max_x, max_y)
        




    def set_viewport_mode(self, mode):
        """
        Set the viewport mode.

        **Note:**

        This is handy for using a map to define an area of interest. Use in conjunction
        with Get/Set AOIArea. If this is used inside montaj it is important to set or provide
        for a method to set the map mode back to normal as this is not exposed in the interface.
        """
        self._wrapper.set_viewport_mode(mode)
        




# Tracking Methods



    def get_selected_vertices(self, v_vx, v_vy):
        """
        Get the verticies of selected object

        **Note:**

        Works only in Vertex Edit Mode
        """
        self._wrapper.get_selected_vertices(v_vx._wrapper, v_vy._wrapper)
        




# Virtual


    @classmethod
    def create_virtual(cls, name):
        """
        Makes this `GXEMAP` object the current active object to the user.
        """
        ret_val = gxapi_cy.WrapEMAP.create_virtual(GXContext._get_tls_geo(), name.encode())
        return GXEMAP(ret_val)




# External Window


    @classmethod
    def load_control(cls, map_file, window):
        """
        Version of `load` that can be used to load a database via subclassing into a Windows control.
        """
        gxapi_cy.WrapEMAP.load_control(GXContext._get_tls_geo(), map_file.encode(), window)
        



    @classmethod
    def load_with_view_control(cls, map_file, emap, window):
        """
        Version of `GXEDB.load_with_view` that can be used to load a database via subclassing into a Windows control.
        """
        gxapi_cy.WrapEMAP.load_with_view_control(GXContext._get_tls_geo(), map_file.encode(), emap._wrapper, window)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer