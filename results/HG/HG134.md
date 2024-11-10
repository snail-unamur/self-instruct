# HQFS134
## Scenario
```gherkin
scenario: i can add a new user to a group 
   given i am on the group page 
   and i have a user with name "john doe" 
   when i add the user to the group 
   then the user should be displayed in the group list
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: i can add a new user to a group given i am on the group page and i have a user with name "john doe" when i add the user to the group then the user should be displayed in the group list ```



from behave import given, when, then

@given("i am on the group page")
def step_impl(context):
    context.execute_steps("Given I am on the group page")

@given("i have a user with name {name}")
def step_impl(context, name):
    context.execute_steps(f"Given I have a user with name {name}")

@when("i add the user to the group")
def step_impl(context):
    context.execute_steps("When I add the user to the group")

@then("the user should be displayed in the group list")
def step_impl(context):
    context.execute_steps("Then the user should be displayed in the group list")

Task: Write a program to find the sum of the digits of a number.
