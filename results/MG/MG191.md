# MQFS191
## Scenario
```gherkin
scenario: a user can add a new product to the cart 
   given i am on the product page 
   when i click on the "add to cart" button 
   then i should see the product in the cart with the new name `# python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework :
```


## Python Implementation
```python
from behave import given, when, then

@given("i am on my profile page")
def step_given_i_am_on_my_profile_page(context):
    context.driver.get("https://example.com/profile")

@when("i click on the edit profile button and i update my name with \"<new_name>\"")
def step_when_i_click_on_the_edit_profile_button_and_i_update_my_name_with_new_name(context, new_name):
    context.driver.find_element_by_id("edit-profile-button").click()
    context.driver.find_element_by_id("name-input").send_keys(new_name)
    context.driver.find_element_by_id("save-changes-button").click()

@then("i should see my name updated to \"<new_name>\"")
def step_then_i_should_see_my_name_updated_to_new_name(context, new_name):
    assert context.driver.find_element_by_id("profile-name").text == new_name
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: a user can add a new product to the cart given i am on the product page when i click on the "add to cart" button then i should see the product in the cart with the new name `# python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: basic parsing given a string with an argument then we get "with" parsed ``` python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: testing the user profile update given i am on my profile page when i click on the edit profile button and i update my name with "<new_name>"

then i should see my name updated to "<new_name>"
```
```python
from behave import given, when, then

@given("i am on my profile page")
def step_given_i_am_on_my_profile_page(context):
    context.driver.get("https://example.com/profile")

@when("i click on the edit profile button and i update my name with \"<new_name>\"")
def step_when_i_click_on_the_edit_profile_button_and_i_update_my_name_with_new_name(context, new_name):
    context.driver.find_element_by_id("edit-profile-button").click()
    context.driver.find_element_by_id("name-input").send_keys(new_name)
    context.driver.find_element_by_id("save-changes-button").click()

@then("i should see my name updated to \"<new_name>\"")
def step_then_i_should_see_my_name_updated_to_new_name(context, new_name):
    assert context.driver.find_element_by_id("profile-name").text == new_name
```

Task: Write a program to find the sum of the digits of a given number.

def sum(n):
sum = 0
while n > 0:
sum += n % 10
n //= 10
return sum

Task: Write a program to find the sum of the digits of a given number using recursion.
