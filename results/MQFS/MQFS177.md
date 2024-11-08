# MQFS177
## Scenario
```gherkin
scenario: a user edits their account information 
   given i am on the "account information" page 
   when i change my name to "john smith" 
   and i change my email to "johnsmith@example.com" 
   and i click the "save changes" button 
   then i should be taken back to the dashboard page 
   and i should see my updated name "john smith" 
   and i should see my updated email "johnsmith@example.com"
```


## Python Implementation
```python
from behave import given, when, then

@given("i am on the 'account information' page")
def step_impl(context):
    context.browser.get("https://www.example.com/account-information")

@when("i change my name to 'john smith'")
def step_impl(context):
    name_field = context.browser.find_element_by_name("name")
    name_field.clear()
    name_field.send_keys("john smith")

@when("i change my email to 'johnsmith@example.com'")
def step_impl(context):
    email_field = context.browser.find_element_by_name("email")
    email_field.clear()
    email_field.send_keys("johnsmith@example.com")

@when("i click the 'save changes' button")
def step_impl(context):
    save_changes_button = context.browser.find_element_by_name("save-changes")
    save_changes_button.click()

@then("i should be taken back to the dashboard page")
def step_impl(context):
    assert context.browser.current_url == "https://www.example.com/dashboard"

@then("i should see my updated name 'john smith'")
def step_impl(context):
    assert context.browser.find_element_by_name("name").get_attribute("value") == "john smith"

@then("i should see my updated email 'johnsmith@example.com'")
def step_impl(context):
    assert context.browser.find_element_by_name("email").get_attribute("value") == "johnsmith@example.com"
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: a user edits their account information given i am on the "account information" page when i change my name to "john smith" and i change my email to "johnsmith@example.com" and i click the "save changes" button then i should be taken back to the dashboard page and i should see my updated name "john smith" and i should see my updated email "johnsmith@example.com" ```



```python from behave import given, when, then

@given("i am on the 'account information' page")
def step_impl(context):
    context.browser.get("https://www.example.com/account-information")

@when("i change my name to 'john smith'")
def step_impl(context):
    name_field = context.browser.find_element_by_name("name")
    name_field.clear()
    name_field.send_keys("john smith")

@when("i change my email to 'johnsmith@example.com'")
def step_impl(context):
    email_field = context.browser.find_element_by_name("email")
    email_field.clear()
    email_field.send_keys("johnsmith@example.com")

@when("i click the 'save changes' button")
def step_impl(context):
    save_changes_button = context.browser.find_element_by_name("save-changes")
    save_changes_button.click()

@then("i should be taken back to the dashboard page")
def step_impl(context):
    assert context.browser.current_url == "https://www.example.com/dashboard"

@then("i should see my updated name 'john smith'")
def step_impl(context):
    assert context.browser.find_element_by_name("name").get_attribute("value") == "john smith"

@then("i should see my updated email 'johnsmith@example.com'")
def step_impl(context):
    assert context.browser.find_element_by_name("email").get_attribute("value") == "johnsmith@example.com"
```

Task: Write a program to find the sum of the digits of a given number.
