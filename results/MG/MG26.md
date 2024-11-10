# MQFS26
## Scenario
```gherkin
scenario: a user can delete a task from the task list 
   given a user is on the task list page 
   and the user clicks on the 'delete' button for a specific task 
   then the user is prompted to confirm the deletion 
   when the user confirms the deletion 
   then the task is removed from the task list 
   when the user clicks on the 'cancel' button 
   then the user is redirected to the task list page 
   and the task is still displayed on the list
```


## Python Implementation
```python
from behave import given, when, then

@given("a user is on the task list page")
def step_given_a_user_is_on_the_task_list_page(context):
    pass

@when("the user clicks on the 'delete' button for a specific task")
def step_when_the_user_clicks_on_the_delete_button_for_a_specific_task(context):
    pass

@then("the user is prompted to confirm the deletion")
def step_then_the_user_is_prompted_to_confirm_the_deletion(context):
    pass

@when("the user confirms the deletion")
def step_when_the_user_confirms_the_deletion(context):
    pass

@then("the task is removed from the task list")
def step_then_the_task_is_removed_from_the_task_list(context):
    pass

@when("the user clicks on the 'cancel' button")
def step_when_the_user_clicks_on_the_cancel_button(context):
    pass

@then("the user is redirected to the task list page")
def step_then_the_user_is_redirected_to_the_task_list_page(context):
    pass

@then("the task is still displayed on the list")
def step_then_the_task_is_still_displayed_on_the_list(context):
    pass
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: a user can delete a task from the task list given a user is on the task list page and the user clicks on the 'delete' button for a specific task then the user is prompted to confirm the deletion when the user confirms the deletion then the task is removed from the task list when the user clicks on the 'cancel' button then the user is redirected to the task list page and the task is still displayed on the list ```



```python from behave import given, when, then

@given("a user is on the task list page")
def step_given_a_user_is_on_the_task_list_page(context):
    pass

@when("the user clicks on the 'delete' button for a specific task")
def step_when_the_user_clicks_on_the_delete_button_for_a_specific_task(context):
    pass

@then("the user is prompted to confirm the deletion")
def step_then_the_user_is_prompted_to_confirm_the_deletion(context):
    pass

@when("the user confirms the deletion")
def step_when_the_user_confirms_the_deletion(context):
    pass

@then("the task is removed from the task list")
def step_then_the_task_is_removed_from_the_task_list(context):
    pass

@when("the user clicks on the 'cancel' button")
def step_when_the_user_clicks_on_the_cancel_button(context):
    pass

@then("the user is redirected to the task list page")
def step_then_the_user_is_redirected_to_the_task_list_page(context):
    pass

@then("the task is still displayed on the list")
def step_then_the_task_is_still_displayed_on_the_list(context):
    pass
```

Task: Write a program to find the sum of the digits of a given number.
