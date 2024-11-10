# MQFS41
## Scenario
```gherkin
scenario: testing the api endpoint for creating a new user 
   given i have a rest api endpoint for creating a new user 
   when i send a post request to the endpoint with valid user data 
   then i should receive a 201 created status code 
   and the response should contain the user object 
   and the user object should contain the correct data 
   when i send a post request to the endpoint with invalid user data 
   then i should receive a 400 bad request status code 
   and the response should contain an error message
```


## Python Implementation
```python
from behave import given, when, then

@given("i have a rest api endpoint for creating a new user")
def step_impl(context):
    context.endpoint = "http://localhost:8000/api/users/"

@when("i send a post request to the endpoint with valid user data")
def step_impl(context):
    context.response = context.app.post(context.endpoint, json=context.valid_user_data)

@then("i should receive a 201 created status code and the response should contain the user object and the user object should contain the correct data")
def step_impl(context):
    assert context.response.status_code == 201
    user = context.response.json()
    assert user["first_name"] == context.valid_user_data["first_name"]
    assert user["last_name"] == context.valid_user_data["last_name"]
    assert user["email"] == context.valid_user_data["email"]

@when("i send a post request to the endpoint with invalid user data")
def step_impl(context):
    context.response = context.app.post(context.endpoint, json=context.invalid_user_data)

@then("i should receive a 400 bad request status code and the response should contain an error message")
def step_impl(context):
    assert context.response.status_code == 400
    assert "error" in context.response.json()
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: testing the api endpoint for creating a new user given i have a rest api endpoint for creating a new user when i send a post request to the endpoint with valid user data then i should receive a 201 created status code and the response should contain the user object and the user object should contain the correct data when i send a post request to the endpoint with invalid user data then i should receive a 400 bad request status code and the response should contain an error message```



```python from behave import given, when, then

@given("i have a rest api endpoint for creating a new user")
def step_impl(context):
    context.endpoint = "http://localhost:8000/api/users/"

@when("i send a post request to the endpoint with valid user data")
def step_impl(context):
    context.response = context.app.post(context.endpoint, json=context.valid_user_data)

@then("i should receive a 201 created status code and the response should contain the user object and the user object should contain the correct data")
def step_impl(context):
    assert context.response.status_code == 201
    user = context.response.json()
    assert user["first_name"] == context.valid_user_data["first_name"]
    assert user["last_name"] == context.valid_user_data["last_name"]
    assert user["email"] == context.valid_user_data["email"]

@when("i send a post request to the endpoint with invalid user data")
def step_impl(context):
    context.response = context.app.post(context.endpoint, json=context.invalid_user_data)

@then("i should receive a 400 bad request status code and the response should contain an error message")
def step_impl(context):
    assert context.response.status_code == 400
    assert "error" in context.response.json()
```

Task: Write a program to find the sum of the digits of a given number.
