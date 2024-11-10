# MQFS162
## Scenario
```gherkin
scenario: user can filter products by category 
   given user is logged in 
   when user selects a category 
   then user is shown a list of products in that category
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: user can filter products by category given user is logged in when user selects a category then user is shown a list of products in that category ```



from behave import given, when, then

@given("user is logged in")
def step_impl(context):
    context.user = User()
    context.user.login()

@when("user selects a category")
def step_impl(context):
    context.category = Category()
    context.category.select()

@then("user is shown a list of products in that category")
def step_impl(context):
    assert context.category.products is not None

Task: Write a program to find the sum of the digits of a given number.
