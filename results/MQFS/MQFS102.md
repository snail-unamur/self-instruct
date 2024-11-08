# MQFS102
## Scenario
```gherkin
scenario: a user can register 
   given i am on the register page 
   when i fill the form with valid data 
   then i verify that status code is "200" 
   and i verify that response contains "registration successful" as "message" attribute
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: a user can register given i am on the register page when i fill the form with valid data then i verify that status code is "200" and i verify that response contains "registration successful" as "message" attribute ```



from behave import given, when, then
from requests import post

@given("i am on the register page")
def step(context):
    context.response = post("http://localhost:8000/api/register", json={
        "username": "testuser",
        "email": "testuser@example.com",
        "password": "testpassword"
    })

@when("i fill the form with valid data")
def step(context):
    pass

@then("i verify that status code is \"200\"")
def step(context):
    assert context.response.status_code == 200

@then("i verify that response contains \"registration successful\" as \"message\" attribute")
def step(context):
    assert context.response.json()["message"] == "registration successful"
