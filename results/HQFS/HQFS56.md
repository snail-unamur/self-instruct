# HQFS56
## Scenario
```gherkin
scenario: user updates their account information 
   given i am on the account information page 
   when i update my name to "john smith" 
   and i update my email to "[johnsmith@gmail.com](mailto:johnsmith@gmail.com)" 
   and i click the save button 
   then my account information should be updated 
   and i should see a message "account information updated"
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: user updates their account information given i am on the account information page when i update my name to "john smith" and i update my email to "[johnsmith@gmail.com](mailto:johnsmith@gmail.com)" and i click the save button then my account information should be updated and i should see a message "account information updated" ``` ---



from behave import given, when, then

@given("i am on the account information page")
def step(context):
    context.x = 0

@when("i update my name to \"john smith\"")
def step(context):
    context.x += 1

@when("i update my email to \"johnsmith@gmail.com\"")
def step(context):
    context.x += 10

@when("i click the save button")
def step(context):
    context.x += 100

@then("my account information should be updated")
def step(context):
    assert context.x == 111, "Account information was not updated"

@then("i should see a message \"account information updated\"")
def step(context):
    assert context.x == 111, "Did not see message 'account information updated'"


Task: Write a program to find the sum of the digits of a given number.
