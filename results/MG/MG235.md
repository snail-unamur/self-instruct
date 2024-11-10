# MQFS235
## Scenario
```gherkin
scenario: a user can place an order 
   given i am on the product page 
   when i add a product to my cart 
   and i go to the cart page 
   when i click on the place order button 
   then my order is placed 
   and i am redirected to the order confirmation page
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: a user can place an order given i am on the product page when i add a product to my cart and i go to the cart page when i click on the place order button then my order is placed and i am redirected to the order confirmation page ```



from behave import given, when, then

@given("i am on the product page")
def step_given_i_am_on_the_product_page(context):
    context.product_page = ProductPage(context.browser)
    context.product_page.navigate_to()

@when("i add a product to my cart")
def step_when_i_add_a_product_to_my_cart(context):
    context.product_page.add_product_to_cart()

@when("i go to the cart page")
def step_when_i_go_to_the_cart_page(context):
    context.cart_page = CartPage(context.browser)
    context.cart_page.navigate_to()

@when("i click on the place order button")
def step_when_i_click_on_the_place_order_button(context):
    context.order = context.cart_page.place_order()

@then("my order is placed and i am redirected to the order confirmation page")
def step_then_my_order_is_placed_and_i_am_redirected_to_the_order_confirmation_page(context):
    context.confirmation_page = ConfirmationPage(context.browser)
    context.confirmation_page.navigate_to()
    context.confirmation_page.assert_order_details(context.order)

Task: Write a program to find the sum of the digits of a number.
