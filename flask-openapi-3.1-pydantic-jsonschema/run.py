import json
from pathlib import Path

from pydantic_openapi_schema.utils.utils import OpenAPI310PydanticSchema, construct_open_api_with_schema_class
from pydantic_openapi_schema.v3_1_0 import OpenAPI, Info, PathItem, Operation, Response, RequestBody, MediaType, Components, Reference

from models import Pet, produce_schema
from wsgi import create_app


open_api = OpenAPI(
    openapi='3.1.0',
    info=Info(
        title="My own API",
        version="v0.0.1",
    ),
    paths={
        "/ping": PathItem(
            get=Operation(
                responses={
                    "200": Response(
                        description="pong"
                    )
                }
            )
        ),
        "/pets": PathItem(
            post=Operation(
                requestBody=RequestBody(
                    required=True,
                    content={
                        "application/json": MediaType(
                            schema=OpenAPI310PydanticSchema(schema_class=Pet)
                        )
                    }
                ),
                responses={
                    "200": Response(
                        description="response",
                        content={
                            "application/json": MediaType(
                                schema=OpenAPI310PydanticSchema(schema_class=Pet)
                            )
                        }
                    )
                },
            )
        ),
        "/produce": PathItem(
            post=Operation(
                requestBody=RequestBody(
                    required=True,
                    content={
                        "application/json": MediaType(
                            schema=Reference(ref="#/components/schemas/Produce")
                            # schema=Schema(**produce_schema)
                        )
                    }
                )
            )
        )
    },
    components=Components(
        schemas={
            "Produce": produce_schema,
        }
    )
)
open_api: OpenAPI = construct_open_api_with_schema_class(open_api)



openapi_file = Path('openapi.json').resolve()
with open(openapi_file, 'w') as f:
    json.dump(open_api.dict(by_alias=True, exclude_none=True), f, indent=2)


create_app(openapi_file).run()
