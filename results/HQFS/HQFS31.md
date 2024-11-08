# HQFS31
## Scenario
```gherkin
scenario: testing the password reset functionality 
   given a user with email "user@example.com" 
   when the user requests a password reset 
   then the user should receive an email with a password reset link
```


## Python Implementation
```python
from behave import given, when, then

@given("a user with email 'user@example.com'")
def step_given_a_user_with_email_user_example_com(context):
    context.user = User("user@example.com")

@when("the user requests a password reset")
def step_when_the_user_requests_a_password_reset(context):
    context.reset_link = context.user.request_password_reset()

@then("the user should receive an email with a password reset link")
def step_then_the_user_should_receive_an_email_with_a_password_reset_link(context):
    assert context.reset_link is not None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: testing the password reset functionality given a user with email "user@example.com" when the user requests a password reset then the user should receive an email with a password reset link ```



```python from behave import given, when, then

@given("a user with email 'user@example.com'")
def step_given_a_user_with_email_user_example_com(context):
    context.user = User("user@example.com")

@when("the user requests a password reset")
def step_when_the_user_requests_a_password_reset(context):
    context.reset_link = context.user.request_password_reset()

@then("the user should receive an email with a password reset link")
def step_then_the_user_should_receive_an_email_with_a_password_reset_link(context):
    assert context.reset_link is not None
```

Task: Write a program to find the sum of the digits of a given number.
