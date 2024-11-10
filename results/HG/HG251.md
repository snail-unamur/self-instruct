# HQFS251
## Scenario
```gherkin
scenario: multiplication 
   given i take the calculator 
   when i multiply 1 
   and 3 
   then the result should be 3 
   given i take the calculator 
   when i multiply 2 
   and 3 
   then the result should be 6 
   given i take the calculator 
   when i multiply 3 
   and 3 
   then the result should be 9
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: multiplication given i take the calculator when i multiply 1 and 3 then the result should be 3 given i take the calculator when i multiply 2 and 3 then the result should be 6 given i take the calculator when i multiply 3 and 3 then the result should be 9 ```



from behave import given, when, then

@given("i take the calculator")
def step_given_i_take_calculator(context):
    context.calculator = Calculator()

@when("i multiply {a} and {b}")
def step_when_i_multiply(context, a, b):
    context.result = context.calculator.multiply(int(a), int(b))

@then("the result should be {result}")
def step_then_the_result_should_be(context, result):
    assert context.result == int(result)

class Calculator:
    def multiply(self, a, b):
        return a * b
