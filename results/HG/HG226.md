# HQFS226
## Scenario
```gherkin
scenario: testing the delete feature 
   given i am on the delete page 
   when i enter a valid id 
   and click delete 
   then the item with that id should be deleted 
   and i am on the delete page 
   and i enter an invalid id 
   and click delete 
   then the item with that id should not be deleted 
   and i am on the delete page 
   and i enter a valid id 
   and click cancel 
   then the item with that id should not be deleted
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: testing the delete feature given i am on the delete page when i enter a valid id and click delete then the item with that id should be deleted and i am on the delete page and i enter an invalid id and click delete then the item with that id should not be deleted and i am on the delete page and i enter a valid id and click cancel then the item with that id should not be deleted ```



```python from behave import given, when, then

@given("i am on the delete page")
def step_given_i_am_on_the_delete_page(context):
    context.delete_page.open()

@when("i enter a valid id and click delete")
def step_when_i_enter_a_valid_id_and_click_delete(context):
    context.delete_page.enter_valid_id()
    context.delete_page.click_delete()

@then("the item with that id should be deleted and i am on the delete page")
def step_then_the_item_with_that_id_should_be_deleted_and_i_am_on_the_delete_page(context):
    assert context.delete_page.is_deleted()
    assert context.delete_page.is_the_current_page()

@when("i enter an invalid id and click delete")
def step_when_i_enter_an_invalid_id_and_click_delete(context):
    context.delete_page.enter_invalid_id()
    context.delete_page.click_delete()

@then("the item with that id should not be deleted and i am on the delete page")
def step_then_the_item_with_that_id_should_not_be_deleted_and_i_am_on_the_delete_page(context):
    assert not context.delete_page.is_deleted()
    assert context.delete_page.is_the_current_page()

@when("i enter a valid id and click cancel")
def step_when_i_enter_a_valid_id_and_click_cancel(context):
    context.delete_page.enter_valid_id()
    context.delete_page.click_cancel()

@then("the item with that id should not be deleted")
def step_then_the_item_with_that_id_should_not_be_deleted(context):
    assert not context.delete_page.is_deleted()

@then("i am on the delete page")
def step_then_i_am_on_the_delete
