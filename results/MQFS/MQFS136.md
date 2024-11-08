# MQFS136
## Scenario
```gherkin
scenario: rdopkg build 
   given a distgit repository exists 
   when i run rdopkg build 
   then a new rpm is created 
   then the rpm is uploaded to koji 
   then the rpm is available in koji
```


## Python Implementation
```python
from behave import given, when, then

@given("a distgit repository exists")
def step_impl(context):
    pass

@when("i run rdopkg build")
def step_impl(context):
    pass

@then("a new rpm is created")
def step_impl(context):
    pass

@then("the rpm is uploaded to koji")
def step_impl(context):
    pass

@then("the rpm is available in koji")
def step_impl(context):
    pass
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: rdopkg build given a distgit repository exists when i run rdopkg build then a new rpm is created then the rpm is uploaded to koji then the rpm is available in koji ```



```python from behave import given, when, then

@given("a distgit repository exists")
def step_impl(context):
    pass

@when("i run rdopkg build")
def step_impl(context):
    pass

@then("a new rpm is created")
def step_impl(context):
    pass

@then("the rpm is uploaded to koji")
def step_impl(context):
    pass

@then("the rpm is available in koji")
def step_impl(context):
    pass
```

Task: Write a program to find the sum of the digits of a given number.
