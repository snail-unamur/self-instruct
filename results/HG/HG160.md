# HQFS160
## Scenario
```gherkin
scenario: user registration 
   given a user is not registered 
   when the user registers 
   then the user is registered
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: user registration given a user is not registered when the user registers then the user is registered ``` here are the python implementations of the step functions for each of the given gherkin scenarios:



from behave import given, when, then

@given("a user is not registered")
def step_given_a_user_is_not_registered(context):
    context.user = User()
    context.user.is_registered = False

@when("the user registers")
def step_when_the_user_registers(context):
    context.user.register()

@then("the user is registered")
def step_then_the_user_is_registered(context):
    assert context.user.is_registered is True

Task: Write a program to find the sum of the digits of a given number.
