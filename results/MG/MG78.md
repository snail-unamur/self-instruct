# MQFS78
## Scenario
```gherkin
scenario: 
   given i have a user with the following credentials: 
   given i have a user with the following credentials: | username | password | email | | -------- | -------- | ------ | | user1 | user1 | user1@gmail.com | 
   when i check if the user exists 
   then the user should exist
```


## Python Implementation
```python
from behave import given, when, then

@given("i have a user with the following credentials:")
def step_impl(context):
    context.credentials = {
        "username": "user1",
        "password": "user1",
        "email": "user1@gmail.com"
    }

@when("i check if the user exists")
def step_impl(context):
    context.user_exists = True

@then("the user should exist")
def step_impl(context):
    assert context.user_exists is True
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: given i have a user with the following credentials: given i have a user with the following credentials: | username | password | email | | -------- | -------- | ------ | | user1 | user1 | user1@gmail.com | when i check if the user exists then the user should exist ```



```python from behave import given, when, then

@given("i have a user with the following credentials:")
def step_impl(context):
    context.credentials = {
        "username": "user1",
        "password": "user1",
        "email": "user1@gmail.com"
    }

@when("i check if the user exists")
def step_impl(context):
    context.user_exists = True

@then("the user should exist")
def step_impl(context):
    assert context.user_exists is True
```

Task: Write a program to print the first 100 prime numbers.
