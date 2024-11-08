# HQFS109
## Scenario
```gherkin
scenario: a user can reset their password 
   given the user has forgotten their password 
   when the user clicks the reset password button 
   then the user should be prompted to enter their email address 
   when the user enters their email address 
   then the user should receive an email with a link to reset their password 
   when the user clicks the link 
   then the user should be taken to the reset password page 
   and the user should be able

to enter a new password 
   when the user submits the new password 
   then the user should be logged in 
   and redirected to the homepage
```


## Python Implementation
```python
from behave import given, when, then

@given("the user has forgotten their password")
def step_impl(context):
    pass

@when("the user clicks the reset password button")
def step_impl(context):
    pass

@then("the user should be prompted to enter their email address")
def step_impl(context):
    pass

@when("the user enters their email address")
def step_impl(context):
    pass

@then("the user should receive an email with a link to reset their password")
def step_impl(context):
    pass

@when("the user clicks the link")
def step_impl(context):
    pass

@then("the user should be taken to the reset password page")
def step_impl(context):
    pass

@when("the user enters a new password")
def step_impl(context):
    pass

@when("the user submits the new password")
def step_impl(context):
    pass

@then("the user should be logged in and redirected to the homepage")
def step_impl(context):
    pass
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: a user can reset their password given the user has forgotten their password when the user clicks the reset password button then the user should be prompted to enter their email address when the user enters their email address then the user should receive an email with a link to reset their password when the user clicks the link then the user should be taken to the reset password page and the user should be able

to enter a new password when the user submits the new password then the user should be logged in and redirected to the homepage

```

```python from behave import given, when, then

@given("the user has forgotten their password")
def step_impl(context):
    pass

@when("the user clicks the reset password button")
def step_impl(context):
    pass

@then("the user should be prompted to enter their email address")
def step_impl(context):
    pass

@when("the user enters their email address")
def step_impl(context):
    pass

@then("the user should receive an email with a link to reset their password")
def step_impl(context):
    pass

@when("the user clicks the link")
def step_impl(context):
    pass

@then("the user should be taken to the reset password page")
def step_impl(context):
    pass

@when("the user enters a new password")
def step_impl(context):
    pass

@when("the user submits the new password")
def step_impl(context):
    pass

@then("the user should be logged in and redirected to the homepage")
def step_impl(context):
    pass
```

Task: Write a program to find the sum of the digits of a given number.
