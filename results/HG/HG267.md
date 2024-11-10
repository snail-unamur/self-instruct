# HQFS267
## Scenario
```gherkin
scenario: a user can filter their transaction history by date 
   given i am logged in 
   and i am on the transaction history page 
   when i select a date range 
   then i should see only the transactions within that date range
```


## Python Implementation
```python
from behave import given, when, then

@given("i am logged in and i am on the transaction history page")
def step_impl(context):
    pass

@when("i select a date range")
def step_impl(context):
    pass

@then("i should see only the transactions within that date range")
def step_impl(context):
    pass
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: a user can filter their transaction history by date given i am logged in and i am on the transaction history page when i select a date range then i should see only the transactions within that date range ```



```python from behave import given, when, then

@given("i am logged in and i am on the transaction history page")
def step_impl(context):
    pass

@when("i select a date range")
def step_impl(context):
    pass

@then("i should see only the transactions within that date range")
def step_impl(context):
    pass
```

Task: Write a program to find the sum of the digits of a given number.
