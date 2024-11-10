# MQFS175
## Scenario
```gherkin
scenario: user can update the quantity of a product in their cart 
   given user is logged in 
   when user updates the quantity of a product 
   then the quantity of the product is updated in user's cart
```


## Python Implementation
```python
from behave import given, when, then

@given("user is logged in")
def step_impl(context):
    context.user = User()
    context.user.login()

@when("user updates the quantity of a product")
def step_impl(context):
    context.product = Product()
    context.cart = Cart()
    context.cart.add_product(context.product)
    context.cart.update_quantity(context.product, 5)

@then("the quantity of the product is updated in user's cart")
def step_impl(context):
    assert context.cart.get_quantity(context.product) == 5
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: user can update the quantity of a product in their cart given user is logged in when user updates the quantity of a product then the quantity of the product is updated in user's cart ```



```python from behave import given, when, then

@given("user is logged in")
def step_impl(context):
    context.user = User()
    context.user.login()

@when("user updates the quantity of a product")
def step_impl(context):
    context.product = Product()
    context.cart = Cart()
    context.cart.add_product(context.product)
    context.cart.update_quantity(context.product, 5)

@then("the quantity of the product is updated in user's cart")
def step_impl(context):
    assert context.cart.get_quantity(context.product) == 5
```

Task: Write a program to print the first 100 prime numbers.
