# MQFS273
## Scenario
```gherkin
scenario: 
   given i have a list of numbers [1, 2, 3, 4, 5] 
   when i calculate the sum of the list 
   then the sum should be 15
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: given i have a list of numbers [1, 2, 3, 4, 5] when i calculate the sum of the list then the sum should be 15 ``` here are the python implementations of the step functions for the given gherkin scenarios using the behave bdd testing framework:



from behave import given, when, then

@given("i have a list of numbers {numbers}")
def step_given(context, numbers):
    context.numbers = [int(i) for i in numbers.split(",")]

@when("i calculate the sum of the list")
def step_when(context):
    context.sum = sum(context.numbers)

@then("the sum should be {sum}")
def step_then(context, sum):
    assert context.sum == int(sum)

Task: Write a program to find the sum of the digits of a given number.
