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
class GXSEMPLOT:
    """
    GXSEMPLOT class.

    Oasis montaj implementation of RTE `GXSEMPLOT`
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapSEMPLOT(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXSEMPLOT`
        
        :returns: A null `GXSEMPLOT`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of `GXSEMPLOT` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of `GXSEMPLOT`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def apply_filter_to_mask(cls, db, filter, mask_ch, mineral_ch, mineral, mode):
        """
        Apply the filter to the mask channel

        **Note:**

        The mask channel is updated for the current data to reflect
        the actions of the filter. Those values passing get 1, those
        failing get 0.
        """
        gxapi_cy.WrapSEMPLOT.apply_filter_to_mask(GXContext._get_tls_geo(), db._wrapper, filter.encode(), mask_ch.encode(), mineral_ch.encode(), mineral.encode(), mode)
        



    @classmethod
    def convert_dummies(cls, db, line):
        """
        Convert dummies to zero values for assay channels.

        **Note:**

        The is operation is controlled by the Preferences
        "Use dummies to indicate no data?" By default, this option is "yes"
        so this function will return with no changes. However, if
        "no", then all ASSAY class channels will have dummy values
        converted to 0.0.
        """
        gxapi_cy.WrapSEMPLOT.convert_dummies(GXContext._get_tls_geo(), db._wrapper, line)
        



    @classmethod
    def create_groups(cls, db, mask_ch):
        """
        Group data by anomaly or string channel - Interactive.
        """
        gxapi_cy.WrapSEMPLOT.create_groups(GXContext._get_tls_geo(), db._wrapper, mask_ch.encode())
        



    @classmethod
    def default_groups(cls, db):
        """
        Group data by selected anomalies.
        """
        gxapi_cy.WrapSEMPLOT.default_groups(GXContext._get_tls_geo(), db._wrapper)
        



    @classmethod
    def edit_map_plot_parameters(cls, db, mask_ch, mineral_ch, map, view):
        """
        Alter parameters in an XYplot Triplot map.

        **Note:**

        The Parameters `GXGUI` is loaded based on settings stored in
        the map. The map is then re-plotted, overwriting the old one,
        based on the new settings. Note that the selection of data
        in the current `GXDB` is used to replot the map.
        """
        gxapi_cy.WrapSEMPLOT.edit_map_plot_parameters(GXContext._get_tls_geo(), db._wrapper, mask_ch.encode(), mineral_ch.encode(), map._wrapper, view.encode())
        



    @classmethod
    def edit_plot_components(cls, db, template):
        """
        Set group names and channels to plot in a template.

        **Note:**

        The "Components" group in the INI file is edited.
        
        Looks first in user\\etc, then in \\etc.
        Looks first for file prefix "semtemplate" then "xyt" or "tri"
        The altered template will be output to the user\\etc directory with
        the file extension "semtemplate".
        """
        gxapi_cy.WrapSEMPLOT.edit_plot_components(GXContext._get_tls_geo(), db._wrapper, template.encode())
        



    @classmethod
    def edit_plot_parameters(cls, db, template):
        """
        Set TriPlot parameters in a template.

        **Note:**

        The "Parameters" group in the INI file is edited.
        
        Looks first in user\\etc, then in \\etc.
        Looks first for file prefix "semtemplate" then "xyt" or "tri"
        The altered template will be output to the user\\etc directory with
        the file extension "semtemplate".
        """
        gxapi_cy.WrapSEMPLOT.edit_plot_parameters(GXContext._get_tls_geo(), db._wrapper, template.encode())
        



    @classmethod
    def export_overlay(cls, overlay, map, mview, group, plot_type, x_stage, x_oxide, y_stage, y_oxide, z_stage, z_oxide, extension):
        """
        Create overlay map and file from a group.

        **Note:**

        The group is written to a new map, and an overlay file
        is created which points to this map.
        """
        gxapi_cy.WrapSEMPLOT.export_overlay(GXContext._get_tls_geo(), overlay.encode(), map.encode(), mview._wrapper, group.encode(), plot_type, x_stage.encode(), x_oxide.encode(), y_stage.encode(), y_oxide.encode(), z_stage.encode(), z_oxide.encode(), extension)
        



    @classmethod
    def export_view(cls, db, lst, p3, p4, p5, p6, p7):
        """
        Create a "View" database
        """
        gxapi_cy.WrapSEMPLOT.export_view(GXContext._get_tls_geo(), db._wrapper, lst._wrapper, p3._wrapper, p4, p5.encode(), p6.encode(), p7.encode())
        



    @classmethod
    def export_view2(cls, db, lst, p3, p4, p5, p6, p7, p8):
        """
        Create a "View" database, with channel selection
        """
        gxapi_cy.WrapSEMPLOT.export_view2(GXContext._get_tls_geo(), db._wrapper, lst._wrapper, p3._wrapper, p4, p5.encode(), p6.encode(), p7.encode(), p8)
        



    @classmethod
    def filter_lst(cls, lst):
        """
        Fill a `GXLST` with existing `GXSEMPLOT` filters

        **Note:**

        "Supplied" filters are stored in \\etc, while user-edited and new filters
        are stored in user\\etc. This function finds all files with the extension
        ".semfilter", first in user\\etc, then in \\etc, and adds the file names
        (without the extension) to the `GXLST`. The name with the extension is stored
        as the value.
        The `GXLST` is cleared first.
        """
        gxapi_cy.WrapSEMPLOT.filter_lst(GXContext._get_tls_geo(), lst._wrapper)
        



    @classmethod
    def filter_mineral_pos_data(cls, db, mask_ch, mineral_ch, mineral, pos):
        """
        Filter raw data by position and mineral values

        **Note:**

        The Mask channel will be updated so that those data values
        which "pass" get "1" and those that "fail" get dummy "*"
        NO DATA IS REMOVED.
        Works on all selected lines of data.
        """
        gxapi_cy.WrapSEMPLOT.filter_mineral_pos_data(GXContext._get_tls_geo(), db._wrapper, mask_ch.encode(), mineral_ch.encode(), mineral.encode(), pos)
        



    @classmethod
    def get_associated_lst(cls, db, group, lst):
        """
        Get the associated channels for this group in a `GXLST`
        """
        gxapi_cy.WrapSEMPLOT.get_associated_lst(GXContext._get_tls_geo(), db._wrapper, group, lst._wrapper)
        



    @classmethod
    def get_current_mineral_lst(cls, db, mineral_ch, lst):
        """
        Retrieve `GXLST` of minerals in selected lines.

        **Note:**

        If the mineral channel name is not specified, it returns
        just the "X" (Unknown) item.
        """
        gxapi_cy.WrapSEMPLOT.get_current_mineral_lst(GXContext._get_tls_geo(), db._wrapper, mineral_ch.encode(), lst._wrapper)
        



    @classmethod
    def get_current_position_lst(cls, db, lst):
        """
        Retrieve `GXLST` of positions in selected lines.
        """
        gxapi_cy.WrapSEMPLOT.get_current_position_lst(GXContext._get_tls_geo(), db._wrapper, lst._wrapper)
        



    @classmethod
    def get_full_mineral_lst(cls, lst):
        """
        Retrieve `GXLST` of all minerals in Semplot_Minerals.csv
        """
        gxapi_cy.WrapSEMPLOT.get_full_mineral_lst(GXContext._get_tls_geo(), lst._wrapper)
        



    @classmethod
    def get_full_position_lst(cls, lst):
        """
        Retrieve `GXLST` of all possible mineral positions.
        """
        gxapi_cy.WrapSEMPLOT.get_full_position_lst(GXContext._get_tls_geo(), lst._wrapper)
        



    @classmethod
    def get_grouping_lst(cls, db, lst):
        """
        Get list of items to group symbols by.

        **Note:**

        The first item is "Anomaly", which gives the line names, The second
        item (if the channel exists in the database) is the Sample Number.
        After this are included all string channels which are NOT oxides or
        elements. (The list can include the mineral).
        Channel symbol is the `GXLST` value (except for the first item - "Anomaly")
        """
        gxapi_cy.WrapSEMPLOT.get_grouping_lst(GXContext._get_tls_geo(), db._wrapper, lst._wrapper)
        



    @classmethod
    def create_ascii_template(cls, name, temp):
        """
        : Generate ASCII import template automatically
        """
        ret_val = gxapi_cy.WrapSEMPLOT.create_ascii_template(GXContext._get_tls_geo(), name.encode(), temp.encode())
        return ret_val



    @classmethod
    def create_database_template(cls, name, temp):
        """
        Generate database import template automatically
        """
        ret_val = gxapi_cy.WrapSEMPLOT.create_database_template(GXContext._get_tls_geo(), name.encode(), temp.encode())
        return ret_val



    @classmethod
    def edit_filter(cls, db, filter, mask_ch, mineral_ch, mineral):
        """
        Edit and create filter on channel values
        """
        ret_val = gxapi_cy.WrapSEMPLOT.edit_filter(GXContext._get_tls_geo(), db._wrapper, filter.encode(), mask_ch.encode(), mineral_ch.encode(), mineral.encode())
        return ret_val



    @classmethod
    def get_mineral_channel_name(cls, db, mineral_ch):
        """
        Retrieve the mineral channel name.

        **Note:**

        First looks at the `GXSEMPLOT`.MINERAL_CHANNEL value.
        If not found, returns the first MINERAL class
        channel found. If still not found, returns a
        blank string.
        """
        mineral_ch.value = gxapi_cy.WrapSEMPLOT.get_mineral_channel_name(GXContext._get_tls_geo(), db._wrapper, mineral_ch.value.encode())
        



    @classmethod
    def import_ascii_wizard(cls, name, temp, anomaly):
        """
        Generate a `GXSEMPLOT` ASCII import template.

        **Note:**

        If the anomaly name is not included, then
        the input data must have an "Anom_Name" field.
        """
        anomaly.value = gxapi_cy.WrapSEMPLOT.import_ascii_wizard(GXContext._get_tls_geo(), name.encode(), temp.encode(), anomaly.value.encode())
        



    @classmethod
    def import_database_odbc(cls, connection, temp):
        """
        Generate a template file for importing ODBC databases.
        """
        connection.value, temp.value = gxapi_cy.WrapSEMPLOT.import_database_odbc(GXContext._get_tls_geo(), connection.value.encode(), temp.value.encode())
        



    @classmethod
    def import_bin(cls, db, data, template, line, flight, date):
        """
        Import blocked binary or archive ASCII data

        **Note:**

        This wrapper is for `GXSEMPLOT`, and does not require the import licence.
        
           1. Binary import templates have extension .I2 by convention.  See
              BINARY.I2 for a description of the template format.
              Archive import templates have extension .I3 by convention. See
              ARCHIVE.I3 for a description of the template format.
        
           2. Both the import template and data file must exist.
        
           3. If a line already exists in the database, a new version is created
              unless a line name is passed in.  In this case, the specified name
              is used and the imported channels on the previous line will be
              destroyed.

        .. seealso::

            `GXDU.lab_template` in du.gxh
        """
        gxapi_cy.WrapSEMPLOT.import_bin(GXContext._get_tls_geo(), db._wrapper, data.encode(), template.encode(), line.encode(), flight, date)
        



    @classmethod
    def import_database_ado(cls, name, temp):
        """
        Generate a template file for importing semplot databases.
        """
        gxapi_cy.WrapSEMPLOT.import_database_ado(GXContext._get_tls_geo(), name.encode(), temp.encode())
        



    @classmethod
    def init_group_symbols_used(cls, db):
        """
        Initializes memory of symbols used in plotting.

        **Note:**

        Maintains a list of the symbols used in plotting. Call before
        Plotting one or more legends - symbols are accumulated.
        `plot_symbol_legend` uses this information to create a legend.
        """
        gxapi_cy.WrapSEMPLOT.init_group_symbols_used(GXContext._get_tls_geo(), db._wrapper)
        



    @classmethod
    def template_type(cls, template):
        """
        Create a new XYPlot or TriPlot template.
        """
        ret_val = gxapi_cy.WrapSEMPLOT.template_type(GXContext._get_tls_geo(), template.encode())
        return ret_val



    @classmethod
    def view_type(cls, map, view):
        """
        Test to see if a view is an XYPlot or Triplot view.

        **Note:**

        First checks the view name to see if it starts with
        ``"XYplt_"`` or ``"Triplt_"``. Failing that it looks in the
        view `GXREG` for a value for "Components.Type", which will
        be either "XYPlot" or "TriPlot".
        If the view does not appear to be an XYPlot or a TriPlot view,
        the function returns `SEMPLOT_PLOT_UNKNOWN`.
        """
        ret_val = gxapi_cy.WrapSEMPLOT.view_type(GXContext._get_tls_geo(), map._wrapper, view.encode())
        return ret_val



    @classmethod
    def mineral_id(cls, db, resid, min_ch, res_ch):
        """
        Identify minerals from the oxide channels.

        **Note:**

        Finds the best mineral matching the composition for each
        row of oxide values. Works using linear programming and
        the simplex method to maximize the oxides used to create
        each of the possible output minerals. The mineral leaving the
        least leftover is selected, as long as the residual (measured
        as a percent of the total) is less than or equal to the
        input value.
        """
        gxapi_cy.WrapSEMPLOT.mineral_id(GXContext._get_tls_geo(), db._wrapper, resid, min_ch, res_ch)
        



    @classmethod
    def new_filter(cls, filter, model):
        """
        Create a new selection filter.

        **Note:**

        Creates a new, empty filter file in the user\\etc directory
        """
        gxapi_cy.WrapSEMPLOT.new_filter(GXContext._get_tls_geo(), filter.encode(), model.encode())
        



    @classmethod
    def new_template(cls, template, type, model):
        """
        Create a new XYPlot or TriPlot template.

        **Note:**

        The new template is written to the user\\etc directory, with
        the file extension "semfilter". The template contains a parameter
        identifying it as an XY or Triplot.
        
        Model Template: Looks first in user\\etc, then in \\etc.
        Looks first for file prefix "semtemplate" then "xyt" or "tri"
        
        Because there are so many shared parameters, it is possible to use
        an XYPlot template as a model for a TriPlot, and vica-verca, with
        few complications.  (e.g. needing to define a "Z" component)
        """
        gxapi_cy.WrapSEMPLOT.new_template(GXContext._get_tls_geo(), template.encode(), type, model.encode())
        



    @classmethod
    def overlay_lst(cls, lst, extension, type):
        """
        Fill a list with the available plot overlay names

        **Note:**

        Looks first in user\\etc, then in \\etc.
        See `SEMPLOT_EXT` definitions above for which files to look for.
        """
        gxapi_cy.WrapSEMPLOT.overlay_lst(GXContext._get_tls_geo(), lst._wrapper, extension, type)
        



    @classmethod
    def plot(cls, db, template, mask_ch, mineral_ch, map, map_mode, plot_symb):
        """
        Plot an XYPlot or TriPlot based on the template.

        **Note:**

        The "Components" and "Parameters" groups in the INI file
        are used.
        Only values with mask values of 1 are plotted, if the mask
        channel is specified.
        
        Call "`reset_used_channel`" prior to this function
        in order to track the values actually plotted.
        
        Call `init_group_symbols_used` prior to this function
        to reset recording of the symbols used in plotting (for legends etc).
        """
        gxapi_cy.WrapSEMPLOT.plot(GXContext._get_tls_geo(), db._wrapper, template.encode(), mask_ch.encode(), mineral_ch.encode(), map.encode(), map_mode, plot_symb)
        



    @classmethod
    def plot_symbol_legend(cls, db, mview, x_min, y_min, y_max, symb_size):
        """
        Plot a symbol legend in a view.

        **Note:**

        This function depends on `init_group_symbols_used`
        before the plot for which this legend is created is made.
        The symbols and groups to use in the legend are stored to
        a database blob after the plot is made. These values are
        recovered by this function to make the legend at the
        specified location.
        """
        gxapi_cy.WrapSEMPLOT.plot_symbol_legend(GXContext._get_tls_geo(), db._wrapper, mview._wrapper, x_min, y_min, y_max, symb_size)
        



    @classmethod
    def prop_symb(cls, db, map, view, chan, mask_ch, mineral_ch, log, area, base, scale, symb, wt, line_col, fill_col, legend):
        """
        Plot a proportional symbol plot.

        **Note:**

        Replots map using proportional symbols
        """
        gxapi_cy.WrapSEMPLOT.prop_symb(GXContext._get_tls_geo(), db._wrapper, map._wrapper, view.encode(), chan.encode(), mask_ch.encode(), mineral_ch.encode(), log, area, base, scale, symb, wt, line_col, fill_col, legend)
        



    @classmethod
    def replot(cls, db, mask_ch, mineral_ch, map, view):
        """
        Replot an existing `GXSEMPLOT` plot based on current data.

        **Note:**

        Note that the selection of data
        in the current `GXDB` is used to replot the map.
        
        Call "`reset_used_channel`" prior to this function
        in order to track the values actually plotted.
        
        Call `init_group_symbols_used` prior to this function
        to reset recording of the symbols used in plotting (for legends etc).
        """
        gxapi_cy.WrapSEMPLOT.replot(GXContext._get_tls_geo(), db._wrapper, mask_ch.encode(), mineral_ch.encode(), map._wrapper, view.encode())
        



    @classmethod
    def re_plot_symbol_legend(cls, db, mview):
        """
        Replot a symbol legend in a view.

        **Note:**

        Searches the VIEW `GXREG` for information on a previously
        created legend, and if it finds that info, replots the Legend,
        using the current data, group key etc.
        """
        gxapi_cy.WrapSEMPLOT.re_plot_symbol_legend(GXContext._get_tls_geo(), db._wrapper, mview._wrapper)
        



    @classmethod
    def reset_groups(cls, db, mask_ch):
        """
        Re-group data using current settings.
        """
        gxapi_cy.WrapSEMPLOT.reset_groups(GXContext._get_tls_geo(), db._wrapper, mask_ch.encode())
        



    @classmethod
    def reset_used_channel(cls, db):
        """
        Set the "Plotted" channel to dummies

        **Note:**

        This function is called before one or a series of plots to initialize
        the "Plotted" channel in all the selected lines to dummy values.
        As the plots are created, those points used in the plot are set to 1,
        so that at the end the database records which values have been plotted.
        This information can then be used to make a symbol legend.
        If the "Plotted" channel does not exist, it is created, associated,
        loaded, and filled with dummies.
        """
        gxapi_cy.WrapSEMPLOT.reset_used_channel(GXContext._get_tls_geo(), db._wrapper)
        



    @classmethod
    def select_poly(cls, db, mview, mask_ch, mineral_ch, pply, mode):
        """
        Select data from a polygonal area on a map.
        """
        gxapi_cy.WrapSEMPLOT.select_poly(GXContext._get_tls_geo(), db._wrapper, mview._wrapper, mask_ch.encode(), mineral_ch.encode(), pply._wrapper, mode)
        



    @classmethod
    def set_channel_order(cls, db, lst):
        """
        Sets preset channel order.

        **Note:**

        Sets channel order as follows:
        
        Sample_No
        X and Y Locations
        Mineral
        Grain_No
        Position (e.g. center, edge etc.)
        Grain Morph
        Oxides (in the order they appear in Semplot_Oxides.csv)
        Trace Elements (Ordered as in the periodic table)
        Total
        Mask
        IsPlotted (flag set when a value is plotted)
        Other channels
        
        Channel order is set for all "RawData" groups.
        """
        gxapi_cy.WrapSEMPLOT.set_channel_order(GXContext._get_tls_geo(), db._wrapper, lst._wrapper)
        



    @classmethod
    def set_channel_units(cls, db):
        """
        Set units for oxides (%) and elements (ppm)

        **Note:**

        If the channel units are already set, then they are not changed.
        Oxide channels are identified from the Semplot_Oxides.csv file.
        Trace elements are identified from the periodic table of the
        elements, except for "Y", if it is the current Y channel.
        """
        gxapi_cy.WrapSEMPLOT.set_channel_units(GXContext._get_tls_geo(), db._wrapper)
        



    @classmethod
    def set_itr(cls, db, ch, itr):
        """
        Put `GXITR` into a channel.
        """
        gxapi_cy.WrapSEMPLOT.set_itr(GXContext._get_tls_geo(), db._wrapper, ch, itr._wrapper)
        



    @classmethod
    def set_mask(cls, db, mask_ch, mineral_ch, p4, p5, p6):
        """
        Set the mask channel ON or OFF.
        """
        gxapi_cy.WrapSEMPLOT.set_mask(GXContext._get_tls_geo(), db._wrapper, mask_ch.encode(), mineral_ch.encode(), p4.encode(), p5, p6)
        



    @classmethod
    def sort_data(cls, db, group, anomaly):
        """
        Sort data by Sample No, Grain and Position
        """
        gxapi_cy.WrapSEMPLOT.sort_data(GXContext._get_tls_geo(), db._wrapper, group, anomaly)
        



    @classmethod
    def template_lst(cls, lst, type):
        """
        Fill a list with the available plot template names

        **Note:**

        Looks first in user\\etc, then in \\etc.
        Looks first for file prefix "semtemplate" then "xyt" or "tri"
        (New-style templates with the "semtemplate" extentsion have the
        plot type "triplot" or "xyplot" inside them.)
        """
        gxapi_cy.WrapSEMPLOT.template_lst(GXContext._get_tls_geo(), lst._wrapper, type)
        



    @classmethod
    def tile_windows(cls):
        """
        Tile currently maximimized windows.
        """
        gxapi_cy.WrapSEMPLOT.tile_windows(GXContext._get_tls_geo())
        



    @classmethod
    def total_oxides(cls, db, mineral_ch):
        """
        Calculate the total oxides channel.

        **Note:**

        The mineral channel is needed in order to adjust the total
        with the Fe Corrected Ferric and Ferrous values, and these
        require a mineral for their identification. If none is provided,
        mineral "X" (unknown) is assumed.
        """
        gxapi_cy.WrapSEMPLOT.total_oxides(GXContext._get_tls_geo(), db._wrapper, mineral_ch.encode())
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer