from datetime import datetime

from bson.objectid import ObjectId
from pydantic import BaseModel, Field

from apps.api.domain.library import ObjectIdField, to_objectid_str, to_isoformat


class ResponseModel(BaseModel):
    message: str


class AddressModel(BaseModel):
    """Execrise 3 - Define properties"""

    pass


class PersonModel(BaseModel):
    class Config:
        json_encoders = {ObjectId: to_objectid_str, datetime: to_isoformat}

    id: ObjectIdField = Field(alias='_id', default_factory=ObjectId)
    name: str
    age: int
    address: AddressModel = Field(default=AddressModel())
    created: datetime = Field(default_factory=datetime.utcnow)