# HQFS246
## Scenario
```gherkin
scenario: 
   given a list of numbers, find the pair with the closest sum to a target number 
   given a list of numbers: [1, 2, 3, 4, 5] 
   and a target number: 10 
   when i find the pair with the closest sum to the target number 
   then the pair should be [5, 5]
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: given a list of numbers, find the pair with the closest sum to a target number given a list of numbers: [1, 2, 3, 4, 5] and a target number: 10 when i find the pair with the closest sum to the target number then the pair should be [5, 5] ```



from behave import given, when, then

@given("a list of numbers: {numbers} and a target number: {target}")
def step_impl(context, numbers, target):
    context.numbers = [int(i) for i in numbers.split(',')]
    context.target = int(target)

@when("i find the pair with the closest sum to the target number")
def step_impl(context):
    context.closest_pair = find_closest_pair(context.numbers, context.target)

@then("the pair should be {pair}")
def step_impl(context, pair):
    assert context.closest_pair == [int(i) for i in pair.split(',')]

def find_closest_pair(numbers, target):
    closest_pair = None
    closest_diff = float('inf')
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            pair_sum = numbers[i] + numbers[j]
            diff = abs(pair_sum - target)
            if diff < closest_diff:
                closest_diff = diff
                closest_pair = [numbers[i], numbers[j]]
    return closest_pair
