from typing import Any
from .util import is_sql
from .Exceptions import SQLInjectionDetected

def add_data(table_name: str, data: dict, check_for_SQL_Injection: bool = True) -> str:
    """
    Generates an SQL query to insert data into a table.
    
    :param str table_name: The name of the table.
    :param str data: A dictionary where keys are column names and values are the data to insert.
    :param bool check_for_SQL_Injection: A boolean flag to check for SQL injection. Default is True.
    
    :return: The SQL `INSERT INTO` query.
    """
    if check_for_SQL_Injection:
        # Check if any value in the data dictionary contains SQL code
        for value in data.values():
            if is_sql(str(value)):
                raise SQLInjectionDetected(f"SQL detected in input data: {value}")
    
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

def update_data(table_name: str, data: dict, id: Any, identifier: Any, check_for_SQL_Injection: bool = True) -> str:
    """
    Generates an SQL query to update data in a table.
    
    :param table_name: The name of the table.
    :param data: A dictionary where keys are column names and values are the new data.
    :param where: The condition to match records to update.
    
    :return: The SQL `UPDATE` query.
    """
    
    if check_for_SQL_Injection:
        # Check if any value in the data dictionary contains SQL code
        for value in data.values():
            if is_sql(str(value)):
                raise SQLInjectionDetected(f"SQL detected in input data: {value}")
    
    set_values = ", ".join([f"{k} = '{v}'" if isinstance(v, str) else f"{k} = {v}" for k, v in data.items()])
    query = f"UPDATE {table_name} SET {set_values} WHERE {identifier} = {id}"
    return query