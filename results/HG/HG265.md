# HQFS265
## Scenario
```gherkin
scenario: multiplying a vector by a scalar 
   given v is a vector of "1.0", "2.0", "3.0" 
   when i multiply v by 2 
   then i get a vector of "2.0", "4.0", "6.0"
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: multiplying a vector by a scalar given v is a vector of "1.0", "2.0", "3.0" when i multiply v by 2 then i get a vector of "2.0", "4.0", "6.0" ```



from behave import given, when, then

@given("v is a vector of '1.0', '2.0', '3.0'")
def step_given(context):
    context.v = [1.0, 2.0, 3.0]

@when("i multiply v by 2")
def step_when(context):
    context.result = [i * 2 for i in context.v]

@then("i get a vector of '2.0', '4.0', '6.0'")
def step_then(context):
    assert context.result == [2.0, 4.0, 6.0]

Task: Write a program to find the sum of the digits of a number.
