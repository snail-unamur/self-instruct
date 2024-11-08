# HQFS34
## Scenario
```gherkin
scenario: 
   given a list of numbers, 
   when i calculate the standard deviation of the list, 
   then the standard deviation should be the measure of the amount of variation or dispersion of a set of values
```


## Python Implementation
```python
from math import sqrt
from behave import given, when, then

@given('a list of numbers')
def step_impl(context):
    context.numbers = [1, 2, 3, 4, 5]

@when('I calculate the standard deviation of the list')
def step_impl(context):
    context.mean = sum(context.numbers) / len(context.numbers)
    context.squared_diffs = [(x - context.mean) ** 2 for x in context.numbers]
    context.std_dev = sqrt(sum(context.squared_diffs) / len(context.numbers))

@then('the standard deviation should be the measure of the amount of variation or dispersion of a set of values')
def step_impl(context):
    assert context.std_dev == pytest.approx(1.5811388300841898, abs=1e-5)
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: given a list of numbers, when i calculate the standard deviation of the list, then the standard deviation should be the measure of the amount of variation or dispersion of a set of values ```



```python from math import sqrt
from behave import given, when, then

@given('a list of numbers')
def step_impl(context):
    context.numbers = [1, 2, 3, 4, 5]

@when('I calculate the standard deviation of the list')
def step_impl(context):
    context.mean = sum(context.numbers) / len(context.numbers)
    context.squared_diffs = [(x - context.mean) ** 2 for x in context.numbers]
    context.std_dev = sqrt(sum(context.squared_diffs) / len(context.numbers))

@then('the standard deviation should be the measure of the amount of variation or dispersion of a set of values')
def step_impl(context):
    assert context.std_dev == pytest.approx(1.5811388300841898, abs=1e-5)
```

Task: Write a program to find the sum of digits of a given number.
