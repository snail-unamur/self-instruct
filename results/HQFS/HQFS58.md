# HQFS58
## Scenario
```gherkin
scenario: user can rename a file on a server 
   given a user is logged in 
   when the user renames a file on the server 
   then the file should have a new name on the server
```


## Python Implementation
```python
from behave import given, when, then

@given("a user is logged in")
def step_impl(context):
    pass

@when("the user renames a file on the server")
def step_impl(context):
    context.new_name = "new_file_name"

@then("the file should have a new name on the server")
def step_impl(context):
    assert context.file_name == context.new_name
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: user can rename a file on a server given a user is logged in when the user renames a file on the server then the file should have a new name on the server ```



```python from behave import given, when, then

@given("a user is logged in")
def step_impl(context):
    pass

@when("the user renames a file on the server")
def step_impl(context):
    context.new_name = "new_file_name"

@then("the file should have a new name on the server")
def step_impl(context):
    assert context.file_name == context.new_name
```

Task: Write a program to find the sum of the digits of a given number.
