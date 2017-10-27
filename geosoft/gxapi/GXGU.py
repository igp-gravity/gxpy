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
class GXGU:
    """
    GXGU class.

    Not a class. A catch-all group of functions performing
    various geophysical processes, including the calculation
    of simple EM model responses, certain instrument dump
    file imports, and 2D Euler deconvolution.
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapGU(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXGU`
        
        :returns: A null `GXGU`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of `GXGU` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of `GXGU`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def dipole_mag(cls, xyz_file, depth, inc, nx, ny, dx, dy):
        """
        Calculate a dipole magnetic field into XYZ file
        """
        gxapi_cy.WrapGU.dipole_mag(GXContext._get_tls_geo(), xyz_file.encode(), depth, inc, nx, ny, dx, dy)
        



    @classmethod
    def em_half_space_inv(cls, coil_spacing, coil_frequency, coil_configuration, tol, threshold, vv_height, vv_in_phase, p8, p9, p10, p11, p12):
        """
        Inverts EM responses to the best halfspace model.
        """
        gxapi_cy.WrapGU.em_half_space_inv(GXContext._get_tls_geo(), coil_spacing, coil_frequency, coil_configuration, tol, threshold, vv_height._wrapper, vv_in_phase._wrapper, p8._wrapper, p9._wrapper, p10, p11, p12)
        



    @classmethod
    def em_half_space_vv(cls, coil_spacing, coil_frequency, coil_configuration, rvv, hvv, ivv, qvv):
        """
        EM Halfspace forward model response.
        """
        gxapi_cy.WrapGU.em_half_space_vv(GXContext._get_tls_geo(), coil_spacing, coil_frequency, coil_configuration, rvv._wrapper, hvv._wrapper, ivv._wrapper, qvv._wrapper)
        



    @classmethod
    def geometrics2_db(cls, db, ra, log_wa, survey_mode, p5, p6, p7, p8, p9, p10, p11):
        """
        Convert a Geometrics STN file to a database.

        **Note:**

        Assumes that the database is new and empty. If not, existing channels
        with names X, Y, Mag1, Mag2, Time, Date, and Mark will deleted and then created.  
        Existing lines will be erased and then created if they are the same as the new ones.
        """
        gxapi_cy.WrapGU.geometrics2_db(GXContext._get_tls_geo(), db._wrapper, ra._wrapper, log_wa._wrapper, survey_mode, p5, p6, p7, p8, p9, p10, p11)
        



    @classmethod
    def geometrics2_tbl(cls, ra, wa, log_wa):
        """
        Convert a Geometrics station file (STN) to a table file (TBL)
        """
        gxapi_cy.WrapGU.geometrics2_tbl(GXContext._get_tls_geo(), ra._wrapper, wa._wrapper, log_wa._wrapper)
        



    @classmethod
    def geometrics_qc(cls, wa, line, in_vv, tol, min_coord, p6, p7, p8):
        """
        Correct reading positions in a database.

        **Note:**

        There are six cases to consider:
        
        ========    ====  =============  ========================================
        Case        Flag  Solutions      Symptoms
        ========    ====  =============  ========================================
        CASE 1A:    0     No correction  Recorded and actual Line lengths same
                                         Reading densities vary slightly (passed
                                         the tolerance test)
        --------    ----  -------------  ----------------------------------------
        CASE 1B     -1    No correction  Line lengths same
                                         Reading densities vary and cannot
                                         pass the tolerance test
        --------    ----  -------------  ----------------------------------------
        CASE 2A     1     Corrected by   Recorded line length too short
                          extension      Possible high readings in segment(s)
                                         Corrected (by extending) and actual
                                         lengths become the same
        --------    ----  -------------  ----------------------------------------
        CASE 2B     2     Corrected by   Recorded line length too short
                          interpolation  Possible high readings in segment(s)
                                         Corrected (by extending) and actual
                                         lengths are not same. Interpolation is
                                         then applied
        --------    ----  -------------  ----------------------------------------
        CASE 3A     1     Corrected by   Recorded line length too long
                          shifting or    Possible low readings in segment(s)
                          (shrank)       Corrected (by shifting) and actual
                                         lengths are same
        --------    ----  -------------  ----------------------------------------
        CASE 3B     2     Corrected by   Recorded line length too long
                          interpolation  Possible low readings in segment(s)
                                         Corrected (by shifting) and actual
                                         lengths are not same. Interpolation
                                         is then applied
        ========    ====  =============  ========================================
        
        
        TERMINOLOGY:
        
        Segments
             A segment refers to the distance and its contents between
             two adjacent fiducial markers
        
        Normal Density
             The density (number of readings) shared by the segments in
             a survey line. The number of segments with the density is greater 
             than the number of segments having a different density in a line.
        
        Tolerance and Bound:
             Tolerance is defined as a percentage, say ``50% (=0.5)``.
             Based on the tolerance, a lower bound and upper bound
        
             can be defined:
        
             ::
        
                 Lower bound = (Normal Density) - (Normal Density)*Tolerance
                 Upper bound = (Normal Density) - (Normal Density)*Tolerance
        
             Segments will pass the tolerance test if the number of readings
             falls within the Lower and Upper Bounds.
        """
        gxapi_cy.WrapGU.geometrics_qc(GXContext._get_tls_geo(), wa._wrapper, line.encode(), in_vv._wrapper, tol, min_coord, p6, p7._wrapper, p8._wrapper)
        



    @classmethod
    def geonics3138_dump2_db(cls, db, r_ah, r_ad, log_wa, line_mult, stat_mult):
        """
        Convert a Geonics EM31/EM38 file in dump format to a database.

        **Note:**

        Assumes that the database is new and empty. If not, existing channels
        with names X, Y, Station, Conductivity, Inphase, Quadrature,
        and Time will deleted and then created.  Existing lines will
        be erased and then created if they are the same as the new ones.
        """
        gxapi_cy.WrapGU.geonics3138_dump2_db(GXContext._get_tls_geo(), db._wrapper, r_ah._wrapper, r_ad._wrapper, log_wa._wrapper, line_mult, stat_mult)
        



    @classmethod
    def geonics61_dump2_db(cls, db, ra, log_wa, line_mult, stat_mult):
        """
        Convert a Geonics EM61 file in dump format to a database.

        **Note:**

        Assumes that the database is new and empty. If not, existing channels
        with names X, Y, Station, Conductivity, Inphase, Quadrature,
        and Time will deleted and then created.  Existing lines will
        be erased and then created if they are the same as the new ones.
        """
        gxapi_cy.WrapGU.geonics61_dump2_db(GXContext._get_tls_geo(), db._wrapper, ra._wrapper, log_wa._wrapper, line_mult, stat_mult)
        



    @classmethod
    def geonics_dat2_db(cls, db, ra, log_wa, line_mult, stat_mult):
        """
        Convert a Geonics EM31/EM38/EM61 file in `GXDAT` format to a database.

        **Note:**

        Assumes that the database is new and empty. If not, existing channels
        with names X, Y, Station, Conductivity, Inphase, Quadrature,
        and Time will deleted and then created.  Existing lines will
        be erased and then created if they are the same as the new ones.
        """
        gxapi_cy.WrapGU.geonics_dat2_db(GXContext._get_tls_geo(), db._wrapper, ra._wrapper, log_wa._wrapper, line_mult, stat_mult)
        



    @classmethod
    def gr_curv_cor(cls, v_velev, v_vlat, v_vboug):
        """
        Gravity Curvature (Bullard B) Correction to Bouguer anomaly
        """
        gxapi_cy.WrapGU.gr_curv_cor(GXContext._get_tls_geo(), v_velev._wrapper, v_vlat._wrapper, v_vboug._wrapper)
        



    @classmethod
    def gr_curv_cor_ex(cls, v_velev, v_vlat, v_vboug, rho):
        """
        Gravity Curvature (Bullard B) Correction to Bouguer anomaly, with user input cap density.
        """
        gxapi_cy.WrapGU.gr_curv_cor_ex(GXContext._get_tls_geo(), v_velev._wrapper, v_vlat._wrapper, v_vboug._wrapper, rho)
        



    @classmethod
    def gr_demvv(cls, im_gdem, v_vx, v_vy, v_vz):
        """
        Get gravity DEM grid `GXVV` for Bouguer anomaly
        """
        gxapi_cy.WrapGU.gr_demvv(GXContext._get_tls_geo(), im_gdem._wrapper, v_vx._wrapper, v_vy._wrapper, v_vz._wrapper)
        



    @classmethod
    def gr_test(cls, xm, ym, zm, v_vx, v_vy, v_vg3, v_vg4, v_vg1, v_vg2):
        """
        Test triangular prism gravity calculation
        """
        gxapi_cy.WrapGU.gr_test(GXContext._get_tls_geo(), xm, ym, zm, v_vx._wrapper, v_vy._wrapper, v_vg3._wrapper, v_vg4._wrapper, v_vg1._wrapper, v_vg2._wrapper)
        



    @classmethod
    def gravity_still_reading_correction(cls, db, grav_in, date, time, still, grav_out):
        """
        Gravity Still Reading Correction on selected lines.
        """
        gxapi_cy.WrapGU.gravity_still_reading_correction(GXContext._get_tls_geo(), db._wrapper, grav_in, date, time, still.encode(), grav_out)
        



    @classmethod
    def em_layer(cls, coil_spacing, coil_frequency, coil_height, coil_configuration, n_layers, p6, p7, p8, p9):
        """
        Calculate the EM response of a layered earth model.
        """
        ret_val, p8.value, p9.value = gxapi_cy.WrapGU.em_layer(GXContext._get_tls_geo(), coil_spacing, coil_frequency, coil_height, coil_configuration, n_layers, p6._wrapper, p7._wrapper, p8.value, p9.value)
        return ret_val



    @classmethod
    def em_plate(cls, strike_length, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20, p21):
        """
        Calculate the conductance of a thin plate model.
        """
        ret_val = gxapi_cy.WrapGU.em_plate(GXContext._get_tls_geo(), strike_length, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11._wrapper, p12, p13, p14, p15, p16._wrapper, p17._wrapper, p18._wrapper, p19._wrapper, p20._wrapper, p21._wrapper)
        return ret_val



    @classmethod
    def gen_ux_detect_symbols_group_name(cls, target_gdb, targets, p3):
        """
        Generate a group name string for UX-Detect symbols

        **Note:**

        Start a new group for the symbols in the UX-Detect system.
        The Target GDB is often in the form "GDB_Targets", where
        "GDB" is the original data. Cut off the part including the
        underscore when creating the map, so you don't get map group
        Names like "SYMBOLS_UxData_Targets_Targets".

        .. seealso::

            `GXSTR.gen_group_name`
        """
        p3.value = gxapi_cy.WrapGU.gen_ux_detect_symbols_group_name(GXContext._get_tls_geo(), target_gdb.encode(), targets.encode(), p3.value.encode())
        



    @classmethod
    def import_daarc500_ethernet(cls, file, output, bytes):
        """
        Import Ethernet data from the RMS Instruments DAARC500.

        **Note:**

        Imports Ethernet data recorded
        by the RMS Instruments DAARC500 instrument, and outputs the data
        to a new binary file, returning the number of bytes per
        block, to make it easier to import the data using the regular binary import.
        """
        bytes.value = gxapi_cy.WrapGU.import_daarc500_ethernet(GXContext._get_tls_geo(), file.encode(), output.encode(), bytes.value)
        



    @classmethod
    def import_daarc500_serial(cls, file, channel, output, bytes):
        """
        Import Serial data from the RMS Instruments DAARC500.

        **Note:**

        Imports a single channel of the up to 8 serial data channels recorded
        by the RMS Instruments DAARC500 instrument, and outputs the data for
        that channel to a new binary file, returning the number of bytes per
        block, to make it easier to import the data using the regular binary import.
        """
        bytes.value = gxapi_cy.WrapGU.import_daarc500_serial(GXContext._get_tls_geo(), file.encode(), channel, output.encode(), bytes.value)
        



    @classmethod
    def import_p190(cls, db, file, rec_type, wa):
        """
        Import navigation data in the P190 format.

        **Note:**

        Imports the data, and, if projection information is included
        set the "X" and "Y" channel projection info. (Note: the last file
        imported always takes precedence).
        Different record types are imported to separate lines, but in the
        same order as in the file. Data in existing lines is overwritten.
        If the record type is specified, only records beginning with that
        letter are imported, otherwise all records (except for the header "H"
        records) are imported.
        """
        gxapi_cy.WrapGU.import_p190(GXContext._get_tls_geo(), db._wrapper, file.encode(), rec_type.encode(), wa._wrapper)
        



    @classmethod
    def lag_daarc500_gps(cls, mag_fid_vv, mag_event_vv, gps_fid_vv):
        """
        Lag the GPS fid values for the DAARC500 import.

        **Note:**

        The fiducial times recorded for the GPS in the RMS Instrument DAARC500
        are delayed, and associated with the "wrong" fid value. They should actually
        be moved to the previous fid value in the mag data where the event flag is non-zero.
        """
        gxapi_cy.WrapGU.lag_daarc500_gps(GXContext._get_tls_geo(), mag_fid_vv._wrapper, mag_event_vv._wrapper, gps_fid_vv._wrapper)
        



    @classmethod
    def maxwell_plate_corners(cls, x, y, z, dip, dip_dir, plunge, length, width, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20):
        """
        Calculate the corner point locations for a Maxwell Plate.

        **Note:**

        This routine calculates the corner locations of plates defined in the Maxwell Plate
        program, given the top-center location and plate geometry parameters.
        """
        p9.value, p10.value, p11.value, p12.value, p13.value, p14.value, p15.value, p16.value, p17.value, p18.value, p19.value, p20.value = gxapi_cy.WrapGU.maxwell_plate_corners(GXContext._get_tls_geo(), x, y, z, dip, dip_dir, plunge, length, width, p9.value, p10.value, p11.value, p12.value, p13.value, p14.value, p15.value, p16.value, p17.value, p18.value, p19.value, p20.value)
        



    @classmethod
    def scan_daarc500_ethernet(cls, file, type, items):
        """
        Scan Ethernet data from the RMS Instruments DAARC500.

        **Note:**

        Scans the file to see what data type is in the Ethernet file.
        Currently only detects GR820 types.
        """
        type.value, items.value = gxapi_cy.WrapGU.scan_daarc500_ethernet(GXContext._get_tls_geo(), file.encode(), type.value, items.value)
        



    @classmethod
    def scan_daarc500_serial(cls, file, v_vtype, v_vitems):
        """
        Scan Serial data from the RMS Instruments DAARC500.

        **Note:**

        Scans the file to see which of the 8 serial channels were used to store data.
        """
        gxapi_cy.WrapGU.scan_daarc500_serial(GXContext._get_tls_geo(), file.encode(), v_vtype._wrapper, v_vitems._wrapper)
        



    @classmethod
    def vv_euler(cls, vv_xin, vv_yin, img_data, imgx, imgy, imgz, vv_xout, vv_yout, vv_depth, vvdc, vv_zer, vvx_yer, wnd_sz, si, wt_pow, x_yfit):
        """
        Get Euler solutions of depth from VVs and grids.

        **Note:**

        All VVs must be REAL
        
        The output X and Y values are the same as the inputs,
        except if `PEAKEULER_XY_FIT` is selected. All other
        output values are set to dummy if:
        
             a) The input X or Y is a dummy
             b) The derived window size is a dummy.
             c) The derived solution is outside the range
             d) The solution is invalid (singular matrix)
        """
        gxapi_cy.WrapGU.vv_euler(GXContext._get_tls_geo(), vv_xin._wrapper, vv_yin._wrapper, img_data._wrapper, imgx._wrapper, imgy._wrapper, imgz._wrapper, vv_xout._wrapper, vv_yout._wrapper, vv_depth._wrapper, vvdc._wrapper, vv_zer._wrapper, vvx_yer._wrapper, wnd_sz, si, wt_pow, x_yfit)
        



    @classmethod
    def vv_euler2(cls, vv_xin, vv_yin, img_data, imgx, imgy, imgz, vv_xout, vv_yout, vv_depth, vvdc, vv_zer, vvx_yer, vv_wnd, si, wt_pow, x_yfit):
        """
        Get Euler solutions of depth from VVs and grids (method 2).

        **Note:**

        All VVs must be REAL

        .. seealso::

            `vv_euler`
        """
        gxapi_cy.WrapGU.vv_euler2(GXContext._get_tls_geo(), vv_xin._wrapper, vv_yin._wrapper, img_data._wrapper, imgx._wrapper, imgy._wrapper, imgz._wrapper, vv_xout._wrapper, vv_yout._wrapper, vv_depth._wrapper, vvdc._wrapper, vv_zer._wrapper, vvx_yer._wrapper, vv_wnd._wrapper, si, wt_pow, x_yfit)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer