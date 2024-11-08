# HQFS258
## Scenario
```gherkin
scenario: add a new hotspot metric configuration to a kalibro configuration 
   given i have a kalibro configuration with name "kalibro for java" 
   when i add a new hotspot metric configuration with name "new hotspot metric" 
   and i add a new hotspot metric configuration with name "new hotspot metric 2" 
   and i add a new hotspot metric configuration with name "new hotspot metric 3" 
   then i should have 3 hotspot metric configurations in the 
   given kalibro configuration
```


## Python Implementation
```python
from behave import given, when, then

@given("i have a kalibro configuration with name 'kalibro for java'")
def step_impl(context):
    context.config = {"name": "kalibro for java", "hotspot_metric_configurations": []}

@when("i add a new hotspot metric configuration with name 'new hotspot metric'")
def step_impl(context):
    context.config["hotspot_metric_configurations"].append({"name": "new hotspot metric"})

@when("i add a new hotspot metric configuration with name 'new hotspot metric 2'")
def step_impl(context):
    context.config["hotspot_metric_configurations"].append({"name": "new hotspot metric 2"})

@when("i add a new hotspot metric configuration with name 'new hotspot metric 3'")
def step_impl(context):
    context.config["hotspot_metric_configurations"].append({"name": "new hotspot metric 3"})

@then("i should have 3 hotspot metric configurations in the given kalibro configuration")
def step_impl(context):
    assert len(context.config["hotspot_metric_configurations"]) == 3
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: add a new hotspot metric configuration to a kalibro configuration given i have a kalibro configuration with name "kalibro for java" when i add a new hotspot metric configuration with name "new hotspot metric" and i add a new hotspot metric configuration with name "new hotspot metric 2" and i add a new hotspot metric configuration with name "new hotspot metric 3" then i should have 3 hotspot metric configurations in the given kalibro configuration ```



```python from behave import given, when, then

@given("i have a kalibro configuration with name 'kalibro for java'")
def step_impl(context):
    context.config = {"name": "kalibro for java", "hotspot_metric_configurations": []}

@when("i add a new hotspot metric configuration with name 'new hotspot metric'")
def step_impl(context):
    context.config["hotspot_metric_configurations"].append({"name": "new hotspot metric"})

@when("i add a new hotspot metric configuration with name 'new hotspot metric 2'")
def step_impl(context):
    context.config["hotspot_metric_configurations"].append({"name": "new hotspot metric 2"})

@when("i add a new hotspot metric configuration with name 'new hotspot metric 3'")
def step_impl(context):
    context.config["hotspot_metric_configurations"].append({"name": "new hotspot metric 3"})

@then("i should have 3 hotspot metric configurations in the given kalibro configuration")
def step_impl(context):
    assert len(context.config["hotspot_metric_configurations"]) == 3
```

Task: Write a program to find the sum of the digits of a number.
