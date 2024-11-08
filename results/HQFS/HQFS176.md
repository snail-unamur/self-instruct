# HQFS176
## Scenario
```gherkin
scenario: a user can view their order history 
   given a user is logged in 
   when they go to their account page 
   and click on the 'order history' tab 
   then they should see a list of their previous orders 
   and they should be able to view the details of each order
```


## Python Implementation
```python
from behave import given, when, then

@given('a user is logged in')
def step_impl(context):
    context.user = User()
    context.user.login()

@when('they go to their account page')
def step_impl(context):
    context.account_page = AccountPage(context.driver)
    context.account_page.go_to()

@when('click on the "order history" tab')
def step_impl(context):
    context.order_history_page = context.account_page.click_order_history_tab()

@then('they should see a list of their previous orders')
def step_impl(context):
    assert context.order_history_page.orders_are_displayed()

@then('they should be able to view the details of each order')
def step_impl(context):
    for order in context.order_history_page.orders:
        context.order_details_page = context.order_history_page.click_order(order)
        assert context.order_details_page.is_displayed()
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: a user can view their order history given a user is logged in when they go to their account page and click on the 'order history' tab then they should see a list of their previous orders and they should be able to view the details of each order ```



```python from behave import given, when, then

@given('a user is logged in')
def step_impl(context):
    context.user = User()
    context.user.login()

@when('they go to their account page')
def step_impl(context):
    context.account_page = AccountPage(context.driver)
    context.account_page.go_to()

@when('click on the "order history" tab')
def step_impl(context):
    context.order_history_page = context.account_page.click_order_history_tab()

@then('they should see a list of their previous orders')
def step_impl(context):
    assert context.order_history_page.orders_are_displayed()

@then('they should be able to view the details of each order')
def step_impl(context):
    for order in context.order_history_page.orders:
        context.order_details_page = context.order_history_page.click_order(order)
        assert context.order_details_page.is_displayed()
```

Task: Write a program to find the sum of the digits of a given number.
