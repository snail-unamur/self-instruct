# HQFS30
## Scenario
```gherkin
scenario: vending machine dispenses product 
   when sufficient funds are inserted 
   given i have inserted 75 cents into the vending machine 
   when i select a product that costs 75 cents 
   then the vending machine dispenses the product
```


## Python Implementation
```python
from behave import given, when, then

@given("i have inserted 75 cents into the vending machine")
def step_given(context):
    context.vending_machine = VendingMachine()
    context.vending_machine.insert_money(0.75)

@when("i select a product that costs 75 cents")
def step_when(context):
    context.vending_machine.select_product(Product(0.75))

@then("the vending machine dispenses the product")
def step_then(context):
    assert context.vending_machine.dispensed
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: vending machine dispenses product when sufficient funds are inserted given i have inserted 75 cents into the vending machine when i select a product that costs 75 cents then the vending machine dispenses the product ```



```python from behave import given, when, then

@given("i have inserted 75 cents into the vending machine")
def step_given(context):
    context.vending_machine = VendingMachine()
    context.vending_machine.insert_money(0.75)

@when("i select a product that costs 75 cents")
def step_when(context):
    context.vending_machine.select_product(Product(0.75))

@then("the vending machine dispenses the product")
def step_then(context):
    assert context.vending_machine.dispensed
```

Task: Write a program to find the sum of the digits of a number.
