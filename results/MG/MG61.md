# MQFS61
## Scenario
```gherkin
scenario: testing the registration of a new user 
   given a user with username "foo" 
   and password "bar" 
   and i am on the login page 
   when i click on the register button 
   then i should see the registration form 
   and i should see the username field 
   and i should see the password field 
   and i should see the confirm password field 
   when i enter "foo" in the username field 
   and i enter "bar" in the password field 
   and i enter "bar" in the confirm password field 
   and i click on the register button 
   then i should see the success message
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: testing the registration of a new user given a user with username "foo" and password "bar" and i am on the login page when i click on the register button then i should see the registration form and i should see the username field and i should see the password field and i should see the confirm password field when i enter "foo" in the username field and i enter "bar" in the password field and i enter "bar" in the confirm password field and i click on the register button then i should see the success message ```



```python from behave import given, when, then

@given("a user with username 'foo' and password 'bar' and i am on the login page")
def step_given_a_user_with_username_foo_and_password_bar_and_i_am_on_the_login_page(context):
    context.user = User("foo", "bar")
    context.page = LoginPage()

@when("i click on the register button")
def step_i_click_on_the_register_button(context):
    context.page.click_register_button()

@then("i should see the registration form")
def step_i_should_see_the_registration_form(context):
    assert isinstance(context.page, RegistrationPage)

@then("i should see the username field")
def step_i_should_see_the_username_field(context):
    assert context.page.has_username_field()

@then("i should see the password field")
def step_i_should_see_the_password_field(context):
    assert context.page.has_password_field()

@then("i should see the confirm password field")
def step_i_should_see_the_confirm_password_field(context):
    assert context.page.has_confirm_password_field()

@when("i enter 'foo' in the username field")
def step_i_enter_foo_in_the_username_field(context):
    context.page.enter_username("foo")

@when("i enter 'bar' in the password field")
def step_i_enter_bar_in_the_password_field(context):
    context.page.enter_password("bar")

@when("i enter 'bar' in the confirm password field")
def step_i_enter_bar_in_the_confirm_password_field(context):
    context.page.enter_confirm_password("bar")

@when("i click on the register button")
def step_i_click_on_the_register_button(context):
    context.page.click_register_button()

@then("
