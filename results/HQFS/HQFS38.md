# HQFS38
## Scenario
```gherkin
scenario: user can add a new task 
   given the user is on the task list page 
   when the user clicks the "add task" button 
   then the user should see the "add task" page 
   and the user should be able to enter a new task description 
   and the user should be able to enter a new task priority 
   and the user should be able to enter a new task due date 
   and the user should be able to save the new task 
   then the new task should be added to the task list 
   and the user should be redirected to the task list page
```


## Python Implementation
```python
from behave import given, when, then

@given("the user is on the task list page")
def step_given_the_user_is_on_the_task_list_page(context):
    pass

@when("the user clicks the 'add task' button")
def step_when_the_user_clicks_the_add_task_button(context):
    pass

@then("the user should see the 'add task' page")
def step_then_the_user_should_see_the_add_task_page(context):
    pass

@then("the user should be able to enter a new task description")
def step_then_the_user_should_be_able_to_enter_a_new_task_description(context):
    pass

@then("the user should be able to enter a new task priority")
def step_then_the_user_should_be_able_to_enter_a_new_task_priority(context):
    pass

@then("the user should be able to enter a new task due date")
def step_then_the_user_should_be_able_to_enter_a_new_task_due_date(context):
    pass

@then("the user should be able to save the new task")
def step_then_the_user_should_be_able_to_save_the_new_task(context):
    pass

@then("the new task should be added to the task list")
def step_then_the_new_task_should_be_added_to_the_task_list(context):
    pass

@then("the user should be redirected to the task list page")
def step_then_the_user_should_be_redirected_to_the_task_list_page(context):
    pass
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: user can add a new task given the user is on the task list page when the user clicks the "add task" button then the user should see the "add task" page and the user should be able to enter a new task description and the user should be able to enter a new task priority and the user should be able to enter a new task due date and the user should be able to save the new task then the new task should be added to the task list and the user should be redirected to the task list page ```



```python from behave import given, when, then

@given("the user is on the task list page")
def step_given_the_user_is_on_the_task_list_page(context):
    pass

@when("the user clicks the 'add task' button")
def step_when_the_user_clicks_the_add_task_button(context):
    pass

@then("the user should see the 'add task' page")
def step_then_the_user_should_see_the_add_task_page(context):
    pass

@then("the user should be able to enter a new task description")
def step_then_the_user_should_be_able_to_enter_a_new_task_description(context):
    pass

@then("the user should be able to enter a new task priority")
def step_then_the_user_should_be_able_to_enter_a_new_task_priority(context):
    pass

@then("the user should be able to enter a new task due date")
def step_then_the_user_should_be_able_to_enter_a_new_task_due_date(context):
    pass

@then("the user should be able to save the new task")
def step_then_the_user_should_be_able_to_save_the_new_task(context):
    pass

@then("the new task should be added to the task list")
def step_then_the_new_task_should_be_added_to_the_task_list(context):
    pass

@then("the user should be redirected to the task list page")
def step_then_the_user_should_be_redirected_to_the_task_list_page(context):
    pass
```

Task: Write a program to find the second largest number in a list.
