# MQFS209
## Scenario
```gherkin
scenario: i can delete a user 
   given i am on the "view users" page 
   when i click on the "delete" button next to the user i want to delete 
   then the user is deleted 
   and i am taken back to the "view users" page
```


## Python Implementation
```python
from behave import given, when, then

@given("i am on the 'view users' page")
def step_given_i_am_on_the_view_users_page(context):
    context.browser.get(context.base_url + "/users")

@when("i click on the 'delete' button next to the user i want to delete")
def step_when_i_click_on_the_delete_button_next_to_the_user_i_want_to_delete(context):
    user = context.execute_steps("then the first user is selected")
    delete_button = context.browser.find_element_by_id(f"delete-{user['id']}")
    delete_button.click()

@then("the user is deleted and i am taken back to the 'view users' page")
def step_then_the_user_is_deleted_and_i_am_taken_back_to_the_view_users_page(context):
    context.browser.find_element_by_id("flash")
    context.browser.find_element_by_link_text("view users")
    context.browser.find_element_by_link_text("view users").click()
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: i can delete a user given i am on the "view users" page when i click on the "delete" button next to the user i want to delete then the user is deleted and i am taken back to the "view users" page ```



```python from behave import given, when, then

@given("i am on the 'view users' page")
def step_given_i_am_on_the_view_users_page(context):
    context.browser.get(context.base_url + "/users")

@when("i click on the 'delete' button next to the user i want to delete")
def step_when_i_click_on_the_delete_button_next_to_the_user_i_want_to_delete(context):
    user = context.execute_steps("then the first user is selected")
    delete_button = context.browser.find_element_by_id(f"delete-{user['id']}")
    delete_button.click()

@then("the user is deleted and i am taken back to the 'view users' page")
def step_then_the_user_is_deleted_and_i_am_taken_back_to_the_view_users_page(context):
    context.browser.find_element_by_id("flash")
    context.browser.find_element_by_link_text("view users")
    context.browser.find_element_by_link_text("view users").click()
```

Task: Write a program to find the sum of the digits of a number.
