# HQFS177
## Scenario
```gherkin
scenario: user wants to view a post 
   given i am on the homepage 
   when i click on a post 
   then i should be taken to the post page 
   and i should see the title 
   and content of the post 
   and i should see the author of the post 
   and i should see the date the post was created
```


## Python Implementation
```python
from behave import given, when, then

@given("i am on the homepage")
def step_given_i_am_on_the_homepage(context):
    context.browser.visit("http://localhost:8000/")

@when("i click on a post")
def step_when_i_click_on_a_post(context):
    post = context.browser.find_by_css("article")[0]
    post.click()

@then("i should be taken to the post page")
def step_then_i_should_be_taken_to_the_post_page(context):
    assert context.browser.url == "http://localhost:8000/post/1"

@then("i should see the title and content of the post")
def step_then_i_should_see_the_title_and_content_of_the_post(context):
    post = context.browser.find_by_css("article")[0]
    assert post.find_by_css("h1").text == "My First Post"
    assert post.find_by_css("p").text == "This is the content of my first post."

@then("i should see the author of the post")
def step_then_i_should_see_the_author_of_the_post(context):
    post = context.browser.find_by_css("article")[0]
    assert post.find_by_css("p.author").text == "Author: John Doe"

@then("i should see the date the post was created")
def step_then_i_should_see_the_date_the_post_was_created(context):
    post = context.browser.find_by_css("article")[0]
    assert post.find_by_css("p.date").text == "Date: 2022-01-01"
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: user wants to view a post given i am on the homepage when i click on a post then i should be taken to the post page and i should see the title and content of the post and i should see the author of the post and i should see the date the post was created ```



```python from behave import given, when, then

@given("i am on the homepage")
def step_given_i_am_on_the_homepage(context):
    context.browser.visit("http://localhost:8000/")

@when("i click on a post")
def step_when_i_click_on_a_post(context):
    post = context.browser.find_by_css("article")[0]
    post.click()

@then("i should be taken to the post page")
def step_then_i_should_be_taken_to_the_post_page(context):
    assert context.browser.url == "http://localhost:8000/post/1"

@then("i should see the title and content of the post")
def step_then_i_should_see_the_title_and_content_of_the_post(context):
    post = context.browser.find_by_css("article")[0]
    assert post.find_by_css("h1").text == "My First Post"
    assert post.find_by_css("p").text == "This is the content of my first post."

@then("i should see the author of the post")
def step_then_i_should_see_the_author_of_the_post(context):
    post = context.browser.find_by_css("article")[0]
    assert post.find_by_css("p.author").text == "Author: John Doe"

@then("i should see the date the post was created")
def step_then_i_should_see_the_date_the_post_was_created(context):
    post = context.browser.find_by_css("article")[0]
    assert post.find_by_css("p.date").text == "Date: 2022-01-01"
```

Task: Write a program to find the sum of the digits of a number.
