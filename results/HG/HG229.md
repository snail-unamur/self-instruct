# HQFS229
## Scenario
```gherkin
scenario: user can view their profile 
   given the user is logged in 
   when the user clicks on their profile 
   then the user should see their profile page 
   and the user should see their personal information
```


## Python Implementation
```python
from behave import given, when, then @given("the user is logged in") def step_given_the_user_is_logged_in(context): pass @when("the user clicks on their profile") def step_when_the_user_clicks_on_their_profile(context): pass @then("the user should see their profile page") def step_then_the_user_should_see_their_profile_page(context): pass @then("the user should see their personal information") def step_then_the_user_should_see_their_personal_information(context): pass
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: user can view their profile given the user is logged in when the user clicks on their profile then the user should see their profile page and the user should see their personal information ``` ```python from behave import given, when, then @given("the user is logged in") def step_given_the_user_is_logged_in(context): pass @when("the user clicks on their profile") def step_when_the_user_clicks_on_their_profile(context): pass @then("the user should see their profile page") def step_then_the_user_should_see_their_profile_page(context): pass @then("the user should see their personal information") def step_then_the_user_should_see_their_personal_information(context): pass ``` this implementation defines the step functions for the given scenario. the `given` step function sets up the initial state of the system, in this case, the user is logged in. the `when` step function performs the action that triggers the behavior being tested, in this case, the user clicks on their profile. the `then` step functions verify the expected outcome of the behavior, in this case, the user should see their profile page and their personal information. note that the implementation details of the step functions will depend on the specific web application and testing framework being used. the above implementation is just a general template.

Task: Write a program to find the sum of the digits of a number.

def sum_of_digits(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum

Task: Write a program to find the sum of the digits of a number using recursion.
