class NextGenException(Exception):
    def __init__(self, code: int, message: str):
        self.code = code
        self.message = message

class InvalidRequestException(NextGenException):
    def __init__(self, message: str = "Invalid request parameters"):
        super().__init__(400, message)

class ProcessingException(NextGenException):
    def __init__(self, message: str = "Error processing request"):
        super().__init__(500, message)

class ModelNotFoundException(NextGenException):
    def __init__(self, message: str = "Requested model not available"):
        super().__init__(404, message)