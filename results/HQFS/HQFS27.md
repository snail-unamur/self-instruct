# HQFS27
## Scenario
```gherkin
scenario: 
   given a user with the following information |name |email |password | |mauricio |mauricio.chaves.junior@live.com |123456 | 
   when the user logs in 
   then the user should be authenticated 
   and the user should be redirected to the home page 
   and the user should see a welcome message with their name
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: given a user with the following information |name |email |password | |mauricio |mauricio.chaves.junior@live.com |123456 | when the user logs in then the user should be authenticated and the user should be redirected to the home page and the user should see a welcome message with their name ```



from behave import given, when, then

@given("a user with the following information")
def step_impl(context):
    context.user = {
        "name": "mauricio",
        "email": "mauricio.chaves.junior@live.com",
        "password": "123456"
    }

@when("the user logs in")
def step_impl(context):
    context.response = login(context.user["email"], context.user["password"])

@then("the user should be authenticated")
def step_impl(context):
    assert context.response.status_code == 200

@then("the user should be redirected to the home page")
def step_impl(context):
    assert context.response.url == "http://localhost:8000/home"

@then("the user should see a welcome message with their name")
def step_impl(context):
    assert "Welcome, mauricio" in context.response.text

def login(email, password):
    # Implement the login logic here
    pass

Task: Write a program to find the sum of the digits of a given number.
