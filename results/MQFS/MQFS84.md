# MQFS84
## Scenario
```gherkin
scenario: user can register 
   given i am on home page 
   when i click on sign in 
   and i click on create an account 
   and i fill the form with valid data 
   then i should be redirected to the home page
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: user can register given i am on home page when i click on sign in and i click on create an account and i fill the form with valid data then i should be redirected to the home page ```



from behave import given, when, then
from selenium import webdriver

@given("i am on home page")
def step_given_i_am_on_home_page(context):
    context.driver = webdriver.Firefox()
    context.driver.get("http://www.example.com")

@when("i click on sign in")
def step_when_i_click_on_sign_in(context):
    sign_in_button = context.driver.find_element_by_id("sign-in-button")
    sign_in_button.click()

@when("i click on create an account")
def step_when_i_click_on_create_an_account(context):
    create_account_button = context.driver.find_element_by_id("create-account-button")
    create_account_button.click()

@when("i fill the form with valid data")
def step_when_i_fill_the_form_with_valid_data(context):
    username_field = context.driver.find_element_by_id("username-field")
    username_field.send_keys("testuser")
    password_field = context.driver.find_element_by_id("password-field")
    password_field.send_keys("testpassword")
    confirm_password_field = context.driver.find_element_by_id("confirm-password-field")
    confirm_password_field.send_keys("testpassword")
    email_field = context.driver.find_element_by_id("email-field")
    email_field.send_keys("testuser@example.com")
    submit_button = context.driver.find_element_by_id("submit-button")
    submit_button.click()

@then("i should be redirected to the home page")
def step_then_i_should_be_redirected_to_the_home_page(context):
    assert context.driver.current_url == "http://www.example.com"
    context.driver.quit()
