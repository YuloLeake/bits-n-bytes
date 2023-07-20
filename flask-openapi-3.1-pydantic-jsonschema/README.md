As of July 2023, there isn't a widely used library that can render OpenAPI 3.1 
(Swagger UI version 5+), especially for Flask.
This project uses
[Swagger UI version `5.1.1`](https://github.com/swagger-api/swagger-ui/tree/v5.1.1)
specifically.

This mini project tests what would take to render OpenAPI 3.1 in Flask.

It also creates an OpanAPI 3.1 schema file from Pydantic and JSON schema files 
(uses 
[pydantic-openapi-schema](https://github.com/litestar-org/pydantic-openapi-schema)
under the hood. Sadly it's been archived so you may need to vendor it or find an
alternative that generated OpenAPI 3.1, which I wasn't able to find).

Simply install the dependencies and run `run.py`.
i.e.,
``` console
pip install -r requirements.txt
python run.py
```
