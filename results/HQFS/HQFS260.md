# HQFS260
## Scenario
```gherkin
scenario: user can view a project's details 
   given i am logged in 
   and i am on the projects page 
   when i click on the "view" button for a project 
   then i am taken to the project details page 
   and i can view the project's name 
   and i can view the project's description 
   and i can view the project's members
```


## Python Implementation
```python
from behave import given, when, then

@given("i am logged in")
def step_impl(context):
    context.login()

@given("i am on the projects page")
def step_impl(context):
    context.projects_page.load()

@when("i click on the 'view' button for a project")
def step_impl(context):
    context.project = context.projects_page.click_view_project()

@then("i am taken to the project details page")
def step_impl(context):
    context.project_details_page.assert_on_page()

@then("i can view the project's name")
def step_impl(context):
    context.project_details_page.assert_project_name(context.project.name)

@then("i can view the project's description")
def step_impl(context):
    context.project_details_page.assert_project_description(context.project.description)

@then("i can view the project's members")
def step_impl(context):
    context.project_details_page.assert_project_members(context.project.members)
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: user can view a project's details given i am logged in and i am on the projects page when i click on the "view" button for a project then i am taken to the project details page and i can view the project's name and i can view the project's description and i can view the project's members ```



```python from behave import given, when, then

@given("i am logged in")
def step_impl(context):
    context.login()

@given("i am on the projects page")
def step_impl(context):
    context.projects_page.load()

@when("i click on the 'view' button for a project")
def step_impl(context):
    context.project = context.projects_page.click_view_project()

@then("i am taken to the project details page")
def step_impl(context):
    context.project_details_page.assert_on_page()

@then("i can view the project's name")
def step_impl(context):
    context.project_details_page.assert_project_name(context.project.name)

@then("i can view the project's description")
def step_impl(context):
    context.project_details_page.assert_project_description(context.project.description)

@then("i can view the project's members")
def step_impl(context):
    context.project_details_page.assert_project_members(context.project.members)
```

Task: Write a program to find the sum of the digits of a given number.
