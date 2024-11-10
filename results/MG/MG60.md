# MQFS60
## Scenario
```gherkin
scenario: testing the edit post feature 
   given i am logged in 
   and i have a post 
   when i go to the edit post page 
   and i fill in the post form with valid information 
   then i should be able to edit my post 
   and i should be redirected to the post page
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: testing the edit post feature given i am logged in and i have a post when i go to the edit post page and i fill in the post form with valid information then i should be able to edit my post and i should be redirected to the post page ```



from behave import given, when, then
from selenium import webdriver

@given("i am logged in and i have a post")
def step_impl(context):
    context.driver = webdriver.Firefox()
    context.driver.get("http://localhost:8000")
    context.driver.find_element_by_name("username").send_keys("testuser")
    context.driver.find_element_by_name("password").send_keys("testpassword")
    context.driver.find_element_by_xpath("//button[@type='submit']").click()
    context.driver.find_element_by_xpath("//a[contains(text(), 'New Post')]").click()
    context.driver.find_element_by_name("title").send_keys("Test Post")
    context.driver.find_element_by_name("content").send_keys("Test Content")
    context.driver.find_element_by_xpath("//button[@type='submit']").click()

@when("i go to the edit post page and i fill in the post form with valid information")
def step_impl(context):
    context.driver.find_element_by_xpath("//a[contains(text(), 'Test Post')]").click()
    context.driver.find_element_by_xpath("//a[contains(text(), 'Edit')]").click()
    context.driver.find_element_by_name("title").clear()
    context.driver.find_element_by_name("title").send_keys("Edited Test Post")
    context.driver.find_element_by_name("content").clear()
    context.driver.find_element_by_name("content").send_keys("Edited Test Content")

@then("i should be able to edit my post and i should be redirected to the post page")
def step_impl(context):
    context.driver.find_element_by_xpath("//button[@type='submit']").click()
    assert context.driver.current_url == "http://localhost:8000/posts/edited-test-post/"
    assert context.
