# MQFS80
## Scenario
```gherkin
scenario: testing the functionality of the delete button 
   given i am on the user profile page 
   and i am the owner of the profile 
   when i click the delete button 
   then i should be taken to the login page 
   and i should not be able to see the user profile page anymore
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: testing the functionality of the delete button given i am on the user profile page and i am the owner of the profile when i click the delete button then i should be taken to the login page and i should not be able to see the user profile page anymore ```



from behave import given, when, then
from features.steps.steps import login

@given('i am on the user profile page and i am the owner of the profile')
def step(context):
    login(context)
    context.browser.get('http://localhost:8000/profile')

@when('i click the delete button')
def step(context):
    context.browser.find_element_by_id('delete-button').click()

@then('i should be taken to the login page and i should not be able to see the user profile page anymore')
def step(context):
    assert context.browser.current_url == 'http://localhost:80000/login'
    assert context.browser.find_elements_by_xpath('//*[@id="profile"]') == []

Task: Write a program to find the sum of the digits of a given number.
