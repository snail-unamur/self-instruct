# HQFS97
## Scenario
```gherkin
scenario: 
   given a list of strings, 
   when i sort them in lexicographical order, 
   then the list should be sorted in lexicographical order 
   given a list of strings: ["apple", "banana", "kiwi", "pineapple"] 
   when i sort the list in lexicographical order 
   then the sorted list should be: ["apple", "banana", "kiwi", "pineapple"]
```


## Python Implementation
```python
from behave import given, when, then

@given("a list of strings: {strings}")
def step_impl(context, strings):
    context.strings = strings.split(",")

@when("i sort them in lexicographical order")
def step_impl(context):
    context.sorted_strings = sorted(context.strings)

@then("the list should be sorted in lexicographical order")
def step_impl(context):
    assert context.sorted_strings == ["apple", "banana", "kiwi", "pineapple"]
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: given a list of strings, when i sort them in lexicographical order, then the list should be sorted in lexicographical order given a list of strings: ["apple", "banana", "kiwi", "pineapple"] when i sort the list in lexicographical order then the sorted list should be: ["apple", "banana", "kiwi", "pineapple"] ```



```python from behave import given, when, then

@given("a list of strings: {strings}")
def step_impl(context, strings):
    context.strings = strings.split(",")

@when("i sort them in lexicographical order")
def step_impl(context):
    context.sorted_strings = sorted(context.strings)

@then("the list should be sorted in lexicographical order")
def step_impl(context):
    assert context.sorted_strings == ["apple", "banana", "kiwi", "pineapple"]
```

Task: Write a program to find the sum of the digits of a given number.
