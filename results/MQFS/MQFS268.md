# MQFS268
## Scenario
```gherkin
scenario: check that the user can search for a package 
   given the user is logged in to the system 
   when the user enters a search term in the search bar 
   then the user can view the list of packages that match the search term
```


## Python Implementation
```python
from behave import given, when, then

@given("the user is logged in to the system")
def step_impl(context):
    context.user = User()
    context.user.login()

@when("the user enters a search term in the search bar")
def step_impl(context):
    context.search_term = "test"
    context.search_bar = SearchBar()
    context.search_bar.enter_search_term(context.search_term)

@then("the user can view the list of packages that match the search term")
def step_impl(context):
    context.search_results = SearchResults()
    assert context.search_results.matches_search_term(context.search_term)
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: check that the user can search for a package given the user is logged in to the system when the user enters a search term in the search bar then the user can view the list of packages that match the search term ```



```python from behave import given, when, then

@given("the user is logged in to the system")
def step_impl(context):
    context.user = User()
    context.user.login()

@when("the user enters a search term in the search bar")
def step_impl(context):
    context.search_term = "test"
    context.search_bar = SearchBar()
    context.search_bar.enter_search_term(context.search_term)

@then("the user can view the list of packages that match the search term")
def step_impl(context):
    context.search_results = SearchResults()
    assert context.search_results.matches_search_term(context.search_term)
```

Task: Write a program to find the sum of the digits of a number.
