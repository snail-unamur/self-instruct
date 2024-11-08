# HQFS196
## Scenario
```gherkin
scenario: user is able to edit a task 
   given user is on the task page 
   when user clicks on the edit button 
   then user is able to see the task in edit mode 
   and user is able to edit the task 
   and user is able to save the task 
   and user is able to see the updated task on the task page
```


## Python Implementation
```python
from behave import given, when, then

@given("user is on the task page")
def step_given_user_is_on_the_task_page(context):
    pass

@when("user clicks on the edit button")
def step_when_user_clicks_on_the_edit_button(context):
    pass

@then("user is able to see the task in edit mode")
def step_then_user_is_able_to_see_the_task_in_edit_mode(context):
    pass

@then("user is able to edit the task")
def step_then_user_is_able_to_edit_the_task(context):
    pass

@then("user is able to save the task")
def step_then_user_is_able_to_save_the_task(context):
    pass

@then("user is able to see the updated task on the task page")
def step_then_user_is_able_to_see_the_updated_task_on_the_task_page(context):
    pass
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: user is able to edit a task given user is on the task page when user clicks on the edit button then user is able to see the task in edit mode and user is able to edit the task and user is able to save the task and user is able to see the updated task on the task page ```



```python from behave import given, when, then

@given("user is on the task page")
def step_given_user_is_on_the_task_page(context):
    pass

@when("user clicks on the edit button")
def step_when_user_clicks_on_the_edit_button(context):
    pass

@then("user is able to see the task in edit mode")
def step_then_user_is_able_to_see_the_task_in_edit_mode(context):
    pass

@then("user is able to edit the task")
def step_then_user_is_able_to_edit_the_task(context):
    pass

@then("user is able to save the task")
def step_then_user_is_able_to_save_the_task(context):
    pass

@then("user is able to see the updated task on the task page")
def step_then_user_is_able_to_see_the_updated_task_on_the_task_page(context):
    pass
```

Task: Write a program to find the sum of the digits of a given number.
