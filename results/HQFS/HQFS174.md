# HQFS174
## Scenario
```gherkin
scenario: testing the deletion of a project 
   given i am on the project dashboard page 
   when i click on the delete button 
   then i should be redirected to the project deletion confirmation page 
   and i should see a message saying "are you sure you want to delete this project?" 
   when i confirm the deletion 
   then i should be redirected to the project dashboard page 
   and i should see a message saying "project deleted successfully"
```


## Python Implementation
```python
from behave import given, when, then

@given("i am on the project dashboard page")
def step_impl(context):
    context.browser.get("http://localhost:8000/projects")

@when("i click on the delete button")
def step_impl(context):
    context.browser.find_element_by_id("delete-project-button").click()

@then("i should be redirected to the project deletion confirmation page")
def step_impl(context):
    context.browser.get("http://localhost:8000/projects/delete")

@then("i should see a message saying {message}")
def step_impl(context, message):
    assert context.browser.find_element_by_id("confirmation-message").text == message

@when("i confirm the deletion")
def step_impl(context):
    context.browser.find_element_by_id("confirm-deletion-button").click()

@then("i should be redirected to the project dashboard page")
def step_impl(context):
    context.browser.get("http://localhost:8000/projects")

@then("i should see a message saying {message}")
def step_impl(context, message):
    assert context.browser.find_element_by_id("success-message").text == message
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: testing the deletion of a project given i am on the project dashboard page when i click on the delete button then i should be redirected to the project deletion confirmation page and i should see a message saying "are you sure you want to delete this project?" when i confirm the deletion then i should be redirected to the project dashboard page and i should see a message saying "project deleted successfully" ```



```python from behave import given, when, then

@given("i am on the project dashboard page")
def step_impl(context):
    context.browser.get("http://localhost:8000/projects")

@when("i click on the delete button")
def step_impl(context):
    context.browser.find_element_by_id("delete-project-button").click()

@then("i should be redirected to the project deletion confirmation page")
def step_impl(context):
    context.browser.get("http://localhost:8000/projects/delete")

@then("i should see a message saying {message}")
def step_impl(context, message):
    assert context.browser.find_element_by_id("confirmation-message").text == message

@when("i confirm the deletion")
def step_impl(context):
    context.browser.find_element_by_id("confirm-deletion-button").click()

@then("i should be redirected to the project dashboard page")
def step_impl(context):
    context.browser.get("http://localhost:8000/projects")

@then("i should see a message saying {message}")
def step_impl(context, message):
    assert context.browser.find_element_by_id("success-message").text == message
```

Task: Write a program to find the sum of the digits of a given number.
