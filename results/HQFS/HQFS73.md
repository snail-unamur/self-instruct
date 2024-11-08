# HQFS73
## Scenario
```gherkin
scenario: user is able to reset their password 
   given a user with email "johndoe@example.com" 
   when the user visits the password reset page 
   then the user should see a password reset form 
   when the user enters their email 
   and clicks the reset button 
   then the user should receive an email with a password reset link 
   when the user clicks the password reset link 
   then the user should be taken to a page where they can enter a new password 
   when the user enters a new password 
   and clicks the change password button 
   then the user's password should be changed 
   and they should be redirected to the login page
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: user is able to reset their password given a user with email "johndoe@example.com" when the user visits the password reset page then the user should see a password reset form when the user enters their email and clicks the reset button then the user should receive an email with a password reset link when the user clicks the password reset link then the user should be taken to a page where they can enter a new password when the user enters a new password and clicks the change password button then the user's password should be changed and they should be redirected to the login page ```



```python from behave import given, when, then

@given("the user visits the password reset page")
def step_given_the_user_visits_the_password_reset_page(context):
    context.browser.get("http://example.com/password-reset")

@when("the user enters their email and clicks the reset button")
def step_when_the_user_enters_their_email_and_clicks_the_reset_button(context):
    context.browser.find_element_by_name("email").send_keys("johndoe@example.com")
    context.browser.find_element_by_name("reset").click()

@then("the user should receive an email with a password reset link")
def step_then_the_user_should_receive_an_email_with_a_password_reset_link(context):
    # Check the user's email for a password reset link
    pass

@when("the user clicks the password reset link")
def step_when_the_user_clicks_the_password_reset_link(context):
    # Click the password reset link in the user's email
    pass

@then("the user should be taken to a page where they can enter a new password")
def step_then_the_user_should_be_taken_to_a_page_where_they_can_enter_a_new_password(context):
    # Check that the user is on the password reset page
    assert context.browser.current_url == "http://example.com/password-reset/johndoe@example.com"

@when("the user enters a new password and clicks the change password button")
def step_when_the_user_enters_a_new_password_and_clicks_the_change_password_button(context):
    context.browser.find_element_by_name("password").send_keys("newpassword")
    context.browser.find_element_by_name("change").click()

@then("the user's password should be changed and they should be redirected to the login page")
def step_then_the_
