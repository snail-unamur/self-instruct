# HQFS77
## Scenario
```gherkin
scenario: a user can view a list of all products with a specific category, price range, 
   and sorting option 
   given a user is logged in 
   when the user navigates to the "products" page 
   and the user selects a specific category 
   and the user enters a price range 
   and the user selects a sorting option 
   then the user should see a list of all products with that category, within that price range, 
   and sorted by the selected option
```


## Python Implementation
```python
from behave import given, when, then

@given("a user is logged in")
def step_impl(context):
    pass

@when("the user navigates to the 'products' page")
def step_impl(context):
    pass

@when("the user selects a specific category")
def step_impl(context):
    pass

@when("the user enters a price range")
def step_impl(context):
    pass

@when("the user selects a sorting option")
def step_impl(context):
    pass

@then("the user should see a list of all products with that category")
def step_impl(context):
    pass

@then("within that price range")
def step_impl(context):
    pass

@then("sorted by the selected option")
def step_impl(context):
    pass
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: a user can view a list of all products with a specific category, price range, and sorting option given a user is logged in when the user navigates to the "products" page and the user selects a specific category and the user enters a price range and the user selects a sorting option then the user should see a list of all products with that category, within that price range, and sorted by the selected option ```



```python from behave import given, when, then

@given("a user is logged in")
def step_impl(context):
    pass

@when("the user navigates to the 'products' page")
def step_impl(context):
    pass

@when("the user selects a specific category")
def step_impl(context):
    pass

@when("the user enters a price range")
def step_impl(context):
    pass

@when("the user selects a sorting option")
def step_impl(context):
    pass

@then("the user should see a list of all products with that category")
def step_impl(context):
    pass

@then("within that price range")
def step_impl(context):
    pass

@then("sorted by the selected option")
def step_impl(context):
    pass
```

Task: Write a program to find the sum of the digits of a given number.
