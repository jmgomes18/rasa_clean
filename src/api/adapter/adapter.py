from typing import Type
from sqlalchemy.exc import IntegrityError
from api.services.fields import RegisterField
from api.presenters.helpers import HttpRequest, HttpResponse
from api.presenters.errors import HttpErrors


def adapter(request: any, api_route: Type[RegisterField]) -> any:
    """Adapter pattern to Lambda
    :param - request
    :api_route: Composite Routes
    """

    http_request = HttpRequest(
        header=request["headers"], body=request["body"], query=["queryStringParameters"]
    )

    try:
        response = api_route.route(http_request)
    except IntegrityError:
        http_error = HttpErrors.error_409()
        return HttpResponse(
            status_code=http_error["statusCode"], body=http_error["body"]
        )
    except Exception as exc:
        print(exc)
        http_error = HttpErrors.error_500()
        return HttpResponse(
            status_code=http_error["statusCode"], body=http_error["body"]
        )

    return response
