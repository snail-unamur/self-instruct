# MQFS33
## Scenario
```gherkin
scenario: test the sum function 
   given i have a sum function 
   when i input 1 
   and 2 
   then i should get 3 
   when i input 2 
   and 3 
   then i should get 5 
   when i input 3 
   and 4 
   then i should get 7
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: test the sum function given i have a sum function when i input 1 and 2 then i should get 3 when i input 2 and 3 then i should get 5 when i input 3 and 4 then i should get 7 ```



from behave import given, when, then

@given("i have a sum function")
def step_impl(context):
    context.sum_function = lambda x, y: x + y

@when("i input {arg1} and {arg2}")
def step_impl(context, arg1, arg2):
    context.result = context.sum_function(int(arg1), int(arg2))

@then("i should get {arg1}")
def step_impl(context, arg1):
    assert context.result == int(arg1)

Task: Write a program to find the sum of the digits of a given number.
