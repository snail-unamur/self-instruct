# MQFS254
## Scenario
```gherkin
scenario: 
   given a user is on the login page 
   when they enter their email 
   and password 
   then they should be taken to their dashboard page
```


## Python Implementation
```python
from behave import given, when, then

@given("a user is on the login page")
def step_given_a_user_is_on_the_login_page(context):
    context.browser.get("https://www.example.com/login")

@when("they enter their email and password")
def step_when_they_enter_their_email_and_password(context):
    email_field = context.browser.find_element_by_name("email")
    email_field.send_keys("user@example.com")

    password_field = context.browser.find_element_by_name("password")
    password_field.send_keys("password")

@then("they should be taken to their dashboard page")
def step_then_they_should_be_taken_to_their_dashboard_page(context):
    context.browser.find_element_by_xpath("//button[@type='submit']").click()
    context.browser.assert_current_url("https://www.example.com/dashboard")
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: given a user is on the login page when they enter their email and password then they should be taken to their dashboard page ```



```python from behave import given, when, then

@given("a user is on the login page")
def step_given_a_user_is_on_the_login_page(context):
    context.browser.get("https://www.example.com/login")

@when("they enter their email and password")
def step_when_they_enter_their_email_and_password(context):
    email_field = context.browser.find_element_by_name("email")
    email_field.send_keys("user@example.com")

    password_field = context.browser.find_element_by_name("password")
    password_field.send_keys("password")

@then("they should be taken to their dashboard page")
def step_then_they_should_be_taken_to_their_dashboard_page(context):
    context.browser.find_element_by_xpath("//button[@type='submit']").click()
    context.browser.assert_current_url("https://www.example.com/dashboard")
```

Task: Write a program to find the sum of the digits of a given number.
