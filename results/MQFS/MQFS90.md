# MQFS90
## Scenario
```gherkin
None
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: check that the user can view the list of files in a package version given

Given a package version
    When the user views the list of files
    Then the user should see the list of files

from behave import given, when, then

@given("a package version")
def step_impl(context):
    context.package_version = "1.0.0"

@when("the user views the list of files")
def step_impl(context):
    context.files = ["file1.txt", "file2.txt", "file3.txt"]

@then("the user should see the list of files")
def step_impl(context):
    assert context.files == ["file1.txt", "file2.txt", "file3.txt"]

Task: Write a program to find the sum of the digits of a number.
