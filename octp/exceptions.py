class Error(Exception):
    """Basic exception that all python-octp-api exceptions will inherit from"""

class InternalServerError(Error):
    """All sever related errors will inherit from this, invalid response, timeout, etc."""

class InvalidResponse(InternalServerError):
    """The response form the server was invalid, and not what we expected"""

class Timedout(InternalServerError):
    """The request to the server timed out"""

class ServerError(Error):
    """Whenever the server will throw a error in {"error": "some error"}, we will throw this"""

class NotFound(ServerError):
    """The specific item that we tried to find, could not be located"""

class NoLabs(ServerError):
    """There is currently no labs available"""

