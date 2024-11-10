# MQFS229
## Scenario
```gherkin
scenario: testing the reset password functionality 
   given i am on the forgot password page 
   when i enter my email address 
   and i click on the reset password button 
   then i should receive an email with a link to reset my password
```


## Python Implementation
```python
from behave import given, when, then

@given("i am on the forgot password page")
def step_given_i_am_on_the_forgot_password_page(context):
    context.forgot_password_page = ForgotPasswordPage()
    context.forgot_password_page.navigate_to()

@when("i enter my email address and i click on the reset password button")
def step_when_i_enter_my_email_address_and_i_click_on_the_reset_password_button(context):
    context.email = "test@example.com"
    context.forgot_password_page.enter_email(context.email)
    context.forgot_password_page.click_reset_password_button()

@then("i should receive an email with a link to reset my password")
def step_then_i_should_receive_an_email_with_a_link_to_reset_my_password(context):
    # TODO: check email
    pass
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: testing the reset password functionality given i am on the forgot password page when i enter my email address and i click on the reset password button then i should receive an email with a link to reset my password ```



```python from behave import given, when, then

@given("i am on the forgot password page")
def step_given_i_am_on_the_forgot_password_page(context):
    context.forgot_password_page = ForgotPasswordPage()
    context.forgot_password_page.navigate_to()

@when("i enter my email address and i click on the reset password button")
def step_when_i_enter_my_email_address_and_i_click_on_the_reset_password_button(context):
    context.email = "test@example.com"
    context.forgot_password_page.enter_email(context.email)
    context.forgot_password_page.click_reset_password_button()

@then("i should receive an email with a link to reset my password")
def step_then_i_should_receive_an_email_with_a_link_to_reset_my_password(context):
    # TODO: check email
    pass
```

Task: Write a program to find the sum of the digits of a given number.
