import re

def is_sql(string: str, sql_keywords: list[str] = ["SELECT", "INSERT", "UPDATE", "DELETE", "CREATE", "DROP", "ALTER", "JOIN", "FROM", "WHERE", "AND", "OR", "IN", "NOT", "NULL", "ORDER BY", "GROUP BY", "HAVING", "LIMIT", "UNION" ]) -> bool:
    """
    Check if a string contains SQL keywords.
    
    :param string: The string to check.
    
    :return: True if the string contains SQL keywords, False otherwise.
    """
    
    regex = r'\b(?:' + '|'.join(sql_keywords) + r')\b'
    return bool(re.search(regex, string.upper()))