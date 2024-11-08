# MQFS37
## Scenario
```gherkin
scenario: 
   given i have a user with the email "[test@test.com](mailto:test@test.com)" 
   and the password "password" 
   when i go to the login page 
   then i should see a login form with fields for email 
   and password 
   and 
   when i enter the email "[test@test.com](mailto:test@test.com)" 
   and the password "password" 
   and i click the login button 
   then i should be logged in 
   and redirected to the homepage 
   and 
   when i click on the "settings" button 
   then i should see a settings page with fields for email 
   and password 
   and 
   when i change the email to "[newtest@test.com](mailto:newtest@test.com)" 
   and the password to "newpassword" 
   and i click the "save" button 
   then i should be logged out 
   and redirected to the login page 
   and 
   when i enter the email "[newtest@test.com](mailto:newtest@test.com)" 
   and the password "newpassword" 
   and i click the login button 
   then i should be logged in 
   and redirected to the homepage
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: given i have a user with the email "[test@test.com](mailto:test@test.com)" and the password "password" when i go to the login page then i should see a login form with fields for email and password and when i enter the email "[test@test.com](mailto:test@test.com)" and the password "password" and i click the login button then i should be logged in and redirected to the homepage and when i click on the "settings" button then i should see a settings page with fields for email and password and when i change the email to "[newtest@test.com](mailto:newtest@test.com)" and the password to "newpassword" and i click the "save" button then i should be logged out and redirected to the login page and when i enter the email "[newtest@test.com](mailto:newtest@test.com)" and the password "newpassword" and i click the login button then i should be logged in and redirected to the homepage ```



from behave import given, when, then
from selenium import webdriver

@given("i have a user with the email 'test@test.com' and the password 'password'")
def step_given(context):
    context.driver = webdriver.Firefox()
    context.driver.get("http://localhost:8000/login")
    context.email = "test@test.com"
    context.password = "password"

@when("i go to the login page")
def step_when(context):
    pass

@when("i should see a login form with fields for email and password")
def step_when(context):
    assert context.driver.find_element_by_name("email")
    assert context.driver.find_element_by_name("password")

@when("i enter the email 'test@test.com' and the password 'password'")
def step_when(context):
    context.driver.find_element_by_name("email").send_keys(context.email)
    context.driver.find_element_by_name("password").send_keys(context.password)

@when("i click the login button")
def step_when(context):
    context.driver.find_element_by_xpath("//button[@type='submit']").click()

@then("i should be logged in and redirected to the homepage")
def step_then(context):
    assert context.driver.current_url == "http://localhost:8000/home"

@when("i click on the 'settings' button")
def step_when(context):
    context.driver.find_element_by_xpath("//a[@href='/settings']").click()

@then("i should see a settings page with fields for email and password")
def step_then(context):
    assert context.driver.find_element_by_name("email")
    assert context.driver.find_element_by_name("password")

@when("i change the email to 'newtest@test.com' and the password to 'newpassword'")
def step_when(context):
    context.driver.
