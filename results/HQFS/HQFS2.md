# HQFS2
## Scenario
```gherkin
scenario: canceling an order 
   given i am logged in to my account 
   when i go to the 'order history' page 
   and i click the 'cancel' button next to a specific order 
   then the order should be canceled 
   and i should receive a confirmation message
```


## Python Implementation
```python
from behave import given, when, then

@given("i am logged in to my account")
def step_impl(context):
    context.login()

@when("i go to the 'order history' page")
def step_impl(context):
    context.go_to_order_history_page()

@when("i click the 'cancel' button next to a specific order")
def step_impl(context):
    context.click_cancel_button()

@then("the order should be canceled")
def step_impl(context):
    assert context.order.is_canceled()

@then("i should receive a confirmation message")
def step_impl(context):
    assert context.is_confirmation_message_displayed()
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: canceling an order given i am logged in to my account when i go to the 'order history' page and i click the 'cancel' button next to a specific order then the order should be canceled and i should receive a confirmation message ```



```python from behave import given, when, then

@given("i am logged in to my account")
def step_impl(context):
    context.login()

@when("i go to the 'order history' page")
def step_impl(context):
    context.go_to_order_history_page()

@when("i click the 'cancel' button next to a specific order")
def step_impl(context):
    context.click_cancel_button()

@then("the order should be canceled")
def step_impl(context):
    assert context.order.is_canceled()

@then("i should receive a confirmation message")
def step_impl(context):
    assert context.is_confirmation_message_displayed()
```

Task: Write a program to find the sum of the digits of a given number.
