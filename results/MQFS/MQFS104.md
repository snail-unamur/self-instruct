# MQFS104
## Scenario
```gherkin
scenario: testing the functionality of the delete account button 
   given i am on the user profile page 
   when i click the delete account button 
   then i should be taken to a confirmation page 
   and i should see a message asking if i am sure i want to delete my account 
   when i confirm that i want to delete my account 
   then i should be taken to the login page 
   and i should not see the user's name 
   and i should not see the user's email address
```


## Python Implementation
```python
from behave import given, when, then

@given("i am on the user profile page")
def step_impl(context):
    context.browser.get("http://localhost:3000/profile")

@when("i click the delete account button")
def step_impl(context):
    context.browser.find_element_by_id("delete-account-button").click()

@then("i should be taken to a confirmation page")
def step_impl(context):
    context.browser.find_element_by_id("confirmation-page")

@then("i should see a message asking if i am sure i want to delete my account")
def step_impl(context):
    context.browser.find_element_by_id("confirmation-message")

@when("i confirm that i want to delete my account")
def step_impl(context):
    context.browser.find_element_by_id("confirm-delete-button").click()

@then("i should be taken to the login page")
def step_impl(context):
    context.browser.find_element_by_id("login-page")

@then("i should not see the user's name")
def step_impl(context):
    assert context.browser.find_element_by_id("user-name").text == ""

@then("i should not see the user's email address")
def step_impl(context):
    assert context.browser.find_element_by_id("user-email").text == ""
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: testing the functionality of the delete account button given i am on the user profile page when i click the delete account button then i should be taken to a confirmation page and i should see a message asking if i am sure i want to delete my account when i confirm that i want to delete my account then i should be taken to the login page and i should not see the user's name and i should not see the user's email address ```



```python from behave import given, when, then

@given("i am on the user profile page")
def step_impl(context):
    context.browser.get("http://localhost:3000/profile")

@when("i click the delete account button")
def step_impl(context):
    context.browser.find_element_by_id("delete-account-button").click()

@then("i should be taken to a confirmation page")
def step_impl(context):
    context.browser.find_element_by_id("confirmation-page")

@then("i should see a message asking if i am sure i want to delete my account")
def step_impl(context):
    context.browser.find_element_by_id("confirmation-message")

@when("i confirm that i want to delete my account")
def step_impl(context):
    context.browser.find_element_by_id("confirm-delete-button").click()

@then("i should be taken to the login page")
def step_impl(context):
    context.browser.find_element_by_id("login-page")

@then("i should not see the user's name")
def step_impl(context):
    assert context.browser.find_element_by_id("user-name").text == ""

@then("i should not see the user's email address")
def step_impl(context):
    assert context.browser.find_element_by_id("user-email").text == ""
```

Task: Write a program to find the sum of the digits of a given number.
