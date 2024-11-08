# MQFS193
## Scenario
```gherkin
scenario: check if the user is able to create a new organization 
   given the user is on the organization page 
   when the user clicks on the create new organization button 
   then the user is redirected to the create new organization page 
   and the user is able to input the name 
   and description of the organization 
   and the user is able to submit the form 
   and the user is redirected to the organization page with the new organization displayed
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: check if the user is able to create a new organization given the user is on the organization page when the user clicks on the create new organization button then the user is redirected to the create new organization page and the user is able to input the name and description of the organization and the user is able to submit the form and the user is redirected to the organization page with the new organization displayed ```



from behave import given, when, then

@given("the user is on the organization page")
def step_given_the_user_is_on_the_organization_page(context):
    context.browser.get("http://localhost:8000/organizations")

@when("the user clicks on the create new organization button")
def step_when_the_user_clicks_on_the_create_new_organization_button(context):
    context.browser.find_element_by_id("create-organization-button").click()

@then("the user is redirected to the create new organization page")
def step_then_the_user_is_redirected_to_the_create_new_organization_page(context):
    assert context.browser.current_url == "http://localhost:8000/organizations/create"

@then("the user is able to input the name and description of the organization")
def step_then_the_user_is_able_to_input_the_name_and_description_of_the_organization(context):
    name_field = context.browser.find_element_by_id("name")
    description_field = context.browser.find_element_by_id("description")
    name_field.send_keys("Test Org")
    description_field.send_keys("Test Org Description")

@then("the user is able to submit the form")
def step_then_the_user_is_able_to_submit_the_form(context):
    context.browser.find_element_by_id("submit-button").click()

@then("the user is redirected to the organization page with the new organization displayed")
def step_then_the_user_is_redirected_to_the_organization_page_with_the_new_organization_displayed(context):
    assert "Test Org" in context.browser.page_source
