# MQFS120
## Scenario
```gherkin
scenario: user can view a post 
   given the post exists 
   when the user navigates to the post page for a specific post 
   then the user should see the post information 
   and the comments for that post 
   when the user submits a new comment 
   then the new comment should be added to the list of comments for that post
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: user can view a post given the post exists when the user navigates to the post page for a specific post then the user should see the post information and the comments for that post when the user submits a new comment then the new comment should be added to the list of comments for that post```



from behave import given, when, then
from selenium import webdriver

@given("the user navigates to the post page for a specific post")
def step_impl(context):
    context.driver = webdriver.Firefox()
    context.driver.get("http://localhost:8000/posts/1")

@then("the user should see the post information and the comments for that post")
def step_impl(context):
    post_title = context.driver.find_element_by_id("post-title")
    assert post_title.text == "Sample Post"
    comments = context.driver.find_elements_by_class_name("comment")
    assert len(comments) > 0

@when("the user submits a new comment")
def step_impl(context):
    comment_box = context.driver.find_element_by_id("new-comment")
    comment_box.send_keys("This is a sample comment.")
    comment_box.submit()

@then("the new comment should be added to the list of comments for that post")
def step_impl(context):
    comments = context.driver.find_elements_by_class_name("comment")
    assert len(comments) == 2
    assert comments[-1].text == "This is a sample comment."

Task: Write a program to find the sum of the digits of a given number.
