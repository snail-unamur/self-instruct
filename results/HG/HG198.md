# HQFS198
## Scenario
```gherkin
scenario: the user should be able to see the list of all the orders that he has made 
   given i am logged in 
   when i go to the "my orders" page 
   then i should see the list of all the orders that i have made
```


## Python Implementation
```python
from behave import given, when, then

@given("i am logged in")
def step_impl(context):
    context.execute_steps("Given I am on the login page")
    context.execute_steps("When I enter my credentials")
    context.execute_steps("And I click on the login button")
    context.execute_steps("Then I should see the dashboard")

@when("i go to the 'my orders' page")
def step_impl(context):
    context.execute_steps("When I click on the 'my orders' link")

@then("i should see the list of all the orders that i have made")
def step_impl(context):
    context.execute_steps("Then I should see the orders page")
    context.execute_steps("Then I should see the list of orders")
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: the user should be able to see the list of all the orders that he has made given i am logged in when i go to the "my orders" page then i should see the list of all the orders that i have made ```



```python from behave import given, when, then

@given("i am logged in")
def step_impl(context):
    context.execute_steps("Given I am on the login page")
    context.execute_steps("When I enter my credentials")
    context.execute_steps("And I click on the login button")
    context.execute_steps("Then I should see the dashboard")

@when("i go to the 'my orders' page")
def step_impl(context):
    context.execute_steps("When I click on the 'my orders' link")

@then("i should see the list of all the orders that i have made")
def step_impl(context):
    context.execute_steps("Then I should see the orders page")
    context.execute_steps("Then I should see the list of orders")
```

Task: Write a program to find the sum of the digits of a given number.
