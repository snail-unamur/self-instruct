# MQFS69
## Scenario
```gherkin
scenario: user wants to update a product's information 
   given i am on the product management page 
   when i select the product i want to update 
   and i click on the "edit" button 
   and i update the required fields 
   and i click on the "save" button 
   then i should see the updated product in the product list
```


## Python Implementation
```python
from behave import given, when, then

@given("i am on the product management page")
def step_impl(context):
    context.product_page.navigate()

@when("i select the product i want to update")
def step_impl(context):
    context.product_page.select_product()

@when("i click on the 'edit' button")
def step_impl(context):
    context.product_page.click_edit()

@when("i update the required fields")
def step_impl(context):
    context.product_page.update_fields()

@when("i click on the 'save' button")
def step_impl(context):
    context.product_page.click_save()

@then("i should see the updated product in the product list")
def step_impl(context):
    context.product_page.verify_update()
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: user wants to update a product's information given i am on the product management page when i select the product i want to update and i click on the "edit" button and i update the required fields and i click on the "save" button then i should see the updated product in the product list ```



```python from behave import given, when, then

@given("i am on the product management page")
def step_impl(context):
    context.product_page.navigate()

@when("i select the product i want to update")
def step_impl(context):
    context.product_page.select_product()

@when("i click on the 'edit' button")
def step_impl(context):
    context.product_page.click_edit()

@when("i update the required fields")
def step_impl(context):
    context.product_page.update_fields()

@when("i click on the 'save' button")
def step_impl(context):
    context.product_page.click_save()

@then("i should see the updated product in the product list")
def step_impl(context):
    context.product_page.verify_update()
```

Task: Write a program to find the sum of digits of a given number.
