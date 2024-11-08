# MQFS137
## Scenario
```gherkin
scenario: a user can view the details of a todo item 
   given edith has opened a browser 
   when edith starts a new todo list 
   then she notices that her list has a unique url 
   when she clicks on a todo item 
   then she should see the todo item details page 
   and she should see the todo item title 
   and she should see the todo item description 
   and she should see the todo item due date 
   and she should see the todo item priority 
   and she should see the todo item status 
   and she should see the todo item tag
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: a user can view the details of a todo item given edith has opened a browser when edith starts a new todo list then she notices that her list has a unique url when she clicks on a todo item then she should see the todo item details page and she should see the todo item title and she should see the todo item description and she should see the todo item due date and she should see the todo item priority and she should see the todo item status and she should see the todo item tag ```



```python from behave import given, when, then

@given("edith has opened a browser")
def step_given_edith_has_opened_a_browser(context):
    context.browser = Browser()

@given("edith starts a new todo list")
def step_given_edith_starts_a_new_todo_list(context):
    context.todo_list = context.browser.create_new_todo_list()

@when("edith clicks on a todo item")
def step_when_edith_clicks_on_a_todo_item(context):
    context.todo_item = context.todo_list.get_random_todo_item()
    context.todo_item_details_page = context.todo_item.view_details()

@then("she should see the todo item details page")
def step_then_she_should_see_the_todo_item_details_page(context):
    assert context.todo_item_details_page.is_the_current_page()

@then("she should see the todo item title")
def step_then_she_should_see_the_todo_item_title(context):
    assert context.todo_item_details_page.title_is_displayed(context.todo_item.title)

@then("she should see the todo item description")
def step_then_she_should_see_the_todo_item_description(context):
    assert context.todo_item_details_page.description_is_displayed(context.todo_item.description)

@then("she should see the todo item due date")
def step_then_she_should_see_the_todo_item_due_date(context):
    assert context.todo_item_details_page.due_date_is_displayed(context.todo_item.due_date)

@then("she should see the todo item priority")
def step_then_she_should_see_the_todo_item_priority(context):
    assert context.todo_item
