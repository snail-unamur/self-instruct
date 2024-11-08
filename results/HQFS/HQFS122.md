# HQFS122
## Scenario
```gherkin
scenario: a user can edit their personal information 
   given i am logged in 
   and i am on my profile page 
   when i update my personal information 
   then i should see the updated information 
   and i should receive a confirmation message
```


## Python Implementation
```python
from behave import given, when, then

@given("i am logged in and i am on my profile page")
def step_impl(context):
    context.browser.get("http://localhost:8000/profile")
    context.browser.find_element_by_name("username").send_keys("testuser")
    context.browser.find_element_by_name("password").send_keys("testpassword")
    context.browser.find_element_by_xpath("//button[@type='submit']").click()

@when("i update my personal information")
def step_impl(context):
    context.browser.find_element_by_name("first_name").clear()
    context.browser.find_element_by_name("first_name").send_keys("New")
    context.browser.find_element_by_name("last_name").clear()
    context.browser.find_element_by_name("last_name").send_keys("Name")
    context.browser.find_element_by_xpath("//button[@type='submit']").click()

@then("i should see the updated information and i should receive a confirmation message")
def step_impl(context):
    updated_first_name = context.browser.find_element_by_name("first_name").get_attribute("value")
    updated_last_name = context.browser.find_element_by_name("last_name").get_attribute("value")
    assert updated_first_name == "New"
    assert updated_last_name == "Name"
    confirmation_message = context.browser.find_element_by_class_name("confirmation-message").text
    assert confirmation_message == "Your personal information has been updated."
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: a user can edit their personal information given i am logged in and i am on my profile page when i update my personal information then i should see the updated information and i should receive a confirmation message ```



```python from behave import given, when, then

@given("i am logged in and i am on my profile page")
def step_impl(context):
    context.browser.get("http://localhost:8000/profile")
    context.browser.find_element_by_name("username").send_keys("testuser")
    context.browser.find_element_by_name("password").send_keys("testpassword")
    context.browser.find_element_by_xpath("//button[@type='submit']").click()

@when("i update my personal information")
def step_impl(context):
    context.browser.find_element_by_name("first_name").clear()
    context.browser.find_element_by_name("first_name").send_keys("New")
    context.browser.find_element_by_name("last_name").clear()
    context.browser.find_element_by_name("last_name").send_keys("Name")
    context.browser.find_element_by_xpath("//button[@type='submit']").click()

@then("i should see the updated information and i should receive a confirmation message")
def step_impl(context):
    updated_first_name = context.browser.find_element_by_name("first_name").get_attribute("value")
    updated_last_name = context.browser.find_element_by_name("last_name").get_attribute("value")
    assert updated_first_name == "New"
    assert updated_last_name == "Name"
    confirmation_message = context.browser.find_element_by_class_name("confirmation-message").text
    assert confirmation_message == "Your personal information has been updated."
```

Task: Write a program to find the sum of the digits of a given number.
