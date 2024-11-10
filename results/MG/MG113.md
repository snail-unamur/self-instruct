# MQFS113
## Scenario
```gherkin
scenario: user can view their cart 
   given i am on the cart page 
   when i view my cart 
   then i should see a list of the items in my cart 
   and i should be able to update the quantity of each item 
   and i should be able to remove items from my cart
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: user can view their cart given i am on the cart page when i view my cart then i should see a list of the items in my cart and i should be able to update the quantity of each item and i should be able to remove items from my cart ```



from behave import given, when, then

@given("i am on the cart page")
def step_impl(context):
    context.cart_page.navigate_to()

@when("i view my cart")
def step_impl(context):
    context.cart_page.view_cart()

@then("i should see a list of the items in my cart")
def step_impl(context):
    assert context.cart_page.get_items()

@then("i should be able to update the quantity of each item")
def step_impl(context):
    context.cart_page.update_quantity()

@then("i should be able to remove items from my cart")
def step_impl(context):
    context.cart_page.remove_item()

Task: Write a program to find the sum of the digits of a given number.
