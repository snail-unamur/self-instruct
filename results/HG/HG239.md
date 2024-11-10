# HQFS239
## Scenario
```gherkin
scenario: testing the checkout functionality 
   given the user has added items to their cart 
   when the user proceeds to checkout 
   then the user should be prompted to enter their shipping information 
   and the user should be able to review their order before submitting it 
   and the user should receive a confirmation email after submitting the order
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: testing the checkout functionality given the user has added items to their cart when the user proceeds to checkout then the user should be prompted to enter their shipping information and the user should be able to review their order before submitting it and the user should receive a confirmation email after submitting the order ```



from behave import given, when, then

@given("the user has added items to their cart")
def step_given_user_has_added_items_to_their_cart(context):
    pass

@when("the user proceeds to checkout")
def step_when_user_proceeds_to_checkout(context):
    pass

@then("the user should be prompted to enter their shipping information")
def step_then_user_should_be_prompted_to_enter_their_shipping_information(context):
    pass

@then("the user should be able to review their order before submitting it")
def step_then_user_should_be_able_to_review_their_order_before_submitting_it(context):
    pass

@then("the user should receive a confirmation email after submitting the order")
def step_then_user_should_receive_a_confirmation_email_after_submitting_the_order(context):
    pass
