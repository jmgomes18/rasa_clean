from typing import Dict


class HttpRequest:
    """Class to http_request representation"""

    def __init__(
        self,
        header: Dict = None,
        body: Dict = None,
        query: Dict = None,
        path_params=None,
    ):
        self.header = header
        self.body = body
        self.query = query
        self.path_params = path_params

    def __repr__(self):
        return f"HttpRequest (header={self.header}, body={self.body}, query={self.query}, path_params={self.path_params})"


class HttpResponse:
    """Class to http_response representation"""

    def __init__(self, status_code: int, body: any):
        self.status_code = status_code
        self.body = body

    def __repr__(self):
        return f"HttpResponse (statusCode={self.status_code}, body={self.body})"
