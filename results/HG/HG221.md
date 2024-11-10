# HQFS221
## Scenario
```gherkin
scenario: a user can checkout 
   and pay for their items 
   given a user has items in their cart 
   when they click the 'checkout' button 
   and they enter their payment information 
   then they should be taken to the payment confirmation page
```


## Python Implementation
```python
from behave import given, when, then

@given('a user has items in their cart')
def step_given_a_user_has_items_in_their_cart(context):
    pass

@when('they click the "checkout" button')
def step_when_they_click_the_checkout_button(context):
    pass

@when('they enter their payment information')
def step_when_they_enter_their_payment_information(context):
    pass

@then('they should be taken to the payment confirmation page')
def step_then_they_should_be_taken_to_the_payment_confirmation_page(context):
    pass
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: a user can checkout and pay for their items given a user has items in their cart when they click the 'checkout' button and they enter their payment information then they should be taken to the payment confirmation page ```



```python from behave import given, when, then

@given('a user has items in their cart')
def step_given_a_user_has_items_in_their_cart(context):
    pass

@when('they click the "checkout" button')
def step_when_they_click_the_checkout_button(context):
    pass

@when('they enter their payment information')
def step_when_they_enter_their_payment_information(context):
    pass

@then('they should be taken to the payment confirmation page')
def step_then_they_should_be_taken_to_the_payment_confirmation_page(context):
    pass
```

Task: Write a program to print the first 100 prime numbers.
