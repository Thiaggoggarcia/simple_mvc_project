from src.view.http_types.http_response import HttpResponse
from src.errors.types.http_bad_request import HttpBadRequest

def handler_errors(error: Exception) -> HttpResponse:
    if isinstance(error, HttpBadRequest):
        return HttpResponse(
            status_code= error.status_code,
            body={
                "errors": [{
                    "title": error.name,
                    "detail": error.mensagem
                }]
            }
        )
    
    return HttpResponse(
        status_code=500,
        body={
            "errors": [{
                "title": "Server Error",
                "detail": str(error)
            }]
        }
        
    )