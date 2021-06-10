import logging
import datetime
from typing import Union, Any

from bson.objectid import ObjectId


logger = logging.getLogger(__name__)


class DomainException(Exception):
    def __init__(self, message: str, code=None, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code:
            self.status_code = status_code
        if code:
            self.code = code
        self.payload = payload

        logger.error(message)

    def to_dict(self):
        exc_dict = dict(self.payload or ())
        exc_dict["message"] = self.message
        exc_dict["code"] = self.code
        return exc_dict


def to_objectid_str(id: Any) -> str:
    return str(id)


def from_objectid_str(id: Any) -> Union[ObjectId, Any]:
    if ObjectId.is_valid(id):
        return ObjectId(id)
    return id


def to_isoformat(date_time: datetime.datetime) -> str:
    return date_time.replace(tzinfo=datetime.timezone.utc, microsecond=0).isoformat()


def from_isoformat(date_time: str) -> datetime.datetime:
    return datetime.datetime.fromisoformat(date_time)


class ObjectIdField(ObjectId):
    """
    A MongoDb ObjectId field
    """

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(
            pattern="^[a-f\d]{24}$",
            examples=["5fdb7e760ee890fcabc426a2"],
        )

    @classmethod
    def validate(cls, value):
        if not ObjectId.is_valid(value):
            raise ValueError("Invalid ObjectId")
        if isinstance(value, str):
            return ObjectId(value)
        return value

    def __repr__(self):
        return f"{self.__class__.__name__}({super().__repr__()})"