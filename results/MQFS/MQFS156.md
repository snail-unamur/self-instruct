# MQFS156
## Scenario
```gherkin
scenario: testing the delete functionality 
   given i am logged in 
   and there is a user with username "testuser" 
   when i delete the user with username "testuser" 
   then the user with username "testuser" is deleted
```


## Python Implementation
```python
from behave import given, when, then

@given("i am logged in")
def step_impl(context):
    context.login()

@given("there is a user with username 'testuser'")
def step_impl(context):
    context.create_user("testuser")

@when("i delete the user with username 'testuser'")
def step_impl(context):
    context.delete_user("testuser")

@then("the user with username 'testuser' is deleted")
def step_impl(context):
    assert not context.get_user("testuser")
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: testing the delete functionality given i am logged in and there is a user with username "testuser" when i delete the user with username "testuser" then the user with username "testuser" is deleted ```



```python from behave import given, when, then

@given("i am logged in")
def step_impl(context):
    context.login()

@given("there is a user with username 'testuser'")
def step_impl(context):
    context.create_user("testuser")

@when("i delete the user with username 'testuser'")
def step_impl(context):
    context.delete_user("testuser")

@then("the user with username 'testuser' is deleted")
def step_impl(context):
    assert not context.get_user("testuser")
```

Task: Write a program to find the sum of the digits of a given number.
