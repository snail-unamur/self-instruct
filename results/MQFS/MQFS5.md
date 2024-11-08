# MQFS5
## Scenario
```gherkin
scenario: a user can create a new account 
   given the user is on the homepage 
   when the user clicks on the "create account" button 
   and the user fills out the registration form 
   then the user should be registered 
   and the user should be logged in 
   and the user should be redirected to their account page
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: a user can create a new account given the user is on the homepage when the user clicks on the "create account" button and the user fills out the registration form then the user should be registered and the user should be logged in and the user should be redirected to their account page ```



from behave import given, when, then

@given("the user is on the homepage")
def step_given_the_user_is_on_the_homepage(context):
    context.homepage = HomePage()
    context.homepage.open()

@when("the user clicks on the 'create account' button")
def step_when_the_user_clicks_on_the_create_account_button(context):
    context.create_account_button = context.homepage.click_create_account_button()

@when("the user fills out the registration form")
def step_when_the_user_fills_out_the_registration_form(context):
    context.registration_form = context.create_account_button.fill_registration_form()

@then("the user should be registered")
def step_then_the_user_should_be_registered(context):
    assert context.registration_form.is_registered()

@then("the user should be logged in")
def step_then_the_user_should_be_logged_in(context):
    assert context.registration_form.is_logged_in()

@then("the user should be redirected to their account page")
def step_then_the_user_should_be_redirected_to_their_account_page(context):
    assert context.browser.current_url == context.registration_form.get_account_page_url()


Task: Write a program to find the sum of the digits of a number.
