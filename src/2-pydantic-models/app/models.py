import uuid

from pydantic import BaseModel, Field


class ResponseModel(BaseModel):
    message: str


class AddressModel(BaseModel):
    """Execrise 3 - Define properties"""

    pass


class PersonModel(BaseModel):
    id: uuid.UUID = Field(default_factory=uuid.uuid4)
    name: str
    age: int
    address: AddressModel = Field(default=AddressModel())