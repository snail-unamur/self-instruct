# HQFS105
## Scenario
```gherkin
scenario: testing the view functionality 
   given i am logged in as a user 
   when i view my profile 
   then i should see my information 
   and i should be able to edit it 
   when i view another user's profile 
   then i should see their information 
   but i should not be able to edit it
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: testing the view functionality given i am logged in as a user when i view my profile then i should see my information and i should be able to edit it when i view another user's profile then i should see their information but i should not be able to edit it ```



from behave import given, when, then
from selenium import webdriver

@given("i am logged in as a user")
def step_impl(context):
    context.driver = webdriver.Firefox()
    context.driver.get("http://localhost:8000")
    context.driver.find_element_by_name("username").send_keys("user")
    context.driver.find_element_by_name("password").send_keys("pass")
    context.driver.find_element_by_css_selector("input[type=submit]").click()

@when("i view my profile")
def step_impl(context):
    context.driver.find_element_by_link_text("My Profile").click()

@then("i should see my information and i should be able to edit it")
def step_impl(context):
    assert context.driver.find_element_by_id("profile-name").text == "user"
    context.driver.find_element_by_id("profile-edit").click()

@when("i view another user's profile")
def step_impl(context):
    context.driver.find_element_by_link_text("Another User").click()

@then("i should see their information but i should not be able to edit it")
def step_impl(context):
    assert context.driver.find_element_by_id("profile-name").text == "another user"
    assert context.driver.find_elements_by_id("profile-edit") == []
