from apps.api.domain.library import DomainException


class EntityNotAdded(DomainException):
    code = "ENTITY_NOT_ADDED"
    status_code = 500


class EntityNotFound(DomainException):
    code = "ENTITY_NOT_FOUND"
    status_code = 404


class ConfigurationError(DomainException):
    code = "CONFIGURATION_ERROR"
    status_code = 500