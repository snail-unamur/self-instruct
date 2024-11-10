# MQFS202
## Scenario
```gherkin
scenario: testing a new feature 
   given a user with username "foo" 
   and password "bar" 
   and i am on the page with relative url "/login/" 
   when i put "foo" in the field with name "username" 
   and i put "bar" in the field with name "password" 
   and i click the element with name "submit" 
   and i am on the page with relative url "/new_feature/" 
   when i click the element with name "try_new_feature" 
   then i should see the message "welcome to the new feature!"
```


## Python Implementation
```python
from behave import given, when, then

@given("a user with username 'foo' and password 'bar'")
def step_impl(context):
    context.user = User("foo", "bar")

@given("i am on the page with relative url '/login/'")
def step_impl(context):
    context.browser.get(context.base_url + "/login/")

@when("i put 'foo' in the field with name 'username'")
def step_impl(context):
    context.browser.find_element_by_name("username").send_keys("foo")

@when("i put 'bar' in the field with name 'password'")
def step_impl(context):
    context.browser.find_element_by_name("password").send_keys("bar")

@when("i click the element with name 'submit'")
def step_impl(context):
    context.browser.find_element_by_name("submit").click()

@then("i am on the page with relative url '/new_feature/'")
def step_impl(context):
    assert context.browser.current_url == context.base_url + "/new_feature/"

@when("i click the element with name 'try_new_feature'")
def step_impl(context):
    context.browser.find_element_by_name("try_new_feature").click()

@then("i should see the message 'welcome to the new feature!'")
def step_impl(context):
    assert "welcome to the new feature!" in context.browser.page_source
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: testing a new feature given a user with username "foo" and password "bar" and i am on the page with relative url "/login/" when i put "foo" in the field with name "username" and i put "bar" in the field with name "password" and i click the element with name "submit" and i am on the page with relative url "/new_feature/" when i click the element with name "try_new_feature" then i should see the message "welcome to the new feature!" ```



```python from behave import given, when, then

@given("a user with username 'foo' and password 'bar'")
def step_impl(context):
    context.user = User("foo", "bar")

@given("i am on the page with relative url '/login/'")
def step_impl(context):
    context.browser.get(context.base_url + "/login/")

@when("i put 'foo' in the field with name 'username'")
def step_impl(context):
    context.browser.find_element_by_name("username").send_keys("foo")

@when("i put 'bar' in the field with name 'password'")
def step_impl(context):
    context.browser.find_element_by_name("password").send_keys("bar")

@when("i click the element with name 'submit'")
def step_impl(context):
    context.browser.find_element_by_name("submit").click()

@then("i am on the page with relative url '/new_feature/'")
def step_impl(context):
    assert context.browser.current_url == context.base_url + "/new_feature/"

@when("i click the element with name 'try_new_feature'")
def step_impl(context):
    context.browser.find_element_by_name("try_new_feature").click()

@then("i should see the message 'welcome to the new feature!'")
def step_impl(context):
    assert "welcome to the new feature!" in context.browser.page_source
```

Task: Write a program to find the sum of the digits of a number.
