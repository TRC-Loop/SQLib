import unittest
import SQLib
import SQLib.SQLEngine

class TestSQLib(unittest.TestCase):
    def setUp(self):
        # Create/Connect to a temporary database for testing
        self.db = SQLib.SQLite3("test.db")
        
    def test_create_and_drop_table(self):
        # Create a table manually
        self.db.execute("CREATE TABLE IF NOT EXISTS test_manual (id INTEGER PRIMARY KEY)")

        # Create a table using the SQLEngine
        table_name = "test_SQLEngine"
        columns = {
            "id": (int, ["PRIMARY KEY", "AUTOINCREMENT"]),
            "username": (str, ["NOT NULL", "UNIQUE"]),
            "email": (str, ["NOT NULL"]),
            "age": (int, []),
            "bio": (str, ["DEFAULT 'No bio provided'"]),
        }

        # Test creating a table
        create_query = SQLib.tables.create_table(table_name, columns)
        self.db.execute(create_query)
        
        # Test inserting data into the table
        self.db.execute(f"INSERT INTO {table_name} (username, email, age, bio) VALUES ('testuser', 'test@example.com', 30, 'Hello World')")

        # Test querying the table
        result = self.db.fetch(f"SELECT * FROM {table_name}")
        self.assertTrue(result)  # Check that there's at least one record

        # Test dropping the table
        drop_query = SQLib.tables.drop_table("test_SQLEngine")
        self.db.execute(drop_query)

        # Test that the table no longer exists
        with self.assertRaises(Exception):  # Should raise if table doesn't exist
            self.db.fetch(f"SELECT * FROM {table_name}")

    def tearDown(self):
        # Close the database connection
        self.db.connection.close()
        # Optionally, clean up test artifacts like removing the test database
        import os
        if os.path.exists("test.db"):
            os.remove("test.db")

# Run the tests
if __name__ == "__main__":
    unittest.main()
