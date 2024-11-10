# HQFS141
## Scenario
```gherkin
scenario: checking the number of pieces on the board 
   given there are 5 pieces on the board 
   when i count the number of pieces on the board 
   then the number of pieces on the board should be 5
```


## Python Implementation
```python
from behave import given, when, then

@given("there are {num} pieces on the board")
def step(context, num):
    context.board = [0] * 5
    for i in range(int(num)):
        context.board[i] = 1

@when("i count the number of pieces on the board")
def step(context):
    context.count = 0
    for piece in context.board:
        context.count += piece

@then("the number of pieces on the board should be {num}")
def step(context, num):
    assert int(num) == context.count
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: checking the number of pieces on the board given there are 5 pieces on the board when i count the number of pieces on the board then the number of pieces on the board should be 5 ```



```python from behave import given, when, then

@given("there are {num} pieces on the board")
def step(context, num):
    context.board = [0] * 5
    for i in range(int(num)):
        context.board[i] = 1

@when("i count the number of pieces on the board")
def step(context):
    context.count = 0
    for piece in context.board:
        context.count += piece

@then("the number of pieces on the board should be {num}")
def step(context, num):
    assert int(num) == context.count
```

Task: Write a program to find the sum of the digits of a given number.
