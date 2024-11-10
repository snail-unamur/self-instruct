# HQFS1
## Scenario
```gherkin
scenario: testing the api 
   given i have a valid api key 
   when i send a get request to "/users" 
   then i should receive a json response with a list of users 
   when i send a get request to "/users/{id}" 
   then i should receive a json response with a single user 
   when i send a post request to "/users" with valid data 
   then i should receive a json response with a new user 
   when i send a put request to "/users/{id}" with valid data 
   then i should receive a json response with an updated user 
   when i send a delete request to "/users/{id}" 
   then i should receive a json response with a message confirming deletion
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: testing the api given i have a valid api key when i send a get request to "/users" then i should receive a json response with a list of users when i send a get request to "/users/{id}" then i should receive a json response with a single user when i send a post request to "/users" with valid data then i should receive a json response with a new user when i send a put request to "/users/{id}" with valid data then i should receive a json response with an updated user when i send a delete request to "/users/{id}" then i should receive a json response with a message confirming deletion ```



```python from behave import given, when, then
import json
import requests

@given("i have a valid api key")
def step_impl(context):
    context.api_key = "valid_api_key"

@when("i send a get request to \"/users\"")
def step_impl(context):
    context.response = requests.get("/users", headers={"Authorization": context.api_key})

@then("i should receive a json response with a list of users")
def step_impl(context):
    assert context.response.status_code == 200
    assert isinstance(context.response.json(), list)

@when("i send a get request to \"/users/{id}\"")
def step_impl(context, id):
    context.response = requests.get(f"/users/{id}", headers={"Authorization": context.api_key})

@then("i should receive a json response with a single user")
def step_impl(context):
    assert context.response.status_code == 200
    assert isinstance(context.response.json(), dict)

@when("i send a post request to \"/users\" with valid data")
def step_impl(context):
    context.response = requests.post("/users", json={"name": "John Doe"}, headers={"Authorization": context.api_key})

@then("i should receive a json response with a new user")
def step_impl(context):
    assert context.response.status_code == 201
    assert isinstance(context.response.json(), dict)

@when("i send a put request to \"/users/{id}\" with valid data")
def step_impl(context, id):
    context.response = requests.put(f"/users/{id}", json={"name": "Jane Doe"}, headers={"Authorization": context.api_key})

@then("i should receive a json response with an updated user")
def step_impl(context):
    assert context.response.status_code == 200
    assert isinstance(context.response.json(), dict)

@when("i send a delete request to \"/users
