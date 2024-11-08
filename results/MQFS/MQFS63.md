# MQFS63
## Scenario
```gherkin
scenario: testing the functionality of the order confirmation page 
   given i have successfully placed an order 
   when i am taken to the order confirmation page 
   then i should see a confirmation message that my order has been placed 
   and i should see a summary of my order



from behave import 
   given, 
   when, 
   then

@
   given("i have successfully placed an order")
def step_given_i_have_successfully_placed_an_order(context):
    pass

@
   when("i am taken to the order confirmation page")
def step_when_i_am_taken_to_the_order_confirmation_page(context):
    pass

@
   then("i should see a confirmation message that my order has been placed")
def step_then_i_should_see_a_confirmation_message_that_my_order_has_been_placed(context):
    pass

@
   then("i should see a summary of my order")
def step_then_i_should_see_a_summary_of_my_order(context):
    pass
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: testing the functionality of the order confirmation page given i have successfully placed an order when i am taken to the order confirmation page then i should see a confirmation message that my order has been placed and i should see a summary of my order



from behave import given, when, then

@given("i have successfully placed an order")
def step_given_i_have_successfully_placed_an_order(context):
    pass

@when("i am taken to the order confirmation page")
def step_when_i_am_taken_to_the_order_confirmation_page(context):
    pass

@then("i should see a confirmation message that my order has been placed")
def step_then_i_should_see_a_confirmation_message_that_my_order_has_been_placed(context):
    pass

@then("i should see a summary of my order")
def step_then_i_should_see_a_summary_of_my_order(context):
    pass

```
