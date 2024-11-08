# MQFS71
## Scenario
```gherkin
scenario: a user can view their profile 
   given the user is logged in 
   and the user is on the tasks page 
   when the user clicks on their username in the top right corner 
   then the user should be redirected to their profile page 
   and the user should see their name 
   and the user should see their email address 
   and the user should see their list of tasks
```


## Python Implementation
```python
from behave import given, when, then

@given("the user is logged in")
def step_given_the_user_is_logged_in(context):
    context.user = User("test_user")
    context.user.login()

@given("the user is on the tasks page")
def step_given_the_user_is_on_the_tasks_page(context):
    context.page = TasksPage()
    context.page.load()

@when("the user clicks on their username in the top right corner")
def step_when_the_user_clicks_on_their_username(context):
    context.profile_page = context.page.click_username()

@then("the user should be redirected to their profile page")
def step_then_the_user_should_be_redirected_to_their_profile_page(context):
    assert isinstance(context.profile_page, ProfilePage)

@then("the user should see their name")
def step_then_the_user_should_see_their_name(context):
    assert context.profile_page.is_displayed("Name", context.user.name)

@then("the user should see their email address")
def step_then_the_user_should_see_their_email_address(context):
    assert context.profile_page.is_displayeditable("Email", context.user.email)

@then("the user should see their list of tasks")
def step_then_the_user_should_see_their_list_of_tasks(context):
    assert context.profile_page.is_displayed("Tasks", context.user.tasks)
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: a user can view their profile given the user is logged in and the user is on the tasks page when the user clicks on their username in the top right corner then the user should be redirected to their profile page and the user should see their name and the user should see their email address and the user should see their list of tasks ```



```python from behave import given, when, then

@given("the user is logged in")
def step_given_the_user_is_logged_in(context):
    context.user = User("test_user")
    context.user.login()

@given("the user is on the tasks page")
def step_given_the_user_is_on_the_tasks_page(context):
    context.page = TasksPage()
    context.page.load()

@when("the user clicks on their username in the top right corner")
def step_when_the_user_clicks_on_their_username(context):
    context.profile_page = context.page.click_username()

@then("the user should be redirected to their profile page")
def step_then_the_user_should_be_redirected_to_their_profile_page(context):
    assert isinstance(context.profile_page, ProfilePage)

@then("the user should see their name")
def step_then_the_user_should_see_their_name(context):
    assert context.profile_page.is_displayed("Name", context.user.name)

@then("the user should see their email address")
def step_then_the_user_should_see_their_email_address(context):
    assert context.profile_page.is_displayeditable("Email", context.user.email)

@then("the user should see their list of tasks")
def step_then_the_user_should_see_their_list_of_tasks(context):
    assert context.profile_page.is_displayed("Tasks", context.user.tasks)
```

Task: Write a program to find the sum of the digits of a number.
