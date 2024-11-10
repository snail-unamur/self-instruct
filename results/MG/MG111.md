# MQFS111
## Scenario
```gherkin
scenario: testing the functionality of the "checkout" button 
   given a user has added products to their cart 
   when they click the "checkout" button 
   then they are taken to the checkout page 
   and the products in the cart are displayed 
   and the total price of the products in the cart is displayed
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: testing the functionality of the "checkout" button given a user has added products to their cart when they click the "checkout" button then they are taken to the checkout page and the products in the cart are displayed and the total price of the products in the cart is displayed ```



from behave import given, when, then

@given("a user has added products to their cart")
def step_given_a_user_has_added_products_to_their_cart(context):
    context.user.add_products_to_cart()

@when("they click the 'checkout' button")
def step_when_they_click_the_checkout_button(context):
    context.user.click_checkout_button()

@then("they are taken to the checkout page")
def step_then_they_are_taken_to_the_checkout_page(context):
    assert context.user.is_on_checkout_page()

@then("the products in the cart are displayed")
def step_then_the_products_in_the_cart_are_displayed(context):
    assert context.user.are_products_displayed_on_checkout_page()

@then("the total price of the products in the cart is displayed")
def step_then_the_total_price_of_the_products_in_the_cart_is_displayed(context):
    assert context.user.is_total_price_displayed_on_checkout_page()


Task: Write a program to find the sum of the digits of a given number.
