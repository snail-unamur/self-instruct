# MQFS231
## Scenario
```gherkin
scenario: 
   given a file with the following content: |id|name|age| |1|john|30| |2|jane|25| 
   when i run the following command: |awk -f '|' '{print $2}' file.txt| 
   then i should get the following output: |name| |john| |jane|
```


## Python Implementation
```python
from behave import given, when, then

@given("a file with the following content:")
def step(context):
    context.file_content = """id|name|age|
1|john|30|
2|jane|25|"""

@when("i run the following command:")
def step(context):
    import subprocess
    context.result = subprocess.run(
        ['awk', '-F', '|', '{print $2}'],
        input=context.file_content,
        capture_output=True,
        text=True
    )

@then("i should get the following output:")
def step(context):
    expected_output = """name
john
jane
"""
    assert context.result.stdout == expected_output
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: given a file with the following content: |id|name|age| |1|john|30| |2|jane|25| when i run the following command: |awk -f '|' '{print $2}' file.txt| then i should get the following output: |name| |john| |jane| ```



```python from behave import given, when, then

@given("a file with the following content:")
def step(context):
    context.file_content = """id|name|age|
1|john|30|
2|jane|25|"""

@when("i run the following command:")
def step(context):
    import subprocess
    context.result = subprocess.run(
        ['awk', '-F', '|', '{print $2}'],
        input=context.file_content,
        capture_output=True,
        text=True
    )

@then("i should get the following output:")
def step(context):
    expected_output = """name
john
jane
"""
    assert context.result.stdout == expected_output
```

Task: Write a program to find the sum of the digits of a number.
