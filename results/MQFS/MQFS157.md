# MQFS157
## Scenario
```gherkin
None
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: testing the api endpoint for adding a new user given i am on the page with relative url "/api-auth/login" when i put "<username>" in the field with name "username" and i put "<password>" in the field with name "password" and i click the element with name "submit" then i should be on the page with relative url "/accounts/profile/" given i am on the page with relative url "/api-auth/login" when i put "<username>" in the field with name "username" and i put "<password>" in the field with name "password" and i click the element with name "submit" then i should be on the page with relative url "/accounts/profile/" given i am on the page with relative url "/api-auth/login" when i put "<username>" in the field with name "username" and i put "<password>" in the field with name "password" and i click the element with name "submit" then i should be on the page with relative url "/accounts/profile/" given i am on the page with relative url "/api-auth/login" when i put "<username>" in the field with name "username" and i put "<password>" in the field with name "password" and i click the element with name "submit" then i should be on the page with relative url "/accounts/profile/" given i am on the page with relative url "/api-auth/login" when i put "<username>" in the field with name "username" and i put "<password>" in the field with name "password" and i click the element with name "submit" then i should be on the page with relative url "/accounts/profile/" given i am on the page with relative url "/api-auth/login" when i put "<username>" in the field with name "username" and i put "<password>" in the field with name "password" and i click the element with name "submit" then i should be on the page with relative url "/accounts/profile/" given i am on the page with relative url "/api-auth/login" when i put "<username>" in the field with name "username" and i put "<password>" in the field with name "password" and i click the element with name "



from behave import given, when, then

@given("i am on the page with relative url '/api-auth/login'")
def step_given_i_am_on_the_page_with_relative_url_api_auth_login(context):
    context.browser.get(context.get_url('/api-auth/login'))

@when("i put '<username>' in the field with name 'username'")
def step_when_i_put_username_in_the_field_with_name_username(context, username):
    context.browser.find_element_by_name('username').send_keys(username)

@when("i put '<password>' in the field with name 'password'")
def step_when_i_put_password_in_the_field_with_name_password(context, password):
    context.browser.find_element_by_name('password').send_keys(password)

@when("i click the element with name 'submit'")
def step_when_i_click_the_element_with_name_submit(context):
    context.browser.find_element_by_name('submit').click()

@then("i should be on the page with relative url '/accounts/profile/'")
def step_then_i_should_be_on_the_page_with_relative_url_accounts_profile(context):
    assert context.browser.current_url == context.get_url('/accounts/profile/')

@given("i am on the page with relative url '/api-auth/login'")
def step_given_i_am_on_the_page_with_relative_url_api_auth_login(context):
    context.browser.get(context.get_url('/api-auth/login'))

@when("i put '<username>' in the field with name 'username'")
def step_when_i_put_username_in_the_field_with_name_username(context, username):
    context.browser.find_element_by_name('username').send_keys(username)

@when("i put '<password>' in the field with name 'password'")
