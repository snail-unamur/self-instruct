# MQFS224
## Scenario
```gherkin
scenario: testing a function that returns a boolean value 
   given a function that returns a boolean value 
   when i call the function with a valid input 
   then i should get true as the output 
   when i call the function with an invalid input 
   then i should get false as the output
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: testing a function that returns a boolean value given a function that returns a boolean value when i call the function with a valid input then i should get true as the output when i call the function with an invalid input then i should get false as the output ```



from behave import given, when, then

@given("a function that returns a boolean value")
def step_impl(context):
    context.func = lambda x: True if x > 0 else False

@when("i call the function with a valid input")
def step_impl(context):
    context.result = context.func(5)

@then("i should get true as the output")
def step_impl(context):
    assert context.result == True

@when("i call the function with an invalid input")
def step_impl(context):
    context.result = context.func(-5)

@then("i should get false as the output")
def step_impl(context):
    assert context.result == False
