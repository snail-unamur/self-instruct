# MQFS112
## Scenario
```gherkin
scenario: testing the functionality of the project creation page 
   given i am on the project creation page 
   when i fill out the form with valid information 
   and i click the "create" button 
   then i should be redirected to the project page 
   and i should see the new project with the information i provided 
   given i am on the project creation page 
   when i fill out the form with invalid information 
   and i click the "create" button 
   then i should see an error message indicating that the information i provided is invalid 
   and i should still be on the project creation page
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: testing the functionality of the project creation page given i am on the project creation page when i fill out the form with valid information and i click the "create" button then i should be redirected to the project page and i should see the new project with the information i provided given i am on the project creation page when i fill out the form with invalid information and i click the "create" button then i should see an error message indicating that the information i provided is invalid and i should still be on the project creation page ```



```python from behave import given, when, then

@given("i am on the project creation page")
def step_given_i_am_on_the_project_creation_page(context):
    context.driver.get("http://localhost:8000/project/create")

@when("i fill out the form with valid information and i click the 'create' button")
def step_when_i_fill_out_the_form_with_valid_information_and_i_click_the_create_button(context):
    form = context.driver.find_element_by_name("project_form")
    form.find_element_by_name("name").send_keys("Test Project")
    form.find_element_by_name("description").send_keys("Test Description")
    form.find_element_by_name("submit").click()

@then("i should be redirected to the project page and i should see the new project with the information i provided")
def step_then_i_should_be_redirected_to_the_project_page_and_i_should_see_the_new_project_with_the_information_i_provided(context):
    assert context.driver.current_url == "http://localhost:8000/project/test-project"
    assert context.driver.find_element_by_name("project_name").text == "Test Project"
    assert context.driver.find_element_by_name("project_description").text == "Test Description"

@given("i am on the project creation page")
def step_given_i_am_on_the_project_creation_page_2(context):
    context.driver.get("http://localhost:8000/project/create")

@when("i fill out the form with invalid information and i click the 'create' button")
def step_when_i_fill_out_the_form_with_invalid_information_and_i_click_the_create_button(context):
    form = context.driver.find_element_by_name("project_form")
    form.find_element_by_name("
