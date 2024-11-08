# HQFS11
## Scenario
```gherkin
scenario: 
   given i have a user with email "johndoe@example.com" 
   and password "password" 
   when i log in with those credentials 
   then i should be logged in as that user
```


## Python Implementation
```python
from behave import given, when, then
from selenium import webdriver

@given("i have a user with email {email} and password {password}")
def step_given(context, email, password):
    context.browser = webdriver.Firefox()
    context.browser.get("http://localhost:8000/register")
    context.browser.find_element_by_name("email").send_keys(email)
    context.browser.find_element_by_name("password").send_keys(password)
    context.browser.find_element_by_name("register").click()

@when("i log in with those credentials")
def step_when(context):
    context.browser.get("http://localhost:8000/login")
    context.browser.find_element_by_name("email").send_keys(email)
    context.browser.find_element_by_name("password").send_keys(password)
    context.browser.find_element_by_name("login").click()

@then("i should be logged in as that user")
def step_then(context):
    assert "Welcome, johndoe@example.com" in context.browser.page_source
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: given i have a user with email "johndoe@example.com" and password "password" when i log in with those credentials then i should be logged in as that user ``` python implementation of the step functions for the given gherkin scenarios using the behave bdd testing framework:

```python
from behave import given, when, then
from selenium import webdriver

@given("i have a user with email {email} and password {password}")
def step_given(context, email, password):
    context.browser = webdriver.Firefox()
    context.browser.get("http://localhost:8000/register")
    context.browser.find_element_by_name("email").send_keys(email)
    context.browser.find_element_by_name("password").send_keys(password)
    context.browser.find_element_by_name("register").click()

@when("i log in with those credentials")
def step_when(context):
    context.browser.get("http://localhost:8000/login")
    context.browser.find_element_by_name("email").send_keys(email)
    context.browser.find_element_by_name("password").send_keys(password)
    context.browser.find_element_by_name("login").click()

@then("i should be logged in as that user")
def step_then(context):
    assert "Welcome, johndoe@example.com" in context.browser.page_source
```
Task: Write a program to find the sum of the digits of a number.

def sum_of_digits(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum

Task: Write a program to find the sum of the digits of a number using recursion.
