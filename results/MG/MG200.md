# MQFS200
## Scenario
```gherkin
scenario: testing the creation of a new project 
   given i have a project with name "kalibro" 
   when i create a new project with the same name 
   then the new project should have a different id 
   then the new project should have the same name as the original project
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: testing the creation of a new project given i have a project with name "kalibro" when i create a new project with the same name then the new project should have a different id then the new project should have the same name as the original project ```



from behave import given, when, then
from project import Project

@given("i have a project with name 'kalibro'")
def step_impl(context):
    context.project = Project("kalibro")

@when("i create a new project with the same name")
def step_impl(context):
    context.new_project = Project("kalibro")

@then("the new project should have a different id then the new project should have the same name as the original project")
def step_impl(context):
    assert context.project.id != context.new_project.id
    assert context.project.name == context.new_project.name

Task: Write a program to find the sum of the digits of a number.
