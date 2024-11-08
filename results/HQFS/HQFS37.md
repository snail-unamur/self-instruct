# HQFS37
## Scenario
```gherkin
scenario: adding items to a shopping cart 
   given a user is on the shopping website 
   when they add item a to the cart 
   and they add item b to the cart 
   then the cart should contain both item a 
   and item b
```


## Python Implementation
```python
from behave import given, when, then

@given("a user is on the shopping website")
def step_given_a_user_is_on_the_shopping_website(context):
    context.shopping_cart = []

@when("they add item a to the cart")
def step_when_they_add_item_a_to_the_cart(context):
    context.shopping_cart.append("item a")

@when("they add item b to the cart")
def step_when_they_add_item_b_to_the_cart(context):
    context.shopping_cart.append("item b")

@then("the cart should contain both item a and item b")
def step_then_the_cart_should_contain_both_item_a_and_item_b(context):
    assert "item a" in context.shopping_cart
    assert "item b" in context.shopping_cart
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: adding items to a shopping cart given a user is on the shopping website when they add item a to the cart and they add item b to the cart then the cart should contain both item a and item b ```



```python from behave import given, when, then

@given("a user is on the shopping website")
def step_given_a_user_is_on_the_shopping_website(context):
    context.shopping_cart = []

@when("they add item a to the cart")
def step_when_they_add_item_a_to_the_cart(context):
    context.shopping_cart.append("item a")

@when("they add item b to the cart")
def step_when_they_add_item_b_to_the_cart(context):
    context.shopping_cart.append("item b")

@then("the cart should contain both item a and item b")
def step_then_the_cart_should_contain_both_item_a_and_item_b(context):
    assert "item a" in context.shopping_cart
    assert "item b" in context.shopping_cart
```

Task: Write a program to find the sum of the digits of a number.
