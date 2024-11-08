# MQFS51
## Scenario
```gherkin
scenario: 
   given i have a user with the email "[test@test.com](mailto:test@test.com)" 
   and the password "password" 
   when i go to the login page 
   then i should see a login form with fields for email 
   and password 
   and 
   when i enter the email "[test@test.com](mailto:test@test.com)" 
   and the password "password" 
   and i click the login button 
   then i should be logged in 
   and redirected to the homepage
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: given i have a user with the email "[test@test.com](mailto:test@test.com)" and the password "password" when i go to the login page then i should see a login form with fields for email and password and when i enter the email "[test@test.com](mailto:test@test.com)" and the password "password" and i click the login button then i should be logged in and redirected to the homepage ```



from behave import given, when, then

@given("i have a user with the email 'test@test.com' and the password 'password'")
def step_given(context):
    context.user = User(email='test@test.com', password='password')

@when("i go to the login page")
def step_when(context):
    context.browser.get('http://localhost:8000/login')

@then("i should see a login form with fields for email and password")
def step_then(context):
    form = context.browser.find_element_by_id('login-form')
    email_field = form.find_element_by_name('email')
    password_field = form.find_element_by_name('password')
    assert email_field, 'Email field not found'
    assert password_field, 'Password field not found'

@when("i enter the email 'test@test.com' and the password 'password'")
def step_when_2(context):
    form = context.browser.find_element_by_id('login-form')
    email_field = form.find_element_by_name('email')
    password_field = form.find_element_by_name('password')
    email_field.send_keys('test@test.com')
    password_field.send_keys('password')

@when("i click the login button")
def step_when_3(context):
    form = context.browser.find_element_by_id('login-form')
    login_button = form.find_element_by_name('login')
    login_button.click()

@then("i should be logged in and redirected to the homepage")
def step_then_2(context):
    assert context.browser.current_url == 'http://localhost:8000/home', 'Not redirected to homepage'
    assert context.browser.find_element_by_id('logout-button'), 'Not logged in'
