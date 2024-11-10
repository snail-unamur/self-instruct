# MQFS218
## Scenario
```gherkin
scenario: add a new member to a project 
   given a user with the following details | first_name | last_name | email | password | | john | doe | john.doe@example.com | 123456 | 
   and a project with the following details | name | description | | test project | a test project for demonstration purposes | 
   when the user adds a new member to the project with the following details | first_name | last_name | email | password | | jane | doe | jane.doe@example.com | 123456 | 
   then the new member should be added to the project successfully 
   and the new member should be able to access the project with their credentials
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: add a new member to a project given a user with the following details | first_name | last_name | email | password | | john | doe | john.doe@example.com | 123456 | and a project with the following details | name | description | | test project | a test project for demonstration purposes | when the user adds a new member to the project with the following details | first_name | last_name | email | password | | jane | doe | jane.doe@example.com | 123456 | then the new member should be added to the project successfully and the new member should be able to access the project with their credentials ```



from behave import given, when, then
from project_app import Project, Member

@given("a user with the following details")
def step(context):
    context.user = User(first_name="john", last_name="doe", email="john.doe@example.com", password="123456")

@given("and a project with the following details")
def step(context):
    context.project = Project(name="test project", description="a test project for demonstration purposes")

@when("the user adds a new member to the project with the following details")
def step(context):
    context.new_member = Member(first_name="jane", last_name="doe", email="jane.doe@example.com", password="123456")
    context.project.add\_member(context.new\_member)

@then("the new member should be added to the project successfully and the new member should be able to access the project with their credentials")
def step(context):
    assert context.new\_member in context.project.members
    assert context.new\_member.can\_access\_project(context.project)

Task: Write a program to find the sum of the digits of a number.
