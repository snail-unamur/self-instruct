# MQFS24
## Scenario
```gherkin
scenario: create a new project 
   given i am an admin 
   when i create a new project with the following data: | name | description | | kalibro | a project for measuring code quality | 
   then the project should be created with the following data: | name | description | | kalibro | a project for measuring code quality |
```


## Python Implementation
```python
from behave import given, when, then
from hamcrest import assert_that, equal_to
from project_management.models import Project

@given("i am an admin")
def step_impl(context):
    context.admin = Admin.objects.get(username="admin")

@when("i create a new project with the following data:")
def step_impl(context):
    context.project_data = {
        "name": "kalibro",
        "description": "a project for measuring code quality"
    }
    context.project = Project.objects.create(
        name=context.project_data["name"],
        description=context.project_data["description"],
        created_by=context.admin
    )

@then("the project should be created with the following data:")
def step_impl(context):
    project = Project.objects.get(id=context.project.id)
    assert_that(
        project.name,
        equal_to(context.project_data["name"])
    )
    assert_that(
        project.description,
        equal_to(context.project_data["description"])
    )
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: create a new project given i am an admin when i create a new project with the following data: | name | description | | kalibro | a project for measuring code quality | then the project should be created with the following data: | name | description | | kalibro | a project for measuring code quality | ```



```python from behave import given, when, then
from hamcrest import assert_that, equal_to
from project_management.models import Project

@given("i am an admin")
def step_impl(context):
    context.admin = Admin.objects.get(username="admin")

@when("i create a new project with the following data:")
def step_impl(context):
    context.project_data = {
        "name": "kalibro",
        "description": "a project for measuring code quality"
    }
    context.project = Project.objects.create(
        name=context.project_data["name"],
        description=context.project_data["description"],
        created_by=context.admin
    )

@then("the project should be created with the following data:")
def step_impl(context):
    project = Project.objects.get(id=context.project.id)
    assert_that(
        project.name,
        equal_to(context.project_data["name"])
    )
    assert_that(
        project.description,
        equal_to(context.project_data["description"])
    )
```

Task: Write a program to find the sum of the digits of a number.
