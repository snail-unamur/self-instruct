# HQFS26
## Scenario
```gherkin
scenario: vending machine does not return change 
   when insufficient funds are inserted


   Given the vending machine has a price of 1.50

   And I insert 1.00

   When I request change

   Then I should be told there is no change to return
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: vending machine does not return change when insufficient funds are inserted

Given the vending machine has a price of 1.50
And I insert 1.00
When I request change
Then I should be told there is no change to return
```

from behave import given, when, then

@given("the vending machine has a price of 1.50")
def step_given(context):
    context.price = 1.50

@given("I insert 1.00")
def step_given(context):
    context.inserted = 1.00

@when("I request change")
def step_when(context):
    context.change = context.inserted - context.price

@then("I should be told there is no change to return")
def step_then(context):
    assert context.change < 0, "Change is {}".format(context.change)

Task: Write a program to find the sum of the digits of a given number.
