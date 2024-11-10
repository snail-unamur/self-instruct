# HQFS191
## Scenario
```gherkin
scenario: testing the pagination 
   given a list of items with pagination 
   when i navigate to the next page 
   then i should see the next page of items 
   when i navigate to the previous page 
   then i should see the previous page of items
```


## Python Implementation
```python
from behave import given, when, then

@given("a list of items with pagination")
def step_impl(context):
    context.items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    context.current_page = 1
    context.page_size = 5

@when("i navigate to the next page")
def step_impl(context):
    context.current_page += 1
    context.items_on_page = context.items[(context.current_page - 1) * context.page_size: context.current_page * context.page_size]

@then("i should see the next page of items")
def step_impl(context):
    assert context.items_on_page == [6, 7, 8, 9, 10]

@when("i navigate to the previous page")
def step_impl(context):
    context.current_page -= 1
    context.items_on_page = context.items[(context.current_page - 1) * context.page_size: context.current_page * context.page_size]

@then("i should see the previous page of items")
def step_impl(context):
    assert context.items_on_page == [1, 2, 3, 4, 5]
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: testing the pagination given a list of items with pagination when i navigate to the next page then i should see the next page of items when i navigate to the previous page then i should see the previous page of items ```



```python from behave import given, when, then

@given("a list of items with pagination")
def step_impl(context):
    context.items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    context.current_page = 1
    context.page_size = 5

@when("i navigate to the next page")
def step_impl(context):
    context.current_page += 1
    context.items_on_page = context.items[(context.current_page - 1) * context.page_size: context.current_page * context.page_size]

@then("i should see the next page of items")
def step_impl(context):
    assert context.items_on_page == [6, 7, 8, 9, 10]

@when("i navigate to the previous page")
def step_impl(context):
    context.current_page -= 1
    context.items_on_page = context.items[(context.current_page - 1) * context.page_size: context.current_page * context.page_size]

@then("i should see the previous page of items")
def step_impl(context):
    assert context.items_on_page == [1, 2, 3, 4, 5]
```

Task: Write a program to find the sum of the digits of a given number.
