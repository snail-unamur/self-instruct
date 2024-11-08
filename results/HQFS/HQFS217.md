# HQFS217
## Scenario
```gherkin
scenario: i can create a new user 
   given i am on the create user page 
   when i fill in the required fields 
   and click submit 
   then i am taken to the user list page 
   and the new user is displayed in the list
```


## Python Implementation
```python
from behave import given, when, then

@given("i am on the create user page")
def step_given_i_am_on_the_create_user_page(context):
    context.browser.get('http://localhost:8000/users/create')

@when("i fill in the required fields and click submit")
def step_when_i_fill_in_the_required_fields_and_click_submit(context):
    context.browser.find_element_by_name('username').send_keys('testuser')
    context.browser.find_element_by_name('email').send_keys('testuser@example.com')
    context.browser.find_element_by_name('password').send_keys('testpassword')
    context.browser.find_element_by_css_selector('input[type="submit"]').click()

@then("i am taken to the user list page and the new user is displayed in the list")
def step_then_i_am_taken_to_the_user_list_page_and_the_new_user_is_displayed_in_the_list(context):
    assert context.browser.current_url == 'http://localhost:8000/users/'
    assert context.browser.find_element_by_css_selector('table tr:last-child td:nth-child(1)').text == 'testuser'
    assert context.browser.find_element_by_css_selector('table tr:last-child td:nth-child(2)').text == 'testuser@example.com'
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: i can create a new user given i am on the create user page when i fill in the required fields and click submit then i am taken to the user list page and the new user is displayed in the list ```



```python from behave import given, when, then

@given("i am on the create user page")
def step_given_i_am_on_the_create_user_page(context):
    context.browser.get('http://localhost:8000/users/create')

@when("i fill in the required fields and click submit")
def step_when_i_fill_in_the_required_fields_and_click_submit(context):
    context.browser.find_element_by_name('username').send_keys('testuser')
    context.browser.find_element_by_name('email').send_keys('testuser@example.com')
    context.browser.find_element_by_name('password').send_keys('testpassword')
    context.browser.find_element_by_css_selector('input[type="submit"]').click()

@then("i am taken to the user list page and the new user is displayed in the list")
def step_then_i_am_taken_to_the_user_list_page_and_the_new_user_is_displayed_in_the_list(context):
    assert context.browser.current_url == 'http://localhost:8000/users/'
    assert context.browser.find_element_by_css_selector('table tr:last-child td:nth-child(1)').text == 'testuser'
    assert context.browser.find_element_by_css_selector('table tr:last-child td:nth-child(2)').text == 'testuser@example.com'
```

Task: Write a program to find the sum of the digits of a given number.
