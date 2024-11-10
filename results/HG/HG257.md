# HQFS257
## Scenario
```gherkin
scenario: i can view a list of all users 
   given i am on the user list page 
   when i click the view all users button 
   then i should be taken to the user list page with a list of all users
```


## Python Implementation
```python
from behave import given, when, then @given("a house price search engine with july 2016 data") def step_impl(context): context.search_engine = housepricesearchengine(july_2016_data) @given("i am on the search page") def step_impl(context): context.browser.get("http://www.example.com/search") @when("i enter the start date of 14 july") def step_impl(context): context.browser.find_element_by_name("start_date").send_keys("14 july") @when("i enter an end date of 21 july") def step_impl(context): context.browser.find_element_by_name("end_date").send_keys("21 july") @when("i click the search button") def step_impl(context): context.browser.find_element_by_name("search").click() @then("all house prices should be for sales between 14 july and 21 july") def step_impl(context): house_prices = context.search_engine.search("14 july", "21 july") for house_price in house_prices: assert house_price.sale_date >= "14 july" and house_price.sale_date <= "21 july" @g
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: i can view a list of all users given i am on the user list page when i click the view all users button then i should be taken to the user list page with a list of all users ``` ```python from behave import given, when, then @given("a house price search engine with july 2016 data") def step_impl(context): context.search_engine = housepricesearchengine(july_2016_data) @given("i am on the search page") def step_impl(context): context.browser.get("http://www.example.com/search") @when("i enter the start date of 14 july") def step_impl(context): context.browser.find_element_by_name("start_date").send_keys("14 july") @when("i enter an end date of 21 july") def step_impl(context): context.browser.find_element_by_name("end_date").send_keys("21 july") @when("i click the search button") def step_impl(context): context.browser.find_element_by_name("search").click() @then("all house prices should be for sales between 14 july and 21 july") def step_impl(context): house_prices = context.search_engine.search("14 july", "21 july") for house_price in house_prices: assert house_price.sale_date >= "14 july" and house_price.sale_date <= "21 july" @g

```

```python from behave import given, when, then @given("i am on the user list page") def step_impl(context): context.browser.get("http://www.example.com/users") @when("i click the view all users button") def step_impl(context): context.browser.find_element_by_name("view_all_users").click() @then("i should be taken to the user list page with a list of all users") def step_impl(context): users = context.browser.find_elements_by_class_name("user") assert len(users) > 0
```

Task: Write a program to find the sum of the digits of a number.
