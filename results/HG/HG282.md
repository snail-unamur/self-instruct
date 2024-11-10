# HQFS282
## Scenario
```gherkin
None
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: user creates a new project given i am logged in when i click on the "create project" button then i am taken to the "create project" page and i can enter a name for the project and i can select a template for the project and i can click on the "create project" button then i am taken to the "create project" page and i can see the project's name and template on the page and i can see the project's main page and i can see the project's name and template on the page and i can see the project's main page and i can see the project's name and template on the page and i can see the project's main



from behave import given, when, then

@given("i am logged in")
def step_given_i_am_logged_in(context):
    context.browser.get("http://project-creation-page.com")
    context.browser.find_element_by_id("username").send_keys("testuser")
    context.browser.find_element_by_id("password").send_keys("testpassword")
    context.browser.find_element_by_id("login-button").click()

@when("i click on the 'create project' button")
def step_when_i_click_on_the_create_project_button(context):
    context.browser.find_element_by_id("create-project-button").click()

@then("i am taken to the 'create project' page")
def step_then_i_am_taken_to_the_create_project_page(context):
    assert context.browser.current_url == "http://project-creation-page.com/create"

@then("i can enter a name for the project")
def step_then_i_can_enter_a_name_for_the_project(context):
    input_field = context.browser.find_element_by_id("project-name-input")
    input_field.send_keys("Test Project")

@then("i can select a template for the project")
def step_then_i_can_select_a_template_for_the_project(context):
    select_field = context.browser.find_element_by_id("template-select")
    select_field.send_keys("Test Template")

@then("i can click on the 'create project' button")
def step_then_i_can_click_on_the_create_project_button(context):
    context.browser.find_element_by_id("create-project-button").click()

@then("i am taken to the 'create project' page")
def step_then_i_am_taken_to_the_create_project_page(context):
    assert context.browser.current_url
