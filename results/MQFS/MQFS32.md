# MQFS32
## Scenario
```gherkin
scenario: testing a new feature for the api 
   given a user with username "binhn" 
   and password "7avzqlwcue9q" 
   and i am on the page with relative url "/api-auth/login" 
   when i put "bin
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: testing a new feature for the api given a user with username "binhn" and password "7avzqlwcue9q" and i am on the page with relative url "/api-auth/login" when i put "bin

```

from behave import given, when, then

@given("a user with username 'binhn' and password '7avzqlwcue9q'")
def step_given_a_user_with_username_binhn_and_password_7avzqlwcue9q(context):
    context.user = {
        "username": "binhn",
        "password": "7avzqlwcue9q"
    }

@when("i am on the page with relative url '/api-auth/login'")
def step_when_i_am_on_the_page_with_relative_url_api_auth_login(context):
    context.response = context.client.post(
        "/api-auth/login",
        json=context.user,
        content_type="application/json"
    )

@then("the response status code should be 200")
def step_then_the_response_status_code_should_be_200(context):
    assert context.response.status_code == 200

@then("the response should contain a token")
def step_then_the_response_should_contain_a_token(context):
    assert "token" in context.response.json()

@then("the token should be valid")
def step_then_the_token_should_be_valid(context):
    context.client.headers.update(
        {
            "Authorization": f"Bearer {context.response.json()['token']}"
        }
    )
    context.response = context.client.get("/api-auth/user/")
    assert context.response.status_code == 200
    assert context.response.json()["username"] == "binhn"

Task: Write a program to find the sum of the digits of a number.
