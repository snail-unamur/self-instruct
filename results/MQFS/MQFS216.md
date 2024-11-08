# MQFS216
## Scenario
```gherkin
scenario: a user can create a new repository 
   given a user is logged in 
   then they should see a "create new repository" button 
   when they click the "create new repository" button 
   then they should be taken to a form where they can enter the name 
   and description of the repository 
   when they submit the form 
   then they should be taken to the new repository page 
   and they should see the name 
   and description of the repository they just created
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: a user can create a new repository given a user is logged in then they should see a "create new repository" button when they click the "create new repository" button then they should be taken to a form where they can enter the name and description of the repository when they submit the form then they should be taken to the new repository page and they should see the name and description of the repository they just created ```



from behave import given, when, then

@given("a user is logged in")
def step_given_a_user_is_logged_in(context):
    context.user = User()
    context.user.login()

@when("they should see a \"create new repository\" button")
def step_when_they_should_see_a_create_new_repository_button(context):
    context.page = RepositoryPage()
    context.page.load()

@when("they click the \"create new repository\" button")
def step_when_they_click_the_create_new_repository_button(context):
    context.page.click_create_new_repository_button()

@then("they should be taken to a form where they can enter the name and description of the repository")
def step_then_they_should_be_taken_to_a_form_where_they_can_enter_the_name_and_description_of_the_repository(context):
    context.page = NewRepositoryPage()
    context.page.load()

@when("they submit the form")
def step_when_they_submit_the_form(context):
    context.page.submit_form()

@then("they should be taken to the new repository page")
def step_then_they_should_be_taken_to_the_new_repository_page(context):
    context.page = NewRepositoryPage()
    assert context.page.on_new_repository_page()

@then("they should see the name and description of the repository they just created")
def step_then_they_should_see_the_name_and_description_of_the_repository_they_just_created(context):
    context.page = NewRepositoryPage()
    assert context.page.name_and_description_match()


Task: Write a program to find the sum of the digits of a number.
