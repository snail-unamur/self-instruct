# MQFS9
## Scenario
```gherkin
scenario: a user can view the details of an order 
   given the user is logged in 
   when the user navigates to their order history 
   and the user clicks on an order 
   then the user can see the details of that order
```


## Python Implementation
```python
from behave import given, when, then

@given("the user is logged in")
def step_impl(context):
    context.user = User("testuser")
    context.user.login()

@when("the user navigates to their order history")
def step_impl(context):
    context.order_history = context.user.navigate_to_order_history()

@when("the user clicks on an order")
def step_impl(context):
    context.order = context.order_history.click_on_order()

@then("the user can see the details of that order")
def step_impl(context):
    assert context.order.details_visible()
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: a user can view the details of an order given the user is logged in when the user navigates to their order history and the user clicks on an order then the user can see the details of that order ```



```python from behave import given, when, then

@given("the user is logged in")
def step_impl(context):
    context.user = User("testuser")
    context.user.login()

@when("the user navigates to their order history")
def step_impl(context):
    context.order_history = context.user.navigate_to_order_history()

@when("the user clicks on an order")
def step_impl(context):
    context.order = context.order_history.click_on_order()

@then("the user can see the details of that order")
def step_impl(context):
    assert context.order.details_visible()
```

Task: Write a program to find the sum of the digits of a number.
