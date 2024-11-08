# HQFS116
## Scenario
```gherkin
scenario: the user can create a new project 
   given i am logged in as "admin" 
   when i go to the page "/projects/new" 
   and i fill the form with the name "kalibro" 
   and i click on the "create" button 
   then i should be redirected to the page "/projects/kalibro" 
   and i should see the project "kalibro" in the list of all the projects i created
```


## Python Implementation
```python
from behave import given, when, then
from selenium.webdriver.common.by import By

@given("i am logged in as 'admin'")
def step_impl(context):
    context.browser.get(context.base_url + "/login")
    context.browser.find_element(By.ID, "username").send_keys("admin")
    context.browser.find_element(By.ID, "password").send_keys("password")
    context.browser.find_element(By.ID, "login").click()

@when("i go to the page '/projects/new'")
def step_impl(context):
    context.browser.get(context.base_url + "/projects/new")

@when("i fill the form with the name 'kalibro'")
def step_impl(context):
    context.browser.find_element(By.ID, "name").send_keys("kalibro")

@when("i click on the 'create' button")
def step_impl(context):
    context.browser.find_element(By.ID, "create").click()

@then("i should be redirected to the page '/projects/kalibro'")
def step_impl(context):
    assert context.browser.current_url == context.base_url + "/projects/kalibro"

@then("i should see the project 'kalibro' in the list of all the projects i created")
def step_impl(context):
    assert context.browser.find_element(By.ID, "project_kalibro")
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: the user can create a new project given i am logged in as "admin" when i go to the page "/projects/new" and i fill the form with the name "kalibro" and i click on the "create" button then i should be redirected to the page "/projects/kalibro" and i should see the project "kalibro" in the list of all the projects i created ```



```python from behave import given, when, then
from selenium.webdriver.common.by import By

@given("i am logged in as 'admin'")
def step_impl(context):
    context.browser.get(context.base_url + "/login")
    context.browser.find_element(By.ID, "username").send_keys("admin")
    context.browser.find_element(By.ID, "password").send_keys("password")
    context.browser.find_element(By.ID, "login").click()

@when("i go to the page '/projects/new'")
def step_impl(context):
    context.browser.get(context.base_url + "/projects/new")

@when("i fill the form with the name 'kalibro'")
def step_impl(context):
    context.browser.find_element(By.ID, "name").send_keys("kalibro")

@when("i click on the 'create' button")
def step_impl(context):
    context.browser.find_element(By.ID, "create").click()

@then("i should be redirected to the page '/projects/kalibro'")
def step_impl(context):
    assert context.browser.current_url == context.base_url + "/projects/kalibro"

@then("i should see the project 'kalibro' in the list of all the projects i created")
def step_impl(context):
    assert context.browser.find_element(By.ID, "project_kalibro")
```

Task: Write a program to find the sum of the digits of a given number.
