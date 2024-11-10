# MQFS3
## Scenario
```gherkin
scenario: user can cancel their order 
   given a user is logged in 
   when they navigate to their order history page 
   and select the cancel option for a specific order 
   then their order should be cancelled
```


## Python Implementation
```python
from behave import given, when, then

@given("a user is logged in")
def step_impl(context):
    context.user = User()
    context.user.login()

@when("they navigate to their order history page")
def step_impl(context):
    context.order_history_page = OrderHistoryPage(context.user)
    context.order_history_page.load()

@when("select the cancel option for a specific order")
def step_impl(context):
    context.order = context.order_history_page.get_order(1)
    context.order.cancel()

@then("their order should be cancelled")
def step_impl(context):
    assert context.order.is_cancelled()
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: user can cancel their order given a user is logged in when they navigate to their order history page and select the cancel option for a specific order then their order should be cancelled ```



```python from behave import given, when, then

@given("a user is logged in")
def step_impl(context):
    context.user = User()
    context.user.login()

@when("they navigate to their order history page")
def step_impl(context):
    context.order_history_page = OrderHistoryPage(context.user)
    context.order_history_page.load()

@when("select the cancel option for a specific order")
def step_impl(context):
    context.order = context.order_history_page.get_order(1)
    context.order.cancel()

@then("their order should be cancelled")
def step_impl(context):
    assert context.order.is_cancelled()
```

Task: Write a program to find the sum of the digits of a given number.
