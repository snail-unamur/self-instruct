# HQFS21
## Scenario
```gherkin
scenario: 
   given i am logged in 
   when i click on my profile picture 
   then i should be able to view my profile
```


## Python Implementation
```python
from behave import given, when, then @given("i am logged in") def step_given_i_am_logged_in(context): pass @when("i click on my profile picture") def step_when_i_click_on_my_profile_picture(context): pass @then("i should be able to view my profile") def step_then_i_should_be_able_to_view_my_profile(context): pass
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: given i am logged in when i click on my profile picture then i should be able to view my profile ``` ```python from behave import given, when, then @given("i am logged in") def step_given_i_am_logged_in(context): pass @when("i click on my profile picture") def step_when_i_click_on_my_profile_picture(context): pass @then("i should be able to view my profile") def step_then_i_should_be_able_to_view_my_profile(context): pass ```



```python from behave import given, when, then @given("i am logged in") def step_given_i_am_logged_in(context): context.logged_in = True @when("i click on my profile picture") def step_when_i_click_on_my_profile_picture(context): context.profile_viewed = context.logged_in @then("i should be able to view my profile") def step_then_i_should_be_able_to_view_my_profile(context): assert context.profile_viewed == True ```

Task: Write a program to find the sum of the digits of a given number.
