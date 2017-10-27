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
class GXTB:
    """
    GXTB class.

    The `GXTB` class is a high-performance table class used to
    perform table-based processing, such as leveling data in
    an OASIS database. The `GXLTB` class is recommended for use
    with small tables produced from short lists such as the
    different geographic projections and their defining parameters.
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapTB(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXTB`
        
        :returns: A null `GXTB`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of `GXTB` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of `GXTB`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous



    def set_search_mode(self, mode):
        """
        Set the search mode of a table.

        **Note:**

        If performance is an issue, you may want to test which search
        mode provides the best performance with typical data.
        """
        self._wrapper.set_search_mode(mode)
        



    @classmethod
    def create(cls, name):
        """
        Loads a table into memory and return a table handle.

        **Note:**

        If the table contains fewer data columns than are defined by the
        the table header, the `GXTB` object will read in the table and dummy
        the elements of the missing data columns.
        """
        ret_val = gxapi_cy.WrapTB.create(GXContext._get_tls_geo(), name.encode())
        return GXTB(ret_val)



    @classmethod
    def create_db(cls, db):
        """
        Create a table from a database.

        **Note:**

        The table will contain fields for all channels in
        the database.
        
        The database is not loaded with data.  Use the `load_db`
        function to load data into the table.
        """
        ret_val = gxapi_cy.WrapTB.create_db(GXContext._get_tls_geo(), db._wrapper)
        return GXTB(ret_val)



    @classmethod
    def create_ltb(cls, ltb):
        """
        Create a table from an `GXLTB` database.
        """
        ret_val = gxapi_cy.WrapTB.create_ltb(GXContext._get_tls_geo(), ltb._wrapper)
        return GXTB(ret_val)






    def field(self, name):
        """
        Get a field handle.
        """
        ret_val = self._wrapper.field(name.encode())
        return ret_val




    def get_string(self, row, col, val):
        """
        Gets a string value from a table element.
        """
        val.value = self._wrapper.get_string(row, col, val.value.encode())
        




    def data_type(self, col):
        """
        Returns the data type for the specified column.
        """
        ret_val = self._wrapper.data_type(col)
        return ret_val




    def find_col_by_index(self, idx, name):
        """
        Finds a column's name by its index.
        """
        name.value = self._wrapper.find_col_by_index(idx, name.value.encode())
        




    def find_col_by_name(self, name):
        """
        Finds a column's index by its name.
        """
        ret_val = self._wrapper.find_col_by_name(name.encode())
        return ret_val




    def format(self, col):
        """
        Returns the channel format for the specified column.
        """
        ret_val = self._wrapper.format(col)
        return ret_val




    def get_int(self, row, col):
        """
        Gets an integer value from a table element.
        """
        ret_val = self._wrapper.get_int(row, col)
        return ret_val




    def num_columns(self):
        """
        Gets the number of data fields (columns) in a table.
        """
        ret_val = self._wrapper.num_columns()
        return ret_val




    def num_rows(self):
        """
        Gets the number of data rows in a table.
        """
        ret_val = self._wrapper.num_rows()
        return ret_val




    def load_db(self, db, line):
        """
        Load a database into a `GXTB`

        **Note:**

        The line is appended to the data already in the table.
        """
        self._wrapper.load_db(db._wrapper, line)
        




    def get_double(self, row, col):
        """
        Gets an real value from a table element.
        """
        ret_val = self._wrapper.get_double(row, col)
        return ret_val




    def save(self, name):
        """
        Saves the data in a table to a file. The table header will be
        in ASCII and the data will be in BINARY format.
        """
        self._wrapper.save(name.encode())
        




    def save_db(self, db, line):
        """
        Save a `GXTB` in a database line

        **Note:**

        Missing channels are created.
        Data in existing channels on the line will be replaced.
        """
        self._wrapper.save_db(db._wrapper, line)
        




    def save_to_ascii(self, name):
        """
        Saves the data in a table to a file. The table header will be
        in ASCII and the data will be in ASCII format.
        """
        self._wrapper.save_to_ascii(name.encode())
        




    def set_int(self, row, col, val):
        """
        Sets an integer value into a table element.

        **Note:**

        The table field containing the element to be set MUST be
        of type `GS_BYTE`, `GS_USHORT`, `GS_SHORT`, or `GS_LONG`.
        If the field is `GS_BYTE`, `GS_USHORT`, or `GS_LONG`, the new data
        value will cause an overflow if the value is out of range of
        the data type. The new element value will then be invalid.
        
        If the row of the new element exceeds the number of rows in
        the table, then the table will AUTOMATICALLY be EXPANDED to
        exactly as many rows needed to hold the new element. The new
        element is placed in the proper field of the last row, and
        all other field elements have invalid data. All fields of
        the new rows up to the new element's row will also contain
        invalid data.
        """
        self._wrapper.set_int(row, col, val)
        




    def set_double(self, row, col, val):
        """
        Sets an real value into a table element.

        **Note:**

        The table field containing the element to be set MUST be
        of type `GS_FLOAT` or `GS_DOUBLE`.
        If the field is `GS_FLOAT` the new data value will cause an
        overflow if the value is out of range of the data type.
        The new element value will then be invalid.
        
        If the row of the new element exceeds the number of rows in
        the table, then the table will AUTOMATICALLY be EXPANDED to
        exactly as many rows needed to hold the new element. The new
        element is placed in the proper field of the last row, and
        all other field elements have invalid data. All fields of
        the new rows up to the new element's row will also contain
        invalid data.
        """
        self._wrapper.set_double(row, col, val)
        




    def set_string(self, row, col, val):
        """
        Sets a string value into a table element.

        **Note:**

        The table field containing the element to be set MUST be
        of 'string'.
        
        If the row of the new element exceeds the number of rows in
        the table, then the table will AUTOMATICALLY be EXPANDED to
        exactly as many rows needed to hold the new element. The new
        element is placed in the proper field of the last row, and
        all other field elements have invalid data. All fields of
        the new rows up to the new element's row will also contain
        invalid data.
        """
        self._wrapper.set_string(row, col, val.encode())
        




    def sort(self, col):
        """
        Sorts a table by a specified column.

        **Note:**

        If the column to sort by contains duplicated values, the
        sorted table is NOT guaranteed to retain the ordering of
        the duplicated values/
        E.g. Given 2 rows of values:   xx   yy   1
        bb   aa   1
        If the table is sorted on column 3, the second row
        may or may not come after the first row in the sorted
        table.
        """
        self._wrapper.sort(col)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer