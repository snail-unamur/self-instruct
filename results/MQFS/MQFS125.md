# MQFS125
## Scenario
```gherkin
scenario: check if the user can create a new project 
   given the user is logged in 
   when i visit the projects page 
   then i should see a "create new project" button 
   when i click the "create new project" button 
   then i should see a form to enter the project details 
   when i submit the form with valid details 
   then the project should be created 
   and i should be redirected to the project page 
   and i should see the project details on the page
```


## Python Implementation
```python
from behave import given, when, then

@given("the user is logged in")
def step_impl(context):
    context.execute_steps("Given the user is logged in as an admin")

@when("i visit the projects page")
def step_impl(context):
    context.projects_page.load()

@then("i should see a \"create new project\" button")
def step_impl(context):
    assert context.projects_page.create_new_project_button.is_displayed()

@when("i click the \"create new project\" button")
def step_impl(context):
    context.projects_page.create_new_project_button.click()

@then("i should see a form to enter the project details")
def step_impl(context):
    assert context.new_project_page.is_displayed()

@when("i submit the form with valid details")
def step_impl(context):
    context.new_project_page.submit()

@then("the project should be created and i should be redirected to the project page")
def step_impl(context):
    assert context.projects_page.is_displayed()

@then("i should see the project details on the page")
def step_impl(context):
    assert context.projects_page.project_details_displayed()
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: check if the user can create a new project given the user is logged in when i visit the projects page then i should see a "create new project" button when i click the "create new project" button then i should see a form to enter the project details when i submit the form with valid details then the project should be created and i should be redirected to the project page and i should see the project details on the page ```



```python from behave import given, when, then

@given("the user is logged in")
def step_impl(context):
    context.execute_steps("Given the user is logged in as an admin")

@when("i visit the projects page")
def step_impl(context):
    context.projects_page.load()

@then("i should see a \"create new project\" button")
def step_impl(context):
    assert context.projects_page.create_new_project_button.is_displayed()

@when("i click the \"create new project\" button")
def step_impl(context):
    context.projects_page.create_new_project_button.click()

@then("i should see a form to enter the project details")
def step_impl(context):
    assert context.new_project_page.is_displayed()

@when("i submit the form with valid details")
def step_impl(context):
    context.new_project_page.submit()

@then("the project should be created and i should be redirected to the project page")
def step_impl(context):
    assert context.projects_page.is_displayed()

@then("i should see the project details on the page")
def step_impl(context):
    assert context.projects_page.project_details_displayed()
```

Task: Write a program to find the sum of the digits of a given number.
