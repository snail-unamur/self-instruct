# HQFS130
## Scenario
```gherkin
scenario: 
   given a user has a balance of 1000, 
   when the user transfers 500 to another user, 
   then the user's balance should be 500 
   given a user has a balance of 1000 
   when the user transfers 500 to another user 
   then the user's balance should be 500
```


## Python Implementation
```python
from behave import given, when, then

@given("a user has a balance of 1000")
def step_given(context):
    context.balance = 1000

@when("the user transfers 500 to another user")
def step_when(context):
    context.balance -= 500

@then("the user's balance should be 500")
def step_then(context):
    assert context.balance == 500
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: given a user has a balance of 1000, when the user transfers 500 to another user, then the user's balance should be 500 given a user has a balance of 1000 when the user transfers 500 to another user then the user's balance should be 500 ```



```python from behave import given, when, then

@given("a user has a balance of 1000")
def step_given(context):
    context.balance = 1000

@when("the user transfers 500 to another user")
def step_when(context):
    context.balance -= 500

@then("the user's balance should be 500")
def step_then(context):
    assert context.balance == 500
```

Task: Write a program to print the first 100 prime numbers.
