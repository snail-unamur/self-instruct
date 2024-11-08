# MQFS86
## Scenario
```gherkin
scenario: 
   given a user is on the login page 
   when they enter an invalid email 
   and password 
   and click on the login button 
   then they should see an error message 
   and they should still be on the login page
```


## Python Implementation
```python
from behave import given, when, then

@given("a user is on the login page")
def step_given_a_user_is_on_the_login_page(context):
    context.driver.get("https://www.example.com/login")

@when("they enter an invalid email and password")
def step_when_they_enter_an_invalid_email_and_password(context):
    email_field = context.driver.find_element_by_name("email")
    email_field.send_keys("invalid_email@example.com")
    password_field = context.driver.find_element_by_name("password")
    password_field.send_keys("invalid_password")

@when("they click on the login button")
def step_when_they_click_on_the_login_button(context):
    login_button = context.driver.find_element_by_xpath("//button[@type='submit']")
    login_button.click()

@then("they should see an error message")
def step_then_they_should_see_an_error_message(context):
    error_message = context.driver.find_element_by_class_name("error-message")
    assert error_message.is_displayed()

@then("they should still be on the login page")
def step_then_they_should_still_be_on_the_login_page(context):
    assert context.driver.current_url == "https://www.example.com/login"
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: given a user is on the login page when they enter an invalid email and password and click on the login button then they should see an error message and they should still be on the login page ``` here are the python implementations of the step functions for the given gherkin scenarios using the behave bdd testing framework:



```python
from behave import given, when, then

@given("a user is on the login page")
def step_given_a_user_is_on_the_login_page(context):
    context.driver.get("https://www.example.com/login")

@when("they enter an invalid email and password")
def step_when_they_enter_an_invalid_email_and_password(context):
    email_field = context.driver.find_element_by_name("email")
    email_field.send_keys("invalid_email@example.com")
    password_field = context.driver.find_element_by_name("password")
    password_field.send_keys("invalid_password")

@when("they click on the login button")
def step_when_they_click_on_the_login_button(context):
    login_button = context.driver.find_element_by_xpath("//button[@type='submit']")
    login_button.click()

@then("they should see an error message")
def step_then_they_should_see_an_error_message(context):
    error_message = context.driver.find_element_by_class_name("error-message")
    assert error_message.is_displayed()

@then("they should still be on the login page")
def step_then_they_should_still_be_on_the_login_page(context):
    assert context.driver.current_url == "https://www.example.com/login"
```
