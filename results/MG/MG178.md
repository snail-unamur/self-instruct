# MQFS178
## Scenario
```gherkin
scenario: add a new task to a project 
   given i am on the homepage 
   when i click on the "projects" button 
   and i click on the name of the project i want to add a task to 
   and i click on the "add task" button 
   and i enter a new task name 
   and i click on the "add" button 
   then i should be taken back to the project page 
   and i should see the new task displayed in the task list
```


## Python Implementation
```python
from behave import given, when, then

@given("i am on the homepage")
def step_impl(context):
    context.browser.get("http://localhost:8000")

@when("i click on the \"projects\" button")
def step_impl(context):
    context.browser.find_element_by_id("projects_button").click()

@when("i click on the name of the project i want to add a task to")
def step_impl(context):
    context.browser.find_element_by_xpath("//a[contains(text(),'Project Name')]").click()

@when("i click on the \"add task\" button")
def step_impl(context):
    context.browser.find_element_by_id("add_task_button").click()

@when("i enter a new task name")
def step_impl(context):
    context.browser.find_element_by_id("task_name").send_keys("New Task")

@when("i click on the \"add\" button")
def step_impl(context):
    context.browser.find_element_by_id("add_button").click()

@then("i should be taken back to the project page")
def step_impl(context):
    assert context.browser.current_url == "http://localhost:8000/project/Project Name"

@then("i should see the new task displayed in the task list")
def step_impl(context):
    assert "New Task" in context.browser.find_element_by_id("task_list").text
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: add a new task to a project given i am on the homepage when i click on the "projects" button and i click on the name of the project i want to add a task to and i click on the "add task" button and i enter a new task name and i click on the "add" button then i should be taken back to the project page and i should see the new task displayed in the task list ```



```python from behave import given, when, then

@given("i am on the homepage")
def step_impl(context):
    context.browser.get("http://localhost:8000")

@when("i click on the \"projects\" button")
def step_impl(context):
    context.browser.find_element_by_id("projects_button").click()

@when("i click on the name of the project i want to add a task to")
def step_impl(context):
    context.browser.find_element_by_xpath("//a[contains(text(),'Project Name')]").click()

@when("i click on the \"add task\" button")
def step_impl(context):
    context.browser.find_element_by_id("add_task_button").click()

@when("i enter a new task name")
def step_impl(context):
    context.browser.find_element_by_id("task_name").send_keys("New Task")

@when("i click on the \"add\" button")
def step_impl(context):
    context.browser.find_element_by_id("add_button").click()

@then("i should be taken back to the project page")
def step_impl(context):
    assert context.browser.current_url == "http://localhost:8000/project/Project Name"

@then("i should see the new task displayed in the task list")
def step_impl(context):
    assert "New Task" in context.browser.find_element_by_id("task_list").text
```

Task: Write a program to find the sum of the digits of a given number.
