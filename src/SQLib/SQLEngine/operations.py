from typing import Any

def add_data(table_name: str, data: dict) -> str:
    """
    Generates an SQL query to insert data into a table.
    
    :param table_name: The name of the table.
    :param data: A dictionary where keys are column names and values are the data to insert.
    
    :return: The SQL `INSERT INTO` query.
    """
    columns = ", ".join(data.keys())
    values = ", ".join([f"'{v}'" if isinstance(v, str) else str(v) for v in data.values()])
    query = f"INSERT INTO {table_name} ({columns}) VALUES ({values})"
    return query

def drop_data(table_name: str, where: str) -> str:
    """
    Generates an SQL query to delete data from a table.
    
    :param table_name: The name of the table.
    :param where: The condition to match records to delete.
    
    :return: The SQL `DELETE FROM` query.
    """
    query = f"DELETE FROM {table_name} WHERE {where}"
    return query

def update_data(table_name: str, data: dict, id: Any, identifier: Any) -> str:
    """
    Generates an SQL query to update data in a table.
    
    :param table_name: The name of the table.
    :param data: A dictionary where keys are column names and values are the new data.
    :param where: The condition to match records to update.
    
    :return: The SQL `UPDATE` query.
    """
    set_values = ", ".join([f"{k} = '{v}'" if isinstance(v, str) else f"{k} = {v}" for k, v in data.items()])
    query = f"UPDATE {table_name} SET {set_values} WHERE {identifier} = {id}"
    return query