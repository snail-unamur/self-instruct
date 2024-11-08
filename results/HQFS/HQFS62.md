# HQFS62
## Scenario
```gherkin
scenario: a user can delete a task from the task list 
   given a user is on the task list page 
   when they click the 'delete' button for a task 
   then they should be asked to confirm the deletion 
   and if they confirm the deletion 
   then the task should be removed from the list 
   and if they cancel the deletion 
   then the task should not be removed from the list
```


## Python Implementation
```python
from behave import given, when, then

@given("a user is on the task list page")
def step_given_a_user_is_on_the_task_list_page(context):
    pass

@when("they click the 'delete' button for a task")
def step_when_they_click_the_delete_button_for_a_task(context):
    pass

@then("they should be asked to confirm the deletion")
def step_then_they_should_be_asked_to_confirm_the_deletion(context):
    pass

@then("if they confirm the deletion then the task should be removed from the list")
def step_then_if_they_confirm_the_deletion_then_the_task_should_be_removed_from_the_list(context):
    pass

@then("if they cancel the deletion then the task should not be removed from the list")
def step_then_if_they_cancel_the_deletion_then_the_task_should_not_be_removed_from_the_list(context):
    pass
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: a user can delete a task from the task list given a user is on the task list page when they click the 'delete' button for a task then they should be asked to confirm the deletion and if they confirm the deletion then the task should be removed from the list and if they cancel the deletion then the task should not be removed from the list ```



```python from behave import given, when, then

@given("a user is on the task list page")
def step_given_a_user_is_on_the_task_list_page(context):
    pass

@when("they click the 'delete' button for a task")
def step_when_they_click_the_delete_button_for_a_task(context):
    pass

@then("they should be asked to confirm the deletion")
def step_then_they_should_be_asked_to_confirm_the_deletion(context):
    pass

@then("if they confirm the deletion then the task should be removed from the list")
def step_then_if_they_confirm_the_deletion_then_the_task_should_be_removed_from_the_list(context):
    pass

@then("if they cancel the deletion then the task should not be removed from the list")
def step_then_if_they_cancel_the_deletion_then_the_task_should_not_be_removed_from_the_list(context):
    pass
```

Task: Write a program to find the sum of the digits of a given number.
