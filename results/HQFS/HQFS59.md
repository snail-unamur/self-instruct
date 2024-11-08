# HQFS59
## Scenario
```gherkin
None
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: testing the calculator given i have a calculator when i add 2 and 3 then the calculator returns 5 and i can add 2 and 3 again then the calculator returns 5 and i can add 2 and 3 again then the calculator returns 5 and i can add 2 and 3 again then the calculator returns 5 and i can add 2 and 3 again then the calculator returns 5 and i can add 2 and 3 again then the calculator returns 5 and i can add 2 and 3 again then the calculator returns 5 and i can add 2 and



from behave import given, when, then

@given("i have a calculator")
def step_given_i_have_a_calculator(context):
    context.calculator = Calculator()

@when("i add 2 and 3")
def step_when_i_add_2_and_3(context):
    context.result = context.calculator.add(2, 3)

@then("the calculator returns 5")
def step_then_the_calculator_returns_5(context):
    assert context.result == 5

@when("i can add 2 and 3 again")
def step_when_i_can_add_2_and_3_again(context):
    context.result = context.calculator.add(2, 3)

@then("the calculator returns 5")
def step_then_the_calculator_returns_5(context):
    assert context.result == 5

@when("i can add 2 and 3 again")
def step_when_i_can_add_2_and_3_again(context):
    context.result = context.calculator.add(2, 3)

@then("the calculator returns 5")
def step_then_the_calculator_returns_5(context):
    assert context.result == 5

@when("i can add 2 and 3 again")
def step_when_i_can_add_2_and_3_again(context):
    context.result = context.calculator.add(2, 3)

@then("the calculator returns 5")
def step_then_the_calculator_returns_5(context):
    assert context.result == 5

@when("i can add 2 and 3 again")
def step_when_i_can_add_2_and_3_again(context):
    context.result = context.calculator.add(2, 3)

@then("the calculator returns 5")
def step_then_the_calculator_returns_5
