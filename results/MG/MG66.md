# MQFS66
## Scenario
```gherkin
scenario: create a new project 
   given i am on the projects page 
   when i click on the "create project" button 
   then i am taken to the "create project" page 
   when i fill in the project details with the following: name: "my project" description: "this is my project" visibility: "private" 
   when i click on the "create" button 
   then i am taken to the project page 
   and i should see the project name "my project" 
   and i should see the project description "this is my project" 
   and i should see the project visibility "private"
```


## Python Implementation
```python
from behave import given, when, then

@given("i am on the projects page")
def step_impl(context):
    context.browser.get("http://localhost:8000/projects")

@when("i click on the 'create project' button")
def step_impl(context):
    create_project_button = context.browser.find_element_by_id("create-project-button")
    create_project_button.click()

@then("i am taken to the 'create project' page")
def step_impl(context):
    assert context.browser.current_url == "http://localhost:8000/projects/create"

@when("i fill in the project details with the following:")
def step_impl(context):
    context.execute_steps(
        """
        when i fill in the text field "name" with "my project"
        when i fill in the text field "description" with "this is my project"
        when i select "private" from the dropdown "visibility"
        """
    )

@when("i click on the 'create' button")
def step_impl(context):
    create_button = context.browser.find_element_by_id("create-button")
    create_button.click()

@then("i am taken to the project page")
def step_impl(context):
    assert context.browser.current_url == "http://localhost:8000/projects/my-project"

@then("i should see the project name 'my project'")
def step_impl(context):
    assert context.browser.find_element_by_id("project-name").text == "my project"

@then("i should see the project description 'this is my project'")
def step_impl(context):
    assert context.browser.find_element_by_id("project-description").text == "this is my project"

@then("i should see the project visibility 'private'")
def step_impl(context):
    assert context.browser.find_element_by_id("project-visibility").text == "private"
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: create a new project given i am on the projects page when i click on the "create project" button then i am taken to the "create project" page when i fill in the project details with the following: name: "my project" description: "this is my project" visibility: "private" when i click on the "create" button then i am taken to the project page and i should see the project name "my project" and i should see the project description "this is my project" and i should see the project visibility "private" ```



```python from behave import given, when, then

@given("i am on the projects page")
def step_impl(context):
    context.browser.get("http://localhost:8000/projects")

@when("i click on the 'create project' button")
def step_impl(context):
    create_project_button = context.browser.find_element_by_id("create-project-button")
    create_project_button.click()

@then("i am taken to the 'create project' page")
def step_impl(context):
    assert context.browser.current_url == "http://localhost:8000/projects/create"

@when("i fill in the project details with the following:")
def step_impl(context):
    context.execute_steps(
        """
        when i fill in the text field "name" with "my project"
        when i fill in the text field "description" with "this is my project"
        when i select "private" from the dropdown "visibility"
        """
    )

@when("i click on the 'create' button")
def step_impl(context):
    create_button = context.browser.find_element_by_id("create-button")
    create_button.click()

@then("i am taken to the project page")
def step_impl(context):
    assert context.browser.current_url == "http://localhost:8000/projects/my-project"

@then("i should see the project name 'my project'")
def step_impl(context):
    assert context.browser.find_element_by_id("project-name").text == "my project"

@then("i should see the project description 'this is my project'")
def step_impl(context):
    assert context.browser.find_element_by_id("project-description").text == "this is my project"

@then("i should see the project visibility 'private'")
def step_impl(context):
    assert context.browser.find_element_by_id("project-visibility").text == "private"
```

Task: Write a
