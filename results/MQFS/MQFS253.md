# MQFS253
## Scenario
```gherkin
scenario: create a new user 
   given i am a user 
   when i visit '/signup' 
   then i should see a 'sign up' button 
   when i click on 'sign up' 
   then i should see a form to enter user details 
   when i enter valid user details 
   and click on 'sign up' 
   then i should be redirected to the homepage 
   and i should see a welcome message with my username
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: create a new user given i am a user when i visit '/signup' then i should see a 'sign up' button when i click on 'sign up' then i should see a form to enter user details when i enter valid user details and click on 'sign up' then i should be redirected to the homepage and i should see a welcome message with my username ```



from behave import given, when, then
from selenium import webdriver

@given('i am a user')
def step_given_i_am_a_user(context):
    context.driver = webdriver.Firefox()
    context.driver.get('http://localhost:8000/signup')

@when('i visit "/signup"')
def step_when_i_visit_signup(context):
    pass

@then('i should see a "sign up" button')
def step_then_i_should_see_a_sign_up_button(context):
    assert context.driver.find_element_by_id('signup-button')

@when('i click on "sign up"')
def step_when_i_click_on_sign_up(context):
    context.driver.find_element_by_id('signup-button').click()

@then('i should see a form to enter user details')
def step_then_i_should_see_a_form_to_enter_user_details(context):
    assert context.driver.find_element_by_id('signup-form')

@when('i enter valid user details and click on "sign up"')
def step_when_i_enter_valid_user_details_and_click_on_sign_up(context):
    context.driver.find_element_by_id('username').send_keys('testuser')
    context.driver.find_element_by_id('email').send_keys('testuser@example.com')
    context.driver.find_element_by_id('password').send_keys('testpassword')
    context.driver.find_element_by_id('signup-button').click()

@then('i should be redirected to the homepage')
def step_then_i_should_be_redirected_to_the_homepage(context):
    assert context.driver.current_url == 'http://localhost:8000/'

@then('i should see a welcome message with my username')
def step_then_i_should_see_a_welcome_message
