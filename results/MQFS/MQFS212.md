# MQFS212
## Scenario
```gherkin
scenario: a user can reset their password 
   given a user has registered an account 
   when the user requests to reset their password 
   then the user should receive an email with a password reset link 
   when the user clicks the password reset link 
   then the user should be taken to a page where they can enter a new password 
   when the user submits their new password 
   then the user should be able to log in with their new password
```


## Python Implementation
```python
from behave import given, when, then

@given("a user has registered an account")
def step_impl(context):
    pass

@when("the user requests to reset their password")
def step_impl(context):
    pass

@then("the user should receive an email with a password reset link")
def step_impl(context):
    pass

@when("the user clicks the password reset link")
def step_impl(context):
    pass

@then("the user should be taken to a page where they can enter a new password")
def step_impl(context):
    pass

@when("the user submits their new password")
def step_impl(context):
    pass

@then("the user should be able to log in with their new password")
def step_impl(context):
    pass
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: a user can reset their password given a user has registered an account when the user requests to reset their password then the user should receive an email with a password reset link when the user clicks the password reset link then the user should be taken to a page where they can enter a new password when the user submits their new password then the user should be able to log in with their new password ```



```python from behave import given, when, then

@given("a user has registered an account")
def step_impl(context):
    pass

@when("the user requests to reset their password")
def step_impl(context):
    pass

@then("the user should receive an email with a password reset link")
def step_impl(context):
    pass

@when("the user clicks the password reset link")
def step_impl(context):
    pass

@then("the user should be taken to a page where they can enter a new password")
def step_impl(context):
    pass

@when("the user submits their new password")
def step_impl(context):
    pass

@then("the user should be able to log in with their new password")
def step_impl(context):
    pass
```

Task: Write a program to find the sum of the digits of a number.
