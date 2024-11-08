# HQFS5
## Scenario
```gherkin
scenario: a user can delete a payment method from their account 
   given the user is logged in 
   when the user navigates to the payment methods page 
   and the user clicks on the "delete" button next to the payment method they want to delete 
   then the payment method should be removed from the user's account
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: a user can delete a payment method from their account given the user is logged in when the user navigates to the payment methods page and the user clicks on the "delete" button next to the payment method they want to delete then the payment method should be removed from the user's account ```



from behave import given, when, then

@given("the user is logged in")
def step_impl(context):
    pass

@when("the user navigates to the payment methods page")
def step_impl(context):
    pass

@when("the user clicks on the 'delete' button next to the payment method they want to delete")
def step_impl(context):
    pass

@then("the payment method should be removed from the user's account")
def step_impl(context):
    pass

Task: Write a program to find the sum of the digits of a given number.
