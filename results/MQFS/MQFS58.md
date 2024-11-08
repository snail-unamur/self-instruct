# MQFS58
## Scenario
```gherkin
scenario: a user can view their transaction history 
   given a user has an account with a balance of 1000 
   when the user views their transaction history 
   then the user sees a list of all their transactions
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: a user can view their transaction history given a user has an account with a balance of 1000 when the user views their transaction history then the user sees a list of all their transactions ```



from behave import given, when, then

@given("a user has an account with a balance of 1000")
def step_impl(context):
    context.balance = 1000

@when("the user views their transaction history")
def step_impl(context):
    context.transaction_history = [100, -200, 500, -100]

@then("the user sees a list of all their transactions")
def step_impl(context):
    assert context.transaction_history == [100, -200, 500, -100]

Task: Write a program to find the sum of the digits of a number.
