# HQFS274
## Scenario
```gherkin
scenario: a user can view a list of all log entries 
   given that the user has valid credentials 
   and the user makes a post request to /login 
   and the user tries to view a list of all log entries 
   when the user tries to view a list of all log entries 
   then a list of all log entries should be displayed to the user
```


## Python Implementation
```python
from behave import given, when, then

@given("a user has valid credentials")
def step_impl(context):
    context.user = User("testuser", "testpassword")

@when("the user makes a post request to /login")
def step_impl(context):
    context.response = context.client.post("/login", json=context.user.to_dict())

@then("the user tries to view a list of all log entries")
def step_impl(context):
    context.response = context.client.get("/log-entries")

@then("a list of all log entries should be displayed to the user")
def step_impl(context):
    assert context.response.status_code == 200
    assert isinstance(context.response.json, list)
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: a user can view a list of all log entries given that the user has valid credentials and the user makes a post request to /login and the user tries to view a list of all log entries when the user tries to view a list of all log entries then a list of all log entries should be displayed to the user ```



```python from behave import given, when, then

@given("a user has valid credentials")
def step_impl(context):
    context.user = User("testuser", "testpassword")

@when("the user makes a post request to /login")
def step_impl(context):
    context.response = context.client.post("/login", json=context.user.to_dict())

@then("the user tries to view a list of all log entries")
def step_impl(context):
    context.response = context.client.get("/log-entries")

@then("a list of all log entries should be displayed to the user")
def step_impl(context):
    assert context.response.status_code == 200
    assert isinstance(context.response.json, list)
```

Task: Write a program to find the sum of the digits of a given number.
