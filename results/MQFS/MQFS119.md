# MQFS119
## Scenario
```gherkin
scenario: a user can add a new recipe 
   given the user is logged in 
   when the user clicks on the "add recipe" button 
   then the user should be taken to the "add recipe" page 
   and the user should see the form to add a new recipe 
   when the user fills in the form 
   and clicks on the "save" button 
   then the recipe should be added to the user's list of recipes
```


## Python Implementation
```python
from behave import given, when, then

@given("the user is logged in")
def step_impl(context):
    context.user = User("testuser@test.com", "testpassword")
    context.user.login()

@when("the user clicks on the 'add recipe' button")
def step_impl(context):
    context.add_recipe_page = AddRecipePage()
    context.add_recipe_page.load()
    context.add_recipe_page.click_add_recipe_button()

@then("the user should be taken to the 'add recipe' page")
def step_impl(context):
    assert context.add_recipe_page.is_the_current_page()

@then("the user should see the form to add a new recipe")
def step_impl(context):
    assert context.add_recipe_page.is_add_recipe_form_visible()

@when("the user fills in the form and clicks on the 'save' button")
def step_impl(context):
    context.recipe = Recipe("Test Recipe", "This is a test recipe.")
    context.add_recipe_page.fill_in_form(context.recipe)
    context.add_recipe_page.click_save_button()

@then("the recipe should be added to the user's list of recipes")
def step_impl(context):
    assert context.recipe in context.user.recipes
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: a user can add a new recipe given the user is logged in when the user clicks on the "add recipe" button then the user should be taken to the "add recipe" page and the user should see the form to add a new recipe when the user fills in the form and clicks on the "save" button then the recipe should be added to the user's list of recipes ```



```python from behave import given, when, then

@given("the user is logged in")
def step_impl(context):
    context.user = User("testuser@test.com", "testpassword")
    context.user.login()

@when("the user clicks on the 'add recipe' button")
def step_impl(context):
    context.add_recipe_page = AddRecipePage()
    context.add_recipe_page.load()
    context.add_recipe_page.click_add_recipe_button()

@then("the user should be taken to the 'add recipe' page")
def step_impl(context):
    assert context.add_recipe_page.is_the_current_page()

@then("the user should see the form to add a new recipe")
def step_impl(context):
    assert context.add_recipe_page.is_add_recipe_form_visible()

@when("the user fills in the form and clicks on the 'save' button")
def step_impl(context):
    context.recipe = Recipe("Test Recipe", "This is a test recipe.")
    context.add_recipe_page.fill_in_form(context.recipe)
    context.add_recipe_page.click_save_button()

@then("the recipe should be added to the user's list of recipes")
def step_impl(context):
    assert context.recipe in context.user.recipes
```

Task: Write a program to find the sum of the digits of a number.
