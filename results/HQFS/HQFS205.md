# HQFS205
## Scenario
```gherkin
scenario: check the output of a function 
   given a function that returns the string "hello" 
   when i call the function 
   then the output of the function should be the string "hello"
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: check the output of a function given a function that returns the string "hello" when i call the function then the output of the function should be the string "hello" ```



from behave import given, when, then

@given("i call the function")
def step_impl(context):
    context.result = hello()

@when("the function returns the string 'hello'")
def step_impl(context):
    assert context.result == "hello"

@then("the output of the function should be the string 'hello'")
def step_impl(context):
    pass

def hello():
    return "hello"

Task: Write a program to find the sum of the digits of a given number.
