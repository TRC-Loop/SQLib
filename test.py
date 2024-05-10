import SQLib
import SQLib.SQLEngine

# Create/Connect to Database
db = SQLib.SQLite3("test.db")

# Create a table manually
db.execute("CREATE TABLE IF NOT EXISTS test_manual (id INTEGER PRIMARY KEY)")

# Create a table using the SQLEngine
table_name = "test_SQLEngine"
columns = {
    "id": (int, ["PRIMARY KEY", "AUTOINCREMENT"]),
    "username": (str, ["NOT NULL", "UNIQUE"]),
    "email": (str, ["NOT NULL"]),
    "age": (int, []),
    "bio": (str, ["DEFAULT 'No bio provided'"]),
}

query = SQLib.tables.create_table(table_name, columns)
db.execute(query)

table_name = "test_SQLEngine2"
query = SQLib.tables.create_table(table_name, columns)
db.execute(query)

db.execute(SQLib.tables.drop_table("test_SQLEngine2"))