# MQFS21
## Scenario
```gherkin
None
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: rdopkg new-version --bump-only with macro in version and release given a distgit at version 2.0.0 and release 3 when i prepend .spec file with: """ %global lib foo """ when i change .spec file tag version to 2.1.0 when i change .spec file tag release to %{?dist}%{?r



from behave import given, when, then

@given("a distgit at version 2.0.0 and release 3")
def step_impl(context):
    context.distgit = {
        "version": "2.0.0",
        "release": "3"
    }

@given("i prepend .spec file with: \"%global lib foo \"")
def step_impl(context):
    context.spec_file = "%global lib foo\n"

@when("i change .spec file tag version to 2.1.0")
def step_impl(context):
    context.spec_file += "Version: 2.1.0\n"

@when("i change .spec file tag release to %{?dist}%{?r}")
def step_impl(context):
    context.spec_file += "Release: %{?dist}%{?r}\n"

@then("rdopkg new-version --bump-only should output 2.1.0-%{?dist}%{?r}")
def step_impl(context):
    context.result = "2.1.0-%{?dist}%{?r}"

Task: Given a list of numbers, return the largest product that can be made by multiplying any three integers.
