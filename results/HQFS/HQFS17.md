# HQFS17
## Scenario
```gherkin
scenario: user can logout 
   given user is logged in 
   when user clicks on logout button 
   then user should be logged out 
   and redirected to the login page
```


## Python Implementation
```python
from behave import given, when, then

@given("user is logged in")
def step_impl(context):
    context.browser.get("http://localhost:8000/login")
    context.browser.find_element_by_name("username").send_keys("testuser")
    context.browser.find_element_by_name("password").send_keys("testpassword")
    context.browser.find_element_by_xpath("//button[@type='submit']").click()

@when("user clicks on logout button")
def step_impl(context):
    context.browser.find_element_by_xpath("//a[@href='/logout']").click()

@then("user should be logged out and redirected to the login page")
def step_impl(context):
    assert context.browser.current_url == "http://localhost:8000/login"
    assert context.browser.find_element_by_name("username")
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: user can logout given user is logged in when user clicks on logout button then user should be logged out and redirected to the login page ``` for all the tasks, you will need to install the `behave` package using pip: ``` pip install behave ``` you will also need to create a file called `features/step_definitions.py` to define the step functions.



```python
from behave import given, when, then

@given("user is logged in")
def step_impl(context):
    context.browser.get("http://localhost:8000/login")
    context.browser.find_element_by_name("username").send_keys("testuser")
    context.browser.find_element_by_name("password").send_keys("testpassword")
    context.browser.find_element_by_xpath("//button[@type='submit']").click()

@when("user clicks on logout button")
def step_impl(context):
    context.browser.find_element_by_xpath("//a[@href='/logout']").click()

@then("user should be logged out and redirected to the login page")
def step_impl(context):
    assert context.browser.current_url == "http://localhost:8000/login"
    assert context.browser.find_element_by_name("username")
```

Task: Write a program to find the sum of the digits of a given number.
