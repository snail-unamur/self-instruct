# HQFS24
## Scenario
```gherkin
scenario: a new file is created 
   given a directory exists 
   when a new file is created in the directory 
   then the file should be visible in the directory
```


## Python Implementation
```python
from behave import given, when, then

@given("a directory exists")
def step_impl(context):
    import os
    context.directory = "test_directory"
    if not os.path.exists(context.directory):
        os.makedirs(context.directory)

@when("a new file is created in the directory")
def step_impl(context):
    import os
    context.filename = "test_file.txt"
    context.filepath = os.path.join(context.directory, context.filename)
    with open(context.filepath, 'w') as file:
        file.write("Test content")

@then("the file should be visible in the directory")
def step_impl(context):
    import os
    assert os.path.exists(context.filepath)
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: a new file is created given a directory exists when a new file is created in the directory then the file should be visible in the directory ```



```python from behave import given, when, then

@given("a directory exists")
def step_impl(context):
    import os
    context.directory = "test_directory"
    if not os.path.exists(context.directory):
        os.makedirs(context.directory)

@when("a new file is created in the directory")
def step_impl(context):
    import os
    context.filename = "test_file.txt"
    context.filepath = os.path.join(context.directory, context.filename)
    with open(context.filepath, 'w') as file:
        file.write("Test content")

@then("the file should be visible in the directory")
def step_impl(context):
    import os
    assert os.path.exists(context.filepath)
```

Task: Write a program to find the sum of the digits of a given number.
