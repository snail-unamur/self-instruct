# MQFS47
## Scenario
```gherkin
None
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: user confirms password reset given i have received a password reset link when i click on the link and enter a new password then my

password is reset

from behave import given, when, then

@given("i have received a password reset link")
def step_impl(context):
    context.reset_link = "https://example.com/reset-password"

@when("i click on the link and enter a new password")
def step_impl(context):
    context.new_password = "new_password"
    context.response = requests.post(context.reset_link, data={"password": context.new_password})

@then("my password is reset")
def step_impl(context):
    assert context.response.status_code == 200
    assert "Password reset successfully" in context.response.text


Task: Write a program to find the sum of the digits of a given number.
