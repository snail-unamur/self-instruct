# HQFS285
## Scenario
```gherkin
scenario: i can search for a house price by date 
   given a house price search engine with data for july 2016 
   when i enter the date of 14 july 2016 
   then the search results should include all house prices for 14 july 2016
```


## Python Implementation
```python
from behave import given, when, then

@given("a house price search engine with data for july 2016")
def step_impl(context):
    context.search_engine = SearchEngine()
    context.search_engine.add_data(
        {"date": "14/07/2016", "price": 100000}
    )
    context.search_engine.add_data(
        {"date": "15/07/2016", "price": 105000}
    )
    context.search_engine.add_data(
        {"date": "16/07/2016", "price": 110000}
    )

@when("i enter the date of 14 july 2016")
def step_impl(context):
    context.search_results = context.search_engine.search("14/07/2016")

@then("the search results should include all house prices for 14 july 2016")
def step_impl(context):
    assert context.search_results == [
        {"date": "14/07/2016", "price": 100000}
    ]
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: i can search for a house price by date given a house price search engine with data for july 2016 when i enter the date of 14 july 2016 then the search results should include all house prices for 14 july 2016 ```



```python from behave import given, when, then

@given("a house price search engine with data for july 2016")
def step_impl(context):
    context.search_engine = SearchEngine()
    context.search_engine.add_data(
        {"date": "14/07/2016", "price": 100000}
    )
    context.search_engine.add_data(
        {"date": "15/07/2016", "price": 105000}
    )
    context.search_engine.add_data(
        {"date": "16/07/2016", "price": 110000}
    )

@when("i enter the date of 14 july 2016")
def step_impl(context):
    context.search_results = context.search_engine.search("14/07/2016")

@then("the search results should include all house prices for 14 july 2016")
def step_impl(context):
    assert context.search_results == [
        {"date": "14/07/2016", "price": 100000}
    ]
```

Task: Write a program to find the sum of the digits of a given number.
