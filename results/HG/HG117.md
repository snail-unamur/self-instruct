# HQFS117
## Scenario
```gherkin
scenario: user is able to edit their profile 
   given a user is logged in 
   when they click on the 'edit profile' button 
   and they make changes to their profile information 
   and they click on the 'save changes' button 
   then their profile information should be updated
```


## Python Implementation
```python
from behave import given, when, then

@given('a user is logged in')
def step_impl(context):
    # Implement login steps here
    pass

@when('they click on the "edit profile" button')
def step_impl(context):
    # Implement clicking on the edit profile button here
    pass

@when('they make changes to their profile information')
def step_impl(context):
    # Implement making changes to profile information here
    pass

@when('they click on the "save changes" button')
def step_impl(context):
    # Implement clicking on the save changes button here
    pass

@then('their profile information should be updated')
def step_impl(context):
    # Implement checking if profile information is updated here
    pass
```


## Raw Text
Generate python code for the following gherkin scenario using the behave bdd testing framework: ```gherkin scenario: user is able to edit their profile given a user is logged in when they click on the 'edit profile' button and they make changes to their profile information and they click on the 'save changes' button then their profile information should be updated ```



```python from behave import given, when, then

@given('a user is logged in')
def step_impl(context):
    # Implement login steps here
    pass

@when('they click on the "edit profile" button')
def step_impl(context):
    # Implement clicking on the edit profile button here
    pass

@when('they make changes to their profile information')
def step_impl(context):
    # Implement making changes to profile information here
    pass

@when('they click on the "save changes" button')
def step_impl(context):
    # Implement clicking on the save changes button here
    pass

@then('their profile information should be updated')
def step_impl(context):
    # Implement checking if profile information is updated here
    pass
```

Task: Write a program to find the second largest number in a list.
