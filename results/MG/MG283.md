# MQFS283
## Scenario
```gherkin
scenario: a user can add a new book to the library 
   given the library has 3 books 
   when a user adds a new book 
   then the library should have 4 books
```


## Python Implementation
```python
from behave import given, when, then

@given("the library has 3 books")
def step_impl(context):
    context.library = [1, 2, 3]

@when("a user adds a new book")
def step_impl(context):
    context.library.append(4)

@then("the library should have 4 books")
def step_impl(context):
    assert context.library == [1, 2, 3, 4]
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: a user can add a new book to the library given the library has 3 books when a user adds a new book then the library should have 4 books ```



```python from behave import given, when, then

@given("the library has 3 books")
def step_impl(context):
    context.library = [1, 2, 3]

@when("a user adds a new book")
def step_impl(context):
    context.library.append(4)

@then("the library should have 4 books")
def step_impl(context):
    assert context.library == [1, 2, 3, 4]
```

Task: Write a program to find the second largest number in a list.
