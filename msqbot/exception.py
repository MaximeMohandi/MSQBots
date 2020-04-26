class MsqbitsReporterException(Exception):
    """Personal Exception for msqbitsReporter"""
    pass


class HttpError(MsqbitsReporterException):
    """An Exception cause by an http error"""
    pass


class HttpClientError(HttpError):
    """Error 4xx: The error seems to have been caused by the client"""
    pass


class HttpBadRequestError(HttpClientError):
    """Error 400: The server cannot or will not process the request due to an apparent client error (e.g.,
    malformed request syntax, size too large, invalid request message framing, or deceptive request routing). """
    pass


class HttpForbiddenError(HttpClientError):
    """Error 403: The request contained valid data and was understood by the server, but the server is refusing
    action. This may be due to the user not having the necessary permissions for a resource or needing an account of
    some sort, or attempting a prohibited action (e.g. creating a duplicate record where only one is allowed). This
    code is also typically used if the request provided authentication via the WWW-Authenticate header field,
    but the server did not accept that authentication. The request should not be repeated. """
    pass


class HttpNotFoundError(HttpClientError):
    """Error 404: The requested resource could not be found but may be available in the future. Subsequent requests
    by the client are permissible. """
    pass


class HttpMethodNotAllowed(HttpClientError):
    """Error 405: A request method is not supported for the requested resource; for example, a GET request on a form
    that requires data to be presented via POST, or a PUT request on a read-only resource. """
    pass


class HttpRequestTimeout(HttpClientError):
    """Error 408: The server timed out waiting for the request. According to HTTP specifications: "The client did not
    produce a request within the time that the server was prepared to wait. The client MAY repeat the request without
    modifications at any later time."[42] """
    pass


class HttpServerError(HttpError):
    """Error 5xx: The server failed to fulfill a request."""
    pass


class HttpInternalServerError(HttpServerError):
    """Error 500: A generic error message, given when an unexpected condition was encountered and no more specific
    message is suitable. """
    pass


class HttpNotImplemented(HttpServerError):
    """Error 501: The server either does not recognize the request method, or it lacks the ability to fulfil the
    request. Usually this implies future availability (e.g., a new feature of a web-service API). """
    pass


class HttpBadGateway(HttpServerError):
    """Error 502: Te server was acting as a gateway or proxy and received an invalid response from the upstream
    server """
    pass


class HttpServiceUnavailable(HttpServerError):
    """Error 503: The server cannot handle the request (because it is overloaded or down for maintenance). Generally,
    this is a temporary state """
    pass


class HttpGatewayTimeout(HttpClientError):
    """Error 504: The server was acting as a gateway or proxy and did not receive a timely response from the upstream
    server. """
    pass


class MsqDataBaseError(MsqbitsReporterException):
    """The action on database encountered an error"""
    pass
