# MQFS116
## Scenario
```gherkin
scenario: testing the functionality of the checkout page 
   given i am on the cart page 
   when i proceed to checkout 
   then i am redirected to the checkout page 
   when i enter the correct information 
   then i am redirected to the confirmation page 
   when i enter the wrong information 
   then i am not redirected to the confirmation page
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: testing the functionality of the checkout page given i am on the cart page when i proceed to checkout then i am redirected to the checkout page when i enter the correct information then i am redirected to the confirmation page when i enter the wrong information then i am not redirected to the confirmation page ```



from behave import given, when, then

@given("i am on the cart page")
def step_given_i_am_on_the_cart_page(context):
    context.cart_page = CartPage()
    context.cart_page.navigate()

@when("i proceed to checkout")
def step_when_i_proceed_to_checkout(context):
    context.checkout_page = context.cart_page.proceed_to_checkout()

@then("i am redirected to the checkout page")
def step_then_i_am_redirected_to_the_checkout_page(context):
    assert isinstance(context.checkout_page, CheckoutPage)

@when("i enter the correct information")
def step_when_i_enter_the_correct_information(context):
    context.checkout_page.enter_correct_information()

@then("i am redirected to the confirmation page")
def step_then_i_am_redirected_to_the_confirmation_page(context):
    assert isinstance(context.checkout_page, ConfirmationPage)

@when("i enter the wrong information")
def step_when_i_enter_the_wrong_information(context):
    context.checkout_page.enter_wrong_information()

@then("i am not redirected to the confirmation page")
def step_then_i_am_not_redirected_to_the_confirmation_page(context):
    assert not isinstance(context.checkout_page, ConfirmationPage)


Task: Write a program to find the sum of the digits of a number.
