# HQFS180
## Scenario
```gherkin
scenario: i can calculate the area of a rectangle 
   given i have the length 
   and width of a rectangle 
   when i calculate the area 
   then the area is calculated correctly
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: i can calculate the area of a rectangle given i have the length and width of a rectangle when i calculate the area then the area is calculated correctly ```



from behave import given, when, then

@given("i have the length and width of a rectangle")
def step_impl(context):
    context.length = 5
    context.width = 10

@when("i calculate the area")
def step_impl(context):
    context.area = context.length * context.width

@then("the area is calculated correctly")
def step_impl(context):
    assert context.area == 50
