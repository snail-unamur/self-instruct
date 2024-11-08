# MQFS257
## Scenario
```gherkin
None
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: testing a simple calculator given a calculator when i add 1 and 1 then the result should be 2 when i subtract 1 from 2 then the result should be 1 when i multiply 2 and 3 then the result should be 6 when i divide 4 by 2 then the result should be 2 when i divide 5 by 2 then the result should be 2.5 when i divide 0 by 2 then the result should be 0 when i divide 2 by 0 then the result should be "infinity" when i divide -2 by 0 then the result should be "-infinity" when i take the square root of 4 then the result should be 2 when i take the square root of 16 then the result should be 4 when i take the square root of -1 then the result should be "nan" when i take the square root of 0 then the result should be 0 when i take the sine of 0 then the result should be 0 when i take the sine of 90 then the result should be 1 when i take the sine of 180 then the result should be 0 when i take the sine of 270 then the result should be -1 when i take the sine of 360 then the result should be 0 when i take the cosine of 0 then the result should be 1 when i take the cosine of 90 then the result should be 0 when i take the cosine of 180 then the result should be -1 when i take the cosine of 270 then the result should be 0 when i take the cosine of 360 then the result should be 1 when i take the tangent of 0 then the result should be 0 when i take the tangent of 45 then the result should be 1 when i take the tangent of 90 then the result should be "infinity" when i take the tangent of 135 then the result should be -1 when i take the tangent of 180 then the result should be 0 when i take the tangent of 225 then the result should be

-1 when i take the tangent of 270 then the result should be "infinity" when i take the tangent of 315 then the result should be 1 when i take the tangent of 360 then the result should be 0

from behave import given, when, then

@given("a calculator")
def step_impl(context):
    context.calculator = Calculator()

@when("i add 1 and 1")
def step_impl(context):
    context.result = context.calculator.add(1, 1)

@then("the result should be 2")
def step_impl(context):
    assert context.result == 2

@when("i subtract 1 from 2")
def step_impl(context):
    context.result = context.calculator.subtract(2, 1)

@then("the result should be 1")
def step_impl(context):
    assert context.result == 1

@when("i multiply 2 and 3")
def step_impl(context):
    context.result = context.calculator.multiply(2, 3)

@then("the result should be 6")
def step_impl(context):
    assert context.result == 6

@when("i divide 4 by 2")
def step_impl(context):
    context.result = context.calculator.divide(4, 2)

@then("the result should be 2")
def step_impl(context):
    assert context.result == 2

@when("i divide 5 by 2")
def step_impl(context):
    context.result = context.calculator.divide(5, 2)

@then("the result should be 2.5")
def step_impl(context):
    assert context.result == 2.5

@when("i divide 0 by 2")
def step_impl(context):
    context.result = context.calculator.divide(0, 2)

@then("the result should be 0")
def step
