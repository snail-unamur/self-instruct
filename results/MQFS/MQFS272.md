# MQFS272
## Scenario
```gherkin
scenario: testing the password reset functionality 
   given a user with the email "test@example.com" 
   when the user requests a password reset with the email "test@example.com" 
   then the user receives a password reset link 
   and the user is redirected to the password reset page 
   and the user is notified via email 
   when the user enters a new password with the password reset link 
   then the user's password is reset 
   and the user is logged in 
   and the user is redirected to the homepage 
   and the user is notified via email
```


## Python Implementation
```python
from behave import given, when, then

@given("a user with the email 'test@example.com'")
def step_impl(context):
    context.user = User(email='test@example.com')

@when("the user requests a password reset with the email 'test@example.com'")
def step_impl(context):
    context.reset_link = context.user.request_password_reset()

@then("the user receives a password reset link and the user is redirected to the password reset page and the user is notified via email")
def step_impl(context):
    assert context.reset_link is not None
    assert context.user.redirect_url == '/reset-password'
    assert context.user.email_notifications == ['Password reset requested']

@when("the user enters a new password with the password reset link")
def step_impl(context):
    context.user.reset_password(context.reset_link, 'new_password')

@then("the user's password is reset and the user is logged in and the user is redirected to the homepage and the user is notified via email")
def step_impl(context):
    assert context.user.is_authenticated
    assert context.user.redirect_url == '/'
    assert context.user.email_notifications == ['Password reset']
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: testing the password reset functionality given a user with the email "test@example.com" when the user requests a password reset with the email "test@example.com" then the user receives a password reset link and the user is redirected to the password reset page and the user is notified via email when the user enters a new password with the password reset link then the user's password is reset and the user is logged in and the user is redirected to the homepage and the user is notified via email ```



```python from behave import given, when, then

@given("a user with the email 'test@example.com'")
def step_impl(context):
    context.user = User(email='test@example.com')

@when("the user requests a password reset with the email 'test@example.com'")
def step_impl(context):
    context.reset_link = context.user.request_password_reset()

@then("the user receives a password reset link and the user is redirected to the password reset page and the user is notified via email")
def step_impl(context):
    assert context.reset_link is not None
    assert context.user.redirect_url == '/reset-password'
    assert context.user.email_notifications == ['Password reset requested']

@when("the user enters a new password with the password reset link")
def step_impl(context):
    context.user.reset_password(context.reset_link, 'new_password')

@then("the user's password is reset and the user is logged in and the user is redirected to the homepage and the user is notified via email")
def step_impl(context):
    assert context.user.is_authenticated
    assert context.user.redirect_url == '/'
    assert context.user.email_notifications == ['Password reset']
```

Task: Write a program to find the sum of the digits of a number.
