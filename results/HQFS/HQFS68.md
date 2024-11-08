# HQFS68
## Scenario
```gherkin
scenario: delete a user 
   given i am on the user management page 
   and i have a user with email "mauricio.chaves.junior@live.com" 
   when i delete the user with email "mauricio.chaves.junior@live.com" 
   then i should be on the user management page 
   and i should not see the user with email "mauricio.chaves.junior@live.com"
```


## Python Implementation
```python
from behave import given, when, then

@given("i am on the user management page")
def step_given_i_am_on_the_user_management_page(context):
    context.driver.get("http://localhost:8000/users")

@given("i have a user with email {email}")
def step_given_i_have_a_user_with_email(context, email):
    context.user = User(email=email)
    context.user.save()

@when("i delete the user with email {email}")
def step_when_i_delete_the_user_with_email(context, email):
    user = User.objects.get(email=email)
    user.delete()

@then("i should be on the user management page")
def step_then_i_should_be_on_the_user_management_page(context):
    assert context.driver.current_url == "http://localhost:8000/users"

@then("i should not see the user with email {email}")
def step_then_i_should_not_see_the_user_with_email(context, email):
    assert User.objects.filter(email=email).exists() == False
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: delete a user given i am on the user management page and i have a user with email "mauricio.chaves.junior@live.com" when i delete the user with email "mauricio.chaves.junior@live.com" then i should be on the user management page and i should not see the user with email "mauricio.chaves.junior@live.com" ```



```python from behave import given, when, then

@given("i am on the user management page")
def step_given_i_am_on_the_user_management_page(context):
    context.driver.get("http://localhost:8000/users")

@given("i have a user with email {email}")
def step_given_i_have_a_user_with_email(context, email):
    context.user = User(email=email)
    context.user.save()

@when("i delete the user with email {email}")
def step_when_i_delete_the_user_with_email(context, email):
    user = User.objects.get(email=email)
    user.delete()

@then("i should be on the user management page")
def step_then_i_should_be_on_the_user_management_page(context):
    assert context.driver.current_url == "http://localhost:8000/users"

@then("i should not see the user with email {email}")
def step_then_i_should_not_see_the_user_with_email(context, email):
    assert User.objects.filter(email=email).exists() == False
```

Task: Write a program to find the sum of the digits of a number.
