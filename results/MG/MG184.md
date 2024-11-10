# MQFS184
## Scenario
```gherkin
scenario: 
   given i have a file named "file.txt" 
   when i run "cat file.txt" 
   then i should see the contents of the file printed to the console
```


## Python Implementation
```python
from behave import given, when, then

@given("i have a file named 'file.txt'")
def step_impl(context):
    context.file = open("file.txt", "w")
    context.file.write("This is the contents of the file")
    context.file.close()

@when("i run 'cat file.txt'")
def step_impl(context):
    context.result = context.text_runner.run("cat file.txt")

@then("i should see the contents of the file printed to the console")
def step_impl(context):
    assert "This is the contents of the file" in context.result
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: given i have a file named "file.txt" when i run "cat file.txt" then i should see the contents of the file printed to the console ```



```python from behave import given, when, then

@given("i have a file named 'file.txt'")
def step_impl(context):
    context.file = open("file.txt", "w")
    context.file.write("This is the contents of the file")
    context.file.close()

@when("i run 'cat file.txt'")
def step_impl(context):
    context.result = context.text_runner.run("cat file.txt")

@then("i should see the contents of the file printed to the console")
def step_impl(context):
    assert "This is the contents of the file" in context.result
```

Task: Write a program to find the sum of the digits of a given number.
