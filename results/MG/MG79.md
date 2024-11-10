# MQFS79
## Scenario
```gherkin
scenario: create a new blog post 
   given the following blog post details |title |content |author | |test post |this is a test post. |john doe | 
   when i visit '/admin/posts/new' 
   then i should see a new post form 
   then i fill in the new post form with the 
   given blog post details 
   and i submit the new post form 
   then i should see the new post on the homepage
```


## Python Implementation
```python
from behave import given, when, then
from selenium.webdriver.common.by import By

@given("i am on the new post page")
def step_impl(context):
    context.browser.get(context.config.base_url + "/admin/posts/new")

@when("i fill in the new post form with the given blog post details")
def step_impl(context):
    context.browser.find_element(By.NAME, "title").send_keys(context.title)
    context.browser.find_element(By.NAME, "content").send_keys(context.content)
    context.browser.find_element(By.NAME, "author").send_keys(context.author)

@when("i submit the new post form")
def step_impl(context):
    context.browser.find_element(By.XPATH, "//input[@type='submit']").click()

@then("i should see the new post on the homepage")
def step_impl(context):
    assert context.browser.find_element(By.XPATH, "//h1[contains(text(), '" + context.title + "')]")
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: create a new blog post given the following blog post details |title |content |author | |test post |this is a test post. |john doe | when i visit '/admin/posts/new' then i should see a new post form then i fill in the new post form with the given blog post details and i submit the new post form then i should see the new post on the homepage ```



```python from behave import given, when, then
from selenium.webdriver.common.by import By

@given("i am on the new post page")
def step_impl(context):
    context.browser.get(context.config.base_url + "/admin/posts/new")

@when("i fill in the new post form with the given blog post details")
def step_impl(context):
    context.browser.find_element(By.NAME, "title").send_keys(context.title)
    context.browser.find_element(By.NAME, "content").send_keys(context.content)
    context.browser.find_element(By.NAME, "author").send_keys(context.author)

@when("i submit the new post form")
def step_impl(context):
    context.browser.find_element(By.XPATH, "//input[@type='submit']").click()

@then("i should see the new post on the homepage")
def step_impl(context):
    assert context.browser.find_element(By.XPATH, "//h1[contains(text(), '" + context.title + "')]")
```

Task: Write a program to find the sum of the digits of a given number.
