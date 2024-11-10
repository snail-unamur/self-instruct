# MQFS161
## Scenario
```gherkin
scenario: a user can sort a list of uploaded files 
   given a user is logged in 
   and files have been uploaded 
   when the user sorts the list of files 
   then the list of files should be sorted according to the selected criteria
```


## Python Implementation
```python
from behave import given, when, then

@given("a user is logged in and files have been uploaded")
def step_impl(context):
    context.user = User()
    context.user.login()
    context.files = [File(name) for name in ["file1.txt", "file2.txt", "file3.txt"]]
    context.files[0].upload()
    context.files[1].upload()
    context.files[2].upload()

@when("the user sorts the list of files")
def step_impl(context):
    context.sorted_files = sorted(context.files, key=lambda file: file.name)

@then("the list of files should be sorted according to the selected criteria")
def step_impl(context):
    assert context.sorted_files == [file for file in context.files if file.name in ["file1.txt", "file2.txt", "file3.txt"]]
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: a user can sort a list of uploaded files given a user is logged in and files have been uploaded when the user sorts the list of files then the list of files should be sorted according to the selected criteria ```



```python from behave import given, when, then

@given("a user is logged in and files have been uploaded")
def step_impl(context):
    context.user = User()
    context.user.login()
    context.files = [File(name) for name in ["file1.txt", "file2.txt", "file3.txt"]]
    context.files[0].upload()
    context.files[1].upload()
    context.files[2].upload()

@when("the user sorts the list of files")
def step_impl(context):
    context.sorted_files = sorted(context.files, key=lambda file: file.name)

@then("the list of files should be sorted according to the selected criteria")
def step_impl(context):
    assert context.sorted_files == [file for file in context.files if file.name in ["file1.txt", "file2.txt", "file3.txt"]]
```

Task: Write a program to find the sum of the digits of a number.
