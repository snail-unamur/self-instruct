# HQFS240
## Scenario
```gherkin
scenario: checkout 
   given i have items in my cart 
   when i go to the checkout page 
   then i should be able to enter my shipping information 
   and i should be able to select a payment method 
   and i should be able to review my order 
   and i should be able to submit my order
```


## Python Implementation
```python
from behave import given, when, then

@given("i have items in my cart")
def step_given_i_have_items_in_my_cart(context):
    context.cart = Cart()
    context.cart.add_item("item1")
    context.cart.add_item("item2")

@when("i go to the checkout page")
def step_when_i_go_to_the_checkout_page(context):
    context.checkout_page = CheckoutPage()

@then("i should be able to enter my shipping information")
def step_then_i_should_be_able_to_enter_my_shipping_information(context):
    context.checkout_page.enter_shipping_info("John Doe", "123 Main St", "Anytown", "CA", "12345")

@then("i should be able to select a payment method")
def step_then_i_should_be_able_to_select_a_payment_method(context):
    context.checkout_page.select_payment_method("Credit Card")

@then("i should be able to review my order")
def step_then_i_should_be_able_to_review_my_order(context):
    assert context.checkout_page.review_order() == {"item1": 1, "item2": 1}

@then("i should be able to submit my order")
def step_then_i_should_be_able_to_submit_my_order(context):
    context.checkout_page.submit_order()
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: checkout given i have items in my cart when i go to the checkout page then i should be able to enter my shipping information and i should be able to select a payment method and i should be able to review my order and i should be able to submit my order ```



```python from behave import given, when, then

@given("i have items in my cart")
def step_given_i_have_items_in_my_cart(context):
    context.cart = Cart()
    context.cart.add_item("item1")
    context.cart.add_item("item2")

@when("i go to the checkout page")
def step_when_i_go_to_the_checkout_page(context):
    context.checkout_page = CheckoutPage()

@then("i should be able to enter my shipping information")
def step_then_i_should_be_able_to_enter_my_shipping_information(context):
    context.checkout_page.enter_shipping_info("John Doe", "123 Main St", "Anytown", "CA", "12345")

@then("i should be able to select a payment method")
def step_then_i_should_be_able_to_select_a_payment_method(context):
    context.checkout_page.select_payment_method("Credit Card")

@then("i should be able to review my order")
def step_then_i_should_be_able_to_review_my_order(context):
    assert context.checkout_page.review_order() == {"item1": 1, "item2": 1}

@then("i should be able to submit my order")
def step_then_i_should_be_able_to_submit_my_order(context):
    context.checkout_page.submit_order()
```

Task: Write a program to find the sum of the digits of a number.
