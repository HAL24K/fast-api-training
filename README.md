# Fast API Training

A repo dedicated to training the team the concepts around Fast API development.

# Prerequisites

- Python 3.8: See [Install Instructions](./docs/INSTALL_PYTHON.md)
- Docker: See [Install Instructions](./docs/INSTALL_DOCKER.md)
- Pipenv: See [Install Instructions](./docs/INSTALL_PIPENV.md)

# 1 - Hello World Fast API

In this lesson we will learn about the basics of creating a RESTful API with the [FastAPI](https://fastapi.tiangolo.com/) micro-web framework.

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

Below are coding exercises to be completed with your group.

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

In this lesson we'll discuss creating [Pydantic](https://pydantic-docs.helpmanual.io/) data models for data integrity and validation.

```shell
$ cd src/2-pydantic-models
```

## Install Requirements with Pipenv

See [Pipenv install instructions](./docs/INSTALL_PIPENV.md).

Run the command below to install the dependencies along with the development dependencies.

```shell
pipenv install --dev
```

Once the dependencies are installed, you will need to start the Pipenv shell.

```shell
pipenv shell
```

# Exercises

## Exercise 1

Open the `app/main.py` file.

Look for the `items` variable, change the dict values into Pydantic models using the `PersonModel`

## Exercise 2

Replace `dict` with the `PersonModel` to validate an object posted to the `/items` endpoint.

## Exercise 3

Create a new `AddressModel ` used for updating a person's address while maintaining their original Uuid.

The new model should contain the following fields:

- street: string - default to empty string
- house_no: string - default to empty string
- postal_code: string - default to empty string
- city: string - default to empty string
- country: string - default to empty string
