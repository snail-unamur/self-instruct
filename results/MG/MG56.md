# MQFS56
## Scenario
```gherkin
scenario: testing the password reset functionality 
   given a user with username "testuser" 
   and password "testpassword" 
   when the user requests a password reset 
   then an email is sent to the user's email address with a link to reset the password 
   when the user clicks on the link 
   and enters the new password 
   then the user's password is reset 
   and the user is logged in 
   and the user is redirected to the homepage
```


## Python Implementation
```python
from behave import given, when, then

@given("a user with username 'testuser' and password 'testpassword'")
def step_given_a_user_with_username_testuser_and_password_testpassword(context):
    context.user = User(username="testuser", password="testpassword")

@when("the user requests a password reset")
def step_when_the_user_requests_a_password_reset(context):
    context.email = context.user.request_password_reset()

@then("an email is sent to the user's email address with a link to reset the password")
def step_then_an_email_is_sent_to_the_user_s_email_address_with_a_link_to_reset_the_password(context):
    assert context.email is not None

@when("the user clicks on the link and enters the new password")
def step_when_the_user_clicks_on_the_link_and_enters_the_new_password(context):
    context.user.reset_password(context.email, "newpassword")

@then("the user's password is reset and the user is logged in and the user is redirected to the homepage")
def step_then_the_user_s_password_is_reset_and_the_user_is_logged_in_and_the_user_is_redirected_to_the_homepage(context):
    assert context.user.check_password("newpassword")
    assert context.user.is_authenticated
    assert context.user.is_active
    assert context.user.get_redirect_url() == "/"
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: testing the password reset functionality given a user with username "testuser" and password "testpassword" when the user requests a password reset then an email is sent to the user's email address with a link to reset the password when the user clicks on the link and enters the new password then the user's password is reset and the user is logged in and the user is redirected to the homepage ```



```python from behave import given, when, then

@given("a user with username 'testuser' and password 'testpassword'")
def step_given_a_user_with_username_testuser_and_password_testpassword(context):
    context.user = User(username="testuser", password="testpassword")

@when("the user requests a password reset")
def step_when_the_user_requests_a_password_reset(context):
    context.email = context.user.request_password_reset()

@then("an email is sent to the user's email address with a link to reset the password")
def step_then_an_email_is_sent_to_the_user_s_email_address_with_a_link_to_reset_the_password(context):
    assert context.email is not None

@when("the user clicks on the link and enters the new password")
def step_when_the_user_clicks_on_the_link_and_enters_the_new_password(context):
    context.user.reset_password(context.email, "newpassword")

@then("the user's password is reset and the user is logged in and the user is redirected to the homepage")
def step_then_the_user_s_password_is_reset_and_the_user_is_logged_in_and_the_user_is_redirected_to_the_homepage(context):
    assert context.user.check_password("newpassword")
    assert context.user.is_authenticated
    assert context.user.is_active
    assert context.user.get_redirect_url() == "/"
```

Task: Write a program to find the sum of the digits of a number.
