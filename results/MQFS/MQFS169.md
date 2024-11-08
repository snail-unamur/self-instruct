# MQFS169
## Scenario
```gherkin
scenario: user can mark an item as done 
   given edith has opened a browser 
   when edith starts a new todo list 
   then she notices that her list has a unique url 
   given edith has opened a browser 
   when edith visits her todo list 
   then she sees the empty list 
   when edith adds an item to the list 
   then the list should contain that item 
   when edith marks an item as done 
   then the item should be marked as done
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: user can mark an item as done given edith has opened a browser when edith starts a new todo list then she notices that her list has a unique url given edith has opened a browser when edith visits her todo list then she sees the empty list when edith adds an item to the list then the list should contain that item when edith marks an item as done then the item should be marked as done ```



```python from behave import given, when, then

@given("edith has opened a browser")
def step_given_edith_has_opened_a_browser(context):
    context.browser = Browser()

@when("edith starts a new todo list")
def step_when_edith_starts_a_new_todo_list(context):
    context.todo_list = context.browser.visit("http://localhost:8000")

@then("she notices that her list has a unique url")
def step_then_she_notices_that_her_list_has_a_unique_url(context):
    assert context.todo_list.url is not None

@given("edith has opened a browser")
def step_given_edith_has_opened_a_browser(context):
    context.browser = Browser()

@when("edith starts a new todo list")
def step_when_edith_starts_a_new_todo_list(context):
    context.todo_list = context.browser.visit("http://localhost:8000")

@then("she notices that her list has a unique url")
def step_then_she_notices_that_her_list_has_a_unique_url(context):
    assert context.todo_list.url is not None

@when("edith visits her todo list")
def step_when_edith_visits_her_todo_list(context):
    context.todo_list = context.browser.visit(context.todo_list.url)

@then("she sees the empty list")
def step_then_she_sees_the_empty_list(context):
    assert context.todo_list.is_empty

@when("edith adds an item to the list")
def step_when_edith_adds_an_item_to_the_list(context):
    context.todo_list.add("Buy milk")

@then("the list should contain that item")
def step_then_the_list_should_contain_
