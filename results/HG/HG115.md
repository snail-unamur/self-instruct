# HQFS115
## Scenario
```gherkin
scenario: 
   given a user has a shopping cart with items in it 
   when they proceed to checkout 
   then they should be taken to the checkout page 
   and they should see their items listed 
   and they should see the total cost of their items 
   and they should be able to enter their shipping information 
   and they should be able to enter their payment information 
   and they should be able to confirm their order 
   and they should be taken to the order confirmation page 
   and they should see their order number 
   and they should see a confirmation message
```


## Python Implementation
```python
from behave import given, when, then

@given("a user has a shopping cart with items in it")
def step_given_a_user_has_a_shopping_cart_with_items_in_it(context):
    pass

@when("they proceed to checkout")
def step_when_they_proceed_to_checkout(context):
    pass

@then("they should be taken to the checkout page")
def step_then_they_should_be_taken_to_the_checkout_page(context):
    pass

@then("they should see their items listed")
def step_then_they_should_see_their_items_listed(context):
    pass

@then("they should see the total cost of their items")
def step_then_they_should_see_the_total_cost_of_their_items(context):
    pass

@then("they should be able to enter their shipping information")
def step_then_they_should_be_able_to_enter_their_shipping_information(context):
    pass

@then("they should be able to enter their payment information")
def step_then_they_should_be_able_to_enter_their_payment_information(context):
    pass

@then("they should be able to confirm their order")
def step_then_they_should_be_able_to_confirm_their_order(context):
    pass

@then("they should be taken to the order confirmation page")
def step_then_they_should_be_taken_to_the_order_confirmation_page(context):
    pass

@then("they should see their order number")
def step_then_they_should_see_their_order_number(context):
    pass

@then("they should see a confirmation message")
def step_then_they_should_see_a_confirmation_message(context):
    pass
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: given a user has a shopping cart with items in it when they proceed to checkout then they should be taken to the checkout page and they should see their items listed and they should see the total cost of their items and they should be able to enter their shipping information and they should be able to enter their payment information and they should be able to confirm their order and they should be taken to the order confirmation page and they should see their order number and they should see a confirmation message ```



```python from behave import given, when, then

@given("a user has a shopping cart with items in it")
def step_given_a_user_has_a_shopping_cart_with_items_in_it(context):
    pass

@when("they proceed to checkout")
def step_when_they_proceed_to_checkout(context):
    pass

@then("they should be taken to the checkout page")
def step_then_they_should_be_taken_to_the_checkout_page(context):
    pass

@then("they should see their items listed")
def step_then_they_should_see_their_items_listed(context):
    pass

@then("they should see the total cost of their items")
def step_then_they_should_see_the_total_cost_of_their_items(context):
    pass

@then("they should be able to enter their shipping information")
def step_then_they_should_be_able_to_enter_their_shipping_information(context):
    pass

@then("they should be able to enter their payment information")
def step_then_they_should_be_able_to_enter_their_payment_information(context):
    pass

@then("they should be able to confirm their order")
def step_then_they_should_be_able_to_confirm_their_order(context):
    pass

@then("they should be taken to the order confirmation page")
def step_then_they_should_be_taken_to_the_order_confirmation_page(context):
    pass

@then("they should see their order number")
def step_then_they_should_see_their_order_number(context):
    pass

@then("they should see a confirmation message")
def step_then_they_should_see_a_confirmation_message(context):
    pass
```

Task: Write a program to find the sum of the digits of a number.
