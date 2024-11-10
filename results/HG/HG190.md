# HQFS190
## Scenario
```gherkin
scenario: a user can checkout 
   and place an order 
   given the user is on the cart page 
   when the user clicks the checkout button 
   then the user should be redirected to the checkout page 
   and the user should be able to enter their shipping information 
   and the user should be able to select their payment method 
   and the user should be able to confirm their order 
   and the user should be redirected to the order confirmation page 
   and the user should receive an email with their order details
```


## Python Implementation
```python
from behave import given, when, then

@given("the user is on the cart page")
def step_given_the_user_is_on_the_cart_page(context):
    pass

@when("the user clicks the checkout button")
def step_when_the_user_clicks_the_checkout_button(context):
    pass

@then("the user should be redirected to the checkout page")
def step_then_the_user_should_be_redirected_to_the_checkout_page(context):
    pass

@then("the user should be able to enter their shipping information")
def step_then_the_user_should_be_able_to_enter_their_shipping_information(context):
    pass

@then("the user should be able to select their payment method")
def step_then_the_user_should_be_able_to_select_their_payment_method(context):
    pass

@then("the user should be able to confirm their order")
def step_then_the_user_should_be_able_to_confirm_their_order(context):
    pass

@then("the user should be redirected to the order confirmation page")
def step_then_the_user_should_be_redirected_to_the_order_confirmation_page(context):
    pass

@then("the user should receive an email with their order details")
def step_then_the_user_should_receive_an_email_with_their_order_details(context):
    pass
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: a user can checkout and place an order given the user is on the cart page when the user clicks the checkout button then the user should be redirected to the checkout page and the user should be able to enter their shipping information and the user should be able to select their payment method and the user should be able to confirm their order and the user should be redirected to the order confirmation page and the user should receive an email with their order details ```



```python from behave import given, when, then

@given("the user is on the cart page")
def step_given_the_user_is_on_the_cart_page(context):
    pass

@when("the user clicks the checkout button")
def step_when_the_user_clicks_the_checkout_button(context):
    pass

@then("the user should be redirected to the checkout page")
def step_then_the_user_should_be_redirected_to_the_checkout_page(context):
    pass

@then("the user should be able to enter their shipping information")
def step_then_the_user_should_be_able_to_enter_their_shipping_information(context):
    pass

@then("the user should be able to select their payment method")
def step_then_the_user_should_be_able_to_select_their_payment_method(context):
    pass

@then("the user should be able to confirm their order")
def step_then_the_user_should_be_able_to_confirm_their_order(context):
    pass

@then("the user should be redirected to the order confirmation page")
def step_then_the_user_should_be_redirected_to_the_order_confirmation_page(context):
    pass

@then("the user should receive an email with their order details")
def step_then_the_user_should_receive_an_email_with_their_order_details(context):
    pass
```

Task: Write a program to find the sum of the digits of a number.
