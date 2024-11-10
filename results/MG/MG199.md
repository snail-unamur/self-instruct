# MQFS199
## Scenario
```gherkin
scenario: user can view a task's details 
   given i am on the project page for "my project" 
   and i have created a new task 
   when i click on the task's name 
   then i should see the task's details page 
   and i should see the task's name, description, due date, 
   and assignee 
   and i should be able to edit the task 
   and i should be able to delete the task 
   and i should be able to mark the task as complete 
   and i should be able to view the task's history
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: user can view a task's details given i am on the project page for "my project" and i have created a new task when i click on the task's name then i should see the task's details page and i should see the task's name, description, due date, and assignee and i should be able to edit the task and i should be able to delete the task and i should be able to mark the task as complete and i should be able to view the task's history ```



```python from behave import given, when, then

@given("i am on the project page for 'my project'")
def step_impl(context):
    context.browser.get("http://localhost:8000/projects/my-project")

@when("i have created a new task")
def step_impl(context):
    task_name = "Test Task"
    task_description = "This is a test task."
    due_date = "2023-03-01"
    assignee = "John Doe"
    context.browser.find_element_by_id("new_task_button").click()
    context.browser.find_element_by_id("task_name").send_keys(task_name)
    context.browser.find_element_by_id("task_description").send_keys(task_description)
    context.browser.find_element_by_id("task_due_date").send_keys(due_date)
    context.browser.find_element_by_id("task_assignee").send_keys(assignee)
    context.browser.find_element_by_id("create_task_button").click()

@then("i should see the task's details page")
def step_impl(context):
    assert context.browser.current_url == "http://localhost:8000/tasks/1"

@then("i should see the task's name, description, due date, and assignee")
def step_impl(context):
    task_name = "Test Task"
    task_description = "This is a test task."
    due_date = "2023-03-01"
    assignee = "John Doe"
    assert context.browser.find_element_by_id("task_name").get_attribute("value") == task_name
    assert context.browser.find_element_by_id("task_description").get_attribute("value") == task_description
    assert context.browser.find_element_by_id("task_due_date").get_attribute("value") == due_date
    assert context.browser
