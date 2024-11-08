# MQFS226
## Scenario
```gherkin
scenario: testing the edit project feature 
   given you are logged in 
   and you are on the project page 
   when you click on the "edit project" button 
   then you should be taken to the project edit page 
   when you enter the updated project details 
   and click "save" 
   then the project should be updated 
   and you should be taken to the project page
```


## Python Implementation
```python
from behave import given, when, then

@given("you are logged in and you are on the project page")
def step_impl(context):
    context.execute_steps("you are logged in")
    context.execute_steps("you are on the project page")

@when("you click on the \"edit project\" button")
def step_impl(context):
    context.project_page.click_edit_project_button()

@then("you should be taken to the project edit page")
def step_impl(context):
    assert context.project_edit_page.current_url == context.base_url + "/project/edit"

@when("you enter the updated project details and click \"save\"")
def step_impl(context):
    context.project_edit_page.enter_updated_project_details()
    context.project_edit_page.click_save_button()

@then("the project should be updated and you should be taken to the project page")
def step_impl(context):
    assert context.project_page.current_url == context.base_url + "/project"
    assert context.project_page.project_name == "Updated Project Name"
    assert context.project_page.project_description == "Updated Project Description"
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: testing the edit project feature given you are logged in and you are on the project page when you click on the "edit project" button then you should be taken to the project edit page when you enter the updated project details and click "save" then the project should be updated and you should be taken to the project page ```



```python from behave import given, when, then

@given("you are logged in and you are on the project page")
def step_impl(context):
    context.execute_steps("you are logged in")
    context.execute_steps("you are on the project page")

@when("you click on the \"edit project\" button")
def step_impl(context):
    context.project_page.click_edit_project_button()

@then("you should be taken to the project edit page")
def step_impl(context):
    assert context.project_edit_page.current_url == context.base_url + "/project/edit"

@when("you enter the updated project details and click \"save\"")
def step_impl(context):
    context.project_edit_page.enter_updated_project_details()
    context.project_edit_page.click_save_button()

@then("the project should be updated and you should be taken to the project page")
def step_impl(context):
    assert context.project_page.current_url == context.base_url + "/project"
    assert context.project_page.project_name == "Updated Project Name"
    assert context.project_page.project_description == "Updated Project Description"
```

Task: Write a program to find the sum of the digits of a given number.
