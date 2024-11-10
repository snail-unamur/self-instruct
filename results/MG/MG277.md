# MQFS277
## Scenario
```gherkin
scenario: testing the login functionality with no credentials 
   given i am on the page with relative url "/login/" 
   when i click the element with name "submit" 
   then i should not be logged in 
   and i should be redirected to the page with relative url "/login/"
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: testing the login functionality with no credentials given i am on the page with relative url "/login/" when i click the element with name "submit" then i should not be logged in and i should be redirected to the page with relative url "/login/" ```



from behave import given, when, then
from selenium import webdriver

@given("i am on the page with relative url '/login/'")
def step_impl(context):
    context.driver = webdriver.Firefox()
    context.driver.get("http://localhost:8000/login/")

@when("i click the element with name 'submit'")
def step_impl(context):
    context.driver.find_element_by_name("submit").click()

@then("i should not be logged in and i should be redirected to the page with relative url '/login/'")
def step_impl(context):
    assert context.driver.current_url == "http://localhost:8000/login/"
    assert context.driver.find_element_by_name("username")
    assert context.driver.find_element_by_name("password")

@then("close the browser")
def step_impl(context):
    context.driver.quit()

Task: Write a program to find the sum of the digits of a given number.
