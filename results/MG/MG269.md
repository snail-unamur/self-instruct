# MQFS269
## Scenario
```gherkin
scenario: 
   given a user is on the profile page 
   when the user updates their profile details 
   then the user's profile is updated 
   and the user is redirected to the profile page 
   when the user enters invalid profile details 
   then the user's profile is not updated 
   and an error message is displayed
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: given a user is on the profile page when the user updates their profile details then the user's profile is updated and the user is redirected to the profile page when the user enters invalid profile details then the user's profile is not updated and an error message is displayed ```



from behave import given, when, then

@given("a user is on the profile page")
def step_given_a_user_is_on_the_profile_page(context):
    context.user = User()
    context.user.go_to_profile_page()

@when("the user updates their profile details")
def step_when_the_user_updates_their_profile_details(context):
    context.user.update_profile_details()

@then("the user's profile is updated and the user is redirected to the profile page")
def step_then_the_user_profile_is_updated_and_the_user_is_redirected_to_the_profile_page(context):
    assert context.user.profile_is_updated()
    assert context.user.is_on_profile_page()

@when("the user enters invalid profile details")
def step_when_the_user_enters_invalid_profile_details(context):
    context.user.enter_invalid_profile_details()

@then("the user's profile is not updated and an error message is displayed")
def step_then_the_user_profile_is_not_updated_and_an_error_message_is_displayed(context):
    assert not context.user.profile_is_updated()
    assert context.user.error_message_is_displayed()
