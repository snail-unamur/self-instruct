# MQFS192
## Scenario
```gherkin
scenario: create a new user 
   given the following user details |username |password |email | |testuser |testpassword |testuser@example.com | 
   when i visit '/register' 
   then i should see a registration form 
   then i fill in the registration form with the 
   given user details 
   and i submit the registration form 
   then i should see a confirmation message 
   then i should be logged in as "testuser"
```


## Python Implementation
```python
from behave import given, when, then

@given("the following user details")
def step_impl(context):
    context.user_details = {
        "username": "testuser",
        "password": "testpassword",
        "email": "testuser@example.com"
    }

@when("i visit '/register'")
def step_impl(context):
    context.browser.visit("/register")

@then("i should see a registration form")
def step_impl(context):
    assert context.browser.is_text_present("Register")

@when("i fill in the registration form with the given user details and i submit the registration form")
def step_impl(context):
    register_form = context.browser.find_by_name("register_form")
    register_form.find_by_name("username").first.fill(context.user_details["username"])
    register_form.find_by_name("password").first.fill(context.user_details["password"])
    register_form.find_by_name("email").first.fill(context.user_details["email"])
    register_form.find_by_name("submit").first.click()

@then("i should see a confirmation message")
def step_impl(context):
    assert context.browser.is_text_present("Registration successful")

@then("i should be logged in as {username}")
def step_impl(context, username):
    assert context.browser.is_text_present(f"Welcome, {username}")
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: create a new user given the following user details |username |password |email | |testuser |testpassword |testuser@example.com | when i visit '/register' then i should see a registration form then i fill in the registration form with the given user details and i submit the registration form then i should see a confirmation message then i should be logged in as "testuser" ```



```python from behave import given, when, then

@given("the following user details")
def step_impl(context):
    context.user_details = {
        "username": "testuser",
        "password": "testpassword",
        "email": "testuser@example.com"
    }

@when("i visit '/register'")
def step_impl(context):
    context.browser.visit("/register")

@then("i should see a registration form")
def step_impl(context):
    assert context.browser.is_text_present("Register")

@when("i fill in the registration form with the given user details and i submit the registration form")
def step_impl(context):
    register_form = context.browser.find_by_name("register_form")
    register_form.find_by_name("username").first.fill(context.user_details["username"])
    register_form.find_by_name("password").first.fill(context.user_details["password"])
    register_form.find_by_name("email").first.fill(context.user_details["email"])
    register_form.find_by_name("submit").first.click()

@then("i should see a confirmation message")
def step_impl(context):
    assert context.browser.is_text_present("Registration successful")

@then("i should be logged in as {username}")
def step_impl(context, username):
    assert context.browser.is_text_present(f"Welcome, {username}")
```

Task: Write a program to find the sum of the digits of a given number.
