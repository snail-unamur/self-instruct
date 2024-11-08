# MQFS267
## Scenario
```gherkin
scenario: testing the functionality of the checkout page 
   given i am on the checkout page 
   when i enter a valid shipping address 
   and i enter a valid billing address 
   and i select a payment method 
   and i click the place order button 
   then i should be able to place an order successfully
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: testing the functionality of the checkout page given i am on the checkout page when i enter a valid shipping address and i enter a valid billing address and i select a payment method and i click the place order button then i should be able to place an order successfully ```



from behave import given, when, then

@given("i am on the checkout page")
def step_given_i_am_on_the_checkout_page(context):
    context.checkout_page.navigate()

@when("i enter a valid shipping address")
def step_when_i_enter_a_valid_shipping_address(context):
    context.checkout_page.enter_shipping_address()

@when("i enter a valid billing address")
def step_when_i_enter_a_valid_billing_address(context):
    context.checkout_page.enter_billing_address()

@when("i select a payment method")
def step_when_i_select_a_payment_method(context):
    context.checkout_page.select_payment_method()

@when("i click the place order button")
def step_when_i_click_the_place_order_button(context):
    context.checkout_page.click_place_order_button()

@then("i should be able to place an order successfully")
def step_then_i_should_be_able_to_place_an_order_successfully(context):
    context.checkout_page.verify_order_placed_successfully()

Task: Write a program to find the sum of the digits of a given number.
