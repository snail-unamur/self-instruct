# HQFS233
## Scenario
```gherkin
scenario: a user can create a new blog post 
   given a user is logged in 
   when the user navigates to the blog post creation page 
   and the user enters a title 
   and body for the post 
   and the user clicks the "publish" button 
   then the user should be redirected to the new blog post page 
   and the new blog post should be visible on the page
```


## Python Implementation
```python
from behave import given, when, then

@given("a user is logged in")
def step_impl(context):
    pass

@when("the user navigates to the blog post creation page")
def step_impl(context):
    pass

@when("the user enters a title and body for the post")
def step_impl(context):
    pass

@when("the user clicks the 'publish' button")
def step_impl(context):
    pass

@then("the user should be redirected to the new blog post page")
def step_impl(context):
    pass

@then("the new blog post should be visible on the page")
def step_impl(context):
    pass
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: a user can create a new blog post given a user is logged in when the user navigates to the blog post creation page and the user enters a title and body for the post and the user clicks the "publish" button then the user should be redirected to the new blog post page and the new blog post should be visible on the page ```



```python from behave import given, when, then

@given("a user is logged in")
def step_impl(context):
    pass

@when("the user navigates to the blog post creation page")
def step_impl(context):
    pass

@when("the user enters a title and body for the post")
def step_impl(context):
    pass

@when("the user clicks the 'publish' button")
def step_impl(context):
    pass

@then("the user should be redirected to the new blog post page")
def step_impl(context):
    pass

@then("the new blog post should be visible on the page")
def step_impl(context):
    pass
```

Task: Write a program to find the sum of the digits of a given number.
