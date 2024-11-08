# MQFS170
## Scenario
```gherkin
None
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: create a new user given i am on the homepage when i click on the create new user button then i should be able to enter a first name then i should be able to enter a last name then i should be able to enter an email then i should be able to enter a password then i should be able to enter a confirm password then i should be able to enter a phone number then i should be able to enter a job title then i should be able to enter a department then i should be able to enter a company then i should be able to enter a country then i should be able to enter a city then i should be able to enter a street then i should be able to enter a building then i should be able to enter a zip then i should be able to enter a website then i should be able to enter a linkedin then i should be able to enter a twitter then i should be able to enter a facebook then i should be able to enter a github then i should be able to enter a stackoverflow then i should be able to enter a bitbucket then i should be able to enter a skype then i should be able to enter a google plus then i should be able to enter a pinterest then i should be able to enter a youtube then i should be able to enter a vimeo then i should be able to enter a behance then i should be able to enter a dribbble then i should be able to enter a medium then i should be able to enter a telegram then i should be able to enter a slack then i should be able to enter a discord then i should be able to enter a reddit then i should be able to enter a tumblr then i should be able to enter a flickr then i should be able to enter a instagram then i should be able to enter a tiktok then i should be able to enter a soundcloud then i should be able to enter a spotify then i should be able to enter a twitch then i should be able to enter a steam then i should be able to enter a xbox then i should be able to enter a playstation then i should be able to enter a nintendo then i should be able to enter a sony then i should be able to enter a microsoft then i should be able to enter a google



from behave import given, when, then

@given("i am on the homepage")
def step_given_i_am_on_the_homepage(context):
    context.homepage = HomePage()
    context.homepage.open()

@when("i click on the create new user button")
def step_when_i_click_on_the_create_new_user_button(context):
    context.create_new_user_button = context.homepage.click_create_new_user_button()

@then("i should be able to enter a first name")
def step_then_i_should_be_able_to_enter_a_first_name(context):
    context.first_name_field = context.create_new_user_button.enter_first_name()

@then("i should be able to enter a last name")
def step_then_i_should_be_able_to_enter_a_last_name(context):
    context.last_name_field = context.first_name_field.enter_last_name()

@then("i should be able to enter an email")
def step_then_i_should_be_able_to_enter_an_email(context):
    context.email_field = context.last_name_field.enter_email()

@then("i should be able to enter a password")
def step_then_i_should_be_able_to_enter_a_password(context):
    context.password_field = context.email_field.enter_password()

@then("i should be able to enter a confirm password")
def step_then_i_should_be_able_to_enter_a_confirm_password(context):
    context.confirm_password_field = context.password_field.enter_confirm_password()

@then("i should be able to enter a phone number")
def step_then_i_should_be_able_to_enter_a_phone_number(context):
    context.phone_number_field = context.confirm_password_field.enter_phone_number()

@then("i should be able to enter
