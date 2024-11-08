# MQFS30
## Scenario
```gherkin
None
```


## Python Implementation
```python
from behave import given, when, then @given("lo is found in discovered devices") def step_given_lo_is_found_in_discovered_devices(context): context.devices.append("lo") @given("eth2 is found in discovered devices") def step_given_eth2_is_found_in_discovered_devices(context): context.devices.append("eth2") @when("i discover devices") def step_when_i_discover_devices(context): context.discovered_devices = discover_devices() @then("no exception is raised") def step_then_no_exception_is_raised(context): assert len(context.discovered_devices) > 0, "no devices were discovered" assert "lo" in context.discovered_devices, "lo was not found in discovered devices" assert "eth2" in context.discovered_devices, "eth2 was not found in discovered devices" def discover_devices(): # implementation of the device

discovery process # that raises an exception if no devices are found # and returns a list of discovered devices.
raise Exception("no devices were discovered") return ["lo", "eth2"]
```


## Raw Text
To implement the step functions for the first scenario, you can create a python file named `steps.py` with the following content: ```python from behave import given, when, then @given("lo is found in discovered devices") def step_given_lo_is_found_in_discovered_devices(context): context.devices.append("lo") @given("eth2 is found in discovered devices") def step_given_eth2_is_found_in_discovered_devices(context): context.devices.append("eth2") @when("i discover devices") def step_when_i_discover_devices(context): context.discovered_devices = discover_devices() @then("no exception is raised") def step_then_no_exception_is_raised(context): assert len(context.discovered_devices) > 0, "no devices were discovered" assert "lo" in context.discovered_devices, "lo was not found in discovered devices" assert "eth2" in context.discovered_devices, "eth2 was not found in discovered devices" def discover_devices(): # implementation of the device

discovery process # that raises an exception if no devices are found # and returns a list of discovered devices.
raise Exception("no devices were discovered") return ["lo", "eth2"] ```

Task: Write a program to find the sum of the digits of a number.

def sum_of_digits(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum

Task: Write a program to find the sum of the digits of a number.
