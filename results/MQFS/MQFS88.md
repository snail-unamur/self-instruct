# MQFS88
## Scenario
```gherkin
scenario: testing the user creation functionality 
   given i am logged in 
   when i create a new user "jane doe" with the following data: | first name | last name | email | password | | "jane" | "doe" | "janedoe@gmail.com" | "password123" | 
   then the user "jane doe" should be created with the email "janedoe@gmail.com" 
   and password "password123" 
   and the user "jane doe" should be able to login with the email "janedoe@gmail.com" 
   and password "password123" 
   and the user "jane doe" should be able to update their profile information 
   and the user "jane doe" should be able to delete their account
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: testing the user creation functionality given i am logged in when i create a new user "jane doe" with the following data: | first name | last name | email | password | | "jane" | "doe" | "janedoe@gmail.com" | "password123" | then the user "jane doe" should be created with the email "janedoe@gmail.com" and password "password123" and the user "jane doe" should be able to login with the email "janedoe@gmail.com" and password "password123" and the user "jane doe" should be able to update their profile information and the user "jane doe" should be able to delete their account ```



```python
from behave import given, when, then

@given("i am logged in")
def step_given_i_am_logged_in(context):
    pass

@when("i create a new user \"jane doe\" with the following data:")
def step_when_i_create_a_new_user_jane_doe_with_the_following_data(context):
    context.execute_steps(
        """
        | Given the following user data:       |
        |   | first name | last name | email                  | password |
        |   | "jane"     | "doe"     | "janedoe@gmail.com"    | "password123" |
        | When I create a new user            |
        """
    )

@then("the user \"jane doe\" should be created with the email \"janedoe@gmail.com\" and password \"password123\"")
def step_then_the_user_jane_doe_should_be_created_with_the_email_janedoe_at_gmail_com_and_password_password123(context):
    assert context.user.email == "janedoe@gmail.com"
    assert context.user.password == "password123"

@then("the user \"jane doe\" should be able to login with the email \"janedoe@gmail.com\" and password \"password123\"")
def step_then_the_user_jane_doe_should_be_able_to_login_with_the_email_janedoe_at_gmail_com_and_password_password123(context):
    assert context.user.login("janedoe@gmail.com", "password123")

@then("the user \"jane doe\" should be able to update their profile information")
def step_then_the_user_jane_doe_should_be_able_to_update_their_profile_information(context):
    context.user.update_profile(first_name="jane", last_name="doe")

@
