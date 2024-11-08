# HQFS118
## Scenario
```gherkin
scenario: i can create a new user 
   given i am on the user creation page 
   when i enter the user details "<first_name>" "<last_name>" "<email>" 
   and i click the create button 
   then the user "<first_name> <last_name>" with email "<email>" should be created
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: i can create a new user given i am on the user creation page when i enter the user details "<first_name>" "<last_name>" "<email>" and i click the create button then the user "<first_name> <last_name>" with email "<email>" should be created ```



from behave import given, when, then
from selenium import webdriver

@given("i am on the user creation page")
def step(context):
    context.driver = webdriver.Firefox()
    context.driver.get("http://localhost:8000/users/new")

@when("i enter the user details {first_name} {last_name} {email}")
def step(context, first_name, last_name, email):
    context.driver.find_element_by_name("first_name").send_keys(first_name)
    context.driver.find_element_by_name("last_name").send_keys(last_name)
    context.driver.find_element_by_name("email").send_keys(email)

@when("i click the create button")
def step(context):
    context.driver.find_element_by_xpath("//input[@type='submit']").click()

@then("the user {first_name} {last_name} with email {email} should be created")
def step(context, first_name, last_name, email):
    assert context.driver.find_element_by_xpath("//td[contains(text(),'{} {}')]".format(first_name, last_name))
    assert context.driver.find_element_by_xpath("//td[contains(text(),'{}')]".format(email))
    context.driver.close()

Task: Write a program to find the sum of the digits of a given number.
