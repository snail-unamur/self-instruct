# MQFS115
## Scenario
```gherkin
scenario: user can checkout 
   and pay for their order 
   given i am a registered user 
   and i have items in my cart 
   when i go to the checkout page 
   and i fill in my shipping 
   and billing information 
   and i select a payment method 
   and i click the submit button 
   then i should see a confirmation page 
   and i should receive an email with the details of my order
```


## Python Implementation
```python
from behave import given, when, then

@given("i am a registered user")
def step_given_i_am_a_registered_user(context):
    context.user = User()
    context.user.register()

@given("i have items in my cart")
def step_given_i_have_items_in_my_cart(context):
    context.cart = Cart()
    context.cart.add_items()

@when("i go to the checkout page")
def step_when_i_go_to_the_checkout_page(context):
    context.checkout_page = CheckoutPage()
    context.checkout_page.load()

@when("i fill in my shipping and billing information")
def step_when_i_fill_in_my_shipping_and_billing_information(context):
    context.checkout_page.fill_shipping_and_billing_information()

@when("i select a payment method")
def step_when_i_select_a_payment_method(context):
    context.checkout_page.select_payment_method()

@when("i click the submit button")
def step_when_i_click_the_submit_button(context):
    context.checkout_page.submit()

@then("i should see a confirmation page")
def step_then_i_should_see_a_confirmation_page(context):
    assert context.checkout_page.is_confirmation_page()

@then("i should receive an email with the details of my order")
def step_then_i_should_receive_an_email_with_the_details_of_my_order(context):
    assert context.user.email_received_order_confirmation()
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: user can checkout and pay for their order given i am a registered user and i have items in my cart when i go to the checkout page and i fill in my shipping and billing information and i select a payment method and i click the submit button then i should see a confirmation page and i should receive an email with the details of my order ```



```python from behave import given, when, then

@given("i am a registered user")
def step_given_i_am_a_registered_user(context):
    context.user = User()
    context.user.register()

@given("i have items in my cart")
def step_given_i_have_items_in_my_cart(context):
    context.cart = Cart()
    context.cart.add_items()

@when("i go to the checkout page")
def step_when_i_go_to_the_checkout_page(context):
    context.checkout_page = CheckoutPage()
    context.checkout_page.load()

@when("i fill in my shipping and billing information")
def step_when_i_fill_in_my_shipping_and_billing_information(context):
    context.checkout_page.fill_shipping_and_billing_information()

@when("i select a payment method")
def step_when_i_select_a_payment_method(context):
    context.checkout_page.select_payment_method()

@when("i click the submit button")
def step_when_i_click_the_submit_button(context):
    context.checkout_page.submit()

@then("i should see a confirmation page")
def step_then_i_should_see_a_confirmation_page(context):
    assert context.checkout_page.is_confirmation_page()

@then("i should receive an email with the details of my order")
def step_then_i_should_receive_an_email_with_the_details_of_my_order(context):
    assert context.user.email_received_order_confirmation()
```

Task: Write a program to find the second largest number in a list.
