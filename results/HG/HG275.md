# HQFS275
## Scenario
```gherkin
None
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: editing account information given i am logged in to my account when i go to the 'account information' page and i edit my information and i click the 'save changes'

button then my account information should be updated

from behave import given, when, then

@given("i am logged in to my account")
def step_impl(context):
    context.browser.get("https://www.example.com/login")
    context.browser.find_element_by_name("username").send_keys("testuser")
    context.browser.find_element_by_name("password").send_keys("testpassword")
    context.browser.find_element_by_xpath("//button[@type='submit']").click()

@when("i go to the 'account information' page")
def step_impl(context):
    context.browser.get("https://www.example.com/account-information")

@when("i edit my information")
def step_impl(context):
    context.browser.find_element_by_name("first_name").clear()
    context.browser.find_element_by_name("first_name").send_keys("NewFirstName")
    context.browser.find_element_by_name("last_name").clear()
    context.browser.find_element_by_name("last_name").send_keys("NewLastName")

@when("i click the 'save changes' button")
def step_impl(context):
    context.browser.find_element_by_xpath("//button[@type='submit']").click()

@then("my account information should be updated")
def step_impl(context):
    first_name = context.browser.find_element_by_name("first_name").get_attribute("value")
    last_name = context.browser.find_element_by_name("last_name").get_attribute("value")
    assert first_name == "NewFirstName"
    assert last_name == "NewLastName"
