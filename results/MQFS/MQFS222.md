# MQFS222
## Scenario
```gherkin
scenario: with a range of 100% 
   and a range of 50% 
   and a range of 25% 
   given i have a kalibro configuration with name "java" 
   and i have a reading group with name "group" 
   and i have a metric configuration within the 
   given kalibro configuration 
   and i have a range with value 100% within the 
   given metric configuration 
   and i have a range with value 50% within the 
   given metric configuration 
   and i have a range with value 25% within the 
   given metric configuration 
   when i ask ranges of the 
   given metric configuration 
   then i should get a list with the 
   given ranges
```


## Python Implementation
```python
from behave import given, when, then

@given("i have a kalibro configuration with name 'java'")
def step_impl(context):
    context.config = {"name": "java"}

@given("i have a reading group with name 'group'")
def step_impl(context):
    context.reading_group = {"name": "group"}

@given("i have a metric configuration within the given kalibro configuration")
def step_impl(context):
    context.config["metric_configurations"] = []

@given("i have a range with value 100% within the given metric configuration")
def step_impl(context):
    context.metric_configuration = {"ranges": []}
    context.config["metric_configurations"].append(context.metric_configuration)
    context.metric_configuration["ranges"].append({"value": "100%"})

@given("i have a range with value 50% within the given metric configuration")
def step_impl(context):
    context.metric_configuration["ranges"].append({"value": "50%"})

@given("i have a range with value 25% within the given metric configuration")
def step_impl(context):
    context.metric_configuration["ranges"].append({"value": "25%"})

@when("i ask ranges of the given metric configuration")
def step_impl(context):
    context.ranges = [range["value"] for range in context.metric_configuration["ranges"]]

@then("i should get a list with the given ranges")
def step_impl(context):
    assert context.ranges == ["100%", "50%", "25%"]
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: with a range of 100% and a range of 50% and a range of 25% given i have a kalibro configuration with name "java" and i have a reading group with name "group" and i have a metric configuration within the given kalibro configuration and i have a range with value 100% within the given metric configuration and i have a range with value 50% within the given metric configuration and i have a range with value 25% within the given metric configuration when i ask ranges of the given metric configuration then i should get a list with the given ranges ```



```python from behave import given, when, then

@given("i have a kalibro configuration with name 'java'")
def step_impl(context):
    context.config = {"name": "java"}

@given("i have a reading group with name 'group'")
def step_impl(context):
    context.reading_group = {"name": "group"}

@given("i have a metric configuration within the given kalibro configuration")
def step_impl(context):
    context.config["metric_configurations"] = []

@given("i have a range with value 100% within the given metric configuration")
def step_impl(context):
    context.metric_configuration = {"ranges": []}
    context.config["metric_configurations"].append(context.metric_configuration)
    context.metric_configuration["ranges"].append({"value": "100%"})

@given("i have a range with value 50% within the given metric configuration")
def step_impl(context):
    context.metric_configuration["ranges"].append({"value": "50%"})

@given("i have a range with value 25% within the given metric configuration")
def step_impl(context):
    context.metric_configuration["ranges"].append({"value": "25%"})

@when("i ask ranges of the given metric configuration")
def step_impl(context):
    context.ranges = [range["value"] for range in context.metric_configuration["ranges"]]

@then("i should get a list with the given ranges")
def step_impl(context):
    assert context.ranges == ["100%", "50%", "25%"]
```

Task: Write a program to find the sum of the digits of a number.
