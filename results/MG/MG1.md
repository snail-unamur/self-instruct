# MQFS1
## Scenario
```gherkin
scenario: user can create a new post 
   given user is on the home page 
   when user clicks on the "new post" button 
   and user enters the title 
   and body of the post 
   and user clicks on the "publish" button 
   then the new post should be created 
   and user should be redirected to the new post page
```


## Python Implementation
```python
from behave import given, when, then

@given("user is on the home page")
def step_given_user_is_on_the_home_page(context):
    context.home_page.open()

@when("user clicks on the 'new post' button")
def step_when_user_clicks_on_the_new_post_button(context):
    context.home_page.click_new_post_button()

@when("user enters the title and body of the post")
def step_when_user_enters_the_title_and_body_of_the_post(context):
    context.new_post_page.enter_title("Test Post")
    context.new_post_page.enter_body("Test Body")

@when("user clicks on the 'publish' button")
def step_when_user_clicks_on_the_publish_button(context):
    context.new_post_page.click_publish_button()

@then("the new post should be created and user should be redirected to the new post page")
def step_then_the_new_post_should_be_created_and_user_should_be_redirected_to_the_new_post_page(context):
    assert context.new_post_page.on_page()
    assert context.new_post_page.post_exists("Test Post")
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: user can create a new post given user is on the home page when user clicks on the "new post" button and user enters the title and body of the post and user clicks on the "publish" button then the new post should be created and user should be redirected to the new post page ```



```python from behave import given, when, then

@given("user is on the home page")
def step_given_user_is_on_the_home_page(context):
    context.home_page.open()

@when("user clicks on the 'new post' button")
def step_when_user_clicks_on_the_new_post_button(context):
    context.home_page.click_new_post_button()

@when("user enters the title and body of the post")
def step_when_user_enters_the_title_and_body_of_the_post(context):
    context.new_post_page.enter_title("Test Post")
    context.new_post_page.enter_body("Test Body")

@when("user clicks on the 'publish' button")
def step_when_user_clicks_on_the_publish_button(context):
    context.new_post_page.click_publish_button()

@then("the new post should be created and user should be redirected to the new post page")
def step_then_the_new_post_should_be_created_and_user_should_be_redirected_to_the_new_post_page(context):
    assert context.new_post_page.on_page()
    assert context.new_post_page.post_exists("Test Post")
```

Task: Write a program to find the sum of the digits of a given number.
