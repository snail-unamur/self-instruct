# HQFS39
## Scenario
```gherkin
scenario: user can create a new account 
   given user is on the login page 
   when user clicks on the register button 
   then user is redirected to the registration page 
   and user fills in the registration form 
   and user submits the registration form 
   then user is redirected to the login page 
   and user can log in with the new account
```


## Python Implementation
```python
from behave import given, when, then

@given("user is on the login page")
def step_given_user_is_on_the_login_page(context):
    context.login_page.open()

@when("user clicks on the register button")
def step_when_user_clicks_on_the_register_button(context):
    context.login_page.click_register_button()

@then("user is redirected to the registration page")
def step_then_user_is_redirected_to_the_registration_page(context):
    assert context.login_page.current_url == context.register_page.url
    context.register_page.open()

@when("user fills in the registration form")
def step_when_user_fills_in_the_registration_form(context):
    context.register_page.fill_form()

@when("user submits the registration form")
def step_when_user_submits_the_registration_form(context):
    context.register_page.submit_form()

@then("user is redirected to the login page")
def step_then_user_is_redirected_to_the_login_page(context):
    assert context.register_page.current_url == context.login_page.url

@then("user can log in with the new account")
def step_then_user_can_log_in_with_the_new_account(context):
    context.login_page.login(context.register_page.email, context.register_page.password)
    assert context.login_page.current_url == context.home_page.url
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: user can create a new account given user is on the login page when user clicks on the register button then user is redirected to the registration page and user fills in the registration form and user submits the registration form then user is redirected to the login page and user can log in with the new account ```



```python from behave import given, when, then

@given("user is on the login page")
def step_given_user_is_on_the_login_page(context):
    context.login_page.open()

@when("user clicks on the register button")
def step_when_user_clicks_on_the_register_button(context):
    context.login_page.click_register_button()

@then("user is redirected to the registration page")
def step_then_user_is_redirected_to_the_registration_page(context):
    assert context.login_page.current_url == context.register_page.url
    context.register_page.open()

@when("user fills in the registration form")
def step_when_user_fills_in_the_registration_form(context):
    context.register_page.fill_form()

@when("user submits the registration form")
def step_when_user_submits_the_registration_form(context):
    context.register_page.submit_form()

@then("user is redirected to the login page")
def step_then_user_is_redirected_to_the_login_page(context):
    assert context.register_page.current_url == context.login_page.url

@then("user can log in with the new account")
def step_then_user_can_log_in_with_the_new_account(context):
    context.login_page.login(context.register_page.email, context.register_page.password)
    assert context.login_page.current_url == context.home_page.url
```

Task: Write a program to find the sum of the digits of a given number.
