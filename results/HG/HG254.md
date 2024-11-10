# HQFS254
## Scenario
```gherkin
scenario: a user is registered with a password that does not meet the requirements 
   given a user with name "john" 
   and email "john@example.com" 
   when they register with a password "short" 
   then they should not be registered as a user
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: a user is registered with a password that does not meet the requirements given a user with name "john" and email "john@example.com" when they register with a password "short" then they should not be registered as a user ```



from behave import given, when, then

@given("a user with name 'john' and email 'john@example.com'")
def step_given(context):
    context.user = User("john", "john@example.com")

@when("they register with a password 'short'")
def step_when(context):
    context.user.password = "short"
    context.result = context.user.register()

@then("they should not be registered as a user")
def step_then(context):
    assert not context.result

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.password = None

    def register(self):
        if len(self.password) < 8:
            return False
        # register user
        return True

Task: Write a program to find the sum of the digits of a given number.
