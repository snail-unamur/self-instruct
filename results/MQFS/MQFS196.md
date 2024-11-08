# MQFS196
## Scenario
```gherkin
scenario: create a new user with the following data: | username | password | email | | "testuser" | "testpassword" | "testuser@test.com" | 
   given i am on the registration page 
   when i enter the following data: | username | password | email | | "testuser" | "testpassword" | "testuser@test.com" | 
   and i click on the register button 
   then i should be redirected to the login page 
   and i should see a message "user created successfully"
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: create a new user with the following data: | username | password | email | | "testuser" | "testpassword" | "testuser@test.com" | given i am on the registration page when i enter the following data: | username | password | email | | "testuser" | "testpassword" | "testuser@test.com" | and i click on the register button then i should be redirected to the login page and i should see a message "user created successfully" ```



from behave import given, when, then
from selenium import webdriver

@given("i am on the registration page")
def step_given_i_am_on_the_registration_page(context):
    context.driver = webdriver.Firefox()
    context.driver.get("http://localhost:8000/register")

@when("i enter the following data: | username | password | email |")
def step_when_i_enter_the_following_data(context, table):
    context.table = table
    username = context.table.hashes[0]['username']
    password = context.table.hashes[0]['password']
    email = context.table.hashes[0]['email']
    context.driver.find_element_by_name("username").send_keys(username)
    context.driver.find_element_by_name("password").send_keys(password)
    context.driver.find_element_by_name("email").send_keys(email)

@when("and i click on the register button")
def step_when_and_i_click_on_the_register_button(context):
    context.driver.find_element_by_xpath("//button[@type='submit']").click()

@then("i should be redirected to the login page")
def step_then_i_should_be_redirected_to_the_login_page(context):
    assert context.driver.current_url == "http://localhost:8000/login"

@then("i should see a message \"user created successfully\"")
def step_then_i_should_see_a_message_user_created_successfully(context):
    assert "user created successfully" in context.driver.page_source

@then("close the browser")
def step_then_close_the_browser(context):
    context.driver.quit()
