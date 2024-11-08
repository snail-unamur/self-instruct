# HQFS168
## Scenario
```gherkin
scenario: 
   given a user has a bank account with balance 1000 
   when the user withdraws 1500 
   then the balance should be 0 
   and an error message should be displayed 
   and the transaction should be recorded in the transaction history
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: given a user has a bank account with balance 1000 when the user withdraws 1500 then the balance should be 0 and an error message should be displayed and the transaction should be recorded in the transaction history ```



from behave import given, when, then

@given("a user has a bank account with balance 1000")
def step_given(context):
    context.balance = 1000

@when("the user withdraws 1500")
def step_when(context):
    context.withdrawal = 1500
    context.balance -= context.withdrawal

@then("the balance should be 0 and an error message should be displayed")
def step_then(context):
    assert context.balance == 0
    assert "Insufficient Funds" in context.message

@then("the transaction should be recorded in the transaction history")
def step_then(context):
    context.transaction_history.append(
        {"withdrawal": context.withdrawal, "balance": context.balance, "message": context.message}
    )

Task: Write a program to find the sum of the digits of a given number.
