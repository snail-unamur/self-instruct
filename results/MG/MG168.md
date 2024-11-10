# MQFS168
## Scenario
```gherkin
scenario: testing the delete functionality 
   given i am on the homepage 
   when i click on the delete button 
   then i am taken to the confirmation page 
   and i see the confirmation message 
   when i confirm the deletion 
   then i am taken back to the homepage 
   and i no longer see the deleted item
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: testing the delete functionality given i am on the homepage when i click on the delete button then i am taken to the confirmation page and i see the confirmation message when i confirm the deletion then i am taken back to the homepage and i no longer see the deleted item ```



from behave import given, when, then

@given("i am on the homepage")
def step_given_i_am_on_the_homepage(context):
    context.homepage = HomePage()
    context.homepage.navigate()

@when("i click on the delete button")
def step_when_i_click_on_the_delete_button(context):
    context.confirmation_page = context.homepage.delete()

@then("i see the confirmation message")
def step_then_i_see_the_confirmation_message(context):
    confirmation_message = context.confirmation_page.get_confirmation_message()
    assert confirmation_message == "Item deleted successfully"

@when("i confirm the deletion")
def step_when_i_confirm_the_deletion(context):
    context.homepage = context.confirmation_page.confirm_deletion()

@then("i no longer see the deleted item")
def step_then_i_no_longer_see_the_deleted_item(context):
    assert context.homepage.is_deleted_item_visible() == False

Task: Write a program to find the sum of the digits of a given number.
