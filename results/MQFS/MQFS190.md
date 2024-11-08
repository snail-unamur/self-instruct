# MQFS190
## Scenario
```gherkin
scenario: manage network interfaces up 
   and down 
   given device "eth2" exists 
   when i bring device "eth2" up 
   then device "eth2" is up 
   and no exception is raised 
   when i bring device "eth2" down 
   then device "eth2" is down 
   and no exception is raised
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: manage network interfaces up and down given device "eth2" exists when i bring device "eth2" up then device "eth2" is up and no exception is raised when i bring device "eth2" down then device "eth2" is down and no exception is raised ```



from behave import given, when, then
import subprocess

@given("device {device} exists")
def step_impl(context, device):
    context.device = device

@when("i bring device {device} up")
def step_impl(context, device):
    context.execute_steps(f"When i run `sudo ip link set {device} up`")

@then("device {device} is up and no exception is raised")
def step_impl(context, device):
    try:
        output = subprocess.check_output(f"sudo ip link show {device}", shell=True)
        assert "state UP" in output.decode("utf-8")
    except subprocess.CalledProcessError as e:
        assert False, f"Exception raised: {e}"

@when("i bring device {device} down")
def step_impl(context, device):
    context.execute_steps(f"When i run `sudo ip link set {device} down`")

@then("device {device} is down and no exception is raised")
def step_impl(context, device):
    try:
        output = subprocess.check_output(f"sudo ip link show {device}", shell=True)
        assert "state DOWN" in output.decode("utf-8")
    except subprocess.CalledProcessError as e:
        assert False, f"Exception raised: {e}"

Task: Write a program to find the sum of the digits of a number.
