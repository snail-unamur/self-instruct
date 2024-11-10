# MQFS149
## Scenario
```gherkin
scenario: testing the login functionality 
   given a user with the following data: | username | password | | "testuser" | "testpassword" | 
   when they visit the login page 
   and they enter their username 
   and password 
   and they click the login button 
   then they should be logged in 
   and they should be redirected to the homepage
```


## Python Implementation
```python
from behave import given, when, then

@given("a user with the following data:")
def step_impl(context):
    context.user_data = {
        "username": "testuser",
        "password": "testpassword"
    }

@when("they visit the login page")
def step_impl(context):
    context.browser.visit("http://www.example.com/login")

@when("they enter their username and password")
def step_impl(context):
    context.browser.fill("username", context.user_data["username"])
    context.browser.fill("password", context.user_data["password"])

@when("they click the login button")
def step_impl(context):
    context.browser.find_by_id("login-button").first.click()

@then("they should be logged in")
def step_impl(context):
    assert context.browser.is_text_present("Welcome, testuser")

@then("they should be redirected to the homepage")
def step_impl(context):
    assert context.browser.url == "http://www.example.com/"
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: testing the login functionality given a user with the following data: | username | password | | "testuser" | "testpassword" | when they visit the login page and they enter their username and password and they click the login button then they should be logged in and they should be redirected to the homepage ```



```python from behave import given, when, then

@given("a user with the following data:")
def step_impl(context):
    context.user_data = {
        "username": "testuser",
        "password": "testpassword"
    }

@when("they visit the login page")
def step_impl(context):
    context.browser.visit("http://www.example.com/login")

@when("they enter their username and password")
def step_impl(context):
    context.browser.fill("username", context.user_data["username"])
    context.browser.fill("password", context.user_data["password"])

@when("they click the login button")
def step_impl(context):
    context.browser.find_by_id("login-button").first.click()

@then("they should be logged in")
def step_impl(context):
    assert context.browser.is_text_present("Welcome, testuser")

@then("they should be redirected to the homepage")
def step_impl(context):
    assert context.browser.url == "http://www.example.com/"
```

Task: Write a program to find the sum of the digits of a number.
