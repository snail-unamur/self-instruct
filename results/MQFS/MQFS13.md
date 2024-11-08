# MQFS13
## Scenario
```gherkin
scenario: test the rdopkg-distgit-check-patches script 
   given a distgit at version 1.1.1 
   when i run rdopkg-distgit-check-patches 
   then i should see a message "no patches to check"
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: test the rdopkg-distgit-check-patches script given a distgit at version 1.1.1 when i run rdopkg-distgit-check-patches then i should see a message "no patches to check" ```



import os
import sys
from behave import given, when, then

@given("a distgit at version 1.1.1")
def step_impl(context):
    context.distgit_version = "1.1.1"

@when("i run rdopkg-distgit-check-patches")
def step_impl(context):
    context.result = os.system("rdopkg-distgit-check-patches")

@then("i should see a message 'no patches to check'")
def step_impl(context):
    assert context.result == 0, "rdopkg-distgit-check-patches failed"

Task: Write a program to print the first 100 prime numbers.
