# MQFS260
## Scenario
```gherkin
scenario: testing the login functionality 
   given the user is on the login page 
   when the user enters the correct username 
   and password 
   and clicks on the login button 
   then the user should be taken to the home page
```


## Python Implementation
```python
from behave import given, when, then @given("the user is on the login page") def step_given_user_is_on_login_page(context): # implementation to navigate to the login page pass @when("the user enters the correct username and password") def step_when_user_enters_credentials(context): # implementation to enter the correct username and password pass @when("clicks on the login button") def step_when_user_clicks_login_button(context): # implementation to click on the login button pass @then("the user should be taken to the home page") def step_then_user_is_taken_to_home_page(context): # implementation to verify that the user is taken to the home page pass
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: testing the login functionality given the user is on the login page when the user enters the correct username and password and clicks on the login button then the user should be taken to the home page ``` here is the python implementation of the step functions for the given gherkin scenario using the behave bdd testing framework: ```python from behave import given, when, then @given("the user is on the login page") def step_given_user_is_on_login_page(context): # implementation to navigate to the login page pass @when("the user enters the correct username and password") def step_when_user_enters_credentials(context): # implementation to enter the correct username and password pass @when("clicks on the login button") def step_when_user_clicks_login_button(context): # implementation to click on the login button pass @then("the user should be taken to the home page") def step_then_user_is_taken_to_home_page(context): # implementation to verify that the user is taken to the home page pass ```

Task: Write a program to find the sum of the digits of a given number.

def sum_of_digits(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum

Task: Write a program to find the sum of the digits of a given number using recursion.
