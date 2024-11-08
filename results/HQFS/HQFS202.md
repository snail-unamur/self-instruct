# HQFS202
## Scenario
```gherkin
scenario: checking the total price of a cart 
   given i am on the cart page 
   when i calculate the total price of the products in the cart 
   then the total price should be displayed on the cart page
```


## Python Implementation
```python
from behave import given, when, then

@given("i am on the cart page")
def step_given_i_am_on_the_cart_page(context):
    context.cart_page.open()

@when("i calculate the total price of the products in the cart")
def step_when_i_calculate_the_total_price_of_the_products_in_the_cart(context):
    context.total_price = context.cart_page.get_total_price()

@then("the total price should be displayed on the cart page")
def step_then_the_total_price_should_be_displayed_on_the_cart_page(context):
    assert context.cart_page.get_total_price() == context.total_price
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: checking the total price of a cart given i am on the cart page when i calculate the total price of the products in the cart then the total price should be displayed on the cart page ```



```python from behave import given, when, then

@given("i am on the cart page")
def step_given_i_am_on_the_cart_page(context):
    context.cart_page.open()

@when("i calculate the total price of the products in the cart")
def step_when_i_calculate_the_total_price_of_the_products_in_the_cart(context):
    context.total_price = context.cart_page.get_total_price()

@then("the total price should be displayed on the cart page")
def step_then_the_total_price_should_be_displayed_on_the_cart_page(context):
    assert context.cart_page.get_total_price() == context.total_price
```

Task: Write a program to find the sum of the digits of a number.
