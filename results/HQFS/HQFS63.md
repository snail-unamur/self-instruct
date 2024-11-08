# HQFS63
## Scenario
```gherkin
scenario: create a new user 
   given i am on the registration page 
   when i fill in the registration form with valid information 
   then i should be registered as a new user 
   and i should be logged in 
   and i should be redirected to the homepage 
   and i should see a welcome message 
   and i should see a confirmation message that my account has been created
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: create a new user given i am on the registration page when i fill in the registration form with valid information then i should be registered as a new user and i should be logged in and i should be redirected to the homepage and i should see a welcome message and i should see a confirmation message that my account has been created ```



from behave import given, when, then
from selenium import webdriver

@given("i am on the registration page")
def step_impl(context):
    context.driver = webdriver.Firefox()
    context.driver.get("http://localhost:8000/register")

@when("i fill in the registration form with valid information")
def step_impl(context):
    context.driver.find_element_by_name("username").send_keys("testuser")
    context.driver.find_element_by_name("email").send_keys("testuser@example.com")
    context.driver.find_element_by_name("password").send_keys("testpassword")
    context.driver.find_element_by_name("confirm_password").send_keys("testpassword")
    context.driver.find_element_by_xpath("//button[@type='submit']").click()

@then("i should be registered as a new user")
def step_impl(context):
    assert context.driver.find_element_by_xpath("//p[contains(text(), 'User created successfully')]")

@then("i should be logged in")
def step_impl(context):
    assert context.driver.find_element_by_xpath("//a[contains(text(), 'Logout')]")

@then("i should be redirected to the homepage")
def step_impl(context):
    assert context.driver.current_url == "http://localhost:8000/"

@then("i should see a welcome message")
def step_impl(context):
    assert context.driver.find_element_by_xpath("//h1[contains(text(), 'Welcome, testuser')]")

@then("i should see a confirmation message that my account has been created")
def step_impl(context):
    assert context.driver.find_element_by_xpath("//p[contains(text(), 'Your account has been created')]")

@then("i should see a confirmation message that my account has been activated")
def step_impl(context):
    assert context.driver.find_element_by_xpath
