# HQFS186
## Scenario
```gherkin
scenario: user can delete their account 
   given user is logged in 
   when user navigates to their account settings 
   and user deletes their account 
   then user is logged out 
   and user cannot log back in 
   given user is logged in 
   when user navigates to their account settings 
   and user deletes their account 
   then user is logged out 
   and user cannot log back in
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: user can delete their account given user is logged in when user navigates to their account settings and user deletes their account then user is logged out and user cannot log back in given user is logged in when user navigates to their account settings and user deletes their account then user is logged out and user cannot log back in ```python from behave import given, when, then from behave.runner import context from behave.steps import step last_name_tag_exists = false @given("last name tag exists") def last_name_tag_exists_step(context: context): global last_name_tag_exists last_name_tag_exists = true @when("last name tag found") def last_name_tag_found_step(context: context): global last_name_tag_exists last_name_tag_exists = true @then("enter last name") def enter_last_name_step(context: context): global last_name_tag_exists if last_name_tag_exists: last_name = "morpheus" print(last_name)

Task: Write a program to find the sum of the digits of a given number.

def sum_of_digits(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum

Task: Write a program to find the sum of the digits of a given number using recursion.
