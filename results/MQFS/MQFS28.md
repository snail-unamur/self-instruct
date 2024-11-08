# MQFS28
## Scenario
```gherkin
scenario: testing the registration functionality 
   given the user is not registered 
   when the user navigates to the registration page 
   and enters valid registration information 
   then the user is registered 
   and logged in 
   when the user navigates to the registration page 
   and enters invalid registration information 
   then an error message is displayed 
   when the user is already registered 
   and navigates to the registration page 
   then the user is already registered 
   and taken to the homepage
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: testing the registration functionality given the user is not registered when the user navigates to the registration page and enters valid registration information then the user is registered and logged in when the user navigates to the registration page and enters invalid registration information then an error message is displayed when the user is already registered and navigates to the registration page then the user is already registered and taken to the homepage ```



from behave import given, when, then

@given("the user is not registered")
def step_given_the_user_is_not_registered(context):
    pass

@when("the user navigates to the registration page")
def step_when_the_user_navigates_to_the_registration_page(context):
    pass

@when("enters valid registration information")
def step_when_enters_valid_registration_information(context):
    pass

@then("the user is registered and logged in")
def step_then_the_user_is_registered_and_logged_in(context):
    pass

@when("enters invalid registration information")
def step_when_enters_invalid_registration_information(context):
    pass

@then("an error message is displayed")
def step_then_an_error_message_is_displayed(context):
    pass

@given("the user is already registered")
def step_given_the_user_is_already_registered(context):
    pass

@when("navigates to the registration page")
def step_when_the_user_navigates_to_the_registration_page_2(context):
    pass

@then("the user is already registered and taken to the homepage")
def step_then_the_user_is_already_registered_and_taken_to_the_homepage(context):
    pass
