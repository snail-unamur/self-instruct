# MQFS95
## Scenario
```gherkin
scenario: a user can place an order 
   given that the user is logged in 
   and the user has added items to their cart 
   when the user proceeds to checkout 
   then the user should be taken to the shipping page 
   and the user should see form fields to enter their shipping information 
   when the user enters their shipping information 
   and clicks continue 
   then the user should be taken to the payment page 
   and the user should see form fields to enter their payment information 
   when the user enters their payment information 
   and clicks place order 
   then the user should be taken to the order confirmation page 
   and the user should see a confirmation of their order 
   and the user should receive an email confirmation of their order
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: a user can place an order given that the user is logged in and the user has added items to their cart when the user proceeds to checkout then the user should be taken to the shipping page and the user should see form fields to enter their shipping information when the user enters their shipping information and clicks continue then the user should be taken to the payment page and the user should see form fields to enter their payment information when the user enters their payment information and clicks place order then the user should be taken to the order confirmation page and the user should see a confirmation of their order and the user should receive an email confirmation of their order ```



```python from behave import given, when, then

@given("a user is logged in")
def step_given_a_user_is_logged_in(context):
    context.user = User()
    context.user.login()

@given("the user has added items to their cart")
def step_given_the_user_has_added_items_to_their_cart(context):
    context.cart = Cart()
    context.cart.add_items()

@when("the user proceeds to checkout")
def step_when_the_user_proceeds_to_checkout(context):
    context.shipping_page = ShippingPage()
    context.shipping_page.load(context.user, context.cart)

@then("the user should be taken to the shipping page")
def step_then_the_user_should_be_taken_to_the_shipping_page(context):
    assert context.shipping_page.is_displayed()

@then("the user should see form fields to enter their shipping information")
def step_then_the_user_should_see_form_fields_to_enter_their_shipping_information(context):
    assert context.shipping_page.has_shipping_form()

@when("the user enters their shipping information and clicks continue")
def step_when_the_user_enters_their_shipping_information_and_clicks_continue(context):
    context.payment_page = PaymentPage()
    context.payment_page.load(context.user, context.cart, context.shipping_page.get_shipping_info())

@then("the user should be taken to the payment page")
def step_then_the_user_should_be_taken_to_the_payment_page(context):
    assert context.payment_page.is_displayed()

@then("the user should see form fields to enter their payment information")
def step_then_the_user_should_see_form_fields_to_enter_their_payment_information(context):
    assert context.payment_page.has
