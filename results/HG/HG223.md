# HQFS223
## Scenario
```gherkin
scenario: i can view the details of a house price 
   and i can see the address 
   and i can see the price 
   and i can see the date of sale 
   given a house price search engine with july 2016 data 
   and i am on the search page 
   when i enter the start date of 14 july 
   and i enter an end date of 21 july 
   and i click the search button 
   and i click on a house price 
   then i should be able to view the details of the house price 
   and i should be able to see the address 
   and i should be able to see the price 
   and i should be able to see the date of sale
```


## Python Implementation
```python
from behave import given, when, then

@given("a house price search engine with july 2016 data")
def step_impl(context):
    context.house_price_search_engine = HousePriceSearchEngine(july_2016_data)

@when("i am on the search page")
def step_impl(context):
    context.page = SearchPage()

@when("i enter the start date of 14 july")
def step_impl(context):
    context.page.enter_start_date("14 july")

@when("i enter an end date of 21 july")
def step_impl(context):
    context.page.enter_end_date("21 july")

@when("i click the search button")
def step_impl(context):
    context.page.click_search_button()

@when("i click on a house price")
def step_impl(context):
    context.page.click_house_price()

@then("i should be able to view the details of the house price")
def step_impl(context):
    assert context.page.is_displayed()

@then("i should be able to see the address")
def step_impl(context):
    assert context.page.address == "123 Main St"

@then("i should be able to see the price")
def step_impl(context):
    assert context.page.price == 500000

@then("i should be able to see the date of sale")
def step_impl(context):
    assert context.page.date_of_sale == "07/15/2016"
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: i can view the details of a house price and i can see the address and i can see the price and i can see the date of sale given a house price search engine with july 2016 data and i am on the search page when i enter the start date of 14 july and i enter an end date of 21 july and i click the search button and i click on a house price then i should be able to view the details of the house price and i should be able to see the address and i should be able to see the price and i should be able to see the date of sale ```



```python from behave import given, when, then

@given("a house price search engine with july 2016 data")
def step_impl(context):
    context.house_price_search_engine = HousePriceSearchEngine(july_2016_data)

@when("i am on the search page")
def step_impl(context):
    context.page = SearchPage()

@when("i enter the start date of 14 july")
def step_impl(context):
    context.page.enter_start_date("14 july")

@when("i enter an end date of 21 july")
def step_impl(context):
    context.page.enter_end_date("21 july")

@when("i click the search button")
def step_impl(context):
    context.page.click_search_button()

@when("i click on a house price")
def step_impl(context):
    context.page.click_house_price()

@then("i should be able to view the details of the house price")
def step_impl(context):
    assert context.page.is_displayed()

@then("i should be able to see the address")
def step_impl(context):
    assert context.page.address == "123 Main St"

@then("i should be able to see the price")
def step_impl(context):
    assert context.page.price == 500000

@then("i should be able to see the date of sale")
def step_impl(context):
    assert context.page.date_of_sale == "07/15/2016"
```

Task: Write a program to find the sum of the digits of a number.
