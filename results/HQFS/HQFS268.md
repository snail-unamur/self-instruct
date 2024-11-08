# HQFS268
## Scenario
```gherkin
scenario: user can view a list of all tasks in a project 
   given i am logged in as "kea@gmail.com" 
   when i go to the tasks page for project "kalibro" 
   then i see a list of all tasks in project "kalibro"
```


## Python Implementation
```python
from behave import given, when, then

@given("i am logged in as 'kea@gmail.com'")
def step_impl(context):
    context.browser.visit("http://project-kalibro.com/login")
    context.browser.fill("username", "kea@gmail.com")
    context.browser.fill("password", "password")
    context.browser.find_by_value("login").first.click()

@when("i go to the tasks page for project 'kalibro'")
def step_impl(context):
    context.browser.visit("http://project-kalibro.com/tasks")

@then("i see a list of all tasks in project 'kalibro'")
def step_impl(context):
    tasks = context.browser.find_by_css(".task")
    assert len(tasks) > 0
    for task in tasks:
        assert task.find_by_css(".project-name")[0].text == "kalibro"
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: user can view a list of all tasks in a project given i am logged in as "kea@gmail.com" when i go to the tasks page for project "kalibro" then i see a list of all tasks in project "kalibro" ```



```python from behave import given, when, then

@given("i am logged in as 'kea@gmail.com'")
def step_impl(context):
    context.browser.visit("http://project-kalibro.com/login")
    context.browser.fill("username", "kea@gmail.com")
    context.browser.fill("password", "password")
    context.browser.find_by_value("login").first.click()

@when("i go to the tasks page for project 'kalibro'")
def step_impl(context):
    context.browser.visit("http://project-kalibro.com/tasks")

@then("i see a list of all tasks in project 'kalibro'")
def step_impl(context):
    tasks = context.browser.find_by_css(".task")
    assert len(tasks) > 0
    for task in tasks:
        assert task.find_by_css(".project-name")[0].text == "kalibro"
```

Task: Write a program to find the sum of the digits of a number.
