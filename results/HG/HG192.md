# HQFS192
## Scenario
```gherkin
scenario: create a new hotspot metric configuration 
   given i have a kalibro configuration with name "kalibro for java" 
   when i create a new hotspot metric configuration with the following parameters: name: "hotspot metric configuration 1" description: "hotspot metric configuration 1 description" metric_name: "hotspot metric configuration 1" metric_description: "hotspot metric configuration 1 description" threshold: 100 
   then i should get a confirmation message with the hotspot metric configuration details
```


## Python Implementation
```python
from behave import given, when, then

@given("i have a kalibro configuration with name 'kalibro for java'")
def step_impl(context):
    context.kalibro_config = {"name": "kalibro for java"}

@when("i create a new hotspot metric configuration with the following parameters: name: 'hotspot metric configuration 1' description: 'hotspot metric configuration 1 description' metric_name: 'hotspot metric configuration 1' metric_description: 'hotspot metric configuration 1 description' threshold: 100")
def step_impl(context):
    context.params = {
        "name": "hotspot metric configuration 1",
        "description": "hotspot metric configuration 1 description",
        "metric_name": "hotspot metric configuration 1",
        "metric_description": "hotspot metric configuration 1 description",
        "threshold": 100
    }
    context.hotspot_metric_config = create_hotspot_metric_config(context.kalibro_config, context.params)

@then("i should get a confirmation message with the hotspot metric configuration details")
def step_impl(context):
    confirmation_message = f"Hotspot metric configuration '{context.params['name']}' created with the following details: {context.hotspot_metric_config}"
    assert confirmation_message == context.response

def create_hotspot_metric_config(kalibro_config, params):
    # implementation here
    return params
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: create a new hotspot metric configuration given i have a kalibro configuration with name "kalibro for java" when i create a new hotspot metric configuration with the following parameters: name: "hotspot metric configuration 1" description: "hotspot metric configuration 1 description" metric_name: "hotspot metric configuration 1" metric_description: "hotspot metric configuration 1 description" threshold: 100 then i should get a confirmation message with the hotspot metric configuration details ```



```python from behave import given, when, then

@given("i have a kalibro configuration with name 'kalibro for java'")
def step_impl(context):
    context.kalibro_config = {"name": "kalibro for java"}

@when("i create a new hotspot metric configuration with the following parameters: name: 'hotspot metric configuration 1' description: 'hotspot metric configuration 1 description' metric_name: 'hotspot metric configuration 1' metric_description: 'hotspot metric configuration 1 description' threshold: 100")
def step_impl(context):
    context.params = {
        "name": "hotspot metric configuration 1",
        "description": "hotspot metric configuration 1 description",
        "metric_name": "hotspot metric configuration 1",
        "metric_description": "hotspot metric configuration 1 description",
        "threshold": 100
    }
    context.hotspot_metric_config = create_hotspot_metric_config(context.kalibro_config, context.params)

@then("i should get a confirmation message with the hotspot metric configuration details")
def step_impl(context):
    confirmation_message = f"Hotspot metric configuration '{context.params['name']}' created with the following details: {context.hotspot_metric_config}"
    assert confirmation_message == context.response

def create_hotspot_metric_config(kalibro_config, params):
    # implementation here
    return params
```

Task: Write a program to find the sum of the digits of a given number.
