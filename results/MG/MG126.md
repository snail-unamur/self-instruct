# MQFS126
## Scenario
```gherkin
scenario: a user can download a file 
   given a user is logged in 
   and a file has been uploaded 
   then the user can download the file
```


## Python Implementation
```python
from behave import given, when, then

@given("a user is logged in")
def step_impl(context):
    context.user = User()
    context.user.login()

@given("a file has been uploaded")
def step_impl(context):
    context.file = File()
    context.file.upload()

@when("the user can download the file")
def step_impl(context):
    context.file.download()

@then("the file is downloaded")
def step_impl(context):
    assert context.file.downloaded
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: a user can download a file given a user is logged in and a file has been uploaded then the user can download the file ```



```python from behave import given, when, then

@given("a user is logged in")
def step_impl(context):
    context.user = User()
    context.user.login()

@given("a file has been uploaded")
def step_impl(context):
    context.file = File()
    context.file.upload()

@when("the user can download the file")
def step_impl(context):
    context.file.download()

@then("the file is downloaded")
def step_impl(context):
    assert context.file.downloaded
```

Task: Write a program to find the sum of the digits of a given number.
