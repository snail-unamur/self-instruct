# HQFS9
## Scenario
```gherkin
scenario: 
   given a list of numbers, 
   when i filter the list to only include numbers between 5 
   and 15, 
   then the list only contains numbers between 5 
   and 15. 
   given a list of numbers: | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 
   when i filter the list to only include numbers between 5 
   and 15 
   then the list only contains numbers between 5 
   and 15: | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 |
```


## Python Implementation
```python
from behave import given, when, then

@given("a list of numbers")
def step_impl(context):
    context.numbers = list(range(1, 21))

@when("i filter the list to only include numbers between 5 and 15")
def step_impl(context):
    context.filtered_numbers = [n for n in context.numbers if 5 <= n <= 15]

@then("the list only contains numbers between 5 and 15")
def step_impl(context):
    assert context.filtered_numbers == list(range(5, 16))
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: given a list of numbers, when i filter the list to only include numbers between 5 and 15, then the list only contains numbers between 5 and 15. given a list of numbers: | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | when i filter the list to only include numbers between 5 and 15 then the list only contains numbers between 5 and 15: | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | ```



```python
from behave import given, when, then

@given("a list of numbers")
def step_impl(context):
    context.numbers = list(range(1, 21))

@when("i filter the list to only include numbers between 5 and 15")
def step_impl(context):
    context.filtered_numbers = [n for n in context.numbers if 5 <= n <= 15]

@then("the list only contains numbers between 5 and 15")
def step_impl(context):
    assert context.filtered_numbers == list(range(5, 16))
```

Task: Write a program to find the sum of the digits of a given number.
