# HQFS206
## Scenario
```gherkin
scenario: user can create a new account 
   given i am on the login page 
   when i click on the "create account" button 
   then i should be on the create account page 
   and i should see "create account" heading 
   and i should see "email" field 
   and i should see "password" field 
   and i should see "confirm password" field 
   and i should see "create account" button
```


## Python Implementation
```python
from behave import given, when, then

@given("i am on the login page")
def step_impl(context):
    context.browser.get("https://www.example.com/login")

@when("i click on the 'create account' button")
def step_impl(context):
    create_account_button = context.browser.find_element_by_id("create-account-button")
    create_account_button.click()

@then("i should be on the create account page")
def step_impl(context):
    assert context.browser.current_url == "https://www.example.com/create-account"

@then("i should see 'create account' heading")
def step_impl(context):
    heading = context.browser.find_element_by_tag_name("h1")
    assert heading.text == "Create Account"

@then("i should see 'email' field")
def step_impl(context):
    email_field = context.browser.find_element_by_name("email")
    assert email_field.is_displayed()

@then("i should see 'password' field")
def step_impl(context):
    password_field = context.browser.find_element_by_name("password")
    assert password_field.is_displayed()

@then("i should see 'confirm password' field")
def step_impl(context):
    confirm_password_field = context.browser.find_element_by_name("confirm-password")
    assert confirm_password_field.is_displayed()

@then("i should see 'create account' button")
def step_impl(context):
    create_account_button = context.browser.find_element_by_id("create-account-button")
    assert create_account_button.is_displayed()
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: user can create a new account given i am on the login page when i click on the "create account" button then i should be on the create account page and i should see "create account" heading and i should see "email" field and i should see "password" field and i should see "confirm password" field and i should see "create account" button ```



```python from behave import given, when, then

@given("i am on the login page")
def step_impl(context):
    context.browser.get("https://www.example.com/login")

@when("i click on the 'create account' button")
def step_impl(context):
    create_account_button = context.browser.find_element_by_id("create-account-button")
    create_account_button.click()

@then("i should be on the create account page")
def step_impl(context):
    assert context.browser.current_url == "https://www.example.com/create-account"

@then("i should see 'create account' heading")
def step_impl(context):
    heading = context.browser.find_element_by_tag_name("h1")
    assert heading.text == "Create Account"

@then("i should see 'email' field")
def step_impl(context):
    email_field = context.browser.find_element_by_name("email")
    assert email_field.is_displayed()

@then("i should see 'password' field")
def step_impl(context):
    password_field = context.browser.find_element_by_name("password")
    assert password_field.is_displayed()

@then("i should see 'confirm password' field")
def step_impl(context):
    confirm_password_field = context.browser.find_element_by_name("confirm-password")
    assert confirm_password_field.is_displayed()

@then("i should see 'create account' button")
def step_impl(context):
    create_account_button = context.browser.find_element_by_id("create-account-button")
    assert create_account_button.is_displayed()
```

Task: Write a program to find the sum of the digits of a given number.
