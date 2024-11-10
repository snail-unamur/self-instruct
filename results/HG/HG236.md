# HQFS236
## Scenario
```gherkin
scenario: i can find the total price of a list of items 
   given i have a list of items with prices: [("apple", 0.5), ("banana", 0.25), ("orange", 0.75)] 
   when i calculate the total price of the list 
   then the total price should be 1.50
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: i can find the total price of a list of items given i have a list of items with prices: [("apple", 0.5), ("banana", 0.25), ("orange", 0.75)] when i calculate the total price of the list then the total price should be 1.50 ```



from behave import given, when, then

@given("i have a list of items with prices: {items}")
def step_impl(context, items):
    context.items = items

@when("i calculate the total price of the list")
def step_impl(context):
    context.total_price = sum(item[1] for item in context.items)

@then("the total price should be {price}")
def step_impl(context, price):
    assert context.total_price == price
