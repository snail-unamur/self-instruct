# MQFS183
## Scenario
```gherkin
scenario: verify that the user can see the list of all products 
   given the user is on the home page 
   when the user clicks on the 'products' button 
   then the user should see the list of all products
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: verify that the user can see the list of all products given the user is on the home page when the user clicks on the 'products' button then the user should see the list of all products ```



from behave import given, when, then

@given('the user is on the home page')
def step_given_the_user_is_on_the_home_page(context):
    context.home_page.open()

@when('the user clicks on the "products" button')
def step_when_the_user_clicks_on_the_products_button(context):
    context.home_page.click_products_button()

@then('the user should see the list of all products')
def step_then_the_user_should_see_the_list_of_all_products(context):
    context.assert_that(context.home_page.get_products()).is_equal_to(context.expected_products)

Task: Write a program to find the sum of the digits of a given number.
