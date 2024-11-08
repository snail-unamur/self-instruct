# MQFS85
## Scenario
```gherkin
scenario: testing the addition of a new product to the inventory 
   given a inventory with 100 products 
   when

the product is added 
   then
the inventory should have 101 products

As a store owner
I want to be able to add new products to my inventory
So that I can keep track of my inventory
```


## Python Implementation
```python
from behave import given, when, then

@given("a inventory with 100 products")
def step_given_a_inventory_with_100_products(context):
    context.inventory = 100

@when("the product is added")
def step_when_the_product_is_added(context):
    context.inventory += 1

@then("the inventory should have 101 products")
def step_then_the_inventory_should_have_101_products(context):
    assert context.inventory == 101
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: testing the addition of a new product to the inventory given a inventory with 100 products when

the product is added then
the inventory should have 101 products

As a store owner
I want to be able to add new products to my inventory
So that I can keep track of my inventory
```

```python
from behave import given, when, then

@given("a inventory with 100 products")
def step_given_a_inventory_with_100_products(context):
    context.inventory = 100

@when("the product is added")
def step_when_the_product_is_added(context):
    context.inventory += 1

@then("the inventory should have 101 products")
def step_then_the_inventory_should_have_101_products(context):
    assert context.inventory == 101
```

Task: Write a program to find the sum of the digits of a given number.
