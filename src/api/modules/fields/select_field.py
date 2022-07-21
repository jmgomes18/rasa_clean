from api.adapter.adapter import adapter
from api.composer.select_field_composite import select_field_composer


def handler(event, context):
    """find users route"""
    message = {}
    try:
        response = adapter(request=event, api_route=select_field_composer())

        if response.status_code < 300:
            message = []

            for data in response.body:
                for x in data:
                    message.append(
                        {
                            "owner_id": x.owner_id,
                            "title": x.title,
                            "description": x.description,
                            "active": x.active,
                            "type": x.type,
                            "order": x.order,
                        }
                    )

            return {"statusCode": 200, "body": {"fields": message}}
        else:
            return {"statusCode": 204}

    except Exception as e:
        # Handling Errors
        print(e)
        return {
            "statusCode": 500,
        }
