# HQFS29
## Scenario
```gherkin
scenario: user wants to log in 
   given the user is not logged in 
   when the user navigates to the "login" page 
   then the user should see a form to enter their credentials 
   when the user enters their credentials 
   and clicks on the submit button 
   then the user should be logged in
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: user wants to log in given the user is not logged in when the user navigates to the "login" page then the user should see a form to enter their credentials when the user enters their credentials and clicks on the submit button then the user should be logged in ```



from behave import given, when, then

@given("the user is not logged in")
def step_given_the_user_is_not_logged_in(context):
    context.user = User()
    context.user.logged_in = False

@when("the user navigates to the 'login' page")
def step_when_the_user_navigates_to_the_login_page(context):
    context.login_page = LoginPage()
    context.login_page.open()

@then("the user should see a form to enter their credentials")
def step_then_the_user_should_see_a_form_to_enter_their_credentials(context):
    assert context.login_page.form_visible()

@when("the user enters their credentials and clicks on the submit button")
def step_when_the_user_enters_their_credentials_and_clicks_on_the_submit_button(context):
    context.credentials = Credentials()
    context.credentials.username = "testuser"
    context.credentials.password = "testpassword"
    context.login_page.enter_credentials(context.credentials)
    context.login_page.submit()

@then("the user should be logged in")
def step_then_the_user_should_be_logged_in(context):
    assert context.user.logged_in

Task: Write a program to find the sum of the digits of a number.
