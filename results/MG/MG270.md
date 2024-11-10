# MQFS270
## Scenario
```gherkin
scenario: 
   given a user has a bank account with $1000 
   when the user withdraws $500 
   then the user should have $500 left in the account
```


## Python Implementation
```python
from behave import given, when, then

@given("a user has a bank account with ${amount}")
def step_impl(context, amount):
    context.balance = int(amount)

@when("the user withdraws ${amount}")
def step_impl(context, amount):
    context.balance -= int(amount)

@then("the user should have ${amount} left in the account")
def step_impl(context, amount):
    assert context.balance == int(amount)
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: given a user has a bank account with $1000 when the user withdraws $500 then the user should have $500 left in the account ```



```python from behave import given, when, then

@given("a user has a bank account with ${amount}")
def step_impl(context, amount):
    context.balance = int(amount)

@when("the user withdraws ${amount}")
def step_impl(context, amount):
    context.balance -= int(amount)

@then("the user should have ${amount} left in the account")
def step_impl(context, amount):
    assert context.balance == int(amount)
```

Task: Write a program to find the sum of the digits of a given number.
