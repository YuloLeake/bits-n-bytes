import json
import inspect

from pydantic import BaseModel

import some_module


def call_func(func, data: str):
    signature = inspect.signature(func)
    input_type = list(signature.parameters.values())[0].annotation
    return_type = signature.return_annotation
    print(input_type)
    print(return_type)
    print(data)

    if issubclass(input_type, BaseModel):
        # Unmarshal input since the function is expecting a Pydantic model
        data = input_type.model_validate_json(data)
    else:
        # Data is encoded JSON so decode it
        data = json.loads(data)

    output = func(data)

    if issubclass(return_type, BaseModel):
        # Marshal output since the function returns a Pydantic model
        output = output.model_dump_json()
    else:
        # Encode JSON data
        output = json.dumps(output)

    print(output)
    return output


func1 = some_module.func1
with open("users.json") as f:
    inp = json.dumps(json.load(f))

out = call_func(func1, inp)
assert isinstance(out, str)

func2 = some_module.func2
with open("users.json") as f:
    inp = json.dumps(json.load(f))

out = call_func(func2, inp)
assert isinstance(out, str)
