# HQFS158
## Scenario
```gherkin
None
```


## Python Implementation
```python
from behave import given, when, then @given("a1 is a tuple of {value1},{value2},{value3},{value4}") def step_given_a1_is_a_tuple_of_value1_value2_value3_value4(context, value1, value2, value3, value4): context.a1 = (float(value1), float(value2), float(value3), float(value4)) @given("a2 is a tuple of {value1},{value2},{value3},{value4}") def step_given_a2_is_a_tuple_of_value1_value2_value3_value4(context, value1, value2, value3, value4): context.a2 = (float(value1), float(value2), float(value3), float(value4)) @when("a1 + a2 is a tuple of {value1},{value2},{value3},{value4}") def step_when_a1_plus_a2_is_a_tuple_of_value1_value2_value3_value4(context, value1, value2, value3, value4): context.result = (float(value1), float(value2), float(value3), float(value4)) @then("a1 + a2 is a tuple of {value1},{value2},{value3},{value4}") def step_then_a1_plus_a2_is_a_tuple_of_value1_value2_value3_value4(context, value1, value2, value3, value4): assert context.result == (float(value1), float(value2), float(value3), float(value4))
```


## Raw Text
Adding two tuples ```python from behave import given, when, then @given("a1 is a tuple of {value1},{value2},{value3},{value4}") def step_given_a1_is_a_tuple_of_value1_value2_value3_value4(context, value1, value2, value3, value4): context.a1 = (float(value1), float(value2), float(value3), float(value4)) @given("a2 is a tuple of {value1},{value2},{value3},{value4}") def step_given_a2_is_a_tuple_of_value1_value2_value3_value4(context, value1, value2, value3, value4): context.a2 = (float(value1), float(value2), float(value3), float(value4)) @when("a1 + a2 is a tuple of {value1},{value2},{value3},{value4}") def step_when_a1_plus_a2_is_a_tuple_of_value1_value2_value3_value4(context, value1, value2, value3, value4): context.result = (float(value1), float(value2), float(value3), float(value4)) @then("a1 + a2 is a tuple of {value1},{value2},{value3},{value4}") def step_then_a1_plus_a2_is_a_tuple_of_value1_value2_value3_value4(context, value1, value2, value3, value4): assert context.result == (float(value1), float(value2), float(value3), float(value4)) ```



```
def test_step_given_a1_is_a_tuple_of_value1_value2_value3_value4():
    context = StepContext()
    context.a1 = (1.0, 2.0, 3.0, 4.0)
    step_given_a1_is_a_tuple_of_value1_value2_value3_value4(context, '1', '2', '3', '4')
    assert context.a1 == (1.0, 2.0, 3.0, 4.0)

def test_step_given_a2_is_a_tuple_of_value1_value2_value3_value4():
    context = StepContext()
    context.a2 = (1.0, 2.0, 3.0, 4.0)
    step_given_a2_is_a_tuple_of_value1_value2_value3_value4(context, '1', '2', '3', '4')
    assert context.a2 == (1.0, 2.0, 3.0, 4.0)

def test_step_when_a1_plus_a2_is_a_tuple_of_value1_value2_value3_value4():
    context = StepContext()
    context.a1 = (1.0, 2.0, 3.0, 4.0)
    context.a2 = (1.0, 2.0, 3.0, 4.0)
    step_when_a1_plus_a2_is_a_tuple_of_value1_value2_value3_value4(context, '2', '4', '6', '8')
    assert context.result == (2.0, 4.0, 6.0, 8.0)

def test_step_then_a1_plus_a2_is_a_tuple_of_value1_value2_value3_value4():
    context = StepContext()
    context.result = (2.0, 4
