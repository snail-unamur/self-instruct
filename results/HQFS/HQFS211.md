# HQFS211
## Scenario
```gherkin
scenario: user wants to edit a project 
   given i am logged in 
   when i navigate to the "projects" page 
   then i should see a list of all my projects 
   when i click on the edit button for a project 
   then i should see a form to edit the project details 
   when i enter the updated project details 
   and click on the submit button 
   then the project should be updated 
   and i should be redirected to the project page
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: user wants to edit a project given i am logged in when i navigate to the "projects" page then i should see a list of all my projects when i click on the edit button for a project then i should see a form to edit the project details when i enter the updated project details and click on the submit button then the project should be updated and i should be redirected to the project page ```



```python from behave import given, when, then

@given("i am logged in")
def step_impl(context):
    context.browser.get("http://localhost:8000/login")
    context.browser.find_element_by_name("username").send_keys("testuser")
    context.browser.find_element_by_name("password").send_keys("testpassword")
    context.browser.find_element_by_xpath("//button[@type='submit']").click()

@when("i navigate to the 'projects' page")
def step_impl(context):
    context.browser.get("http://localhost:8000/projects")

@then("i should see a list of all my projects")
def step_impl(context):
    projects = context.browser.find_elements_by_xpath("//tr/td[1]")
    assert len(projects) > 0

@when("i click on the edit button for a project")
def step_impl(context):
    edit_button = context.browser.find_element_by_xpath("//tr[1]/td[5]/a")
    edit_button.click()

@then("i should see a form to edit the project details")
def step_impl(context):
    form = context.browser.find_element_by_tag_name("form")
    assert form is not None

@when("i enter the updated project details and click on the submit button")
def step_impl(context):
    form = context.browser.find_element_by_tag_name("form")
    form.find_element_by_name("name").send_keys("Updated Project")
    form.find_element_by_name("description").send_keys("This is an updated project.")
    form.find_element_by_xpath("//button[@type='submit']").click()

@then("the project should be updated and i should be redirected to the project page")
def step_impl(context):
    assert context.browser.current_url == "http://localhost:8000/projects/1"
    assert context.browser.find_element_by
