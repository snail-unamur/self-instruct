# MQFS50
## Scenario
```gherkin
scenario: testing the edit profile feature 
   given i am logged in 
   when i click on the edit profile button 
   then i should be able to edit my profile information 
   and i should be able to save my changes 
   when i save my changes 
   then my profile information should be updated 
   and i should see a success message
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: testing the edit profile feature given i am logged in when i click on the edit profile button then i should be able to edit my profile information and i should be able to save my changes when i save my changes then my profile information should be updated and i should see a success message ```



from behave import given, when, then

@given("i am logged in")
def step_impl(context):
    context.browser.get("http://localhost:8000/profile")
    context.browser.find_element_by_id("username").send_keys("testuser")
    context.browser.find_element_by_id("password").send_keys("testpassword")
    context.browser.find_element_by_id("login").click()

@when("i click on the edit profile button")
def step_impl(context):
    context.browser.find_element_by_id("edit_profile").click()

@then("i should be able to edit my profile information")
def step_impl(context):
    context.browser.find_element_by_id("first_name").clear()
    context.browser.find_element_by_id("first_name").send_keys("new_first_name")
    context.browser.find_element_by_id("last_name").clear()
    context.browser.find_element_by_id("last_name").send_keys("new_last_name")

@then("i should be able to save my changes")
def step_impl(context):
    context.browser.find_element_by_id("save_changes").click()

@then("my profile information should be updated")
def step_impl(context):
    assert context.browser.find_element_by_id("first_name").get_attribute("value") == "new_first_name"
    assert context.browser.find_element_by_id("last_name").get_attribute("value") == "new_last_name"

@then("i should see a success message")
def step_impl(context):
    assert context.browser.find_element_by_id("success_message").text == "Profile updated successfully"
