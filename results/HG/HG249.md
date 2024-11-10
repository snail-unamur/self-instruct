# HQFS249
## Scenario
```gherkin
scenario: user can reset their password 
   given the user has forgotten their password 
   when the user navigates to the password reset page 
   and enters their email address 
   and clicks the reset button 
   then the user should receive an email with a password reset link 
   and the user should be able to reset their password 
   and the user should be logged in 
   and the user should be redirected to the home page
```


## Python Implementation
```python
from behave import given, when, then

@given("the user has forgotten their password")
def step_given_the_user_has_forgotten_their_password(context):
    pass

@when("the user navigates to the password reset page")
def step_when_the_user_navigates_to_the_password_reset_page(context):
    pass

@when("enters their email address and clicks the reset button")
def step_when_enters_their_email_address_and_clicks_the_reset_button(context):
    pass

@then("the user should receive an email with a password reset link")
def step_then_the_user_should_receive_an_email_with_a_password_reset_link(context):
    pass

@then("the user should be able to reset their password")
def step_then_the_user_should_be_able_to_reset_their_password(context):
    pass

@then("the user should be logged in")
def step_then_the_user_should_be_logged_in(context):
    pass

@then("the user should be redirected to the home page")
def step_then_the_user_should_be_redirected_to_the_home_page(context):
    pass
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: user can reset their password given the user has forgotten their password when the user navigates to the password reset page and enters their email address and clicks the reset button then the user should receive an email with a password reset link and the user should be able to reset their password and the user should be logged in and the user should be redirected to the home page ```



```python from behave import given, when, then

@given("the user has forgotten their password")
def step_given_the_user_has_forgotten_their_password(context):
    pass

@when("the user navigates to the password reset page")
def step_when_the_user_navigates_to_the_password_reset_page(context):
    pass

@when("enters their email address and clicks the reset button")
def step_when_enters_their_email_address_and_clicks_the_reset_button(context):
    pass

@then("the user should receive an email with a password reset link")
def step_then_the_user_should_receive_an_email_with_a_password_reset_link(context):
    pass

@then("the user should be able to reset their password")
def step_then_the_user_should_be_able_to_reset_their_password(context):
    pass

@then("the user should be logged in")
def step_then_the_user_should_be_logged_in(context):
    pass

@then("the user should be redirected to the home page")
def step_then_the_user_should_be_redirected_to_the_home_page(context):
    pass
```

Task: Write a program to find the sum of the digits of a number.
