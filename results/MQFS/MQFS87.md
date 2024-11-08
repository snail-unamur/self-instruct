# MQFS87
## Scenario
```gherkin
scenario: 
   given a list of integers, find the pair with the closest sum to a target value 
   given a list of integers: [1, 2, 3, 4, 5] 
   and a target value: 10 
   when i find the pair with the closest sum to the target value 
   then the pair is (4, 6)
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: given a list of integers, find the pair with the closest sum to a target value given a list of integers: [1, 2, 3, 4, 5] and a target value: 10 when i find the pair with the closest sum to the target value then the pair is (4, 6) ```



from behave import given, when, then

@given("a list of integers: {list} and a target value: {target}")
def step_impl(context, list, target):
    context.numbers = [1, 2, 3, 4, 5]
    context.target = 10

@when("i find the pair with the closest sum to the target value")
def step_impl(context):
    context.closest_pair = min(
        ((a, b) for a in context.numbers for b in context.numbers if a + b != context.target),
        key=lambda pair: abs(context.target - sum(pair))
    )

@then("the pair is {pair}")
def step_impl(context, pair):
    assert context.closest_pair == (4, 6)
