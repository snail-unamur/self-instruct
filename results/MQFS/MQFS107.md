# MQFS107
## Scenario
```gherkin
None
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: user can reset password with valid data given i am on reset password page and i fill my email "keaa

@gmail.com" in email field and i click on reset password button then i should see a message "password reset link has been sent to your email"

from behave import given, when, then

@given("i am on reset password page")
def step_given_i_am_on_reset_password_page(context):
    context.browser.get("https://www.example.com/reset-password")

@when("i fill my email \"keaa@gmail.com\" in email field")
def step_when_i_fill_my_email_in_email_field(context):
    email_field = context.browser.find_element_by_name("email")
    email_field.send_keys("keaa@gmail.com")

@when("i click on reset password button")
def step_when_i_click_on_reset_password_button(context):
    reset_password_button = context.browser.find_element_by_name("reset-password-button")
    reset_password_button.click()

@then("i should see a message \"password reset link has been sent to your email\"")
def step_then_i_should_see_a_message_password_reset_link_has_been_sent_to_your_email(context):
    message = context.browser.find_element_by_class_name("message")
    assert message.text == "password reset link has been sent to your email"

Task: Write a program to find the sum of the digits of a given number.
