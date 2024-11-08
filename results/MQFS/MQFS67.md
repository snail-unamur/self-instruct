# MQFS67
## Scenario
```gherkin
scenario: add a new user 
   given i am on the user list page 
   when i click on the add user button 
   then i should be redirected to the add user page 
   and i should see the add user form 
   and i fill the form with valid data 
   and i click on the submit button 
   then i should be redirected to the user list page 
   and i should see the new user on the list 
   and i click on the user link 
   then i should be redirected to the user details page 
   and i should see the user details
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: add a new user given i am on the user list page when i click on the add user button then i should be redirected to the add user page and i should see the add user form and i fill the form with valid data and i click on the submit button then i should be redirected to the user list page and i should see the new user on the list and i click on the user link then i should be redirected to the user details page and i should see the user details ```



```python from behave import given, when, then
from pages.user_list_page import UserListPage
from pages.add_user_page import AddUserPage
from pages.user_details_page import UserDetailsPage

@given("i am on the user list page")
def step_given_i_am_on_the_user_list_page(context):
    user_list_page = UserListPage(context.browser)
    user_list_page.navigate_to()
    context.user_list_page = user_list_page

@when("i click on the add user button")
def step_when_i_click_on_the_add_user_button(context):
    context.user_list_page.click_add_user_button()

@then("i should be redirected to the add user page")
def step_then_i_should_be_redirected_to_the_add_user_page(context):
    add_user_page = AddUserPage(context.browser)
    assert add_user_page.is_displayed()
    context.add_user_page = add_user_page

@then("i should see the add user form")
def step_then_i_should_see_the_add_user_form(context):
    assert context.add_user_page.is_add_user_form_displayed()

@when("i fill the form with valid data")
def step_when_i_fill_the_form_with_valid_data(context):
    context.add_user_page.fill_add_user_form()

@when("i click on the submit button")
def step_when_i_click_on_the_submit_button(context):
    context.add_user_page.click_submit_button()

@then("i should be redirected to the user list page")
def step_then_i_should_be_redirected_to_the_user_list_page(context):
    user_list_page = UserListPage(context.browser)
    assert user_list_page.is_displayed()
    context.user_list_
