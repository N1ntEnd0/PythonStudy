"""
Write a wrapper class TableData for database table, that when initialized with database name and table acts as
collection object (implements Collection protocol). Assume all data has unique values in 'name' column.
So, if presidents = TableData(database_name='example.sqlite', table_name='presidents')

then
    len(presidents) will give current amount of rows in presidents table in database
    presidents['Yeltsin'] should return single data row for president with name Yeltsin
    'Yeltsin' in presidents should return if president with same name exists in table

    object implements iteration protocol. i.e. you could use it in for loops::

        for president in presidents:
            print(president['name'])

    all above mentioned calls should reflect most recent data.
    If data in table changed after you created collection instance, your calls should return updated data.

Avoid reading entire table into memory. When iterating through records, start reading the first record,
then go to the next one, until records are exhausted. When writing tests,
it's not always neccessary to mock database calls completely. Use supplied example.sqlite file as database fixture file.
"""
import sqlite3


class TableData:
    def __init__(self, *, database_name, table_name):
        self.table_name = table_name
        self.database_name = database_name

    def __len__(self):
        self._cursor.execute(f"select count(*) from {self.table_name}")
        return self._cursor.fetchone()[0]

    def __getitem__(self, item):
        self._cursor.execute(
            f"select * from {self.table_name} where name=:name", {"name": item}
        )
        return self._cursor.fetchone()

    def __contains__(self, item):
        for i in self.__iter__():
            if item in i.values():
                return True
        return False

    def __iter__(self):
        def dict_factory(row):
            d = {}
            for idx, col in enumerate(self._cursor.description):
                d[col[0]] = row[idx]
            return d

        yield from (
            dict_factory(row)
            for row in self._cursor.execute(f"select * from {self.table_name}")
        )

    def __enter__(self):
        self._conn = sqlite3.connect(self.database_name)
        self._cursor = self._conn.cursor()

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._conn.close()
