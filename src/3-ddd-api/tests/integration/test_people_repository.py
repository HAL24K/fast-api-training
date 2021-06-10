import pytest

from bson.objectid import ObjectId

from apps.api.adapters import people_repository
from apps.api.domain import models


@pytest.mark.parametrize(
    "name, age",
    [
        pytest.param("John", 20),
        pytest.param("Lisa", 32),
        pytest.param("Frank", 55),
        pytest.param("Suzy", 61),
    ],
)
def test_add_person(name, age):
    person = models.PersonModel(name=name, age=age)
    repo = people_repository.InMemoryPeopleRepository()

    repo.add(person)


def test_get_person():
    id = ObjectId("60c2866a704fb00b25276344")
    repo = people_repository.InMemoryPeopleRepository()

    person = repo.get(id)

    assert person.name == "Jack"