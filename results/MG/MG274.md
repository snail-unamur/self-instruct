# MQFS274
## Scenario
```gherkin
scenario: create a new user account 
   given i am on the home page 
   when i click on the "create account" button 
   then i should be on the "create account" page 
   when i fill in the form with the following details: name: "john doe" email: "[johndoe@example.com](mailto:johndoe@example.com)" password: "password123" 
   then i should be on the home page 
   when i click on the "log in" button 
   then i should be on the "log in" page 
   when i fill in the form with the following details: email: "[johndoe@example.com](mailto:johndoe@example.com)" password: "password123" 
   then i should be on the home page 
   and i should see a welcome message with my name in it
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: create a new user account given i am on the home page when i click on the "create account" button then i should be on the "create account" page when i fill in the form with the following details: name: "john doe" email: "[johndoe@example.com](mailto:johndoe@example.com)" password: "password123" then i should be on the home page when i click on the "log in" button then i should be on the "log in" page when i fill in the form with the following details: email: "[johndoe@example.com](mailto:johndoe@example.com)" password: "password123" then i should be on the home page and i should see a welcome message with my name in it ```



```python from behave import given, when, then

@given("i am on the home page")
def step_given_i_am_on_the_home_page(context):
    context.home_page.open()

@when("i click on the 'create account' button")
def step_when_i_click_on_the_create_account_button(context):
    context.home_page.click_create_account_button()

@then("i should be on the 'create account' page")
def step_then_i_should_be_on_the_create_account_page(context):
    context.create_account_page.assert_current_page()

@when("i fill in the form with the following details: name: 'john doe' email: '[johndoe@example.com](mailto:johndoe@example.com)' password: 'password123'")
def step_when_i_fill_in_the_form_with_the_following_details(context):
    context.create_account_page.fill_name("john doe")
    context.create_account_page.fill_email("[johndoe@example.com](mailto:johndoe@example.com)")
    context.create_account_page.fill_password("password123")

@then("i should be on the home page")
def step_then_i_should_be_on_the_home_page(context):
    context.home_page.assert_current_page()

@when("i click on the 'log in' button")
def step_when_i_click_on_the_log_in_button(context):
    context.home_page.click_log_in_button()

@then("i should be on the 'log in' page")
def step_then_i_should_be_on_the_log_in_page(context):
    context.log_in_page.assert_current_page()

@when("i fill in the form with the following details: email: '[johndoe@example.com](mailto:joh
