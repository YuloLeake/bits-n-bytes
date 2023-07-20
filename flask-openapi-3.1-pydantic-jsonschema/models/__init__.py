import json
from pathlib import Path

from .petstore import Pet


produce_schema_file = Path(__name__).resolve() / 'produce-schema.json'
print(produce_schema_file)
with open(produce_schema_file) as f:
    produce_schema = json.load(f)


__all__ = ['Pet', 'produce_schema']
