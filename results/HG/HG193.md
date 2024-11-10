# HQFS193
## Scenario
```gherkin
scenario: 
   given a list of numbers, i want to find the average of the numbers 
   given a list of numbers: [1, 2, 3, 4, 5] 
   when i find the average of the numbers 
   then the average should be 3.0
```


## Python Implementation
```python
from behave import given, when, then @given("a list of numbers: {numbers}") def step_given(context, numbers): context.numbers = [int(x) for x in numbers.split(",")] @when("i find the average of the numbers") def step_when(context): context.average = sum(context.numbers) / len(context.numbers) @then("the average should be {avg}") def step_then(context, avg): assert context.average == float(avg)
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: given a list of numbers, i want to find the average of the numbers given a list of numbers: [1, 2, 3, 4, 5] when i find the average of the numbers then the average should be 3.0 ``` here is an example of how the python file for this scenario might look like: ```python from behave import given, when, then @given("a list of numbers: {numbers}") def step_given(context, numbers): context.numbers = [int(x) for x in numbers.split(",")] @when("i find the average of the numbers") def step_when(context): context.average = sum(context.numbers) / len(context.numbers) @then("the average should be {avg}") def step_then(context, avg): assert context.average == float(avg) ```



```python from behave import given, when, then @given("a list of numbers: {numbers}") def step_given(context, numbers): context.numbers = [int(x) for x in numbers.split(",")] @when("i find the average of the numbers") def step_when(context): context.average = sum(context.numbers) / len(context.numbers) @then("the average should be {avg}") def step_then(context, avg): assert context.average == float(avg) ```

Task: Write a program to find the sum of the digits of a number.
