# HQFS166
## Scenario
```gherkin
scenario: testing the registration functionality 
   given i am on the registration page 
   when i enter the correct registration details 
   then i should be registered 
   and i should be redirected to the homepage 
   when i enter the incorrect registration details 
   then i should not be registered 
   and i should see an error message
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: testing the registration functionality given i am on the registration page when i enter the correct registration details then i should be registered and i should be redirected to the homepage when i enter the incorrect registration details then i should not be registered and i should see an error message ```



from behave import given, when, then
from selenium import webdriver

@given("i am on the registration page")
def step_given_i_am_on_the_registration_page(context):
    context.driver = webdriver.Firefox()
    context.driver.get("http://www.example.com/register")

@when("i enter the correct registration details")
def step_when_i_enter_the_correct_registration_details(context):
    context.driver.find_element_by_name("username").send_keys("testuser")
    context.driver.find_element_by_name("password").send_keys("testpassword")
    context.driver.find_element_by_name("confirm_password").send_keys("testpassword")
    context.driver.find_element_by_name("submit").click()

@then("i should be registered and i should be redirected to the homepage")
def step_then_i_should_be_registered_and_i_should_be_redirected_to_the_homepage(context):
    assert context.driver.current_url == "http://www.example.com/"
    assert context.driver.find_element_by_id("welcome_message").text == "Welcome, testuser!"

@when("i enter the incorrect registration details")
def step_when_i_enter_the_incorrect_registration_details(context):
    context.driver.find_element_by_name("username").send_keys("testuser")
    context.driver.find_element_by_name("password").send_keys("testpassword")
    context.driver.find_element_by_name("confirm_password").send_keys("wrongpassword")
    context.driver.find_element_by_name("submit").click()

@then("i should not be registered and i should see an error message")
def step_then_i_should_not_be_registered_and_i_should_see_an_error_message(context):
    assert context.driver.current_url == "http://www.example.com/register"
    assert context.
