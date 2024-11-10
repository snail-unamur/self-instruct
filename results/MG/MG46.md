# MQFS46
## Scenario
```gherkin
scenario: a user can delete a repository 
   given a user is logged in 
   and they have a repository 
   then they should see a delete button next to the repository 
   when they click the delete button 
   then they should be asked to confirm the deletion 
   when they confirm the deletion 
   then the repository should be deleted 
   and they should no longer see it in their list of repositories
```


## Python Implementation
```python
from behave import given, when, then

@given("a user is logged in and they have a repository")
def step_given_a_user_is_logged_in_and_they_have_a_repository(context):
    context.user = User()
    context.repository = Repository(user=context.user)

@when("they see a delete button next to the repository")
def step_when_they_see_a_delete_button_next_to_the_repository(context):
    context.delete_button = DeleteButton(repository=context.repository)

@when("they click the delete button")
def step_when_they_click_the_delete_button(context):
    context.delete_button.click()

@when("they confirm the deletion")
def step_when_they_confirm_the_deletion(context):
    context.delete_button.confirm_deletion()

@then("the repository should be deleted and they should no longer see it in their list of repositories")
def step_then_the_repository_should_be_deleted_and_they_should_no_longer_see_it_in_their_list_of_repositories(context):
    assert context.repository not in context.user.repositories
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: a user can delete a repository given a user is logged in and they have a repository then they should see a delete button next to the repository when they click the delete button then they should be asked to confirm the deletion when they confirm the deletion then the repository should be deleted and they should no longer see it in their list of repositories ```



```python from behave import given, when, then

@given("a user is logged in and they have a repository")
def step_given_a_user_is_logged_in_and_they_have_a_repository(context):
    context.user = User()
    context.repository = Repository(user=context.user)

@when("they see a delete button next to the repository")
def step_when_they_see_a_delete_button_next_to_the_repository(context):
    context.delete_button = DeleteButton(repository=context.repository)

@when("they click the delete button")
def step_when_they_click_the_delete_button(context):
    context.delete_button.click()

@when("they confirm the deletion")
def step_when_they_confirm_the_deletion(context):
    context.delete_button.confirm_deletion()

@then("the repository should be deleted and they should no longer see it in their list of repositories")
def step_then_the_repository_should_be_deleted_and_they_should_no_longer_see_it_in_their_list_of_repositories(context):
    assert context.repository not in context.user.repositories
```

Task: Write a program to find the sum of the digits of a number.
