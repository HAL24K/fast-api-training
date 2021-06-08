# Fast API Training

A repo dedicated to training the team the concepts around Fast API development

# 1 - Hello World Fast API

```shell
$ cd 1-hello-world-api
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

## Run the Tests

```shell
$ pytest tests
```

## Run Tests with Coverage Report

```shell
$ pytest --cov app
```

# Exercises

## Exercise 1

Write a test for `get_item` function.

## Exercise 2

Create a new endpoint which returns all items.

Write a test to check the response.

## Exercise 3

Create a new endpointwhich adds a new item to the list.
Use the Fast API field validation to validate inputs.

- The name value should be a valid string.
- The age value should be a valid int.

Write a test to check your inputs.

## Exercise 4

Create a new endpoint which allows the `age` value to be updated.

Write a test to check that the value is updated.

## Exercise 5

Create an endpoint which deletes an item by its index.

Write a test to check that the item is deleted.
