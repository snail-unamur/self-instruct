# MQFS227
## Scenario
```gherkin
scenario: adding a new product to the inventory 
   given a user is logged in 
   when the user navigates to the inventory page 
   then the user should see a button to add a new product 
   when the user clicks the button to add a new product 
   then the user should be taken to a new page with a form to add a new product 
   when the user fills out the form with valid information 
   then the user should be taken to the inventory page with the new product listed 
   when the user clicks on the new product 
   then the user should be taken to the product page for the new product
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: adding a new product to the inventory given a user is logged in when the user navigates to the inventory page then the user should see a button to add a new product when the user clicks the button to add a new product then the user should be taken to a new page with a form to add a new product when the user fills out the form with valid information then the user should be taken to the inventory page with the new product listed when the user clicks on the new product then the user should be taken to the product page for the new product ```



```python from behave import given, when, then

@given("a user is logged in")
def step_given_a_user_is_logged_in(context):
    context.user = User()
    context.user.login()

@when("the user navigates to the inventory page")
def step_when_the_user_navigates_to_the_inventory_page(context):
    context.page = InventoryPage()
    context.page.load()

@then("the user should see a button to add a new product")
def step_then_the_user_should_see_a_button_to_add_a_new_product(context):
    assert context.page.add_new_product_button.is_displayed()

@when("the user clicks the button to add a new product")
def step_when_the_user_clicks_the_button_to_add_a_new_product(context):
    context.page.add_new_product_button.click()

@then("the user should be taken to a new page with a form to add a new product")
def step_then_the_user_should_be_taken_to_a_new_page_with_a_form_to_add_a_new_product(context):
    context.page = AddProductPage()
    assert context.page.is_current_page()

@when("the user fills out the form with valid information")
def step_when_the_user_fills_out_the_form_with_valid_information(context):
    context.product = Product()
    context.product.name = "New Product"
    context.product.description = "A new product"
    context.product.price = 10.00
    context.page = AddProductPage()
    context.page.add_product(context.product)

@then("the user should be taken to the inventory page with the new product listed")
def step_then_the_user_should_be_taken_to_the_inventory_page_with_the_new_product_listed(context):
    context.page
