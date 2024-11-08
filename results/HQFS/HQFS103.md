# HQFS103
## Scenario
```gherkin
scenario: a user can search for a product 
   given i am a customer 
   when i search for a product with the keyword "shoes" 
   then i should see a list of all the products that match the keyword "shoes"
```


## Python Implementation
```python
from behave import given, when, then

@given("i am a customer")
def step_impl(context):
    pass

@when("i search for a product with the keyword 'shoes'")
def step_impl(context):
    context.search_results = context.app.search_for_product("shoes")

@then("i should see a list of all the products that match the keyword 'shoes'")
def step_impl(context):
    assert len(context.search_results) > 0
    for product in context.search_results:
        assert "shoes" in product.name.lower()
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: a user can search for a product given i am a customer when i search for a product with the keyword "shoes" then i should see a list of all the products that match the keyword "shoes" ```



```python from behave import given, when, then

@given("i am a customer")
def step_impl(context):
    pass

@when("i search for a product with the keyword 'shoes'")
def step_impl(context):
    context.search_results = context.app.search_for_product("shoes")

@then("i should see a list of all the products that match the keyword 'shoes'")
def step_impl(context):
    assert len(context.search_results) > 0
    for product in context.search_results:
        assert "shoes" in product.name.lower()
```

Task: Write a program to find the second largest number in a list.
