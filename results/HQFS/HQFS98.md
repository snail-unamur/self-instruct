# HQFS98
## Scenario
```gherkin
scenario: testing the login functionality 
   given a user is registered 
   when the user logs in with correct credentials 
   then the user should be logged in 
   and the user should be redirected to the homepage 
   when the user logs in with incorrect credentials 
   then the user should not be logged in 
   and the user should be shown an error message
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: testing the login functionality given a user is registered when the user logs in with correct credentials then the user should be logged in and the user should be redirected to the homepage when the user logs in with incorrect credentials then the user should not be logged in and the user should be shown an error message ```



from behave import given, when, then

@given("a user is registered")
def step_given_a_user_is_registered(context):
    pass

@when("the user logs in with correct credentials")
def step_when_the_user_logs_in_with_correct_credentials(context):
    pass

@then("the user should be logged in and the user should be redirected to the homepage")
def step_then_the_user_should_be_logged_in_and_the_user_should_be_redirected_to_the_homepage(context):
    pass

@when("the user logs in with incorrect credentials")
def step_when_the_user_logs_in_with_incorrect_credentials(context):
    pass

@then("the user should not be logged in and the user should be shown an error message")
def step_then_the_user_should_not_be_logged_in_and_the_user_should_be_shown_an_error_message(context):
    pass
