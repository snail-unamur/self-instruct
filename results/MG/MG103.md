# MQFS103
## Scenario
```gherkin
scenario: adding a new user 
   given i am on the homepage 
   when i click on the "add user" button 
   then i should be taken to the "add user" page 
   when i enter the username "testuser" in the "username" field 
   then i enter the password "testpassword" in the "password" field 
   then i enter the email "[testuser@example.com](mailto:testuser@example.com)" in the "email" field 
   then i click on the "save" button 
   then i should be taken back to the homepage 
   and i should see the new user "testuser" listed on the page
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: adding a new user given i am on the homepage when i click on the "add user" button then i should be taken to the "add user" page when i enter the username "testuser" in the "username" field then i enter the password "testpassword" in the "password" field then i enter the email "[testuser@example.com](mailto:testuser@example.com)" in the "email" field then i click on the "save" button then i should be taken back to the homepage and i should see the new user "testuser" listed on the page ```



```python from behave import given, when, then

@given("i am on the homepage")
def step_given_i_am_on_the_homepage(context):
    context.driver.get("http://localhost:8000")

@when("i click on the \"add user\" button")
def step_when_i_click_on_the_add_user_button(context):
    add_user_button = context.driver.find_element_by_id("add-user-button")
    add_user_button.click()

@then("i should be taken to the \"add user\" page")
def step_then_i_should_be_taken_to_the_add_user_page(context):
    assert context.driver.current_url == "http://localhost:8000/add-user"

@when("i enter the username \"testuser\" in the \"username\" field")
def step_when_i_enter_the_username_testuser_in_the_username_field(context):
    username_field = context.driver.find_element_by_id("username-field")
    username_field.send_keys("testuser")

@when("i enter the password \"testpassword\" in the \"password\" field")
def step_when_i_enter_the_password_testpassword_in_the_password_field(context):
    password_field = context.driver.find_element_by_id("password-field")
    password_field.send_keys("testpassword")

@when("i enter the email \"testuser@example.com\" in the \"email\" field")
def step_when_i_enter_the_email_testuser_example_com_in_the_email_field(context):
    email_field = context.driver.find_element_by_id("email-field")
    email_field.send_keys("testuser@example.com")

@when("i click on the \"save\" button")
def step_when_i_click_on_the_save_button(context):
    save_button = context.driver.find_element_by_
