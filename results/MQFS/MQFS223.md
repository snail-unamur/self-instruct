# MQFS223
## Scenario
```gherkin
scenario: testing the calculate_total function 
   given a cart with the following items: | id | name | price | quantity | | --- | --- | --- | --- | | 123 | product 1 | 10.00 | 2 | | 456 | product 2 | 20.00 | 1 | 
   when i call calculate_total() 
   then the total should be 30.00
```


## Python Implementation
```python
from behave import given, when, then

@given("a cart with the following items:")
def step_impl(context):
    context.cart = {
        "123": {"name": "product 1", "price": 10.00, "quantity": 2},
        "456": {"name": "product 2", "price": 20.00, "quantity": 1},
    }

@when("i call calculate_total()")
def step_impl(context):
    context.total = calculate_total(context.cart)

@then("the total should be 30.00")
def step_impl(context):
    assert context.total == 30.00

def calculate_total(cart):
    total = 0
    for item in cart.values():
        total += item["price"] * item["quantity"]
    return total
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: testing the calculate_total function given a cart with the following items: | id | name | price | quantity | | --- | --- | --- | --- | | 123 | product 1 | 10.00 | 2 | | 456 | product 2 | 20.00 | 1 | when i call calculate_total() then the total should be 30.00 ```



```python from behave import given, when, then

@given("a cart with the following items:")
def step_impl(context):
    context.cart = {
        "123": {"name": "product 1", "price": 10.00, "quantity": 2},
        "456": {"name": "product 2", "price": 20.00, "quantity": 1},
    }

@when("i call calculate_total()")
def step_impl(context):
    context.total = calculate_total(context.cart)

@then("the total should be 30.00")
def step_impl(context):
    assert context.total == 30.00

def calculate_total(cart):
    total = 0
    for item in cart.values():
        total += item["price"] * item["quantity"]
    return total
```

Task: Write a program to find the sum of the digits of a number.
