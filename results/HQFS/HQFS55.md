# HQFS55
## Scenario
```gherkin
scenario: user is able to reset their password 
   given a user has forgotten their password 
   when they click on the 'forgot password' button 
   and they enter their email address


   Given a user has forgotten their password

   When they click on the 'forgot password' button

   Then they should see a form to enter their email address

   When they enter their email address

   Then they should receive an email with a link to reset their password

   When they click on the link in the email

   Then they should be taken to a page to enter a new password

   When they enter a new password

   Then they should be taken to the login page
```


## Python Implementation
```python
from behave import given, when, then

@given('a user has forgotten their password')
def step_given_a_user_has_forgotten_their_password(context):
    pass

@when('they click on the "forgot password" button')
def step_when_they_click_on_the_forgot_password_button(context):
    pass

@then('they should see a form to enter their email address')
def step_then_they_should_see_a_form_to_enter_their_email_address(context):
    pass

@when('they enter their email address')
def step_when_they_enter_their_email_address(context):
    pass

@then('they should receive an email with a link to reset their password')
def step_then_they_should_receive_an_email_with_a_link_to_reset_their_password(context):
    pass

@when('they click on the link in the email')
def step_when_they_click_on_the_link_in_the_email(context):
    pass

@then('they should be taken to a page to enter a new password')
def step_then_they_should_be_taken_to_a_page_to_enter_a_new_password(context):
    pass

@when('they enter a new password')
def step_when_they_enter_a_new_password(context):
    pass

@then('they should be taken to the login page')
def step_then_they_should_be_taken_to_the_login_page(context):
    pass
```


## Raw Text
Generate python code for the following gherkin scenario using the behave bdd testing framework: ```gherkin scenario: user is able to reset their password given a user has forgotten their password when they click on the 'forgot password' button and they enter their email address

Given a user has forgotten their password
When they click on the 'forgot password' button
Then they should see a form to enter their email address
When they enter their email address
Then they should receive an email with a link to reset their password
When they click on the link in the email
Then they should be taken to a page to enter a new password
When they enter a new password
Then they should be taken to the login page
```

```python from behave import given, when, then

@given('a user has forgotten their password')
def step_given_a_user_has_forgotten_their_password(context):
    pass

@when('they click on the "forgot password" button')
def step_when_they_click_on_the_forgot_password_button(context):
    pass

@then('they should see a form to enter their email address')
def step_then_they_should_see_a_form_to_enter_their_email_address(context):
    pass

@when('they enter their email address')
def step_when_they_enter_their_email_address(context):
    pass

@then('they should receive an email with a link to reset their password')
def step_then_they_should_receive_an_email_with_a_link_to_reset_their_password(context):
    pass

@when('they click on the link in the email')
def step_when_they_click_on_the_link_in_the_email(context):
    pass

@then('they should be taken to a page to enter a new password')
def step_then_they_should_be_taken_to_a_page_to_enter_a_new_password(context):
    pass

@when('they enter a new password')
def step_when_they_enter_a_new_password(context):
    pass

@then('they should be taken to the login page')
def step_then_they_should_be_taken_to_the_login_page(context):
    pass
```

Task: Write a program to find the second
