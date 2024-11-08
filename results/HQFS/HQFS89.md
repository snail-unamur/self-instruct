# HQFS89
## Scenario
```gherkin
scenario: 
   given i have a kalibro configuration with name "kalibro for java" 
   when i request for hotspot_metric_configurations of the 
   given kalibro configuration 
   then i should get a list with the 
   given hotspotmetricconfiguration
```


## Python Implementation
```python
from behave import given, when, then @given("i have a kalibro configuration with name {name}") def step_impl(context, name): # implementation here pass @when("i request for hotspot_metric_configurations of the given kalibro configuration") def step_impl(context): # implementation here pass @then("i should get a list with the given hotspotmetricconfiguration") def step_impl(context): # implementation here pass
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: given i have a kalibro configuration with name "kalibro for java" when i request for hotspot_metric_configurations of the given kalibro configuration then i should get a list with the given hotspotmetricconfiguration ``` ```python from behave import given, when, then @given("i have a kalibro configuration with name {name}") def step_impl(context, name): # implementation here pass @when("i request for hotspot_metric_configurations of the given kalibro configuration") def step_impl(context): # implementation here pass @then("i should get a list with the given hotspotmetricconfiguration") def step_impl(context): # implementation here pass ```



```python from behave import given, when, then @given("i have a kalibro configuration with name {name}") def step_impl(context, name):     context.kalibro_config = {"name": name} @when("i request for hotspot_metric_configurations of the given kalibro configuration") def step_impl(context):     context.hotspot_metric_configurations = [{"name": "hotspot1"}, {"name": "hotspot2"}] @then("i should get a list with the given hotspotmetricconfiguration") def step_impl(context):     assert context.hotspot_metric_configurations == context.response ```

Task: Write a program to find the sum of the digits of a given number.
