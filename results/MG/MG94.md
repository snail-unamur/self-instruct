# MQFS94
## Scenario
```gherkin
scenario: testing the product page functionality 
   given a user is on a product page 
   when the user adds the product to their cart 
   then the product should be added to the cart if the user tries to add more of the same product to the cart than the quantity of the product in the cart should be updated
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: testing the product page functionality given a user is on a product page when the user adds the product to their cart then the product should be added to the cart if the user tries to add more of the same product to the cart than the quantity of the product in the cart should be updated ```



from behave import given, when, then

@given("a user is on a product page")
def step_given_a_user_is_on_a_product_page(context):
    context.product_page = ProductPage()
    context.product_page.open()

@when("the user adds the product to their cart")
def step_when_the_user_adds_the_product_to_their_cart(context):
    context.product_page.add_to_cart()

@then("the product should be added to the cart")
def step_then_the_product_should_be_added_to_the_cart(context):
    assert context.product_page.cart.quantity == 1

@when("the user tries to add more of the same product to the cart")
def step_when_the_user_tries_to_add_more_of_the_same_product_to_the_cart(context):
    context.product_page.add_to_cart()

@then("the quantity of the product in the cart should be updated")
def step_then_the_quantity_of_the_product_in_the_cart_should_be_updated(context):
    assert context.product_page.cart.quantity == 2

Task: Write a program to find the sum of the digits of a number.
