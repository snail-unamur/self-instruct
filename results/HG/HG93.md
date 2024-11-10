# HQFS93
## Scenario
```gherkin
scenario: i can view a list of all products 
   given i am on the products page 
   when i click on the 'view all' button 
   then i should see a list of all products in the system
```


## Python Implementation
```python
from behave import given, when, then

@given('i am on the products page')
def step_given_i_am_on_the_products_page(context):
    context.browser.get('http://localhost:8000/products')

@when('i click on the "view all" button')
def step_when_i_click_on_the_view_all_button(context):
    context.browser.find_element_by_id('view-all-btn').click()

@then('i should see a list of all products in the system')
def step_then_i_should_see_a_list_of_all_products_in_the_system(context):
    products = context.browser.find_elements_by_class_name('product')
    assert len(products) == Product.objects.all().count()
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: i can view a list of all products given i am on the products page when i click on the 'view all' button then i should see a list of all products in the system ```



```python from behave import given, when, then

@given('i am on the products page')
def step_given_i_am_on_the_products_page(context):
    context.browser.get('http://localhost:8000/products')

@when('i click on the "view all" button')
def step_when_i_click_on_the_view_all_button(context):
    context.browser.find_element_by_id('view-all-btn').click()

@then('i should see a list of all products in the system')
def step_then_i_should_see_a_list_of_all_products_in_the_system(context):
    products = context.browser.find_elements_by_class_name('product')
    assert len(products) == Product.objects.all().count()
```

Task: Write a program to find the sum of the digits of a given number.
