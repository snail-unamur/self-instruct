# HQFS52
## Scenario
```gherkin
scenario: user wants to delete a task 
   given i am on the task list page 
   and there is a task with the title "test task" 
   when i click on the delete button for the "test task" 
   then the task should be deleted 
   and i should be redirected to the task list page
```


## Python Implementation
```python
from behave import given, when, then

@given("i am on the task list page")
def step_given_i_am_on_the_task_list_page(context):
    context.driver.get("http://localhost:3000/tasks")

@given("there is a task with the title 'test task'")
def step_given_there_is_a_task_with_the_title_test_task(context):
    context.task = context.task_manager.create_task("test task")

@when("i click on the delete button for the 'test task'")
def step_when_i_click_on_the_delete_button_for_the_test_task(context):
    context.task_manager.delete_task(context.task)

@then("the task should be deleted and i should be redirected to the task list page")
def step_then_the_task_should_be_deleted_and_i_should_be_redirected_to_the_task_list_page(context):
    assert context.task not in context.task_manager.get_tasks()
    assert context.driver.current_url == "http://localhost:3000/tasks"
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: user wants to delete a task given i am on the task list page and there is a task with the title "test task" when i click on the delete button for the "test task" then the task should be deleted and i should be redirected to the task list page ```



```python from behave import given, when, then

@given("i am on the task list page")
def step_given_i_am_on_the_task_list_page(context):
    context.driver.get("http://localhost:3000/tasks")

@given("there is a task with the title 'test task'")
def step_given_there_is_a_task_with_the_title_test_task(context):
    context.task = context.task_manager.create_task("test task")

@when("i click on the delete button for the 'test task'")
def step_when_i_click_on_the_delete_button_for_the_test_task(context):
    context.task_manager.delete_task(context.task)

@then("the task should be deleted and i should be redirected to the task list page")
def step_then_the_task_should_be_deleted_and_i_should_be_redirected_to_the_task_list_page(context):
    assert context.task not in context.task_manager.get_tasks()
    assert context.driver.current_url == "http://localhost:3000/tasks"
```

Task: Write a program to find the sum of the digits of a given number.
