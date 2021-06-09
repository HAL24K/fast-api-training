import uuid

from pydantic import BaseModel, Field


class ResponseModel(BaseModel):
    message: str


class AddressModel(BaseModel):
    """Execrise 3"""

    pass


class PersonModel(BaseModel):
    id: uuid.UUID = Field(default=uuid.uuid4())
    name: str
    age: int
    address: AddressModel = Field(default=AddressModel())