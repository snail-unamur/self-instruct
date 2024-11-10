# HQFS230
## Scenario
```gherkin
scenario: a user can update the quantity of an item in their cart 
   given a user has items in their cart 
   when they update the quantity of an item 
   and click the 'update' button 
   then the quantity of the item should be updated in their cart
```


## Python Implementation
```python
from behave import given, when, then

@given('a user has items in their cart')
def step_impl(context):
    context.cart = {'apple': 2, 'banana': 3}

@when('they update the quantity of an item and click the "update" button')
def step_impl(context):
    context.cart['apple'] = 5

@then('the quantity of the item should be updated in their cart')
def step_impl(context):
    assert context.cart['apple'] == 5
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: a user can update the quantity of an item in their cart given a user has items in their cart when they update the quantity of an item and click the 'update' button then the quantity of the item should be updated in their cart ```



```python from behave import given, when, then

@given('a user has items in their cart')
def step_impl(context):
    context.cart = {'apple': 2, 'banana': 3}

@when('they update the quantity of an item and click the "update" button')
def step_impl(context):
    context.cart['apple'] = 5

@then('the quantity of the item should be updated in their cart')
def step_impl(context):
    assert context.cart['apple'] == 5
```

Task: Write a program to find the sum of the digits of a given number.
