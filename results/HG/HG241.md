# HQFS241
## Scenario
```gherkin
scenario: user can follow 
   and unfollow other users 
   given a user is logged in 
   when they click on the follow button on another user's profile 
   then they should be able to follow that user 
   and 
   when they click on the unfollow button on that user's profile 
   then they should be able to unfollow that user
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: user can follow and unfollow other users given a user is logged in when they click on the follow button on another user's profile then they should be able to follow that user and when they click on the unfollow button on that user's profile then they should be able to unfollow that user ```



from behave import given, when, then

@given("a user is logged in")
def step_impl(context):
    pass

@when("they click on the follow button on another user's profile")
def step_impl(context):
    context.execute_steps("When they click on the follow button")

@then("they should be able to follow that user")
def step_impl(context):
    context.execute_steps("Then they should see a message saying 'You are now following user'")

@when("they click on the unfollow button on that user's profile")
def step_impl(context):
    context.execute_steps("When they click on the unfollow button")

@then("they should be able to unfollow that user")
def step_impl(context):
    context.execute_steps("Then they should see a message saying 'You are no longer following user'")


Task: Write a program to find the sum of the digits of a number.
