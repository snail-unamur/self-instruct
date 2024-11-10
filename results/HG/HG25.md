# HQFS25
## Scenario
```gherkin
None
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: given a list of numbers, when i find the range, then the range should be correct given [1, 2, 3, in general, the cost of living is higher in the city than in the country. | city | country | | --- | --- | | 1000 | 500 | | 1500 | 750 | |



from behave import given, when, then

@given("a list of numbers")
def step_impl(context):
    context.numbers = [1, 2, 3]

@when("i find the range")
def step_impl(context):
    context.range = max(context.numbers) - min(context.numbers)

@then("the range should be correct")
def step_impl(context):
    assert context.range == 2
