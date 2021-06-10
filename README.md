# Fast API Training

A repo dedicated to training the team the concepts around Fast API development.

# Prerequisites

- Python 3.8: See [Install Instructions](./docs/INSTALL_PYTHON.md)
- Docker: See [Install Instructions](./docs/INSTALL_DOCKER.md)
- Pipenv: See [Install Instructions](./docs/INSTALL_PIPENV.md)

# 1 - Hello World Fast API

In this lesson we will learn about the basics of creating a RESTful API with the
[FastAPI](https://fastapi.tiangolo.com/) micro-web framework.

```shell
$ cd src/1-hello-world-api
```

## Setup Virtual Environment

```shell
$ python3 -m venv .venv
$ source .venv/bin/activate
```

## Install Requirements

```shell
$ pip install -r requirements.txt
```

## Run the API

```shell
$ uvicorn app.main:app --reload
```

Navigate to `http://127.0.0.1:8000/items/1`

## Documentation

Redoc documentation using OpenAPI can be found at http://127.0.0.1:8000/redoc

## Run the Tests

```shell
$ pytest tests
```

## Run Tests with Coverage Report

```shell
$ pytest --cov app
```

# Exercises

Below are coding exercises to be completed with your group. See the
[FastAPI documentation](https://fastapi.tiangolo.com/) for reference.

## Exercise 1

Write a test for `get_item` function.

## Exercise 2

Create a new endpoint which returns all items.

Write a test to check the response.

## Exercise 3

Create a new endpoint which adds a new item to the list.
Use the Fast API field validation to validate inputs.

- The name value should be a valid string.
- The age value should be a valid int.

Return the added item in the response.

Write a test to check your inputs.

## Exercise 4

Create a new endpoint which allows the `age` value to be updated.

Return the updated item in the response.

Write a test to check that the value is updated.

## Exercise 5

Create an endpoint which deletes an item by its index.

Write a test to check that the item is deleted.

# 2 - Pydantic Models

In this lesson we'll discuss creating [Pydantic](https://pydantic-docs.helpmanual.io/) data models
for data integrity and validation.

```shell
$ cd src/2-pydantic-models
```

## Install Requirements with Pipenv

See [Pipenv install instructions](./docs/INSTALL_PIPENV.md).

Run the command below to install the dependencies along with the development dependencies.

```shell
$ pipenv install --dev
```

Once the dependencies are installed, you will need to start the Pipenv shell.

```shell
$ pipenv shell
```

# Run the App

Like in the previous example, start the app with:

```shell
$ uvicorn app.main:app --reload
```

# Exercises

When you complete the exercises below, the tests should all pass

```shell
$ pytest tests
```

## Exercise 1

Open the `app/main.py` file.

Look for the `items` variable, change the dict values into Pydantic models using the `PersonModel`

Hint: set one item to use a fixed uuid value of `5152cda2-db25-4338-8ffa-77923f2c885f`.

```python
uuid.UUID("5152cda2-db25-4338-8ffa-77923f2c885f")
```

## Exercise 2

Open the `app/main.py` file.

Replace the generic `dict` type with the `PersonModel` to validate an object posted to the `/items` endpoint.

## Exercise 3

Open the `app/models.py` file.

Update only the `AddressModel ` used for updating a person's address while maintaining their original Uuid,
name and age properties.

The new model should contain the following fields:

- street: string - default to empty string
- house_no: string - default to empty string
- postal_code: string - default to empty string
- city: string - default to empty string
- country: string - default to empty string

# Fast API with Domain Driven Design (DDD)

```shell
$ cd src/3-ddd-api
```

The code in this example follows the [Domain Driven Design](https://en.wikipedia.org/wiki/Domain-driven_design)
pattern.

In short, Domain-driven design (DDD) is the concept that the structure and language of software code (class names,
class methods, class variables) should match the business domain. For example, if a software processes
loan applications, it might have classes such as LoanApplication and Customer, and methods such as AcceptOffer and Withdraw.

In this example the domain classes are stored in the `apps/api/domain` directory as pure classes. The persistence layer is handled
via `adapters` which are abstracted into their own classes. These are located in the `apps/api/adapters` directory.

The `Context` class loads the correct adapters, commands, and messagebus

# Install Dependencies

```shell
$ pipenv install --dev
$ pipenv shell
```

# Run the Tests

```shell
$ pytest tests
```

# Applications

To show how DDD can be used in multiple applications, there is a RESTful API using FastAPI,
and a CLI using Click.

## FastApi

In a separate shell you can run the following command to start the FastAPI implementation.

```shell
$ uvicorn apps.api.entrypoint:app --reload
```

## Click

In another shell you can run the following command to get and add a person to the same person repository
used in the FastAPI implementation.

### Add Person

```shell
PYTHONPATH=. python apps/cli/people.py add Henry 45
```

### Get Person

```shell
PYTHONPATH=. python apps/cli/people.py get 60c2866a704fb00b25276344
```
