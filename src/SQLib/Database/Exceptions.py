class FetchError(Exception):
    def __init__(self, message: str):
        super().__init__(message)
        
class QueryError(Exception):
    def __init__(self, message: str):
        super().__init__(message)