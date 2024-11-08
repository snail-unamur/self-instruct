# MQFS166
## Scenario
```gherkin
scenario: testing the payment functionality 
   given i have items in my cart 
   and i have entered my payment details 
   when i proceed to payment 
   then i should see a confirmation of my payment 
   and my items should be marked as paid for
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: testing the payment functionality given i have items in my cart and i have entered my payment details when i proceed to payment then i should see a confirmation of my payment and my items should be marked as paid for ```



from behave import given, when, then

@given("i have items in my cart")
def step_given_i_have_items_in_my_cart(context):
    context.cart = Cart()
    context.cart.add_item("item1")
    context.cart.add_item("item2")

@given("i have entered my payment details")
def step_given_i_have_entered_my_payment_details(context):
    context.payment_details = PaymentDetails()
    context.payment_details.card_number = "1234567890123456"
    context.payment_details.expiry_date = "12/25"
    context.payment_details.cvv = "123"

@when("i proceed to payment")
def step_when_i_proceed_to_payment(context):
    context.payment_processor = PaymentProcessor()
    context.payment_result = context.payment_processor.process_payment(context.cart, context.payment_details)

@then("i should see a confirmation of my payment")
def step_then_i_should_see_a_confirmation_of_my_payment(context):
    assert context.payment_result.status == "paid"

@then("my items should be marked as paid for")
def step_then_my_items_should_be_marked_as_paid_for(context):
    for item in context.cart.items:
        assert item.payment_status == "paid"


Task: Write a program to find the sum of the digits of a number.
