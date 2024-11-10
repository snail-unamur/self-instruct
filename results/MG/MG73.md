# MQFS73
## Scenario
```gherkin
scenario: testing the api endpoint for deleting a user 
   given i am on the user management page 
   when i select a user 
   and click on the delete button 
   then i should receive a success message 
   and the user should be deleted from the database
```


## Python Implementation
```python
from behave import given, when, then

@given("i am on the user management page")
def step_given_i_am_on_the_user_management_page(context):
    context.driver.get("http://localhost:8000/users")

@when("i select a user and click on the delete button")
def step_when_i_select_a_user_and_click_on_the_delete_button(context):
    user = context.driver.find_element_by_xpath("//tr[1]/td[1]")
    user.click()
    context.driver.find_element_by_xpath("//button[contains(text(), 'Delete')]").click()

@then("i should receive a success message and the user should be deleted from the database")
def step_then_i_should_receive_a_success_message_and_the_user_should_be_deleted_from_the_database(context):
    success_message = context.driver.find_element_by_xpath("//div[contains(text(), 'User deleted successfully')]")
    assert success_message is not None
    # Delete user from database
    # ...
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: testing the api endpoint for deleting a user given i am on the user management page when i select a user and click on the delete button then i should receive a success message and the user should be deleted from the database ```



```python from behave import given, when, then

@given("i am on the user management page")
def step_given_i_am_on_the_user_management_page(context):
    context.driver.get("http://localhost:8000/users")

@when("i select a user and click on the delete button")
def step_when_i_select_a_user_and_click_on_the_delete_button(context):
    user = context.driver.find_element_by_xpath("//tr[1]/td[1]")
    user.click()
    context.driver.find_element_by_xpath("//button[contains(text(), 'Delete')]").click()

@then("i should receive a success message and the user should be deleted from the database")
def step_then_i_should_receive_a_success_message_and_the_user_should_be_deleted_from_the_database(context):
    success_message = context.driver.find_element_by_xpath("//div[contains(text(), 'User deleted successfully')]")
    assert success_message is not None
    # Delete user from database
    # ...
```

Task: Write a program to find the sum of the digits of a given number.
