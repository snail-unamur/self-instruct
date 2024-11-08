# HQFS283
## Scenario
```gherkin
scenario: adding two numbers 
   given i have a calculator 
   and i have entered 5 into the calculator 
   and i have entered 3 into the calculator 
   when i press add 
   then the result should be 8 on the calculator screen
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: adding two numbers given i have a calculator and i have entered 5 into the calculator and i have entered 3 into the calculator when i press add then the result should be 8 on the calculator screen ```



from behave import given, when, then

@given("i have a calculator")
def step_given_i_have_a_calculator(context):
    context.calculator = Calculator()

@given("i have entered 5 into the calculator")
def step_given_i_have_entered_5_into_the_calculator(context):
    context.calculator.enter_number(5)

@given("i have entered 3 into the calculator")
def step_given_i_have_entered_3_into_the_calculator(context):
    context.calculator.enter_number(3)

@when("i press add")
def step_when_i_press_add(context):
    context.calculator.add()

@then("the result should be 8 on the calculator screen")
def step_then_the_result_should_be_8_on_the_calculator_screen(context):
    assert context.calculator.result == 8

class Calculator(object):
    def __init__(self):
        self.result = 0
        self.entered_numbers = []

    def enter_number(self, number):
        self.entered_numbers.append(number)

    def add(self):
        self.result = sum(self.entered_numbers)

Task: Write a program to find the sum of the digits of a number.
