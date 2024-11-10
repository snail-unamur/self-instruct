# MQFS213
## Scenario
```gherkin
None
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: testing the registration functionality given i am on the registration page when i enter the email "mauricio.chaves.junior@live.com" and the password "123456" and i click on the register button then i should be redirected to the login page and i should see the message "registration successful" when i enter the email "mauricio.chaves.junior@live.com" and the password "123456" and i click on the register button again then i should see the message "email already registered" when i enter the email "mauricio.chaves.junior@live.com" and the password "12345" and i click on the register button then i should see the message "password must be at least 6 characters long" when i enter the email "mauricio.chaves.

junior@live.com" and the password "123456" and i click on the register button then i should see the message "email must contain a domain"

from behave import given, when, then

@given("i am on the registration page")
def step_given_i_am_on_the_registration_page(context):
    pass

@when("i enter the email \"{email}\" and the password \"{password}\"")
def step_when_i_enter_the_email_and_the_password(context, email, password):
    context.email = email
    context.password = password

@when("i click on the register button")
def step_when_i_click_on_the_register_button(context):
    pass

@then("i should be redirected to the login page")
def step_then_i_should_be_redirected_to_the_login_page(context):
    pass

@then("i should see the message \"{message}\"")
def step_then_i_should_see_the_message(context, message):
    assert message in context.text

@when("i enter the email \"{email}\" and the password \"{password}\" and i click on the register button again")
def step_when_i_enter_the_email_and_the_password_and_i_click_on_the_register_button_again(context, email, password):
    context.email = email
    context.password = password
    context.execute_steps("when i click on the register button")
    context.execute_steps("then i should see the message \"email already registered\"")

@when("i enter the email \"{email}\" and the password \"{password}\" and i click on the register button")
def step_when_i_enter_the_email_and_the_password_and_i_click_on_the_register_button(context, email, password):
    context.email = email
    context.password = password
    context.execute_steps("when i click on the register button")

@then("i should see the message \"{message}\
