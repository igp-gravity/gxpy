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
class GXPGU:
    """
    GXPGU class.

    A collection of methods applied to `GXPG` objects, including
    fills, trending and 2-D `GXFFT` operations.
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapPGU(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXPGU`
        
        :returns: A null `GXPGU`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of `GXPGU` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of `GXPGU`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# General


    @classmethod
    def bool_mask(cls, pg, ref_fil):
        """
        Apply reference file boolean mask to pager
        """
        gxapi_cy.WrapPGU.bool_mask(GXContext._get_tls_geo(), pg._wrapper, ref_fil.encode())
        



    @classmethod
    def direct_gridding_dat(cls, pg, xo, yo, dx, dy, rot, p7, p8):
        """
        Direct-gridding method, `GXDAT` version.

        **Note:**

        Grid cells take on the specified statistic of the values inside the
        cell area. Grid cells containing no data values are set to dummy.
        """
        gxapi_cy.WrapPGU.direct_gridding_dat(GXContext._get_tls_geo(), pg._wrapper, xo, yo, dx, dy, rot, p7._wrapper, p8)
        



    @classmethod
    def direct_gridding_dat_3d(cls, pg, xo, yo, zo, dx, dy, dz, rot, p9, p10):
        """
        Direct-gridding method, `GXDAT` version, 3D.

        **Note:**

        3D grid cells take on the specified statistic of the values inside the
        cell area. Grid cells containing no data values are set to dummy.
        """
        gxapi_cy.WrapPGU.direct_gridding_dat_3d(GXContext._get_tls_geo(), pg._wrapper, xo, yo, zo, dx, dy, dz, rot, p9._wrapper, p10)
        



    @classmethod
    def direct_gridding_db(cls, pg, xo, yo, dx, dy, rot, p7, p8, p9, p10, p11):
        """
        Direct-gridding method, `GXDB` version.

        **Note:**

        Grid cells take on the specified statistic of the values inside the
        cell area. Grid cells containing no data values are set to dummy.
        """
        gxapi_cy.WrapPGU.direct_gridding_db(GXContext._get_tls_geo(), pg._wrapper, xo, yo, dx, dy, rot, p7._wrapper, p8, p9, p10, p11)
        



    @classmethod
    def direct_gridding_db_3d(cls, pg, xo, yo, zo, dx, dy, dz, rot, p9, p10, p11, p12, p13, p14):
        """
        Direct-gridding method, `GXDB` version, 3D.

        **Note:**

        3D grid cells take on the specified statistic of the values inside the
        cell area. Grid cells containing no data values are set to dummy.
        """
        gxapi_cy.WrapPGU.direct_gridding_db_3d(GXContext._get_tls_geo(), pg._wrapper, xo, yo, zo, dx, dy, dz, rot, p9._wrapper, p10, p11, p12, p13, p14)
        



    @classmethod
    def direct_gridding_vv(cls, pg, xo, yo, dx, dy, rot, p7, p8, p9, p10):
        """
        Direct-gridding method, `GXVV` version.

        **Note:**

        Grid cells take on the specified statistic of the values inside the
        cell area. Grid cells containing no data values are set to dummy.
        """
        gxapi_cy.WrapPGU.direct_gridding_vv(GXContext._get_tls_geo(), pg._wrapper, xo, yo, dx, dy, rot, p7._wrapper, p8._wrapper, p9._wrapper, p10)
        



    @classmethod
    def expand(cls, p_gi, p_go, ex_pcnt, ex_shp, ex_x, p6):
        """
        Expand a pager by filling the dummies for expanded edges

        **Note:**

        3D pagers are expanded in X,Y direction the number of slices(Z) is unchanged .
        """
        gxapi_cy.WrapPGU.expand(GXContext._get_tls_geo(), p_gi._wrapper, p_go._wrapper, ex_pcnt, ex_shp, ex_x, p6)
        



    @classmethod
    def fill(cls, pg, fl_roll_wt, fl_roll_base, fl_roll_dist, p5, p6, p7, p8, p9, p10, p11):
        """
        Replace all dummies in a pager by predict values.
        """
        gxapi_cy.WrapPGU.fill(GXContext._get_tls_geo(), pg._wrapper, fl_roll_wt, fl_roll_base, fl_roll_dist, p5, p6, p7, p8, p9, p10, p11.encode())
        



    @classmethod
    def fill_value(cls, pg, value):
        """
        Set all values in a pager to a single value.
        """
        gxapi_cy.WrapPGU.fill_value(GXContext._get_tls_geo(), pg._wrapper, value)
        



    @classmethod
    def filt_sym(cls, pg, npass, usefile, file, size, vv):
        """
        Apply 5x5, 7x7 or 9X9 symmetric convolution filter to a `GXPG`.
        """
        gxapi_cy.WrapPGU.filt_sym(GXContext._get_tls_geo(), pg._wrapper, npass, usefile, file.encode(), size, vv._wrapper)
        



    @classmethod
    def filt_sym5(cls, pg, npass, usefile, file, vv):
        """
        Apply 5x5 symmetric convolution filter to a `GXPG`.
        """
        gxapi_cy.WrapPGU.filt_sym5(GXContext._get_tls_geo(), pg._wrapper, npass, usefile, file.encode(), vv._wrapper)
        



    @classmethod
    def grid_peak(cls, grid, nlmt, p3, p4, p5):
        """
        Pick grid peaks.

        **Note:**

        Blakey test limit defines how grid peaks are to be found.
        For example, with the `BLAKEY_TEST_ONESIDE`, a grid
        point will be picked if its grid value is greater than
        the value of one or more of its four neighouring points.
        """
        gxapi_cy.WrapPGU.grid_peak(GXContext._get_tls_geo(), grid.encode(), nlmt, p3._wrapper, p4._wrapper, p5._wrapper)
        



    @classmethod
    def dw_gridding_dat(cls, pg, dat, reg):
        """
        `dw_gridding_dat`     Inverse-distance weighting gridding method, `GXDAT` version.

        **Note:**

        See the notes for `dw_gridding_db`.
        """
        gxapi_cy.WrapPGU.dw_gridding_dat(GXContext._get_tls_geo(), pg._wrapper, dat._wrapper, reg._wrapper)
        



    @classmethod
    def dw_gridding_dat_3d(cls, pg, dat, reg):
        """
        `dw_gridding_dat_3d`     Inverse-distance weighting gridding method, `GXDAT` version, 3D.

        **Note:**

        See the notes for `dw_gridding_db_3d`.
        """
        gxapi_cy.WrapPGU.dw_gridding_dat_3d(GXContext._get_tls_geo(), pg._wrapper, dat._wrapper, reg._wrapper)
        



    @classmethod
    def dw_gridding_db(cls, pg, db, x, y, z, reg):
        """
        `dw_gridding_db`     Inverse-distance weighting gridding method, `GXDB` version.

        **Note:**

        Grid cells take on the averaged values within a search radius, weighted inversely by distance.
        
        Weighting can be controlled using the power and slope properties;
        
        weighting = 1 / (distance^wtpower + 1/slope) where distance is in
        units of grid cells (X dimenstion). Default is 0.0,
        
        If the blanking distance is set, all cells whose center point is not within the blanking distance of
        at least one data point are set to dummy.
        
        `GXREG` Parameters:
        
        X0, Y0, DX, DY: Grid origin, and cell sizes (required)
        WT_POWER (default=2), WT_SLOPE (default=1) Weighting function parameters
        SEARCH_RADIUS: Distance weighting limit (default = 4 * SQRT(DX*DY))
        BLANKING_DISTANCE: Dummy values farther from data than this distance. (default = 4 * SQRT(DX*DY))
        LOG: Apply log transform to input data before gridding (0:No (default), 1:Yes)?
        LOG_BASE: One of `VV_LOG_BASE_10` (default) or `VV_LOG_BASE_E`
        LOG_NEGATIVE: One of `VV_LOG_NEGATIVE_NO` (default) or `VV_LOG_NEGATIVE_YES`
        """
        gxapi_cy.WrapPGU.dw_gridding_db(GXContext._get_tls_geo(), pg._wrapper, db._wrapper, x, y, z, reg._wrapper)
        



    @classmethod
    def dw_gridding_db_3d(cls, pg, db, x, y, z, data, reg):
        """
        `dw_gridding_db_3d`     Inverse-distance weighting gridding method, `GXDB` version, 3D.

        **Note:**

        3D cells take on the averaged values within a search radius, weighted inversely by distance.
        
        Weighting can be controlled using the power and slope properties;
        
        weighting = 1 / (distance^wtpower + 1/slope) where distance is in
        units of grid cells (X dimenstion). Default is 0.0,
        
        If the blanking distance is set, all cells whose center point is not within the blanking distance of
        at least one data point are set to dummy.
        
        `GXREG` Parameters:
        
        X0, Y0, Z0, DX, DY, DZ: Grid origin, and cell sizes (required)
        WT_POWER (default=2), WT_SLOPE (default=1) Weighting function parameters
        SEARCH_RADIUS: Distance weighting limit (default = 4 * CUBE_ROOT(DX*DY*DZ))
        BLANKING_DISTANCE: Dummy values farther from data than this distance. (default = 4 * CUBE_ROOT(DX*DY*DZ))
        LOG: Apply log transform to input data before gridding (0:No (default), 1:Yes)?
        LOG_BASE: One of `VV_LOG_BASE_10` (default) or `VV_LOG_BASE_E`
        LOG_NEGATIVE: One of `VV_LOG_NEGATIVE_NO` (default) or `VV_LOG_NEGATIVE_YES`
        """
        gxapi_cy.WrapPGU.dw_gridding_db_3d(GXContext._get_tls_geo(), pg._wrapper, db._wrapper, x, y, z, data, reg._wrapper)
        



    @classmethod
    def dw_gridding_vv(cls, pg, v_vx, v_vy, v_vz, reg):
        """
        `dw_gridding_vv`     Inverse-distance weighting gridding method, `GXVV` version.

        **Note:**

        See the notes for `dw_gridding_db`.
        """
        gxapi_cy.WrapPGU.dw_gridding_vv(GXContext._get_tls_geo(), pg._wrapper, v_vx._wrapper, v_vy._wrapper, v_vz._wrapper, reg._wrapper)
        



    @classmethod
    def numeric_to_thematic(cls, p_gi, vv, p_go):
        """
        `numeric_to_thematic`    Set index values in a pager based on a numeric pager with translation `GXVV`.
        
        Returns			  Nothing

        **Note:**

        The values in the input data `GXVV` represent the center-of-range
        values of unique properties with indices 0 to N-1, where N
        is the number of items in the input `GXVV`.
        
        This `GXVV` is sorted from smallest to largest, and each value in
        in the input numeric `GXPG` is tested to see into which range it goes.
        The closest range value for each item is used, so the half-way point
        is the dividing point. The top and bottom-most range widths are determined
        by the "inside half-width" to the nearest range.
        
        The INDEX of the closest range is then inserted into the output `GXPG`, so
        it can be used in a thematic voxel (for instance).
        """
        gxapi_cy.WrapPGU.numeric_to_thematic(GXContext._get_tls_geo(), p_gi._wrapper, vv._wrapper, p_go._wrapper)
        



    @classmethod
    def peakedness(cls, grid, pkness, p3, p4, p5):
        """
        Find all peaks in peakedneess grid pager
        """
        gxapi_cy.WrapPGU.peakedness(GXContext._get_tls_geo(), grid.encode(), pkness, p3._wrapper, p4._wrapper, p5._wrapper)
        



    @classmethod
    def peakedness_grid(cls, grdi, grdo, p3, p4):
        """
        Create peakedneess grid from input grid.

        **Note:**

        This function creates a peakedneess grid from input grid.
        Radius, is the maximum radius at which the value of the parent pixel is compared to
        the value of surrounding pixels.
        PercentLesser, is used to indicate the percentage of pixels at each radii smaller than
        or equal to Radius that must have value lower than the parent pixel in order to call
        that radius true or equal to 1.
        Description:  For each pixel in the grid a series of radii are evaluated from 1 to Radius.
        If the percentage of pixels for a given radius is less than PercentLesser the parent pixel
        receives an additional 1.
        For examples if the Radius is set to 5 and the PercentLesser is set to 70%.
        And radius 1 = 90%, radius 2 = 85%, radius 3 = 75%, radius 4 = 70% and radius 5 = 65%
        then the parent pixel would receive 1+1+1+1+0 = 4.
        Use:  This function is useful in isolating the anomaly peaks in data that has a large
        value range for anomalies. For example the 1 mV anomaly could quite possibly have
        the same representation as the 100 mV anomaly using this function.
        """
        gxapi_cy.WrapPGU.peakedness_grid(GXContext._get_tls_geo(), grdi.encode(), grdo.encode(), p3, p4)
        



    @classmethod
    def ref_file(cls, pg, ref_fil):
        """
        Create a reference file (boolean mask flag) from pager.

        **Note:**

        A reference file is a binary file with the following format:
        
        The first 8 bytes are the pager dimensions NX and NY as longs.
        The remaining bits, one bit per pager cell - (NX * NY)/8 bytes
        are zero where the pager is dummy, and 1 where the pager is defined.
        
        The reference file is used in various operations where it is
        necessary to mask some output to the original defined cells.
        """
        gxapi_cy.WrapPGU.ref_file(GXContext._get_tls_geo(), pg._wrapper, ref_fil.encode())
        



    @classmethod
    def save_file(cls, pg, xo, yo, dx, dy, rot, tr, ipj, file):
        """
        Writes a `GXPG` to an image file.

        **Note:**

        The trend object and projection are optional.
        """
        gxapi_cy.WrapPGU.save_file(GXContext._get_tls_geo(), pg._wrapper, xo, yo, dx, dy, rot, tr._wrapper, ipj._wrapper, file.encode())
        



    @classmethod
    def thematic_to_numeric(cls, p_gi, vv, p_go):
        """
        Set numeric values in a pager based on an index pager with translation `GXVV`.
        
        Returns			  Nothing

        **Note:**

        The items in the input data `GXVV` are inserted into
        the output `GXPG` using the indices in the index `GXPG`.
        
        This function is useful when converting a thematic voxel, which is
        type `GS_LONG` and contains indices into its own internal `GXTPAT`
        object, and you provide a numeric mapping `GXVV`, calculated using
        SetupTranslateToNumericVV_TPAT.
        """
        gxapi_cy.WrapPGU.thematic_to_numeric(GXContext._get_tls_geo(), p_gi._wrapper, vv._wrapper, p_go._wrapper)
        



    @classmethod
    def trend(cls, p_gi, p_go, tr, tr_opt, tr_pt_bs, xo, yo, dx, dy):
        """
        Trend remove or replace back in pager
        """
        gxapi_cy.WrapPGU.trend(GXContext._get_tls_geo(), p_gi._wrapper, p_go._wrapper, tr._wrapper, tr_opt, tr_pt_bs, xo, yo, dx, dy)
        




# Math Operations


    @classmethod
    def add_scalar(cls, pg, scalar):
        """
        Add a scalar value to a pager

        **Note:**

        Only available for FLOAT or DOUBLE pagers
        """
        gxapi_cy.WrapPGU.add_scalar(GXContext._get_tls_geo(), pg._wrapper, scalar)
        



    @classmethod
    def multiply_scalar(cls, pg, scalar):
        """
        Multiply a scalar value and a pager

        **Note:**

        Only available for FLOAT or DOUBLE pagers
        """
        gxapi_cy.WrapPGU.multiply_scalar(GXContext._get_tls_geo(), pg._wrapper, scalar)
        




# Matrix Operation


    @classmethod
    def correlation_matrix(cls, p_gu, p_go):
        """
        Find the correlations between columns in a matrix

        **Note:**

        The input matrix is M rows by N columns. The returned matrix
        is a symmetric N by N matrix whose elements are the normalized
        dot products of the columns of the input matrix with themselves.
        The elements take on values from 0 (orthogonal) to 1 (parallel).
        """
        gxapi_cy.WrapPGU.correlation_matrix(GXContext._get_tls_geo(), p_gu._wrapper, p_go._wrapper)
        



    @classmethod
    def correlation_matrix2(cls, p_gu, corr, p_go):
        """
        Same as `correlation_matrix`, but select correlation type.
        """
        gxapi_cy.WrapPGU.correlation_matrix2(GXContext._get_tls_geo(), p_gu._wrapper, corr, p_go._wrapper)
        



    @classmethod
    def invert_matrix(cls, p_gi, p_go):
        """
        Inverts a square matrix using LU decomp. and back-substitution

        **Note:**

        This is an "in-place" operation, and set up so that the input and
        output pagers may be the same handle. (If they are different, the
        input pager remains unchanged).
        Pagers and VVs must be type `GS_DOUBLE`.
        """
        gxapi_cy.WrapPGU.invert_matrix(GXContext._get_tls_geo(), p_gi._wrapper, p_go._wrapper)
        



    @classmethod
    def jacobi(cls, p_gi, v_vd, p3):
        """
        Find eigenvalues, eigenvectors of a real symmetric matrix.

        **Note:**

        The number of rows must equal the number of columns.
        Eienvalues, vectors are sorted in descending order.
        """
        gxapi_cy.WrapPGU.jacobi(GXContext._get_tls_geo(), p_gi._wrapper, v_vd._wrapper, p3._wrapper)
        



    @classmethod
    def lu_back_sub(cls, p_ga, v_vi, p3, p4):
        """
        Solve a linear system using LU decomposition and back-substitution.

        **Note:**

        Solves the system Ax = b for a given b, using the LU decomposition
        of the matrix a
        The LU decomposition and the permutation vector are obtained
        from `lu_back_sub`.
        Pagers and VVs must be type `GS_DOUBLE` except for the permutation vector,
        which should be INT
        """
        gxapi_cy.WrapPGU.lu_back_sub(GXContext._get_tls_geo(), p_ga._wrapper, v_vi._wrapper, p3._wrapper, p4._wrapper)
        



    @classmethod
    def lu_decomp(cls, p_gi, p_go, p3):
        """
        Perform an LU decomposition on a square pager.

        **Note:**

        The L and U matrix are both contained in the returned pager; The
        "L" matrix is composed of the sub-diagonal elements of the output
        pager, as well as "1" values on the diagonal. The "U" matrix is
        composed of the diagonal elements (sub-diagonal elements set to 0).
        This is an "in-place" operation, and set up so that the input and
        output pagers may be the same handle. (If they are different, the
        input pager remains unchanged).
        The LU decomposition, and the permutation vector are used for
        `lu_back_sub`.
        Pagers must be type `GS_DOUBLE` and the permutation vector type INT
        """
        gxapi_cy.WrapPGU.lu_decomp(GXContext._get_tls_geo(), p_gi._wrapper, p_go._wrapper, p3._wrapper)
        



    @classmethod
    def matrix_mult(cls, p_gu, transpose_u, p_gv, p4, p5):
        """
        Multiply two pagers as if they were matrices.

        **Note:**

        The matrices must be correctly dimensioned, taking into
        account whether transposition should occur before
        multiplication. The input matrices are not altered on output (even
        if transposition is requested).
        Assertions if: Matrices are not expected sizes
        Dummies are treated as 0 values.
        """
        gxapi_cy.WrapPGU.matrix_mult(GXContext._get_tls_geo(), p_gu._wrapper, transpose_u, p_gv._wrapper, p4, p5._wrapper)
        



    @classmethod
    def matrix_vector_mult(cls, p_gu, v_vx, v_vo):
        """
        Multiply a `GXVV` by a pager like a matrix*vector multiply.

        **Note:**

        The matrix is input as an M rows (data) by N columns (variables) `GXPG`.
        The vector must be of length N. The output `GXVV` is set to length M.
        The `GXPG` and VVs must be type `GS_DOUBLE`.
        
        Terminates if: 
        
             Matrices, `GXVV` are not expected sizes (taken from U)
             PGs are not `GS_DOUBLE`.
        
        Dummies are treated as 0 values.
        """
        gxapi_cy.WrapPGU.matrix_vector_mult(GXContext._get_tls_geo(), p_gu._wrapper, v_vx._wrapper, v_vo._wrapper)
        



    @classmethod
    def sv_decompose(cls, p1, p2, p3, p4):
        """
        Do a singular value decomposition on a matrix stored as a `GXPG`

        **Note:**

        The matrix is input as an N rows (data) by M columns (variables) `GXPG`.
        On return, the matrix is decomposed to A = U * W * Vt. If M<N, then an error will 
        be registered. In this case, augment the "A" `GXPG` with rows of zero values.
        
        The input matrices must be A[M,N], U[M.N] and V[N,N]. The length of the W `GXVV`
        is set by sSVD_PGU to N.
        
        The Pagers must be type `GS_DOUBLE`.
        
        Terminates if: 
        
             U is not M by N. (Taken from size of A)
             V is not N by N. (Taken from #columns in A).
             PGs, VV are not `GS_DOUBLE`
        """
        gxapi_cy.WrapPGU.sv_decompose(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4._wrapper)
        



    @classmethod
    def sv_recompose(cls, p1, p2, p3, p4, p5):
        """
        Reconstitute the original matrix from an SVD.

        **Note:**

        The matrix is input as an N rows (data) by M columns (variables) `GXPG`.
        On return, the matrix is decomposed to A = U * W * Vt.
        If M<N, then an error will be registered. In this case, augment the
        "A" `GXPG` with rows of zero values.
        The input matrices must be A[M,N], U[M.N] and V[N,N]. The length of the W `GXVV`
        is set by sSVDecompose_PGU to N.
        The Pagers must be type `GS_DOUBLE`.
        
        Terminates if: 
        
             U is not M by N. (Taken from size of A)
             V is not N by N. (Taken from #columns in A).
             PGs, VV are not `GS_DOUBLE`.
        
        Dummies are treated as 0 values.
        """
        gxapi_cy.WrapPGU.sv_recompose(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4, p5._wrapper)
        




# Principal Component Analysis


    @classmethod
    def pc_communality(cls, p_gi, v_vc):
        """
        Determines principal component communalities.

        **Note:**

        Calculate communalities (sums of the squares of the column
        values in each row)
        Pagers and VVs must be type `GS_DOUBLE`.
        """
        gxapi_cy.WrapPGU.pc_communality(GXContext._get_tls_geo(), p_gi._wrapper, v_vc._wrapper)
        



    @classmethod
    def pc_loadings(cls, p_gx, p2):
        """
        Compute the principal component loadings from the standardized data.

        **Note:**

        Works on columns of the `GXPG`.
        Calculates the correlation matrix from the columns of the
        standardized data, then computes the eigen values and eigenvectors
        of the correlation matrix. The loadings are the eigenvectors, ordered
        by descending eigenvalues, scaled by the square root of the
        eigenvalues. The returned pager must be sized the same as the
        input pager.
        Correlations are performed using "`PGU_CORR_SIMPLE`", so if you want
        Pearson correlations, or wish to use a modified correlation matrix,
        use `pc_loadings2` and input the correlation matrix directly.
        """
        gxapi_cy.WrapPGU.pc_loadings(GXContext._get_tls_geo(), p_gx._wrapper, p2._wrapper)
        



    @classmethod
    def pc_loadings2(cls, p_gc, p2):
        """
        Same as PCLoading_PGU, but input correlation matrix.

        **Note:**

        See `pc_loadings`.
        """
        gxapi_cy.WrapPGU.pc_loadings2(GXContext._get_tls_geo(), p_gc._wrapper, p2._wrapper)
        



    @classmethod
    def pc_scores(cls, p_gx, p2, p3):
        """
        Compute the principal component scores from the standardized data.

        **Note:**

        t  -1
        Forms the product X Ap (Ap Ap),  where X is the
        standardized data matrix, and Ap is the matrix of
        principal component loadings (see `pc_loadings`).
        The loadings must be input, and can be calculated by calling
        `pc_loadings`.
        Pagers and VVs must be type `GS_DOUBLE`.
        """
        gxapi_cy.WrapPGU.pc_scores(GXContext._get_tls_geo(), p_gx._wrapper, p2._wrapper, p3._wrapper)
        



    @classmethod
    def pc_standardize(cls, pg, v_vm, v_vs, dir):
        """
        Remove/Replace mean and standard deviation

        **Note:**

        Works on columns of the `GXPG`.
        """
        gxapi_cy.WrapPGU.pc_standardize(GXContext._get_tls_geo(), pg._wrapper, v_vm._wrapper, v_vs._wrapper, dir)
        



    @classmethod
    def pc_standardize2(cls, pg, v_vmask, v_vm, v_vs, dir):
        """
        Remove/Replace mean and standard deviation, subset values.

        **Note:**

        Like `pc_standardize`, except that not all the values are
        included in the calculation of the means and standard
        deviations. The inclusion is controlled by a mask `GXVV`,
        The rows where the mask is dummy are not included
        in the calculation, but ALL the values are standardized.
        """
        gxapi_cy.WrapPGU.pc_standardize2(GXContext._get_tls_geo(), pg._wrapper, v_vmask._wrapper, v_vm._wrapper, v_vs._wrapper, dir)
        



    @classmethod
    def pc_transform(cls, pg, v_vd, v_vf, v_vt, dir):
        """
        Transform/De-transform data.

        **Note:**

        Works on columns of the `GXPG`.
        Forward direction: Applies the selected transform to the data.
        Backward direction: Applies the inverse transform to the data.
        The detection limits are input with a `GXVV`. In the forward
        transform, data values less than the detection limit are set
        to the limit.
        The factor limits are input with a `GXVV`. In the forward
        transform, data values greater than the maximum values are set
        to the maximum.
        """
        gxapi_cy.WrapPGU.pc_transform(GXContext._get_tls_geo(), pg._wrapper, v_vd._wrapper, v_vf._wrapper, v_vt._wrapper, dir)
        



    @classmethod
    def pc_varimax(cls, p_gi, p_go):
        """
        Perform the Kaiser Varimax transformation on pr. comp. loadings

        **Note:**

        Rotates the principal components using the Kaiser's varimax
        scheme to move move each factor axis to positions so that
        projections from each variable on the factor axes are either
        near the extremities or near the origin.
        Pagers must be type `GS_DOUBLE`.
        """
        gxapi_cy.WrapPGU.pc_varimax(GXContext._get_tls_geo(), p_gi._wrapper, p_go._wrapper)
        




# Specialized Operations


    @classmethod
    def maximum_terrain_steepness(cls, pg, annular_size):
        """
        Compute the Maximum Steepness of a topography Pager

        **Note:**

        Calculates forward-looking slopes SX and SY in the X and Y directions
        using pager locations (ix, iy), (ix+size, iy), (ix, iy+isize)
        and returns SX*SX + SY*SY.
        The values in the last "size" rows and columns are not
        processed.
        The wrapper was created for testing and development purposes.
        """
        ret_val = gxapi_cy.WrapPGU.maximum_terrain_steepness(GXContext._get_tls_geo(), pg._wrapper, annular_size)
        return ret_val





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer