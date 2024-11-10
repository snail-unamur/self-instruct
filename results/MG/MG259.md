# MQFS259
## Scenario
```gherkin
scenario: testing the addition of two numbers 
   given i have two numbers <num1> 
   and <num2> 
   when i add them 
   then i should get the result <result> examples: |num1|num2|result| |2|3|5| |10|20|30| |100|200|300|
```


## Python Implementation
```python
from behave import given, when, then

@given("i have two numbers {num1} and {num2}")
def step(context, num1, num2):
    context.num1 = int(num1)
    context.num2 = int(num2)

@when("i add them")
def step(context):
    context.result = context.num1 + context.num2

@then("i should get the result {result}")
def step(context, result):
    assert context.result == int(result)
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: testing the addition of two numbers given i have two numbers <num1> and <num2> when i add them then i should get the result <result> examples: |num1|num2|result| |2|3|5| |10|20|30| |100|200|300| ```



```python from behave import given, when, then

@given("i have two numbers {num1} and {num2}")
def step(context, num1, num2):
    context.num1 = int(num1)
    context.num2 = int(num2)

@when("i add them")
def step(context):
    context.result = context.num1 + context.num2

@then("i should get the result {result}")
def step(context, result):
    assert context.result == int(result)
```

Task: Write a program to find the sum of the digits of a given number.
