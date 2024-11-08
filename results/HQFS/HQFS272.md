# HQFS272
## Scenario
```gherkin
scenario: testing a function that returns a list of integers 
   given a function that returns a list of integers 
   when i call the function with an argument of 5 
   then i should get a list of integers with a length of 5 
   and the first element should be 0 
   and the second element should be 1 
   and the third element should be 2 
   and the fourth element should be 3 
   and the fifth element should be 4
```


## Python Implementation
```python
from behave import given, when, then

@given("a function that returns a list of integers")
def step_impl(context):
    context.func = lambda x: list(range(x))

@when("i call the function with an argument of 5")
def step_impl(context):
    context.result = context.func(5)

@then("i should get a list of integers with a length of 5")
def step_impl(context):
    assert len(context.result) == 5

@then("the first element should be 0")
def step_impl(context):
    assert context.result[0] == 0

@then("the second element should be 1")
def step_impl(context):
    assert context.result[1] == 1

@then("the third element should be 2")
def step_impl(context):
    assert context.result[2] == 2

@then("the fourth element should be 3")
def step_impl(context):
    assert context.result[3] == 3

@then("the fifth element should be 4")
def step_impl(context):
    assert context.result[4] == 4
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: testing a function that returns a list of integers given a function that returns a list of integers when i call the function with an argument of 5 then i should get a list of integers with a length of 5 and the first element should be 0 and the second element should be 1 and the third element should be 2 and the fourth element should be 3 and the fifth element should be 4 ```



```python from behave import given, when, then

@given("a function that returns a list of integers")
def step_impl(context):
    context.func = lambda x: list(range(x))

@when("i call the function with an argument of 5")
def step_impl(context):
    context.result = context.func(5)

@then("i should get a list of integers with a length of 5")
def step_impl(context):
    assert len(context.result) == 5

@then("the first element should be 0")
def step_impl(context):
    assert context.result[0] == 0

@then("the second element should be 1")
def step_impl(context):
    assert context.result[1] == 1

@then("the third element should be 2")
def step_impl(context):
    assert context.result[2] == 2

@then("the fourth element should be 3")
def step_impl(context):
    assert context.result[3] == 3

@then("the fifth element should be 4")
def step_impl(context):
    assert context.result[4] == 4
```
