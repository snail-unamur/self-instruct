# MQFS38
## Scenario
```gherkin
scenario: testing the login functionality 
   given the user has an account 
   when the user enters their email address 
   and password 
   and clicks login 
   then the user should be logged in 
   and taken to their profile page 
   when the user enters an invalid email address 
   then the user should see an error message 
   when the user enters an invalid password 
   then the user should see an error message 
   when the user enters no password 
   then the user should see an error message 
   when the user enters no email address 
   then the user should see an error message
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: testing the login functionality given the user has an account when the user enters their email address and password and clicks login then the user should be logged in and taken to their profile page when the user enters an invalid email address then the user should see an error message when the user enters an invalid password then the user should see an error message when the user enters no password then the user should see an error message when the user enters no email address then the user should see an error message ```



```python from behave import given, when, then

@given("the user has an account")
def step_given_the_user_has_an_account(context):
    context.user = User()

@when("the user enters their email address and password and clicks login")
def step_when_the_user_enters_their_email_address_and_password_and_clicks_login(context):
    context.login_page = LoginPage()
    context.login_page.load()
    context.login_page.login(context.user.email, context.user.password)

@then("the user should be logged in and taken to their profile page")
def step_then_the_user_should_be_logged_in_and_taken_to_their_profile_page(context):
    assert context.login_page.is_logged_in()
    assert context.login_page.is_on_profile_page()

@when("the user enters an invalid email address")
def step_when_the_user_enters_an_invalid_email_address(context):
    context.login_page = LoginPage()
    context.login_page.load()
    context.login_page.login("invalid_email", context.user.password)

@then("the user should see an error message")
def step_then_the_user_should_see_an_error_message(context):
    assert context.login_page.is_error_message_visible()

@when("the user enters an invalid password")
def step_when_the_user_enters_an_invalid_password(context):
    context.login_page = LoginPage()
    context.login_page.load()
    context.login_page.login(context.user.email, "invalid_password")

@then("the user should see an error message")
def step_then_the_user_should_see_an_error_message(context):
    assert context.login_page.is_error_message_visible()

@when("the user enters no password")
def step_when_the_user_enters_no
