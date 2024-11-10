# HQFS250
## Scenario
```gherkin
scenario: testing the "isdisjoint" method of the "set" class 
   given two "set" classes with "isdisjoint" method 
   when i call the "isdisjoint" method of the two "set" classes 
   then it returns true if the sets have no elements in common 
   and false otherwise
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: testing the "isdisjoint" method of the "set" class given two "set" classes with "isdisjoint" method when i call the "isdisjoint" method of the two "set" classes then it returns true if the sets have no elements in common and false otherwise ```



from behave import given, when, then

@given("two 'set' classes with 'isdisjoint' method")
def step_impl(context):
    context.set1 = set([1, 2, 3])
    context.set2 = set([4, 5, 6])

@when("i call the 'isdisjoint' method of the two 'set' classes")
def step_impl(context):
    context.result = context.set1.isdisjoint(context.set2)

@then("it returns true if the sets have no elements in common and false otherwise")
def step_impl(context):
    assert context.result == True

@given("two 'set' classes with 'isdisjoint' method and common elements")
def step_impl(context):
    context.set1 = set([1, 2, 3])
    context.set2 = set([3, 4, 5])

@when("i call the 'isdisjoint' method of the two 'set' classes")
def step_impl(context):
    context.result = context.set1.isdisjoint(context.set2)

@then("it returns false")
def step_impl(context):
    assert context.result == False
