# MQFS211
## Scenario
```gherkin
scenario: 
   given i am on the homepage 
   when i click on the "login" button 
   then i should see the login page 
   given i am on the login page 
   when i enter my email 
   and password 
   then i should see the homepage 
   given i am on the homepage 
   when i click on the "register" button 
   then i should see the registration page 
   given i am on the registration page 
   when i enter my email 
   and password 
   then i should see the homepage 
   given i am on the homepage 
   when i click on the "logout" button 
   then i should see the login page 
   given i am on the login page 
   when i click on the "forgot password" button 
   then i should see the reset password page 
   given i am on the reset password page 
   when i enter my email 
   and click on the "reset password" button 
   then i should see the email sent page 
   given i am on the email sent page 
   when i click on the "back to login" button 
   then i should see the login page
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: given i am on the homepage when i click on the "login" button then i should see the login page given i am on the login page when i enter my email and password then i should see the homepage given i am on the homepage when i click on the "register" button then i should see the registration page given i am on the registration page when i enter my email and password then i should see the homepage given i am on the homepage when i click on the "logout" button then i should see the login page given i am on the login page when i click on the "forgot password" button then i should see the reset password page given i am on the reset password page when i enter my email and click on the "reset password" button then i should see the email sent page given i am on the email sent page when i click on the "back to login" button then i should see the login page ```



```python from behave import given, when, then

@given("i am on the homepage")
def step_impl(context):
    context.browser.get("http://www.example.com")

@when("i click on the 'login' button")
def step_impl(context):
    context.browser.find_element_by_id("login-button").click()

@then("i should see the login page")
def step_impl(context):
    assert context.browser.title == "Login Page"

@given("i am on the login page")
def step_impl(context):
    context.browser.get("http://www.example.com/login")

@when("i enter my email and password")
def step_impl(context):
    context.browser.find_element_by_id("email").send_keys("test@example.com")
    context.browser.find_element_by_id("password").send_keys("test123")

@then("i should see the homepage")
def step_impl(context):
    context.browser.find_element_by_id("home-button").click()
    assert context.browser.title == "Home Page"

@given("i am on the homepage")
def step_impl(context):
    context.browser.get("http://www.example.com")

@when("i click on the 'register' button")
def step_impl(context):
    context.browser.find_element_by_id("register-button").click()

@then("i should see the registration page")
def step_impl(context):
    assert context.browser.title == "Registration Page"

@given("i am on the registration page")
def step_impl(context):
    context.browser.get("http://www.example.com/register")

@when("i enter my email and password")
def step_impl(context):
    context.browser.find_element_by_id("email").send_keys("test@example.com")
    context.browser.find_element_by_id("password").send_keys("test123")

@
