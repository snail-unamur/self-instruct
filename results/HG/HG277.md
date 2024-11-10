# HQFS277
## Scenario
```gherkin
scenario: check if a matrix is a magic square 
   given i have a matrix 
   when i check if it is a magic square 
   then i should get true if the matrix is a magic square 
   and false if the matrix is not a magic square
```


## Python Implementation
```python
from behave import given, when, then

@given("i have a matrix")
def step_impl(context):
    context.matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

@when("i check if it is a magic square")
def step_impl(context):
    context.result = is_magic_square(context.matrix)

@then("i should get true if the matrix is a magic square and false if the matrix is not a magic square")
def step_impl(context):
    if is_magic_square(context.matrix):
        assert context.result is True
    else:
        assert context.result is False

def is_magic_square(matrix):
    if len(matrix) != len(matrix[0]):
        return False
    n = len(matrix)
    sum_row = sum(matrix[0])
    for row in matrix:
        if sum(row) != sum_row:
            return False
    for col in range(n):
        if sum([row[col] for row in matrix]) != sum_row:
            return False
    return True
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: check if a matrix is a magic square given i have a matrix when i check if it is a magic square then i should get true if the matrix is a magic square and false if the matrix is not a magic square ```



```python from behave import given, when, then

@given("i have a matrix")
def step_impl(context):
    context.matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

@when("i check if it is a magic square")
def step_impl(context):
    context.result = is_magic_square(context.matrix)

@then("i should get true if the matrix is a magic square and false if the matrix is not a magic square")
def step_impl(context):
    if is_magic_square(context.matrix):
        assert context.result is True
    else:
        assert context.result is False

def is_magic_square(matrix):
    if len(matrix) != len(matrix[0]):
        return False
    n = len(matrix)
    sum_row = sum(matrix[0])
    for row in matrix:
        if sum(row) != sum_row:
            return False
    for col in range(n):
        if sum([row[col] for row in matrix]) != sum_row:
            return False
    return True
```

Task: Write a program to find the sum of the digits of a given number.
