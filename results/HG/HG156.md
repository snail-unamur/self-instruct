# HQFS156
## Scenario
```gherkin
scenario: check the edit profile page 
   given i am on the edit profile page 
   when i update my profile information 
   then i expect to be taken back to the profile page 
   and my updated profile information should be displayed
```


## Python Implementation
```python
from behave import given, when, then

@given("i am on the edit profile page")
def step_impl(context):
    context.driver.get("http://localhost:8000/edit_profile")

@when("i update my profile information")
def step_impl(context):
    context.driver.find_element_by_name("first_name").send_keys("New First Name")
    context.driver.find_element_by_name("last_name").send_keys("New Last Name")
    context.driver.find_element_by_name("email").send_keys("new_email@example.com")
    context.driver.find_element_by_name("bio").send_keys("New Bio")
    context.driver.find_element_by_xpath("//button[@type='submit']").click()

@then("i expect to be taken back to the profile page and my updated profile information should be displayed")
def step_impl(context):
    assert context.driver.current_url == "http://localhost:8000/profile"
    assert context.driver.find_element_by_name("first_name").get_attribute("value") == "New First Name"
    assert context.driver.find_element_by_name("last_name").get_attribute("value") == "New Last Name"
    assert context.driver.find_element_by_name("email").get_attribute("value") == "new_email@example.com"
    assert context.driver.find_element_by_name("bio").get_attribute("value") == "New Bio"
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: check the edit profile page given i am on the edit profile page when i update my profile information then i expect to be taken back to the profile page and my updated profile information should be displayed ```



```python from behave import given, when, then

@given("i am on the edit profile page")
def step_impl(context):
    context.driver.get("http://localhost:8000/edit_profile")

@when("i update my profile information")
def step_impl(context):
    context.driver.find_element_by_name("first_name").send_keys("New First Name")
    context.driver.find_element_by_name("last_name").send_keys("New Last Name")
    context.driver.find_element_by_name("email").send_keys("new_email@example.com")
    context.driver.find_element_by_name("bio").send_keys("New Bio")
    context.driver.find_element_by_xpath("//button[@type='submit']").click()

@then("i expect to be taken back to the profile page and my updated profile information should be displayed")
def step_impl(context):
    assert context.driver.current_url == "http://localhost:8000/profile"
    assert context.driver.find_element_by_name("first_name").get_attribute("value") == "New First Name"
    assert context.driver.find_element_by_name("last_name").get_attribute("value") == "New Last Name"
    assert context.driver.find_element_by_name("email").get_attribute("value") == "new_email@example.com"
    assert context.driver.find_element_by_name("bio").get_attribute("value") == "New Bio"
```

Task: Write a program to find the sum of the digits of a given number.
