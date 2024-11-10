# HQFS213
## Scenario
```gherkin
scenario: user can add a new task to the board 
   given user is on the board page 
   when user clicks on the "add task" button 
   then user is able to input the task name, description, 
   and assignee 
   and user clicks on the "save" button 
   then the new task is added to the board 
   and the task is displayed on the board
```


## Python Implementation
```python
from behave import given, when, then

@given("user is on the board page")
def step_given_user_is_on_the_board_page(context):
    pass

@when("user clicks on the 'add task' button")
def step_when_user_clicks_on_the_add_task_button(context):
    pass

@then("user is able to input the task name, description, and assignee")
def step_then_user_is_able_to_input_the_task_name_description_and_assignee(context):
    pass

@when("user clicks on the 'save' button")
def step_when_user_clicks_on_the_save_button(context):
    pass

@then("the new task is added to the board")
def step_then_the_new_task_is_added_to_the_board(context):
    pass

@then("the task is displayed on the board")
def step_then_the_task_is_displayed_on_the_board(context):
    pass
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: user can add a new task to the board given user is on the board page when user clicks on the "add task" button then user is able to input the task name, description, and assignee and user clicks on the "save" button then the new task is added to the board and the task is displayed on the board ```



```python from behave import given, when, then

@given("user is on the board page")
def step_given_user_is_on_the_board_page(context):
    pass

@when("user clicks on the 'add task' button")
def step_when_user_clicks_on_the_add_task_button(context):
    pass

@then("user is able to input the task name, description, and assignee")
def step_then_user_is_able_to_input_the_task_name_description_and_assignee(context):
    pass

@when("user clicks on the 'save' button")
def step_when_user_clicks_on_the_save_button(context):
    pass

@then("the new task is added to the board")
def step_then_the_new_task_is_added_to_the_board(context):
    pass

@then("the task is displayed on the board")
def step_then_the_task_is_displayed_on_the_board(context):
    pass
```

Task: Write a program to find the sum of the digits of a number.
