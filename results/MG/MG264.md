# MQFS264
## Scenario
```gherkin
scenario: 
   given a file with the following content: 1 2 3 4 5 6 7 8 9 10 
   when i run the command: "python3 ppm_to_canvas.py file.ppm" 
   then i should get the following output: [1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 0, 0]
```


## Python Implementation
```python
from behave import given, when, then
import subprocess

@given("a file with the following content: {content}")
def step(context, content):
    context.content = content

@when("i run the command: \"python3 ppm_to_canvas.py {file}\"")
def step(context, file):
    context.result = subprocess.run(
        ["python3", "ppm_to_canvas.py", file],
        capture_output=True,
        text=True,
    )

@then("i should get the following output: {output}")
def step(context, output):
    lines = context.result.stdout.strip().split("\n")
    assert len(lines) == 1
    assert lines[0] == output
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: given a file with the following content: 1 2 3 4 5 6 7 8 9 10 when i run the command: "python3 ppm_to_canvas.py file.ppm" then i should get the following output: [1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 0, 0] ```



```python
from behave import given, when, then
import subprocess

@given("a file with the following content: {content}")
def step(context, content):
    context.content = content

@when("i run the command: \"python3 ppm_to_canvas.py {file}\"")
def step(context, file):
    context.result = subprocess.run(
        ["python3", "ppm_to_canvas.py", file],
        capture_output=True,
        text=True,
    )

@then("i should get the following output: {output}")
def step(context, output):
    lines = context.result.stdout.strip().split("\n")
    assert len(lines) == 1
    assert lines[0] == output
```

Task: Write a program to find the sum of the digits of a number.
