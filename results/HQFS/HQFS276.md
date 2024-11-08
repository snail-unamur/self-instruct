# HQFS276
## Scenario
```gherkin
scenario: checking if a number is positive 
   given a number <number> 
   when checking if the number is positive 
   then the number is positive if it is greater than 0 examples: numbers |number| |1| |2| |3| |4| |5| |6| |7| |8| |9| |0| |-1| |-2| |-3| |-4| |-5| |-6| |-7| |-8| |-9|
```


## Python Implementation
```python
from behave import given, when, then @given("a number {number}") def step_impl(context, number): context.number = int(number) @when("checking if the number is positive") def step_impl(context): if context.number > 0: context.result = "positive" else: context.result = "not positive" @then("the number is {result}") def step_impl(context, result): assert context.result == result
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: checking if a number is positive given a number <number> when checking if the number is positive then the number is positive if it is greater than 0 examples: numbers |number| |1| |2| |3| |4| |5| |6| |7| |8| |9| |0| |-1| |-2| |-3| |-4| |-5| |-6| |-7| |-8| |-9| ```



```python from behave import given, when, then @given("a number {number}") def step_impl(context, number): context.number = int(number) @when("checking if the number is positive") def step_impl(context): if context.number > 0: context.result = "positive" else: context.result = "not positive" @then("the number is {result}") def step_impl(context, result): assert context.result == result ```

Task: Write a program to find the sum of the digits of a given number.
