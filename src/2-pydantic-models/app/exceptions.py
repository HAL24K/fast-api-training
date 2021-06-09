import logging


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


class EntityNotFound(DomainException):
    code = "ENTITY_NOT_FOUND"
    status_code = 404