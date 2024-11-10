# HQFS137
## Scenario
```gherkin
scenario: a user can reset their password 
   given a user with email "test@example.com" 
   and the user has forgotten their password 
   when the user tries to reset their password 
   then the user receives an email with a link to reset their password 
   and the user can reset their password with the link



from behave import 
   given, 
   when, 
   then
from behave.runner import Context

@
   given("a user with email {email}")
def step_impl(context: Context, email: str):
    context.user = User(email=email)

@
   when("the user tries to reset their password")
def step_impl(context: Context):
    context.reset_password_token = context.user.reset_password()

@
   then("the user receives an email with a link to reset their password")
def step_impl(context: Context):
    assert context.reset_password_token is not None

@
   then("the user can reset their password with the link")
def step_impl(context: Context):
    context.user.reset_password(context.reset_password_token)
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: a user can reset their password given a user with email "test@example.com" and the user has forgotten their password when the user tries to reset their password then the user receives an email with a link to reset their password and the user can reset their password with the link



from behave import given, when, then
from behave.runner import Context

@given("a user with email {email}")
def step_impl(context: Context, email: str):
    context.user = User(email=email)

@when("the user tries to reset their password")
def step_impl(context: Context):
    context.reset_password_token = context.user.reset_password()

@then("the user receives an email with a link to reset their password")
def step_impl(context: Context):
    assert context.reset_password_token is not None

@then("the user can reset their password with the link")
def step_impl(context: Context):
    context.user.reset_password(context.reset_password_token)

```

Task: Write a program to find the number of occurrences of a given word in a given string.
