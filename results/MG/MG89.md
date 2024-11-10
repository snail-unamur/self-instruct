# MQFS89
## Scenario
```gherkin
scenario: testing the login functionality 
   given i am registering a new account 
   when i enter an already registered email 
   and i enter the same password 
   and i click on the checkbox 
   and i click on the register button 
   then i should be able to register a new account
```


## Python Implementation
```python
from behave import given, when, then

@given("i am registering a new account")
def step_given_i_am_registering_a_new_account(context):
    context.register_page = RegisterPage()
    context.register_page.navigate_to()

@when("i enter an already registered email")
def step_when_i_enter_an_already_registered_email(context):
    context.register_page.email_field.send_keys("test@test.com")

@when("i enter the same password")
def step_when_i_enter_the_same_password(context):
    context.register_page.password_field.send_keys("test1234")

@when("i click on the checkbox")
def step_when_i_click_on_the_checkbox(context):
    context.register_page.checkbox.click()

@when("i click on the register button")
def step_when_i_click_on_the_register_button(context):
    context.register_page.register_button.click()

@then("i should be able to register a new account")
def step_then_i_should_be_able_to_register_a_new_account(context):
    assert context.register_page.success_message.is_displayed()
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: testing the login functionality given i am registering a new account when i enter an already registered email and i enter the same password and i click on the checkbox and i click on the register button then i should be able to register a new account ```



```python from behave import given, when, then

@given("i am registering a new account")
def step_given_i_am_registering_a_new_account(context):
    context.register_page = RegisterPage()
    context.register_page.navigate_to()

@when("i enter an already registered email")
def step_when_i_enter_an_already_registered_email(context):
    context.register_page.email_field.send_keys("test@test.com")

@when("i enter the same password")
def step_when_i_enter_the_same_password(context):
    context.register_page.password_field.send_keys("test1234")

@when("i click on the checkbox")
def step_when_i_click_on_the_checkbox(context):
    context.register_page.checkbox.click()

@when("i click on the register button")
def step_when_i_click_on_the_register_button(context):
    context.register_page.register_button.click()

@then("i should be able to register a new account")
def step_then_i_should_be_able_to_register_a_new_account(context):
    assert context.register_page.success_message.is_displayed()
```

Task: Write a program to find the sum of the digits of a given number.
