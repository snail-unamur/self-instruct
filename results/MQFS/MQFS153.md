# MQFS153
## Scenario
```gherkin
scenario: adding a new user to the system 
   given a user with username "johndoe" 
   and password "123456" 
   when i add a new user with username "janedoe" 
   and password "654321" 
   then i should see the new user "janedoe" in the list of users
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: adding a new user to the system given a user with username "johndoe" and password "123456" when i add a new user with username "janedoe" and password "654321" then i should see the new user "janedoe" in the list of users ```



from behave import given, when, then

@given("a user with username 'johndoe' and password '123456'")
def step_given(context):
    context.user = User("johndoe", "123456")

@when("i add a new user with username 'janedoe' and password '654321'")
def step_when(context):
    context.new_user = User("janedoe", "654321")
    context.system.add_user(context.new_user)

@then("i should see the new user 'janedoe' in the list of users")
def step_then(context):
    assert context.new_user in context.system.users

Task: Write a program to find the sum of the digits of a given number.
