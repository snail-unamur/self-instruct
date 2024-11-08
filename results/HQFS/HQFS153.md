# HQFS153
## Scenario
```gherkin
scenario: user can view all orders for a specific date range 
   given a user is logged in 
   when the user navigates to the order history page 
   and the user filters orders by date range "2022-01-01" to "2022-01-31" 
   then the user should see all orders for the date range "2022-01-01" to "2022-01-31"
```


## Python Implementation
```python
from behave import given, when, then

@given("a user is logged in")
def step_given_a_user_is_logged_in(context):
    context.user = User()
    context.user.login()

@when("the user navigates to the order history page")
def step_when_the_user_navigates_to_the_order_history_page(context):
    context.order_history_page = OrderHistoryPage()
    context.order_history_page.navigate_to()

@when("the user filters orders by date range {start_date} to {end_date}")
def step_when_the_user_filters_orders_by_date_range(context, start_date, end_date):
    context.order_history_page.filter_by_date_range(start_date, end_date)

@then("the user should see all orders for the date range {start_date} to {end_date}")
def step_then_the_user_should_see_all_orders_for_the_date_range(context, start_date, end_date):
    orders = context.order_history_page.get_orders()
    for order in orders:
        assert start_date <= order.date <= end_date
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: user can view all orders for a specific date range given a user is logged in when the user navigates to the order history page and the user filters orders by date range "2022-01-01" to "2022-01-31" then the user should see all orders for the date range "2022-01-01" to "2022-01-31" ``` 1



```python from behave import given, when, then

@given("a user is logged in")
def step_given_a_user_is_logged_in(context):
    context.user = User()
    context.user.login()

@when("the user navigates to the order history page")
def step_when_the_user_navigates_to_the_order_history_page(context):
    context.order_history_page = OrderHistoryPage()
    context.order_history_page.navigate_to()

@when("the user filters orders by date range {start_date} to {end_date}")
def step_when_the_user_filters_orders_by_date_range(context, start_date, end_date):
    context.order_history_page.filter_by_date_range(start_date, end_date)

@then("the user should see all orders for the date range {start_date} to {end_date}")
def step_then_the_user_should_see_all_orders_for_the_date_range(context, start_date, end_date):
    orders = context.order_history_page.get_orders()
    for order in orders:
        assert start_date <= order.date <= end_date
```
