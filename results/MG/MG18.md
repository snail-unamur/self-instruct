# MQFS18
## Scenario
```gherkin
scenario: create a new project 
   given i have a project with name "kalibro" 
   when i create a new project with name "kalibro2" 
   then a new project with name "kalibro2" is created 
   and i have a project with name "kalibro2" 
   and i don't have a project with name "kalibro" 
   and i have a project with name "kalibro2"
```


## Python Implementation
```python
from behave import given, when, then

@given("i have a project with name 'kalibro'")
def step_given_i_have_a_project_with_name_kalibro(context):
    context.project = Project("kalibro")

@when("i create a new project with name 'kalibro2'")
def step_when_i_create_a_new_project_with_name_kalibro2(context):
    context.new_project = Project("kalibro2")
    context.project.create_new_project(context.new_project)

@then("a new project with name 'kalibro2' is created")
def step_then_a_new_project_with_name_kalibro2_is_created(context):
    assert context.new_project.name == "kalibro2"

@then("i have a project with name 'kalibro2'")
def step_then_i_have_a_project_with_name_kalibro2(context):
    assert context.project.name == "kalibro2"

@then("i don't have a project with name 'kalibro'")
def step_then_i_dont_have_a_project_with_name_kalibro(context):
    assert context.project.name != "kalibro"
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: create a new project given i have a project with name "kalibro" when i create a new project with name "kalibro2" then a new project with name "kalibro2" is created and i have a project with name "kalibro2" and i don't have a project with name "kalibro" and i have a project with name "kalibro2" ```



```python from behave import given, when, then

@given("i have a project with name 'kalibro'")
def step_given_i_have_a_project_with_name_kalibro(context):
    context.project = Project("kalibro")

@when("i create a new project with name 'kalibro2'")
def step_when_i_create_a_new_project_with_name_kalibro2(context):
    context.new_project = Project("kalibro2")
    context.project.create_new_project(context.new_project)

@then("a new project with name 'kalibro2' is created")
def step_then_a_new_project_with_name_kalibro2_is_created(context):
    assert context.new_project.name == "kalibro2"

@then("i have a project with name 'kalibro2'")
def step_then_i_have_a_project_with_name_kalibro2(context):
    assert context.project.name == "kalibro2"

@then("i don't have a project with name 'kalibro'")
def step_then_i_dont_have_a_project_with_name_kalibro(context):
    assert context.project.name != "kalibro"
```

Task: Write a program to find the sum of the digits of a number.
