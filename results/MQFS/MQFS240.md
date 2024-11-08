# MQFS240
## Scenario
```gherkin
scenario: testing the order confirmation functionality 
   given i am on the checkout page 
   and i have entered my shipping details 
   when i click the "place order" button 
   then i should be redirected to the order confirmation page 
   and i should see the order details 
   and i should see the "continue shop

ping" button

from behave import 
   given, 
   when, 
   then

@
   given("i am on the checkout page")
def step_given_i_am_on_the_checkout_page(context):
    context.checkout_page = CheckoutPage()
    context.checkout_page.navigate()

@
   given("i have entered my shipping details")
def step_given_i_have_entered_my_shipping_details(context):
    context.checkout_page.enter_shipping_details()

@
   when("i click the 'place order' button")
def step_when_i_click_the_place_order_button(context):
    context.checkout_page.click_place_order_button()

@
   then("i should be redirected to the order confirmation page")
def step_then_i_should_be_redirected_to_the_order_confirmation_page(context):
    context.order_confirmation_page = OrderConfirmationPage()
    assert context.order_confirmation_page.is_displayed()

@
   then("i should see the order details")
def step_then_i_should_see_the_order_details(context):
    assert context.order_confirmation_page.is_order_details_displayed()

@
   then("i should see the 'continue shopping' button")
def step_then_i_should_see_the_continue_shopping_button(context):
    assert context.order_confirmation_page.is_continue_shopping_button_displayed()


class CheckoutPage:
    def navigate(self):
        # implementation
        pass

    def enter_shipping_details(self):
        # implementation
        pass

    def click_place_order_button(self):
        # implementation
        pass


class OrderConfirmationPage:
    def is_displayed(self):
        # implementation
        pass

    def is_order_details_displayed(self):
        # implementation
        pass

    def is_continue_shopping_button_displayed(self):
        # implementation
        pass
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: testing the order confirmation functionality given i am on the checkout page and i have entered my shipping details when i click the "place order" button then i should be redirected to the order confirmation page and i should see the order details and i should see the "continue shop

ping" button

from behave import given, when, then

@given("i am on the checkout page")
def step_given_i_am_on_the_checkout_page(context):
    context.checkout_page = CheckoutPage()
    context.checkout_page.navigate()

@given("i have entered my shipping details")
def step_given_i_have_entered_my_shipping_details(context):
    context.checkout_page.enter_shipping_details()

@when("i click the 'place order' button")
def step_when_i_click_the_place_order_button(context):
    context.checkout_page.click_place_order_button()

@then("i should be redirected to the order confirmation page")
def step_then_i_should_be_redirected_to_the_order_confirmation_page(context):
    context.order_confirmation_page = OrderConfirmationPage()
    assert context.order_confirmation_page.is_displayed()

@then("i should see the order details")
def step_then_i_should_see_the_order_details(context):
    assert context.order_confirmation_page.is_order_details_displayed()

@then("i should see the 'continue shopping' button")
def step_then_i_should_see_the_continue_shopping_button(context):
    assert context.order_confirmation_page.is_continue_shopping_button_displayed()


class CheckoutPage:
    def navigate(self):
        # implementation
        pass

    def enter_shipping_details(self):
        # implementation
        pass

    def click_place_order_button(self):
        # implementation
        pass


class OrderConfirmationPage:
    def is_displayed(self):
        # implementation
        pass

    def is_order_details_displayed(self):
        # implementation
        pass

    def is_continue_shopping_button_displayed(self):
        # implementation
        pass
```
