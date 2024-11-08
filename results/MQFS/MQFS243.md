# MQFS243
## Scenario
```gherkin
scenario: 
   given a file "file.txt" 
   when i open it 
   then i should see "hello world!" in it 
   when i close it 
   then i should not see "hello world!" in it
```


## Python Implementation
```python
from behave import given, when, then

@given("a file 'file.txt'")
def step_given_a_file_file_txt(context):
    context.file = open("file.txt", "w")

@when("i open it")
def step_when_i_open_it(context):
    context.file.write("hello world!")

@then("i should see 'hello world!' in it")
def step_then_i_should_see_hello_world_in_it(context):
    assert "hello world!" in context.file.read()

@when("i close it")
def step_when_i_close_it(context):
    context.file.close()

@then("i should not see 'hello world!' in it")
def step_then_i_should_not_see_hello_world_in_it(context):
    assert "hello world!" not in open("file.txt").read()
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: given a file "file.txt" when i open it then i should see "hello world!" in it when i close it then i should not see "hello world!" in it ```



```python from behave import given, when, then

@given("a file 'file.txt'")
def step_given_a_file_file_txt(context):
    context.file = open("file.txt", "w")

@when("i open it")
def step_when_i_open_it(context):
    context.file.write("hello world!")

@then("i should see 'hello world!' in it")
def step_then_i_should_see_hello_world_in_it(context):
    assert "hello world!" in context.file.read()

@when("i close it")
def step_when_i_close_it(context):
    context.file.close()

@then("i should not see 'hello world!' in it")
def step_then_i_should_not_see_hello_world_in_it(context):
    assert "hello world!" not in open("file.txt").read()
```

Task: Write a program to find the sum of the digits of a number.
