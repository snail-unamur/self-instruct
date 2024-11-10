# HQFS114
## Scenario
```gherkin
scenario: i can login to the site 
   given i open the site "/" 
   when i enter "admin" as username 
   and "admin" as password 
   then i should be logged in
```


## Python Implementation
```python
from behave import given, when, then

@given("i open the site '/'")
def step_given_i_open_the_site_slash(context):
    context.browser.visit("/")

@when("i enter {username} as username and {password} as password")
def step_when_i_enter_username_and_password(context, username, password):
    context.browser.fill("username", username)
    context.browser.fill("password", password)
    context.browser.find_by_name("login").first.click()

@then("i should be logged in")
def step_then_i_should_be_logged_in(context):
    assert context.browser.is_text_present("Welcome, admin!") is True
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: i can login to the site given i open the site "/" when i enter "admin" as username and "admin" as password then i should be logged in ```



```python from behave import given, when, then

@given("i open the site '/'")
def step_given_i_open_the_site_slash(context):
    context.browser.visit("/")

@when("i enter {username} as username and {password} as password")
def step_when_i_enter_username_and_password(context, username, password):
    context.browser.fill("username", username)
    context.browser.fill("password", password)
    context.browser.find_by_name("login").first.click()

@then("i should be logged in")
def step_then_i_should_be_logged_in(context):
    assert context.browser.is_text_present("Welcome, admin!") is True
```

Task: Write a program to find the sum of the digits of a given number.
