# HQFS129
## Scenario
```gherkin
scenario: user can delete a project 
   given i am logged in as a user with the role of "admin" 
   when i go to the project list page 
   and i select a project 
   and i click the delete button 
   then the project should be deleted from the system
```


## Python Implementation
```python
from behave import given, when, then

@given("i am logged in as a user with the role of 'admin'")
def step_impl(context):
    context.execute_steps(u"""
        Given i am logged in
        And my role is "admin"
    """)

@when("i go to the project list page")
def step_impl(context):
    context.project_list_page.go_to()

@when("i select a project")
def step_impl(context):
    context.project_list_page.select_project()

@when("i click the delete button")
def step_impl(context):
    context.project_list_page.click_delete_button()

@then("the project should be deleted from the system")
def step_impl(context):
    assert context.project_list_page.is_deleted() is True
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: user can delete a project given i am logged in as a user with the role of "admin" when i go to the project list page and i select a project and i click the delete button then the project should be deleted from the system ```



```python from behave import given, when, then

@given("i am logged in as a user with the role of 'admin'")
def step_impl(context):
    context.execute_steps(u"""
        Given i am logged in
        And my role is "admin"
    """)

@when("i go to the project list page")
def step_impl(context):
    context.project_list_page.go_to()

@when("i select a project")
def step_impl(context):
    context.project_list_page.select_project()

@when("i click the delete button")
def step_impl(context):
    context.project_list_page.click_delete_button()

@then("the project should be deleted from the system")
def step_impl(context):
    assert context.project_list_page.is_deleted() is True
```

Task: Write a program to find the sum of the digits of a given number.
