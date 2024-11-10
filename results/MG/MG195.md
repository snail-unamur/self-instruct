# MQFS195
## Scenario
```gherkin
scenario: create a new project 
   given i am on the project creation page 
   when i enter a name 
   and description for the project 
   then i should be able to create a new project 
   when i am on the project page 
   then i should see the name 
   and description of the project i just created
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: create a new project given i am on the project creation page when i enter a name and description for the project then i should be able to create a new project when i am on the project page then i should see the name and description of the project i just created ```



from behave import given, when, then

@given("i am on the project creation page")
def step_impl(context):
    context.project_creation_page.navigate()

@when("i enter a name and description for the project")
def step_impl(context):
    context.project_creation_page.enter_name_and_description()

@then("i should be able to create a new project")
def step_impl(context):
    context.project = context.project_creation_page.create_project()

@then("i am on the project page")
def step_impl(context):
    context.project_page.navigate()

@then("i should see the name and description of the project i just created")
def step_impl(context):
    context.project_page.verify_project_name_and_description(context.project.name, context.project.description)


class ProjectCreationPage:
    def navigate(self):
        # Navigate to the project creation page
        pass

    def enter_name_and_description(self):
        # Enter a name and description for the project
        pass

    def create_project(self):
        # Create a new project
        pass


class ProjectPage:
    def navigate(self):
        # Navigate to the project page
        pass

    def verify_project_name_and_description(self, name, description):
        # Verify the project name and description
        pass


class Project:
    def __init__(self, name, description):
        self.name = name
        self.description = description


class Context:
    pass


context = Context()


Task: Write a program to find the sum of the digits of a number.
