# HQFS91
## Scenario
```gherkin
scenario: 
   given that the user has a valid credit card 
   and the user is on the checkout page 
   when the user enters the credit card details 
   then the user should be able to complete the purchase
```


## Python Implementation
```python
from behave import given, when, then

@given("the user has a valid credit card")
def step_given_the_user_has_a_valid_credit_card(context):
    context.credit_card = {"number": "4111111111111111", "cvv": "123", "expiry_date": "12/22"}

@given("the user is on the checkout page")
def step_given_the_user_is_on_the_checkout_page(context):
    context.checkout_page = True

@when("the user enters the credit card details")
def step_when_the_user_enters_the_credit_card_details(context):
    context.checkout_page.enter_credit_card_details(context.credit_card)

@then("the user should be able to complete the purchase")
def step_then_the_user_should_be_able_to_complete_the_purchase(context):
    assert context.checkout_page.purchase_successful()
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: given that the user has a valid credit card and the user is on the checkout page when the user enters the credit card details then the user should be able to complete the purchase ```



```python from behave import given, when, then

@given("the user has a valid credit card")
def step_given_the_user_has_a_valid_credit_card(context):
    context.credit_card = {"number": "4111111111111111", "cvv": "123", "expiry_date": "12/22"}

@given("the user is on the checkout page")
def step_given_the_user_is_on_the_checkout_page(context):
    context.checkout_page = True

@when("the user enters the credit card details")
def step_when_the_user_enters_the_credit_card_details(context):
    context.checkout_page.enter_credit_card_details(context.credit_card)

@then("the user should be able to complete the purchase")
def step_then_the_user_should_be_able_to_complete_the_purchase(context):
    assert context.checkout_page.purchase_successful()
```

Task: Write a program to find the sum of the digits of a given number.
