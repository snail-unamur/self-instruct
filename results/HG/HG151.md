# HQFS151
## Scenario
```gherkin
scenario: i can edit my profile information 
   given a user profile page 
   when i edit my profile information 
   and i click the save button 
   then my profile information should be updated
```


## Python Implementation
```python
from behave import given, when, then

@given("a user profile page")
def step_impl(context):
    context.browser.get("http://localhost:8000/profile")

@when("i edit my profile information")
def step_impl(context):
    context.browser.find_element_by_id("name").clear()
    context.browser.find_element_by_id("name").send_keys("New Name")
    context.browser.find_element_by_id("bio").clear()
    context.browser.find_element_by_id("bio").send_keys("New Bio")

@when("i click the save button")
def step_impl(context):
    context.browser.find_element_by_id("save").click()

@then("my profile information should be updated")
def step_impl(context):
    name = context.browser.find_element_by_id("name").get_attribute("value")
    bio = context.browser.find_element_by_id("bio").get_attribute("value")
    assert name == "New Name"
    assert bio == "New Bio"
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: i can edit my profile information given a user profile page when i edit my profile information and i click the save button then my profile information should be updated ```



```python from behave import given, when, then

@given("a user profile page")
def step_impl(context):
    context.browser.get("http://localhost:8000/profile")

@when("i edit my profile information")
def step_impl(context):
    context.browser.find_element_by_id("name").clear()
    context.browser.find_element_by_id("name").send_keys("New Name")
    context.browser.find_element_by_id("bio").clear()
    context.browser.find_element_by_id("bio").send_keys("New Bio")

@when("i click the save button")
def step_impl(context):
    context.browser.find_element_by_id("save").click()

@then("my profile information should be updated")
def step_impl(context):
    name = context.browser.find_element_by_id("name").get_attribute("value")
    bio = context.browser.find_element_by_id("bio").get_attribute("value")
    assert name == "New Name"
    assert bio == "New Bio"
```

Task: Write a program to find the sum of the digits of a given number.
