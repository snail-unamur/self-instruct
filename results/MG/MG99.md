# MQFS99
## Scenario
```gherkin
scenario: a user can change their password 
   when the user is logged in 
   then the user can change their password 
   given a user is logged in 
   when the user changes their password 
   then the user can change their password
```


## Python Implementation
```python
from behave import given, when, then

@given("a user is logged in")
def step_impl(context):
    context.user = User()
    context.user.login()

@when("the user changes their password")
def step_impl(context):
    context.user.change_password("old_password", "new_password")

@then("the user can change their password")
def step_impl(context):
    assert context.user.check_password("new_password")
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: a user can change their password when the user is logged in then the user can change their password given a user is logged in when the user changes their password then the user can change their password ```



```python from behave import given, when, then

@given("a user is logged in")
def step_impl(context):
    context.user = User()
    context.user.login()

@when("the user changes their password")
def step_impl(context):
    context.user.change_password("old_password", "new_password")

@then("the user can change their password")
def step_impl(context):
    assert context.user.check_password("new_password")
```

Task: Write a program to find the sum of the digits of a given number.
