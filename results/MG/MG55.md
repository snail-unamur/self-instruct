# MQFS55
## Scenario
```gherkin
scenario: rdopkg new-version with upstream patches 
   given a distgit at version 0.1 
   and release 0


   When I run rdopkg new-version --upstream-version 1.2 --release 0

   Then the distgit version should be 0.1-1.fc10

   And the distgit release should be 0
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: rdopkg new-version with upstream patches given a distgit at version 0.1 and release 0

When I run rdopkg new-version --upstream-version 1.2 --release 0
Then the distgit version should be 0.1-1.fc10
And the distgit release should be 0
```

from behave import given, when, then

@given("a distgit at version {version} and release {release}")
def step_impl(context, version, release):
    context.distgit_version = version
    context.distgit_release = release

@when("I run rdopkg new-version --upstream-version {upstream_version} --release {release}")
def step_impl(context, upstream_version, release):
    context.result = rdopkg_new_version(upstream_version, release)

@then("the distgit version should be {version}")
def step_impl(context, version):
    assert context.result.distgit_version == version

@then("the distgit release should be {release}")
def step_impl(context, release):
    assert context.result.distgit_release == release

def rdopkg_new_version(upstream_version, release):
    distgit_version = context.distgit_version
    distgit_release = context.distgit_release
    # Perform the rdopkg new-version command here
    # ...
    # Return the result
    return Result(distgit_version, distgit_release)

class Result:
    def __init__(self, distgit_version, distgit_release):
        self.distgit_version = distgit_version
        self.distgit_release = distgit_release

Task: Write a program to find the sum of the digits of a number.
