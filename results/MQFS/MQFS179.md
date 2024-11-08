# MQFS179
## Scenario
```gherkin
scenario: user can add a new task 
   given a user is logged in 
   when they navigate to the task creation page 
   then they should see a form to add a new task with fields for: - task name - task description - task due date - task priority 
   when they fill out the form 
   and submit it 
   then they should be taken to the task list page 
   and they should see their new task listed
```


## Python Implementation
```python
from behave import given, when, then

@given("a user is logged in")
def step_impl(context):
    pass

@when("they navigate to the task creation page")
def step_impl(context):
    pass

@then("they should see a form to add a new task with fields for:")
def step_impl(context):
    assert context.browser.find_element_by_name("task_name")
    assert context.browser.find_element_by_name("task_description")
    assert context.browser.find_element_by_name("task_due_date")
    assert context.browser.find_element_by_name("task_priority")

@when("they fill out the form and submit it")
def step_impl(context):
    context.browser.find_element_by_name("task_name").send_keys("Test Task")
    context.browser.find_element_by_name("task_description").send_keys("Test Description")
    context.browser.find_element_by_name("task_due_date").send_keys("2023-01-01")
    context.browser.find_element_by_name("task_priority").send_keys("High")
    context.browser.find_element_by_name("submit").click()

@then("they should be taken to the task list page")
def step_impl(context):
    assert context.browser.current_url == "http://localhost:8000/tasks/"

@then("they should see their new task listed")
def step_impl(context):
    assert context.browser.find_element_by_link_text("Test Task")
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: user can add a new task given a user is logged in when they navigate to the task creation page then they should see a form to add a new task with fields for: - task name - task description - task due date - task priority when they fill out the form and submit it then they should be taken to the task list page and they should see their new task listed ```



```python from behave import given, when, then

@given("a user is logged in")
def step_impl(context):
    pass

@when("they navigate to the task creation page")
def step_impl(context):
    pass

@then("they should see a form to add a new task with fields for:")
def step_impl(context):
    assert context.browser.find_element_by_name("task_name")
    assert context.browser.find_element_by_name("task_description")
    assert context.browser.find_element_by_name("task_due_date")
    assert context.browser.find_element_by_name("task_priority")

@when("they fill out the form and submit it")
def step_impl(context):
    context.browser.find_element_by_name("task_name").send_keys("Test Task")
    context.browser.find_element_by_name("task_description").send_keys("Test Description")
    context.browser.find_element_by_name("task_due_date").send_keys("2023-01-01")
    context.browser.find_element_by_name("task_priority").send_keys("High")
    context.browser.find_element_by_name("submit").click()

@then("they should be taken to the task list page")
def step_impl(context):
    assert context.browser.current_url == "http://localhost:8000/tasks/"

@then("they should see their new task listed")
def step_impl(context):
    assert context.browser.find_element_by_link_text("Test Task")
```

Task: Write a program to find the sum of the digits of a given number.
