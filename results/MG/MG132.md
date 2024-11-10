# MQFS132
## Scenario
```gherkin
scenario: testing the api 
   given i have a running api 
   when i send a get request to the api 
   then i should receive a json response with a status code of 200 
   when i send a post request to the api with valid data 
   then i should receive a json response with a status code of 201 
   when i send a put request to the api with valid data 
   then i should receive a json response with a status code of 200 
   when i send a delete request to the api with a valid id 
   then i should receive a json response with a status code of 200 
   when i send a get request to the api with an invalid id 
   then i should receive a json response with a status code of 404 
   when i send a post request to the api with invalid data 
   then i should receive a json response with a status code of 400 
   when i send a put request to the api with an invalid id 
   then i should receive a json response with a status code of 404 
   when i send a delete request to the api with an invalid id 
   then i should receive a json response with a status code of 404
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: testing the api given i have a running api when i send a get request to the api then i should receive a json response with a status code of 200 when i send a post request to the api with valid data then i should receive a json response with a status code of 201 when i send a put request to the api with valid data then i should receive a json response with a status code of 200 when i send a delete request to the api with a valid id then i should receive a json response with a status code of 200 when i send a get request to the api with an invalid id then i should receive a json response with a status code of 404 when i send a post request to the api with invalid data then i should receive a json response with a status code of 400 when i send a put request to the api with an invalid id then i should receive a json response with a status code of 404 when i send a delete request to the api with an invalid id then i should receive a json response with a status code of 404 ```



```python from behave import given, when, then
import json
import requests

@given("i have a running api")
def step_impl(context):
    context.base_url = "http://localhost:8000"

@when("i send a get request to the api")
def step_impl(context):
    context.response = requests.get(context.base_url)

@then("i should receive a json response with a status code of 200")
def step_impl(context):
    assert context.response.status_code == 200
    assert context.response.headers["Content-Type"] == "application/json"

@when("i send a post request to the api with valid data")
def step_impl(context):
    context.valid_data = {"key": "value"}
    context.response = requests.post(context.base_url, json=context.valid_data)

@then("i should receive a json response with a status code of 201")
def step_impl(context):
    assert context.response.status_code == 201
    assert context.response.headers["Content-Type"] == "application/json"

@when("i send a put request to the api with valid data")
def step_impl(context):
    context.valid_data = {"key": "value"}
    context.response = requests.put(context.base_url, json=context.valid_data)

@then("i should receive a json response with a status code of 200")
def step_impl(context):
    assert context.response.status_code == 200
    assert context.response.headers["Content-Type"] == "application/json"

@when("i send a delete request to the api with a valid id")
def step_impl(context):
    context.valid_id = 1
    context.response = requests.delete(f"{context.base_url}/{context.valid_id}")

@then("i should receive a json response with a status code of 200")
def step_impl(context):
    assert context.response.status_code ==
