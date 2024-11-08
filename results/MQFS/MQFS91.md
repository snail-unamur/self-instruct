# MQFS91
## Scenario
```gherkin
scenario: testing the delete functionality 
   given the user is on the list page 
   when the user clicks on the delete button 
   then the item should be deleted from the list 
   when the user clicks on the delete button for an item that does not exist 
   then an error message should be displayed
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: testing the delete functionality given the user is on the list page when the user clicks on the delete button then the item should be deleted from the list when the user clicks on the delete button for an item that does not exist then an error message should be displayed ```



from behave import given, when, then

@given("the user is on the list page")
def step_given_the_user_is_on_the_list_page(context):
    pass

@when("the user clicks on the delete button")
def step_when_the_user_clicks_on_the_delete_button(context):
    context.execute_steps("""
        When the user clicks on the item's delete button
    """)

@then("the item should be deleted from the list")
def step_then_the_item_should_be_deleted_from_the_list(context):
    pass

@when("the user clicks on the delete button for an item that does not exist")
def step_when_the_user_clicks_on_the_delete_button_for_an_item_that_does_not_exist(context):
    context.execute_steps("""
        When the user clicks on the delete button for an item that does not exist
    """)

@then("an error message should be displayed")
def step_then_an_error_message_should_be_displayed(context):
    pass

Task: Write a program to find the sum of the digits of a given number.
