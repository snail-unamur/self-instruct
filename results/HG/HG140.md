# HQFS140
## Scenario
```gherkin
scenario: a user can remove an item from their cart 
   given the user has items in their cart 
   when the user clicks the remove button for a specific item 
   then that item is removed from their cart
```


## Python Implementation
```python
from behave import given, when, then

@given("the user has items in their cart")
def step_impl(context):
    context.cart = [1, 2, 3]

@when("the user clicks the remove button for a specific item")
def step_impl(context):
    context.cart.remove(2)

@then("that item is removed from their cart")
def step_impl(context):
    assert 2 not in context.cart
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: a user can remove an item from their cart given the user has items in their cart when the user clicks the remove button for a specific item then that item is removed from their cart ```



```python from behave import given, when, then

@given("the user has items in their cart")
def step_impl(context):
    context.cart = [1, 2, 3]

@when("the user clicks the remove button for a specific item")
def step_impl(context):
    context.cart.remove(2)

@then("that item is removed from their cart")
def step_impl(context):
    assert 2 not in context.cart
```

Task: Write a program to find the second largest number in a list.
