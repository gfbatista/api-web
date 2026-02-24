from src.views.http_types.http_response import HttpResponse
from .error_types.http_not_found import HttpNotFoundError
from .error_types.http_bad_request import HttpBadRequestError

def handle_errors(error: Exception) -> HttpResponse:
    if isinstance(error, (HttpNotFoundError, HttpBadRequestError)):
        return HttpResponse(
            status_code=error.status_code,
            body={
                "detail": error.message,
                "title": error.name
            }
        )
    return HttpResponse(
        status_code=error.status_code,
            body={
                "detail": str(error),
                "title": 'Internal Server Error'
            }
    )
