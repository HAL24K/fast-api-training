from apps.api.adapters import people_repository
from apps.api.domain import commands, models


def get_person(
    command: commands.GetPerson,
    people_repository: people_repository.AbstractPeopleRepository,
) -> models.PersonModel:
    return people_repository.get(command.id)


def add_person(
    command: commands.AddPerson,
    people_repository: people_repository.AbstractPeopleRepository,
) -> models.PersonModel:
    return people_repository.add(command.person)


COMMAND_HANDLERS = {
    commands.GetPerson: get_person,
    commands.AddPerson: add_person,
}
