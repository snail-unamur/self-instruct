# MQFS187
## Scenario
```gherkin
scenario: adding a new user 
   given you are on the user management page 
   when you click on the "add user" button 
   then you are taken to the user creation page 
   when you enter the user's details 
   and click "create" 
   then the user as a result of the new user being added
```


## Python Implementation
```python
from behave import given, when, then

@given("you are on the user management page")
def step_given_you_are_on_the_user_management_page(context):
    context.browser.get("http://localhost:8000/users")

@when("you click on the 'add user' button")
def step_when_you_click_on_the_add_user_button(context):
    add_user_button = context.browser.find_element_by_id("add-user-button")
    add_user_button.click()

@then("you are taken to the user creation page")
def step_then_you_are_taken_to_the_user_creation_page(context):
    assert context.browser.current_url == "http://localhost:8000/users/create"

@when("you enter the user's details and click 'create'")
def step_when_you_enter_the_users_details_and_click_create(context):
    username_field = context.browser.find_element_by_name("username")
    username_field.send_keys("newuser")

    password_field = context.browser.find_element_by_name("password")
    password_field.send_keys("password")

    create_button = context.browser.find_element_by_id("create-button")
    create_button.click()

@then("the user as a result of the new user being added")
def step_then_the_user_as_a_result_of_the_new_user_being_added(context):
    assert "newuser" in context.browser.page_source
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: adding a new user given you are on the user management page when you click on the "add user" button then you are taken to the user creation page when you enter the user's details and click "create" then the user as a result of the new user being added ```



```python from behave import given, when, then

@given("you are on the user management page")
def step_given_you_are_on_the_user_management_page(context):
    context.browser.get("http://localhost:8000/users")

@when("you click on the 'add user' button")
def step_when_you_click_on_the_add_user_button(context):
    add_user_button = context.browser.find_element_by_id("add-user-button")
    add_user_button.click()

@then("you are taken to the user creation page")
def step_then_you_are_taken_to_the_user_creation_page(context):
    assert context.browser.current_url == "http://localhost:8000/users/create"

@when("you enter the user's details and click 'create'")
def step_when_you_enter_the_users_details_and_click_create(context):
    username_field = context.browser.find_element_by_name("username")
    username_field.send_keys("newuser")

    password_field = context.browser.find_element_by_name("password")
    password_field.send_keys("password")

    create_button = context.browser.find_element_by_id("create-button")
    create_button.click()

@then("the user as a result of the new user being added")
def step_then_the_user_as_a_result_of_the_new_user_being_added(context):
    assert "newuser" in context.browser.page_source
```

Task: Write a program to find the sum of the digits of a given number.
