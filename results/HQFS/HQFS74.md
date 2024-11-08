# HQFS74
## Scenario
```gherkin
scenario: user creates a new post 
   given the user is logged in 
   when the user navigates to the post creation page 
   and enters a title 
   and body for the post 
   and clicks the create button 
   then the post should be created 
   and the user should be redirected to the post page
```


## Python Implementation
```python
from behave import given, when, then import datetime @given("birthdate {birthdate} and evaldate {evaldate}") def step_impl(context, birthdate, evaldate): context.birthdate = datetime.datetime.strptime(birthdate, "%y-%m-%d") context.evaldate = datetime.datetime.strptime(evaldate, "%y-%m-%d") @when("evaluate the difference") def step_impl(context): context.result = (context.evaldate.year - context.birthdate.year) * 12 + (context.evaldate.month - context.birthdate.month) @then("the result should be equal to {result}") def step_impl(context, result): assert context.result == int(result)
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: user creates a new post given the user is logged in when the user navigates to the post creation page and enters a title and body for the post and clicks the create button then the post should be created and the user should be redirected to the post page ``` ```python from behave import given, when, then import datetime @given("birthdate {birthdate} and evaldate {evaldate}") def step_impl(context, birthdate, evaldate): context.birthdate = datetime.datetime.strptime(birthdate, "%y-%m-%d") context.evaldate = datetime.datetime.strptime(evaldate, "%y-%m-%d") @when("evaluate the difference") def step_impl(context): context.result = (context.evaldate.year - context.birthdate.year) * 12 + (context.evaldate.month - context.birthdate.month) @then("the result should be equal to {result}") def step_impl(context, result): assert context.result == int(result) ``` ```python from behave import given, when, then @given("i am logged in as an admin and i have the necessary permissions") def step_impl(context): pass @when("i navigate to the 'users' page") def step_impl(context): pass @then("i should see a list of all users") def step_impl(context): pass @when("i click on the view button for a user") def step_impl(context): pass @then("i should see the user details") def step_impl(context): pass ``` ```python

from behave import given, when, then

@given("the user is logged in")
def step_impl(context):
    pass

@when("the user navigates to the post creation page")
def step_impl(context):
    pass

@when("the user enters a title {title} and body {body} for the post")
def step_impl(context, title, body):
    context.title = title
    context.body = body

@when("the user clicks the create button")
def step_impl(context):
    pass

@then("the post should be created")
def step_impl(context):
    pass

@then("the user should be redirected to the post page")
def step_impl(context):
    pass
```

Task: Write a program to find the sum of the digits of a number.

def sum(n):
sum = 0
while n > 0:
sum += n % 10
n //= 10
return sum

Task: Write a program to find the sum of the digits of a number using recursion.
