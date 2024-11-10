# HQFS100
## Scenario
```gherkin
scenario: user creates a new account 
   given i am on the homepage 
   when i click on the sign up button 
   then i should be redirected to the sign up page 
   when i fill in the required fields with valid information 
   then i should be redirected to the homepage 
   when i check my email 
   then i should have received a confirmation email
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: user creates a new account given i am on the homepage when i click on the sign up button then i should be redirected to the sign up page when i fill in the required fields with valid information then i should be redirected to the homepage when i check my email then i should have received a confirmation email ```



from behave import given, when, then
from selenium import webdriver

@given("i am on the homepage")
def step_given_i_am_on_the_homepage(context):
    context.driver = webdriver.Firefox()
    context.driver.get("http://www.example.com")

@when("i click on the sign up button")
def step_when_i_click_on_the_sign_up_button(context):
    context.driver.find_element_by_id("signup").click()

@then("i should be redirected to the sign up page")
def step_then_i_should_be_redirected_to_the_sign_up_page(context):
    assert context.driver.current_url == "http://www.example.com/signup"

@when("i fill in the required fields with valid information")
def step_when_i_fill_in_the_required_fields_with_valid_information(context):
    context.driver.find_element_by_name("username").send_keys("testuser")
    context.driver.find_element_by_name("email").send_keys("testuser@example.com")
    context.driver.find_element_by_name("password").send_keys("testpassword")
    context.driver.find_element_by_name("confirmpassword").send_keys("testpassword")
    context.driver.find_element_by_id("signup").click()

@then("i should be redirected to the homepage")
def step_then_i_should_be_redirected_to_the_homepage(context):
    assert context.driver.current_url == "http://www.example.com"

@then("i should have received a confirmation email")
def step_then_i_should_have_received_a_confirmation_email(context):
    # TODO: check email
    pass

@then("i should have received a confirmation email with the subject {subject}")
def step_then_i_should_have_received_a_confirmation_email_with_the_subject(
