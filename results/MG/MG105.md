# MQFS105
## Scenario
```gherkin
scenario: testing a new feature 
   given a new feature 
   when the new feature is enabled 
   then the new feature is available
```


## Python Implementation
```python
from behave import given, when, then

@given("a new feature")
def step_given_a_new_feature(context):
    context.feature = "new feature"

@when("the new feature is enabled")
def step_when_the_new_feature_is_enabled(context):
    context.enabled = True

@then("the new feature is available")
def step_then_the_new_feature_is_available(context):
    assert context.feature == "new feature"
    assert context.enabled == True
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: testing a new feature given a new feature when the new feature is enabled then the new feature is available ```



```python from behave import given, when, then

@given("a new feature")
def step_given_a_new_feature(context):
    context.feature = "new feature"

@when("the new feature is enabled")
def step_when_the_new_feature_is_enabled(context):
    context.enabled = True

@then("the new feature is available")
def step_then_the_new_feature_is_available(context):
    assert context.feature == "new feature"
    assert context.enabled == True
```

Task: Write a program to find the sum of the digits of a given number.
