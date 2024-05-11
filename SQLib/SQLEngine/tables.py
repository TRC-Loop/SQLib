TYPES = {
    int: "INTEGER",
    str: "TEXT",
    float: "REAL",
    bytes: "BLOB",
    type(None): "NULL",
}

# SQL modifiers you can apply to columns
MODS = ["PRIMARY KEY", "NOT NULL", "UNIQUE", "CHECK", "DEFAULT"]


def create_table(table_name: str, columns: dict[str, tuple[type, list[str]]]) -> str:
    """
    Generates an SQL query to create a table.
    
    :param table_name: The name of the table.
    :param columns: A dictionary where keys are column names and values are tuples.
                    Each tuple contains the Python type and a list of SQL modifiers.
    :return: The SQL `CREATE TABLE` query.
    """
    column_definitions = []
    
    for column_name, (py_type, mods) in columns.items():
        sql_type = TYPES.get(py_type, "TEXT")  # Default to "TEXT" if type is unknown
        modifiers = " ".join(mods)  # Convert the list of modifiers to a string
        
        # Build the column definition
        column_definitions.append(f"{column_name} {sql_type} {modifiers}")

    # Combine the column definitions to form the CREATE TABLE query
    column_definitions_str = ", ".join(column_definitions)
    
    # Sanitize table_name to prevent SQL injection
    sanitized_table_name = table_name.replace("'", "''")
    
    create_query = f"CREATE TABLE IF NOT EXISTS '{sanitized_table_name}' ({column_definitions_str})"
    return create_query


def drop_table(table_name: str) -> str:
    """
    Generates an SQL query to drop a table.
    
    :param table_name: The name of the table to drop.
    :return: The SQL `DROP TABLE` query.
    """
    return f"DROP TABLE IF EXISTS {table_name}"