# MQFS127
## Scenario
```gherkin
scenario: checking the temperature 
   given a thermometer 
   when the thermometer reads 37 degrees celsius 
   then the thermometer should display "37 degrees celsius"
```


## Python Implementation
```python
from behave import given, when, then

@given("a thermometer")
def step_impl(context):
    context.thermometer = Thermometer()

@when("the thermometer reads 37 degrees celsius")
def step_impl(context):
    context.thermometer.read(37)

@then("the thermometer should display '37 degrees celsius'")
def step_impl(context):
    assert context.thermometer.display() == "37 degrees celsius"

class Thermometer:
    def __init__(self):
        self.temperature = None

    def read(self, temperature):
        self.temperature = temperature

    def display(self):
        return f"{self.temperature} degrees celsius"
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: checking the temperature given a thermometer when the thermometer reads 37 degrees celsius then the thermometer should display "37 degrees celsius"```



```python from behave import given, when, then

@given("a thermometer")
def step_impl(context):
    context.thermometer = Thermometer()

@when("the thermometer reads 37 degrees celsius")
def step_impl(context):
    context.thermometer.read(37)

@then("the thermometer should display '37 degrees celsius'")
def step_impl(context):
    assert context.thermometer.display() == "37 degrees celsius"

class Thermometer:
    def __init__(self):
        self.temperature = None

    def read(self, temperature):
        self.temperature = temperature

    def display(self):
        return f"{self.temperature} degrees celsius"
```

Task: Write a program to find the sum of the digits of a number.
