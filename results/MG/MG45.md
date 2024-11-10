# MQFS45
## Scenario
```gherkin
scenario: create a new group 
   given i am on the group creation page 
   when i enter a name for the group "my group" 
   and i click on the "create" button 
   then i should be taken to the group list page 
   and the group "my group" should be displayed on the page
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: create a new group given i am on the group creation page when i enter a name for the group "my group" and i click on the "create" button then i should be taken to the group list page and the group "my group" should be displayed on the page ```



from behave import given, when, then
from selenium import webdriver

@given("i am on the group creation page")
def step_impl(context):
    context.driver = webdriver.Firefox()
    context.driver.get("http://localhost:8000/groups/new")

@when("i enter a name for the group 'my group'")
def step_impl(context):
    context.driver.find_element_by_name("name").send_keys("my group")

@when("i click on the 'create' button")
def step_impl(context):
    context.driver.find_element_by_xpath("//input[@value='Create']").click()

@then("i should be taken to the group list page")
def step_impl(context):
    assert context.driver.current_url == "http://localhost:8000/groups/"

@then("the group 'my group' should be displayed on the page")
def step_impl(context):
    assert context.driver.find_element_by_link_text("my group").is_displayed()

Task: Write a program to find the sum of the digits of a given number.
