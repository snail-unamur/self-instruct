# MQFS82
## Scenario
```gherkin
scenario: testing the edit functionality 
   given a list of items 
   when the user selects an item 
   and clicks edit 
   then the user should be taken to the edit page for that item where the user can make changes to the item 
   and save the changes 
   then the user should be taken back to the list of items 
   and the changes should be reflected in the list
```


## Python Implementation
```python
from behave import given, when, then

@given("a list of items")
def step_given_a_list_of_items(context):
    context.items = ["item1", "item2", "item3"]

@when("the user selects an item and clicks edit")
def step_when_the_user_selects_an_item_and_clicks_edit(context):
    context.selected_item = context.items[0]
    context.edit_page = EditPage(context.selected_item)

@then("the user should be taken to the edit page for that item")
def step_then_the_user_should_be_taken_to_the_edit_page_for_that_item(context):
    assert context.edit_page.on_page()

@when("the user makes changes to the item and saves the changes")
def step_when_the_user_makes_changes_to_the_item_and_saves_the_changes(context):
    context.edited_item = context.edit_page.edit("edited item")

@then("the user should be taken back to the list of items")
def step_then_the_user_should_be_taken_back_to_the_list_of_items(context):
    context.list_page = ListPage()
    assert context.list_page.on_page()

@then("the changes should be reflected in the list")
def step_then_the_changes_should_be_reflected_in_the_list(context):
    assert context.edited_item in context.list_page.items
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: testing the edit functionality given a list of items when the user selects an item and clicks edit then the user should be taken to the edit page for that item where the user can make changes to the item and save the changes then the user should be taken back to the list of items and the changes should be reflected in the list ```



```python from behave import given, when, then

@given("a list of items")
def step_given_a_list_of_items(context):
    context.items = ["item1", "item2", "item3"]

@when("the user selects an item and clicks edit")
def step_when_the_user_selects_an_item_and_clicks_edit(context):
    context.selected_item = context.items[0]
    context.edit_page = EditPage(context.selected_item)

@then("the user should be taken to the edit page for that item")
def step_then_the_user_should_be_taken_to_the_edit_page_for_that_item(context):
    assert context.edit_page.on_page()

@when("the user makes changes to the item and saves the changes")
def step_when_the_user_makes_changes_to_the_item_and_saves_the_changes(context):
    context.edited_item = context.edit_page.edit("edited item")

@then("the user should be taken back to the list of items")
def step_then_the_user_should_be_taken_back_to_the_list_of_items(context):
    context.list_page = ListPage()
    assert context.list_page.on_page()

@then("the changes should be reflected in the list")
def step_then_the_changes_should_be_reflected_in_the_list(context):
    assert context.edited_item in context.list_page.items
```

Task: Write a program to find the sum of the digits of a number.
