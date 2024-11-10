# HQFS142
## Scenario
```gherkin
scenario: i can add a new project 
   given i have a project with name "kalibro" 
   when i add a new project with name "kalibro for java" 
   then i should have two projects with name "kalibro" 
   and "kalibro for java"
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: i can add a new project given i have a project with name "kalibro" when i add a new project with name "kalibro for java" then i should have two projects with name "kalibro" and "kalibro for java" ```



from behave import given, when, then

@given("i have a project with name 'kalibro'")
def step_given_i_have_a_project_with_name_kalibro(context):
    context.projects = {'kalibro': 'kalibro'}

@when("i add a new project with name 'kalibro for java'")
def step_when_i_add_a_new_project_with_name_kalibro_for_java(context):
    context.projects['kalibro for java'] = 'kalibro for java'

@then("i should have two projects with name 'kalibro' and 'kalibro for java'")
def step_then_i_should_have_two_projects_with_name_kalibro_and_kalibro_for_java(context):
    assert 'kalibro' in context.projects
    assert 'kalibro for java' in context.projects
    assert len(context.projects) == 2

Task: Write a program to find the sum of the digits of a given number.
