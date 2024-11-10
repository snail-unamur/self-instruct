# MQFS139
## Scenario
```gherkin
scenario: testing the function of the 'ls' command 
   given a directory with the files "test.txt" 
   and "test2.txt" 
   when i run "ls" 
   then i should see "test.txt" 
   and "test2.txt" in the output
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: testing the function of the 'ls' command given a directory with the files "test.txt" and "test2.txt" when i run "ls" then i should see "test.txt" and "test2.txt" in the output ```



import os
import sys
from behave import given, when, then

@given("a directory with the files 'test.txt' and 'test2.txt'")
def step_given_a_directory_with_the_files_test_txt_and_test2_txt(context):
    context.directory = "test_directory"
    if not os.path.exists(context.directory):
        os.makedirs(context.directory)
    with open(os.path.join(context.directory, "test.txt"), "w") as file:
        file.write("test")
    with open(os.path.join(context.directory, "test2.txt"), "w") as file:
        file.write("test2")

@when("i run 'ls'")
def step_when_i_run_ls(context):
    context.output = subprocess.check_output(["ls", context.directory], stderr=subprocess.STDOUT, shell=True)

@then("i should see 'test.txt' and 'test2.txt' in the output")
def step_then_i_should_see_test_txt_and_test2_txt_in_the_output(context):
    assert "test.txt" in context.output.decode("utf-8")
    assert "test2.txt" in context.output.decode("utf-8")

Task: Write a program to find the sum of the digits of a number.
