# MQFS44
## Scenario
```gherkin
scenario: user logs in 
   given the user is on the login page 
   when the user enters their credentials correctly 
   then the user should be logged in 
   and the user should be redirected to their profile page
```


## Python Implementation
```python
from behave import given, when, then @given("a user is logged in") def step_given_a_user_is_logged_in(context): pass @when("the user navigates to the profile page") def step_when_the_user_navigates_to_the_profile_page(context): pass @then("the user should see their profile information displayed") def step_then_the_user_should_see_their_profile_information_displayed(context): pass @given("the spy is equipped with a silenced pistol") def step_given_the_spy_is_equipped_with_a_silenced_pistol(context): pass @when("approaching a guard from behind") def step_when_approaching_a_guard_from_behind(context): pass @then("the spy should incapacitate the guard silently") def step_then_the_spy_should_incapacitate_the_guard_silently(context): pass @given("a house price search engine with july 2016 data") def step_given_a_house_price_search_engine_with_july_2016_data(context): pass
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: user logs in given the user is on the login page when the user enters their credentials correctly then the user should be logged in and the user should be redirected to their profile page ``` ```python from behave import given, when, then @given("a user is logged in") def step_given_a_user_is_logged_in(context): pass @when("the user navigates to the profile page") def step_when_the_user_navigates_to_the_profile_page(context): pass @then("the user should see their profile information displayed") def step_then_the_user_should_see_their_profile_information_displayed(context): pass @given("the spy is equipped with a silenced pistol") def step_given_the_spy_is_equipped_with_a_silenced_pistol(context): pass @when("approaching a guard from behind") def step_when_approaching_a_guard_from_behind(context): pass @then("the spy should incapacitate the guard silently") def step_then_the_spy_should_incapacitate_the_guard_silently(context): pass @given("a house price search engine with july 2016 data") def step_given_a_house_price_search_engine_with_july_2016_data(context): pass

```

```python from behave import given, when, then @given("the user is on the login page") def step_given_the_user_is_on_the_login_page(context): pass @when("the user enters their credentials correctly") def step_when_the_user_enters_their_credentials_correctly(context): pass @then("the user should be logged in") def step_then_the_user_should_be_logged_in(context): pass @then("the user should be redirected to their profile page") def step_then_the_user_should_be_redirected_to_their_profile_page(context): pass ```

Task: Write a program to find the sum of the digits of a number.
