class SQLInjectionDetected(Exception):
    """
    Raised when SQL code is detected in the input data.
    This is called SQL injection and is a security risk.
    It can be used to delete or modify data in the database.
    """
    def __init__(self, message: str):
        super().__init__(message)