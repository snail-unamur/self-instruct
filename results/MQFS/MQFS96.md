# MQFS96
## Scenario
```gherkin
scenario: create a new user with the 
   given user details 
   given i am on the page with relative url "/users/new" 
   when i fill in the username field with "testuser" 
   and i fill in the password field with "testpassword" 
   and i fill in the email field with "testuser@test.com" 
   and i click the element with name "submit" 
   then i should see the text "user was successfully created"
```


## Python Implementation
```python
from behave import given, when, then
from selenium.webdriver.common.by import By

@given("i am on the page with relative url '/users/new'")
def step_impl(context):
    context.browser.get(context.config.base_url + '/users/new')

@when("i fill in the username field with 'testuser'")
def step_impl(context):
    context.browser.find_element(By.NAME, "username").send_keys("testuser")

@when("i fill in the password field with 'testpassword'")
def step_impl(context):
    context.browser.find_element(By.NAME, "password").send_keys("testpassword")

@when("i fill in the email field with 'testuser@test.com'")
def step_impl(context):
    context.browser.find_element(By.NAME, "email").send_keys("testuser@test.com")

@when("i click the element with name 'submit'")
def step_impl(context):
    context.browser.find_element(By.NAME, "submit").click()

@then("i should see the text 'user was successfully created'")
def step_impl(context):
    assert "user was successfully created" in context.browser.page_source
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: create a new user with the given user details given i am on the page with relative url "/users/new" when i fill in the username field with "testuser" and i fill in the password field with "testpassword" and i fill in the email field with "testuser@test.com" and i click the element with name "submit" then i should see the text "user was successfully created" ```



```python from behave import given, when, then
from selenium.webdriver.common.by import By

@given("i am on the page with relative url '/users/new'")
def step_impl(context):
    context.browser.get(context.config.base_url + '/users/new')

@when("i fill in the username field with 'testuser'")
def step_impl(context):
    context.browser.find_element(By.NAME, "username").send_keys("testuser")

@when("i fill in the password field with 'testpassword'")
def step_impl(context):
    context.browser.find_element(By.NAME, "password").send_keys("testpassword")

@when("i fill in the email field with 'testuser@test.com'")
def step_impl(context):
    context.browser.find_element(By.NAME, "email").send_keys("testuser@test.com")

@when("i click the element with name 'submit'")
def step_impl(context):
    context.browser.find_element(By.NAME, "submit").click()

@then("i should see the text 'user was successfully created'")
def step_impl(context):
    assert "user was successfully created" in context.browser.page_source
```

Task: Write a program to find the sum of the digits of a given number.
