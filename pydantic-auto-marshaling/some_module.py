from datetime import datetime

from pydantic import BaseModel, PositiveInt, RootModel


# Set up data models
class User(BaseModel):
    id: int
    name: str = 'John Doe'
    signup_ts: datetime | None
    tastes: dict[str, PositiveInt]


class Users(RootModel):
    root: list[User]

    def __iter__(self):
        return iter(self.root)

    def __getitem__(self, item):
        return self.root[item]


# A function that takes in a Pydantic object
def func1(data: Users) -> Users:
    assert isinstance(data, Users)
    # In a production settings, you would do something here
    return data


def func2(data: list) -> list:
    assert isinstance(data, list)
    return data
