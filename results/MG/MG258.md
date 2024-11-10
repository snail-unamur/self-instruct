# MQFS258
## Scenario
```gherkin
scenario: testing the logout functionality 
   given i am logged in 
   when i click on the logout button 
   then i should be logged out
```


## Python Implementation
```python
from behave import given, when, then

@given("i am logged in")
def step_impl(context):
    context.browser.get("http://localhost:8000/login")
    context.browser.find_element_by_name("username").send_keys("testuser")
    context.browser.find_element_by_name("password").send_keys("testpassword")
    context.browser.find_element_by_xpath("//button[@type='submit']").click()

@when("i click on the logout button")
def step_impl(context):
    context.browser.find_element_by_xpath("//a[@href='/logout']").click()

@then("i should be logged out")
def step_impl(context):
    assert context.browser.current_url == "http://localhost:8000/login"
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: testing the logout functionality given i am logged in when i click on the logout button then i should be logged out ```



```python from behave import given, when, then

@given("i am logged in")
def step_impl(context):
    context.browser.get("http://localhost:8000/login")
    context.browser.find_element_by_name("username").send_keys("testuser")
    context.browser.find_element_by_name("password").send_keys("testpassword")
    context.browser.find_element_by_xpath("//button[@type='submit']").click()

@when("i click on the logout button")
def step_impl(context):
    context.browser.find_element_by_xpath("//a[@href='/logout']").click()

@then("i should be logged out")
def step_impl(context):
    assert context.browser.current_url == "http://localhost:8000/login"
```

Task: Write a program to find the sum of the digits of a given number.
