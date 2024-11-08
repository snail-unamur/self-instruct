# MQFS171
## Scenario
```gherkin
scenario: create a new project with a specific name 
   given the project name is "myproject" 
   when i create a new project 
   then the project is created with the name "myproject"
```


## Python Implementation
```python
from behave import given, when, then

@given("i create a new project")
def step_impl(context):
    context.project = Project()

@when("the project name is \"myproject\"")
def step_impl(context):
    context.project.name = "myproject"

@then("the project is created with the name \"myproject\"")
def step_impl(context):
    assert context.project.name == "myproject"

class Project:
    def __init__(self):
        self.name = None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: create a new project with a specific name given the project name is "myproject" when i create a new project then the project is created with the name "myproject" ```



```python from behave import given, when, then

@given("i create a new project")
def step_impl(context):
    context.project = Project()

@when("the project name is \"myproject\"")
def step_impl(context):
    context.project.name = "myproject"

@then("the project is created with the name \"myproject\"")
def step_impl(context):
    assert context.project.name == "myproject"

class Project:
    def __init__(self):
        self.name = None
```

Task: Write a program to find the sum of the digits of a given number.
