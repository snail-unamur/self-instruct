# HQFS188
## Scenario
```gherkin
scenario: a user can register 
   and login 
   given we have a user with email "user@example.com" 
   and the user is not registered 
   when

the user navigates to the registration page
the user enters their email "user@example.com"
the user clicks the register button

   then the user should be registered

   and the user should be logged in


   given we have a user with email "user@example.com" 
   and the user is not registered 
   when
the user navigates to the login page
the user enters their email "user@example.com"
the user clicks the login button

   then the user should not be logged in


   given we have a user with email "user@example.com" 
   and the user is registered 
   when
the user navigates to the login page
the user enters their email "user@example.com"
the user clicks the login button

   then the user should be logged in


   given we have a user with email "user@example.com" 
   and the user is logged in 
   when
the user navigates to the profile page

   then the user should see their profile page


   given we have a user with email "user@example.com" 
   and the user is logged in 
   when
the user navigates to the logout page
the user clicks the logout button

   then the user should not be logged in
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: a user can register and login given we have a user with email "user@example.com" and the user is not registered when

the user navigates to the registration page
the user enters their email "user@example.com"
the user clicks the register button
then the user should be registered
and the user should be logged in

given we have a user with email "user@example.com" and the user is not registered when
the user navigates to the login page
the user enters their email "user@example.com"
the user clicks the login button
then the user should not be logged in

given we have a user with email "user@example.com" and the user is registered when
the user navigates to the login page
the user enters their email "user@example.com"
the user clicks the login button
then the user should be logged in

given we have a user with email "user@example.com" and the user is logged in when
the user navigates to the profile page
then the user should see their profile page

given we have a user with email "user@example.com" and the user is logged in when
the user navigates to the logout page
the user clicks the logout button
then the user should not be logged in
```

```python
from behave import given, when, then

@given("we have a user with email 'user@example.com' and the user is not registered when")
def step_given_we_have_a_user_with_email_user_example_com_and_the_user_is_not_registered_when(context):
    pass

@when("the user navigates to the registration page")
def step_when_the_user_navigates_to_the_registration_page(context):
    pass

@when("the user enters their email 'user@example.com'")
def step_when_the_user_enters_their_email_user_example_com(context):
    pass

@when("the user clicks the register button")
def step_when_the_user_clicks_the_register_button(context):
    pass

@then("the user should be registered")
def step_then_the_user_should_be_registered(context):
    pass
