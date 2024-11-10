# MQFS230
## Scenario
```gherkin
None
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: a user can view the details of a todo item given edith has opened a browser when edith starts a new todo list then she notices that her list has a unique url when

edith clicks on a todo item then she is taken to the details page of that todo item when
edith clicks the back button then she is taken back to her todo list

from behave import given, when, then

@given("edith has opened a browser")
def step(context):
    context.browser = Browser()

@given("edith starts a new todo list")
def step(context):
    context.todo_list = context.browser.visit(TodoListPage)

@then("she notices that her list has a unique url")
def step(context):
    assert context.todo_list.url != TodoListPage.url

@when("edith clicks on a todo item")
def step(context):
    todo_item = context.todo_list.get_first_todo_item()
    context.todo_details = todo_item.click_on_details()

@then("she is taken to the details page of that todo item")
def step(context):
    assert context.todo_details.page_title == TodoDetailsPage.page_title

@when("edith clicks the back button")
def step(context):
    context.browser.back()

@then("she is taken back to her todo list")
def step(context):
    assert context.browser.current_page == context.todo_list.page_title

Task: Write a program to find the sum of the digits of a number.
