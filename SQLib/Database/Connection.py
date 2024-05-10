import sqlite3 as _sqlite3
from .Exceptions import FetchError, QueryError

class SQLite3:
    def __init__(self, db_name):
        try:
            self.connection = _sqlite3.connect(db_name)  # Initialize connection
            self.cursor = self.connection.cursor()  # Initialize cursor
        except _sqlite3.Error as e:
            print(f"Error initializing database connection: {e}")
            self.cursor = None  # This should only happen if there's an error

    def __enter__(self):
        self.connection = _sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.connection:
            self.connection.close()

    def __del__(self):
        # Close the connection
        if self.connection:
            self.connection.close()
    
    def execute(self, query: str, params: tuple = ()) -> None:
        try:
            self.cursor.execute(query, params)
            self.connection.commit()
        except _sqlite3.Error as e:
            raise QueryError(f"Error executing: {str(e)}")

    def fetch(self, query: str, params: tuple = ()) -> list:
        try:
            self.cursor.execute(query, params)
            return self.cursor.fetchall()
        except _sqlite3.Error as e:
            raise FetchError(f"Error fetching: {str(e)}")