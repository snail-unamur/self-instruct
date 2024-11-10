# MQFS236
## Scenario
```gherkin
scenario: a user can edit a task in a project 
   given i am on the task's details page for "my task" 
   when i click the "edit" button 
   then i should be taken to the edit task form with fields for the task's title, description, due date, priority, status, 
   and tags 
   when i update the task's information 
   then the task's information should be updated 
   and i should be redirected back to the task's details page
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: a user can edit a task in a project given i am on the task's details page for "my task" when i click the "edit" button then i should be taken to the edit task form with fields for the task's title, description, due date, priority, status, and tags when i update the task's information then the task's information should be updated and i should be redirected back to the task's details page ```



```python from behave import given, when, then

@given("i am on the task's details page for 'my task'")
def step_impl(context):
    context.browser.visit(context.get_url("task_details", task_id="my_task"))

@when("i click the 'edit' button")
def step_impl(context):
    context.browser.click("edit_task_button")

@then("i should be taken to the edit task form with fields for the task's title, description, due date, priority, status, and tags")
def step_impl(context):
    assert context.browser.is_text_present("Edit Task")
    assert context.browser.is_text_present("Title:")
    assert context.browser.is_text_present("Description:")
    assert context.browser.is_text_present("Due Date:")
    assert context.browser.is_text_present("Priority:")
    assert context.browser.is_text_present("Status:")
    assert context.browser.is_text_present("Tags:")

@when("i update the task's information")
def step_impl(context):
    context.browser.fill("title_field", "New Task Title")
    context.browser.fill("description_field", "New Task Description")
    context.browser.fill("due_date_field", "2023-01-01")
    context.browser.fill("priority_field", "High")
    context.browser.fill("status_field", "In Progress")
    context.browser.fill("tags_field", "new_tag1, new_tag2")
    context.browser.click("update_task_button")

@then("the task's information should be updated and i should be redirected back to the task's details page")
def step_impl(context):
    assert context.browser.is_text_present("Task Updated")
    assert context.browser.is_text_present("New Task Title")
    assert context.browser.is_text_present("New Task Description")
    assert context.browser.is_text_present("01/01
