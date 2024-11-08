# MQFS247
## Scenario
```gherkin
scenario: testing the behavior of the "add_item" function 
   given i have a "add_item" function 
   when i call the "add_item" function with the following parameters: name="item1", price=10.0, quantity=5 
   then i should get a list with the following items: [{"name": "item1", "price": 10.0, "quantity": 5}]
```


## Python Implementation
```python
from behave import given, then

@given("i have an 'add_item' function")
def step_impl(context):
    context.add_item = lambda name, price, quantity: [{"name": name, "price": price, "quantity": quantity}]

@when("i call the 'add_item' function with the following parameters: name='item1', price=10.0, quantity=5")
def step_impl(context):
    context.result = context.add_item("item1", 10.0, 5)

@then("i should get a list with the following items: [{'name': 'item1', 'price': 10.0, 'quantity': 5}]")
def step_impl(context):
    assert context.result == [{"name": "item1", "price": 10.0, "quantity": 5}]
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: testing the behavior of the "add_item" function given i have a "add_item" function when i call the "add_item" function with the following parameters: name="item1", price=10.0, quantity=5 then i should get a list with the following items: [{"name": "item1", "price": 10.0, "quantity": 5}] ```



```python from behave import given, then

@given("i have an 'add_item' function")
def step_impl(context):
    context.add_item = lambda name, price, quantity: [{"name": name, "price": price, "quantity": quantity}]

@when("i call the 'add_item' function with the following parameters: name='item1', price=10.0, quantity=5")
def step_impl(context):
    context.result = context.add_item("item1", 10.0, 5)

@then("i should get a list with the following items: [{'name': 'item1', 'price': 10.0, 'quantity': 5}]")
def step_impl(context):
    assert context.result == [{"name": "item1", "price": 10.0, "quantity": 5}]
```

Task: Write a program to find the sum of the digits of a number.
