# MQFS40
## Scenario
```gherkin
scenario: user wants to create a new list 
   given user is logged in 
   when user goes to the home page 
   then user sees a button to create a new list 
   when user clicks on the button 
   then user is redirected to a page to create a new list 
   when user enters a name 
   and clicks on the button 
   then user is redirected to the home page 
   and sees the new list
```


## Python Implementation
```python
from behave import given, when, then

@given("user is logged in")
def step_impl(context):
    context.user = User()
    context.user.login()

@when("user goes to the home page")
def step_impl(context):
    context.home_page = HomePage()
    context.home_page.load()

@then("user sees a button to create a new list")
def step_impl(context):
    assert context.home_page.new_list_button.is_displayed()

@when("user clicks on the button")
def step_impl(context):
    context.new_list_page = context.home_page.click_new_list_button()

@then("user is redirected to a page to create a new list")
def step_impl(context):
    assert isinstance(context.new_list_page, NewListPage)

@when("user enters a name and clicks on the button")
def step_impl(context):
    context.new_list_page.enter_name("My List")
    context.home_page = context.new_list_page.click_create_button()

@then("user is redirected to the home page and sees the new list")
def step_impl(context):
    assert isinstance(context.home_page, HomePage)
    assert "My List" in context.home_page.get_list_names()
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: user wants to create a new list given user is logged in when user goes to the home page then user sees a button to create a new list when user clicks on the button then user is redirected to a page to create a new list when user enters a name and clicks on the button then user is redirected to the home page and sees the new list ```



```python from behave import given, when, then

@given("user is logged in")
def step_impl(context):
    context.user = User()
    context.user.login()

@when("user goes to the home page")
def step_impl(context):
    context.home_page = HomePage()
    context.home_page.load()

@then("user sees a button to create a new list")
def step_impl(context):
    assert context.home_page.new_list_button.is_displayed()

@when("user clicks on the button")
def step_impl(context):
    context.new_list_page = context.home_page.click_new_list_button()

@then("user is redirected to a page to create a new list")
def step_impl(context):
    assert isinstance(context.new_list_page, NewListPage)

@when("user enters a name and clicks on the button")
def step_impl(context):
    context.new_list_page.enter_name("My List")
    context.home_page = context.new_list_page.click_create_button()

@then("user is redirected to the home page and sees the new list")
def step_impl(context):
    assert isinstance(context.home_page, HomePage)
    assert "My List" in context.home_page.get_list_names()
```

Task: Write a program to find the sum of the digits of a number.
