# MQFS276
## Scenario
```gherkin
scenario: user can edit a user 
   given a list of users 
   when a user navigates to the user list page 
   and they select a user to edit 
   then they should see an edit form for the user 
   and they can edit the user's information 
   and save the changes 
   then the user's information should be updated in the list
```


## Python Implementation
```python
from behave import given, when, then

@given("a user navigates to the user list page")
def step_impl(context):
    context.browser.visit("http://localhost:8000/users")

@when("they select a user to edit")
def step_impl(context):
    user_row = context.browser.find_by_css("tr")[1]
    user_row.find_by_css("a.edit").first.click()

@then("they should see an edit form for the user")
def step_impl(context):
    context.browser.find_by_css("form#edit_user")

@when("they edit the user's information and save the changes")
def step_impl(context):
    edit_form = context.browser.find_by_css("form#edit_user")
    edit_form.find_by_name("name").first.fill("New Name")
    edit_form.find_by_name("email").first.fill("new@email.com")
    edit_form.find_by_css("input[type='submit']").first.click()

@then("the user's information should be updated in the list")
def step_impl(context):
    user_row = context.browser.find_by_css("tr")[1]
    assert user_row.find_by_css("td.name").first.text == "New Name"
    assert user_row.find_by_css("td.email").first.text == "new@email.com"
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: user can edit a user given a list of users when a user navigates to the user list page and they select a user to edit then they should see an edit form for the user and they can edit the user's information and save the changes then the user's information should be updated in the list ```



```python from behave import given, when, then

@given("a user navigates to the user list page")
def step_impl(context):
    context.browser.visit("http://localhost:8000/users")

@when("they select a user to edit")
def step_impl(context):
    user_row = context.browser.find_by_css("tr")[1]
    user_row.find_by_css("a.edit").first.click()

@then("they should see an edit form for the user")
def step_impl(context):
    context.browser.find_by_css("form#edit_user")

@when("they edit the user's information and save the changes")
def step_impl(context):
    edit_form = context.browser.find_by_css("form#edit_user")
    edit_form.find_by_name("name").first.fill("New Name")
    edit_form.find_by_name("email").first.fill("new@email.com")
    edit_form.find_by_css("input[type='submit']").first.click()

@then("the user's information should be updated in the list")
def step_impl(context):
    user_row = context.browser.find_by_css("tr")[1]
    assert user_row.find_by_css("td.name").first.text == "New Name"
    assert user_row.find_by_css("td.email").first.text == "new@email.com"
```

Task: Write a program to find the sum of the digits of a number.
