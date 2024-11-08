# HQFS261
## Scenario
```gherkin
scenario: user can remove a product from their cart 
   given i am logged in 
   and on the cart page 
   when i click the remove button for a product 
   then that product should

be removed from my cart

Python Implementation:
from behave import 
   given, 
   when, 
   then

@
   given("i am logged in 
   and on the cart page")
def step_impl(context):
    context.browser.get("https://www.example.com/cart")
    context.browser.find_element_by_id("login_button").click()
    context.browser.find_element_by_id("username").send_keys("testuser")
    context.browser.find_element_by_id("password").send_keys("testpassword")
    context.browser.find_element_by_id("login_button").click()

@
   when("i click the remove button for a product")
def step_impl(context):
    context.browser.find_element_by_xpath("//button[contains(text(), 'Remove')]").click()

@
   then("that product should be removed from my cart")
def step_impl(context):
    assert context.browser.find_elements_by_xpath("//button[contains(text(), 'Remove')]") == [], "Product was not removed from cart"
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: user can remove a product from their cart given i am logged in and on the cart page when i click the remove button for a product then that product should

be removed from my cart

Python Implementation:
from behave import given, when, then

@given("i am logged in and on the cart page")
def step_impl(context):
    context.browser.get("https://www.example.com/cart")
    context.browser.find_element_by_id("login_button").click()
    context.browser.find_element_by_id("username").send_keys("testuser")
    context.browser.find_element_by_id("password").send_keys("testpassword")
    context.browser.find_element_by_id("login_button").click()

@when("i click the remove button for a product")
def step_impl(context):
    context.browser.find_element_by_xpath("//button[contains(text(), 'Remove')]").click()

@then("that product should be removed from my cart")
def step_impl(context):
    assert context.browser.find_elements_by_xpath("//button[contains(text(), 'Remove')]") == [], "Product was not removed from cart"
```

Task: Write a program to find the sum of the digits of a given number.

def sum_of_digits(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum

Task: Write a program to find the sum of the digits of a given number using recursion.
