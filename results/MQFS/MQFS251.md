# MQFS251
## Scenario
```gherkin
scenario: user can create a new post 
   given user is on the home page 
   when user clicks the "create post" button 
   then user is taken to the "create post" page 
   when user fills out the form with valid data 
   then user clicks the "submit" button 
   when post is successfully created 
   then user is taken to the "view post" page 
   and the new post is displayed
```


## Python Implementation
```python
from behave import given, when, then

@given("user is on the home page")
def step_impl(context):
    context.browser.visit("http://localhost:8000")

@when("user clicks the 'create post' button")
def step_impl(context):
    context.browser.click("create_post_button")

@then("user is taken to the 'create post' page")
def step_impl(context):
    assert context.browser.url == "http://localhost:8000/create_post"

@when("user fills out the form with valid data")
def step_impl(context):
    context.browser.fill("title", "Test Post")
    context.browser.fill("content", "Test Content")

@when("user clicks the 'submit' button")
def step_impl(context):
    context.browser.click("submit_button")

@then("post is successfully created")
def step_impl(context):
    assert context.browser.url == "http://localhost:8000/view_post/1"

@then("user is taken to the 'view post' page and the new post is displayed")
def step_impl(context):
    assert context.browser.is_text_present("Test Post")
    assert context.browser.is_text_present("Test Content")
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: user can create a new post given user is on the home page when user clicks the "create post" button then user is taken to the "create post" page when user fills out the form with valid data then user clicks the "submit" button when post is successfully created then user is taken to the "view post" page and the new post is displayed ```



```python from behave import given, when, then

@given("user is on the home page")
def step_impl(context):
    context.browser.visit("http://localhost:8000")

@when("user clicks the 'create post' button")
def step_impl(context):
    context.browser.click("create_post_button")

@then("user is taken to the 'create post' page")
def step_impl(context):
    assert context.browser.url == "http://localhost:8000/create_post"

@when("user fills out the form with valid data")
def step_impl(context):
    context.browser.fill("title", "Test Post")
    context.browser.fill("content", "Test Content")

@when("user clicks the 'submit' button")
def step_impl(context):
    context.browser.click("submit_button")

@then("post is successfully created")
def step_impl(context):
    assert context.browser.url == "http://localhost:8000/view_post/1"

@then("user is taken to the 'view post' page and the new post is displayed")
def step_impl(context):
    assert context.browser.is_text_present("Test Post")
    assert context.browser.is_text_present("Test Content")
```

Task: Write a program to find the sum of the digits of a given number.
