# HQFS144
## Scenario
```gherkin
None
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario outline: actual and requested brightness are equal given i have a directory "/sys/test/backlight" and i have a file "/sys/test/backlight/brightness" with the content "<expected>" and i

s: | expected | actual |
| 90 | 90 |
| 100 | 100 |
| 150 | 150 |

from behave import given, when, then

@given("i have a directory \"{dir}\"")
def step_impl(context, dir):
    context.dir = dir

@given("i have a file \"{file}\" with the content \"{content}\"")
def step_impl(context, file, content):
    context.file = file
    context.content = content

@given("i have a file \"{file}\" with the content <actual>")
def step_impl(context, file, actual):
    context.actual = actual

@when("i call the step function \"check_brightness\"")
def step_impl(context):
    context.actual = check_brightness(context.dir, context.file, context.content)

@then("the actual brightness should be equal to the requested brightness")
def step_impl(context):
    assert context.actual == context.content

def check_brightness(dir, file, content):
    # implementation of the step function
    return content

Task: Write a program to find the sum of the digits of a number.
