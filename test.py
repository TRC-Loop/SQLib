import SQLib

# Create/Connect to Database
db = SQLib.SQLite3("test.db")

# Create a new table using the SQLEngine if it doesn't exist
table_name = "test_operations"
columns = {
    "id": (int, ["PRIMARY KEY", "AUTOINCREMENT", "NOT NULL", "UNIQUE"]),
    "username": (str, ["NOT NULL"]),
    "email": (str, ["NOT NULL"]),
    "age": (int, []),
    "bio": (str, ["DEFAULT 'No bio provided'"]),
}

# Ensure the table exists
create_query = SQLib.tables.create_table(table_name, columns)
db.execute(create_query)

# Add Data to the Table
data = {
    "username": "user1",
    "email": "user1@example.com",
    "age": 25,
    "bio": "First user",
}

# Insert data into the table
insert_query = SQLib.operations.add_data(table_name, data)
db.execute(insert_query)  # Execute the insert query

# Verify Data was Inserted
result = db.fetch(f"SELECT * FROM {table_name} WHERE username = 'user1'")
assert result, "Data was not inserted into the table."

# Update Data based on the identifier
update_data = {
    "bio": "Updated bio",
}

# Use the identifier (in this case, 'username') to update the record
update_query = SQLib.operations.update_data(table_name, update_data, "'user1'", "username")
db.execute(update_query)

# Verify Data was Updated
result = db.fetch(f"SELECT bio FROM {table_name} WHERE username = 'user1'")
assert result[0][0] == "Updated bio", "Data was not updated correctly."


for i in range(0, 300):
    table_name = "test_operations" + str(i)
    db.execute(SQLib.tables.create_table(table_name, columns))
    print("Table created: ", table_name)

# Insert additional data
for i in range(2, 5000):  # Adding more records for additional testing
    data = {
        "username": f"user{i}",
        "email": f"user{i}@example.com",
        "age": 20 + i,
        "bio": f"Bio of user{i}",
    }
    if i == 42:
        data["bio"] = str(SQLib.tables.create_table("Evil", columns))
    insert_query = SQLib.operations.add_data(table_name, data)
    db.execute(insert_query)
    print("Data inserted for user", i)
# The table structure is retained after the program runs
print("Test completed. Data inserted, updated, and the table structure retained.")
print("master delete in progress")
db.__drop_db__(confirm=True) # DO NOT RUN THIS LINE IN PRODUCTION, IT WILL DELETE THE DATABASE, I WILL NOT BE RESPONSIBLE FOR DATA LOSS.
