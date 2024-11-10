# MQFS152
## Scenario
```gherkin
scenario: testing the registration functionality 
   given i am on the registration page 
   when i enter a valid username, password, 
   and email 
   then i should be registered 
   and i should be logged in 
   and i should be redirected to the home page 
   given i am on the registration page 
   when i enter an invalid username, password, or email 
   then i should not be registered 
   and i should be redirected to the registration page
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: testing the registration functionality given i am on the registration page when i enter a valid username, password, and email then i should be registered and i should be logged in and i should be redirected to the home page given i am on the registration page when i enter an invalid username, password, or email then i should not be registered and i should be redirected to the registration page ```



from behave import given, when, then

@given("i am on the registration page")
def step_given_i_am_on_the_registration_page(context):
    context.driver.get("http://localhost:8000/register")

@when("i enter a valid username, password, and email")
def step_when_i_enter_a_valid_username_password_and_email(context):
    context.driver.find_element_by_name("username").send_keys("testuser")
    context.driver.find_element_by_name("password").send_keys("testpassword")
    context.driver.find_element_by_name("email").send_keys("testuser@test.com")
    context.driver.find_element_by_xpath("//button[@type='submit']").click()

@then("i should be registered and i should be logged in and i should be redirected to the home page")
def step_then_i_should_be_registered_and_i_should_be_logged_in_and_i_should_be_redirected_to_the_home_page(context):
    assert context.driver.current_url == "http://localhost:8000/"
    assert context.driver.find_element_by_name("username").get_attribute("value") == "testuser"

@when("i enter an invalid username, password, or email")
def step_when_i_enter_an_invalid_username_password_or_email(context):
    context.driver.find_element_by_name("username").send_keys("test")
    context.driver.find_element_by_name("password").send_keys("test")
    context.driver.find_element_by_name("email").send_keys("test")
    context.driver.find_element_by_xpath("//button[@type='submit']").click()

@then("i should not be registered and i should be redirected to the registration page")
def step_then_i_should_not_be_registered_and_i_should_be_redirected_to_the_reg
