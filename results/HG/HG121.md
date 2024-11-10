# HQFS121
## Scenario
```gherkin
scenario: calculating the total cost of items in a shopping cart 
   given a shopping cart with items 
   and their respective prices 
   when the user clicks on the 'calculate total' button 
   then the total cost of the items in the shopping cart should be displayed
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: calculating the total cost of items in a shopping cart given a shopping cart with items and their respective prices when the user clicks on the 'calculate total' button then the total cost of the items in the shopping cart should be displayed ```



from behave import given, when, then

@given('a shopping cart with items and their respective prices')
def step(context):
    context.items = {'item1': 10, 'item2': 20, 'item3': 30}

@when('the user clicks on the "calculate total" button')
def step(context):
    context.total = sum(context.items.values())

@then('the total cost of the items in the shopping cart should be displayed')
def step(context):
    assert context.total == 60
