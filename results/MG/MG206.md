# MQFS206
## Scenario
```gherkin
scenario: testing the shopping cart 
   given a shopping cart with the following items: - apples - bananas - oranges 
   when i add 2 apples to the cart 
   then the cart contains 2 apples 
   when i remove 1 banana from the cart 
   then the cart contains 1 banana 
   when i clear the cart 
   then the cart is empty 
   when i view the cart 
   then i see the following items: - apples - bananas - oranges
```


## Python Implementation
```python
from behave import given, when, then

@given("a shopping cart with the following items: - apples - bananas - oranges")
def step_given_a_shopping_cart_with_the_following_items(context):
    context.cart = {"apples": 1, "bananas": 1, "oranges": 1}

@when("i add 2 apples to the cart")
def step_i_add_2_apples_to_the_cart(context):
    context.cart["apples"] += 2

@then("the cart contains 2 apples")
def step_the_cart_contains_2_apples(context):
    assert context.cart["apples"] == 2

@when("i remove 1 banana from the cart")
def step_i_remove_1_banana_from_the_cart(context):
    context.cart["bananas"] -= 1

@then("the cart contains 1 banana")
def step_the_cart_contains_1_banana(context):
    assert context.cart["bananas"] == 1

@when("i clear the cart")
def step_i_clear_the_cart(context):
    context.cart = {}

@then("the cart is empty")
def step_the_cart_is_empty(context):
    assert context.cart == {}

@when("i view the cart")
def step_i_view_the_cart(context):
    pass

@then("i see the following items: - apples - bananas - oranges")
def step_i_see_the_following_items(context):
    assert set(context.cart.keys()) == {"apples", "bananas", "oranges"}
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: testing the shopping cart given a shopping cart with the following items: - apples - bananas - oranges when i add 2 apples to the cart then the cart contains 2 apples when i remove 1 banana from the cart then the cart contains 1 banana when i clear the cart then the cart is empty when i view the cart then i see the following items: - apples - bananas - oranges ```



```python from behave import given, when, then

@given("a shopping cart with the following items: - apples - bananas - oranges")
def step_given_a_shopping_cart_with_the_following_items(context):
    context.cart = {"apples": 1, "bananas": 1, "oranges": 1}

@when("i add 2 apples to the cart")
def step_i_add_2_apples_to_the_cart(context):
    context.cart["apples"] += 2

@then("the cart contains 2 apples")
def step_the_cart_contains_2_apples(context):
    assert context.cart["apples"] == 2

@when("i remove 1 banana from the cart")
def step_i_remove_1_banana_from_the_cart(context):
    context.cart["bananas"] -= 1

@then("the cart contains 1 banana")
def step_the_cart_contains_1_banana(context):
    assert context.cart["bananas"] == 1

@when("i clear the cart")
def step_i_clear_the_cart(context):
    context.cart = {}

@then("the cart is empty")
def step_the_cart_is_empty(context):
    assert context.cart == {}

@when("i view the cart")
def step_i_view_the_cart(context):
    pass

@then("i see the following items: - apples - bananas - oranges")
def step_i_see_the_following_items(context):
    assert set(context.cart.keys()) == {"apples", "bananas", "oranges"}
```

Task: Write a program to find the number of occurrences of a given word in a given string.
