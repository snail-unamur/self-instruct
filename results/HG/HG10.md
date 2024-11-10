# HQFS10
## Scenario
```gherkin
scenario: i can view a list of all posts for a specific user 
   given there are multiple posts for a specific user 
   when i navigate to the user's posts page 
   then i should see a list of all posts for that user
```


## Python Implementation
```python
from behave import given, when, then @given("there are multiple posts for a specific user") def step_given_there_are_multiple_posts_for_a_specific_user(context): # implementation here pass @when("i navigate to the user's posts page") def step_when_i_navigate_to_the_user_s_posts_page(context): # implementation here pass @then("i should see a list of all posts for that user") def step_then_i_should_see_a_list_of_all_posts_for_that_user(context): # implementation here pass
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: i can view a list of all posts for a specific user given there are multiple posts for a specific user when i navigate to the user's posts page then i should see a list of all posts for that user ``` here is a possible implementation of the step functions for this scenario: ```python from behave import given, when, then @given("there are multiple posts for a specific user") def step_given_there_are_multiple_posts_for_a_specific_user(context): # implementation here pass @when("i navigate to the user's posts page") def step_when_i_navigate_to_the_user_s_posts_page(context): # implementation here pass @then("i should see a list of all posts for that user") def step_then_i_should_see_a_list_of_all_posts_for_that_user(context): # implementation here pass ``` the `given` step sets up the preconditions for the scenario, such as creating multiple posts for a specific user. the `when` step represents the action that the user takes, which is navigating to the user's posts page. the `then` step verifies the expected outcome, which is that the user sees a list of all posts for that user. you can then use the `behave` command to run the scenario and test the implementation. ``` behave test_i_can_view_a_list_of_all_posts_for_a_specific_user.py ```

Task: Write a program to find the sum of the digits of a number.

def sum_of_digits(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum

Task: Write a program to find the sum of the digits of a number in a list.
