# HQFS159
## Scenario
```gherkin
scenario: user updates a project 
   given the user is authenticated 
   and the user has a project with name "test project" 
   when the user updates the project name to "updated test project" 
   then the project name should be updated to "updated test project" 
   and the project should still be listed in the user's projects
```


## Python Implementation
```python
from behave import given, when, then

@given("the user is authenticated")
def step_impl(context):
    context.user = User()
    context.user.is_authenticated = True

@given("the user has a project with name 'test project'")
def step_impl(context):
    context.project = Project()
    context.project.name = "test project"
    context.user.projects.append(context.project)

@when("the user updates the project name to 'updated test project'")
def step_impl(context):
    context.project.name = "updated test project"

@then("the project name should be updated to 'updated test project'")
def step_impl(context):
    assert context.project.name == "updated test project"

@then("the project should still be listed in the user's projects")
def step_impl(context):
    assert context.project in context.user.projects
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: user updates a project given the user is authenticated and the user has a project with name "test project" when the user updates the project name to "updated test project" then the project name should be updated to "updated test project" and the project should still be listed in the user's projects ```



```python from behave import given, when, then

@given("the user is authenticated")
def step_impl(context):
    context.user = User()
    context.user.is_authenticated = True

@given("the user has a project with name 'test project'")
def step_impl(context):
    context.project = Project()
    context.project.name = "test project"
    context.user.projects.append(context.project)

@when("the user updates the project name to 'updated test project'")
def step_impl(context):
    context.project.name = "updated test project"

@then("the project name should be updated to 'updated test project'")
def step_impl(context):
    assert context.project.name == "updated test project"

@then("the project should still be listed in the user's projects")
def step_impl(context):
    assert context.project in context.user.projects
```

Task: Write a program to find the sum of the digits of a number.
