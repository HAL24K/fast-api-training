def test_root(client):
    response = client.get("/")

    assert response.status_code == 200


def test_get_person(client):
    id = "60c2866a704fb00b25276344"
    response = client.get(f"people/{id}")

    assert response.status_code == 200
    assert response.json()["name"] == "Jack"


def test_add_person(client):
    person = dict(person=dict(_id="60c28f63e968a7d3251fa518", name="Bob", age=24))
    response = client.post("people", json=person)

    assert response.status_code == 200
    assert response.json()["name"] == "Bob"