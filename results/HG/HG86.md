# HQFS86
## Scenario
```gherkin
scenario: a user can view a list of all projects 
   given a user is registered 
   when the user views a list of all projects 
   then the list of all projects is viewed
```


## Python Implementation
```python
from behave import given, when, then

@given("a user is registered")
def step_impl(context):
    context.user = User()
    context.user.register()

@when("the user views a list of all projects")
def step_impl(context):
    context.projects = Project.get_all_projects()

@then("the list of all projects is viewed")
def step_impl(context):
    assert context.projects == Project.get_all_projects()
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: a user can view a list of all projects given a user is registered when the user views a list of all projects then the list of all projects is viewed ```



```python from behave import given, when, then

@given("a user is registered")
def step_impl(context):
    context.user = User()
    context.user.register()

@when("the user views a list of all projects")
def step_impl(context):
    context.projects = Project.get_all_projects()

@then("the list of all projects is viewed")
def step_impl(context):
    assert context.projects == Project.get_all_projects()
```

Task: Write a program to find the sum of the digits of a given number.
