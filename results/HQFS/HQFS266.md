# HQFS266
## Scenario
```gherkin
scenario: a user can create a new post with a title 
   and a body 
   given i am logged in as "kea@gmail.com" 
   and i am on the home page 
   when i click on the "new post" button 
   then i am redirected to the "new post" page 
   and i fill the title field with "my first post" 
   and i fill the body field with "this is my first post" 
   and i click on the "publish" button 
   then i am redirected to the home page 
   and i see the new post with title "my first post"
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: a user can create a new post with a title and a body given i am logged in as "kea@gmail.com" and i am on the home page when i click on the "new post" button then i am redirected to the "new post" page and i fill the title field with "my first post" and i fill the body field with "this is my first post" and i click on the "publish" button then i am redirected to the home page and i see the new post with title "my first post" ```



```python from behave import given, when, then
from selenium import webdriver

@given("i am logged in as 'kea@gmail.com' and i am on the home page")
def step_impl(context):
    context.driver = webdriver.Firefox()
    context.driver.get("http://localhost:8000")
    context.driver.find_element_by_name("email").send_keys("kea@gmail.com")
    context.driver.find_element_by_name("password").send_keys("password")
    context.driver.find_element_by_xpath("//button[contains(text(),'Log In')]").click()

@when("i click on the 'new post' button")
def step_impl(context):
    context.driver.find_element_by_xpath("//a[contains(text(),'New Post')]").click()

@then("i am redirected to the 'new post' page")
def step_impl(context):
    assert context.driver.current_url == "http://localhost:8000/new_post"

@when("i fill the title field with 'my first post'")
def step_impl(context):
    context.driver.find_element_by_name("title").send_keys("my first post")

@when("i fill the body field with 'this is my first post'")
def step_impl(context):
    context.driver.find_element_by_name("body").send_keys("this is my first post")

@when("i click on the 'publish' button")
def step_impl(context):
    context.driver.find_element_by_xpath("//button[contains(text(),'Publish')]").click()

@then("i am redirected to the home page")
def step_impl(context):
    assert context.driver.current_url == "http://localhost:8000"

@then("i see the new post with title 'my first post'")
def step_impl(context):
    assert context.driver.find_element_element_by_xpath("//h2[contains
