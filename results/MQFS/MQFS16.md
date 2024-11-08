# MQFS16
## Scenario
```gherkin
scenario: user can view their order history 
   given i am logged in 
   when i go to my order history page 
   then i should see a list of all my previous orders
```


## Python Implementation
```python
from behave import given, when, then

@given("i am logged in")
def step_impl(context):
    context.user = User()
    context.user.login()

@when("i go to my order history page")
def step_impl(context):
    context.order_history_page = OrderHistoryPage()
    context.order_history_page.load()

@then("i should see a list of all my previous orders")
def step_impl(context):
    assert context.order_history_page.orders == context.user.orders
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: user can view their order history given i am logged in when i go to my order history page then i should see a list of all my previous orders ```



```python from behave import given, when, then

@given("i am logged in")
def step_impl(context):
    context.user = User()
    context.user.login()

@when("i go to my order history page")
def step_impl(context):
    context.order_history_page = OrderHistoryPage()
    context.order_history_page.load()

@then("i should see a list of all my previous orders")
def step_impl(context):
    assert context.order_history_page.orders == context.user.orders
```

Task: Write a program to find the sum of the digits of a given number.
