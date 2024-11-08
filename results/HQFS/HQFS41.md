# HQFS41
## Scenario
```gherkin
scenario: user adds a product to their wishlist 
   given i am logged in 
   when i go to the product page 
   and add the product to my wishlist 
   then the product is added to my wishlist
```


## Python Implementation
```python
from behave import given, when, then

@given("i am logged in")
def step_impl(context):
    context.user = User()
    context.user.login()

@when("i go to the product page")
def step_impl(context):
    context.product_page = ProductPage()
    context.product_page.open()

@when("add the product to my wishlist")
def step_impl(context):
    context.wishlist = Wishlist()
    context.product_page.add_to_wishlist()
    context.wishlist.open()

@then("the product is added to my wishlist")
def step_impl(context):
    assert context.product_page.product_on_wishlist()
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: user adds a product to their wishlist given i am logged in when i go to the product page and add the product to my wishlist then the product is added to my wishlist ```



```python from behave import given, when, then

@given("i am logged in")
def step_impl(context):
    context.user = User()
    context.user.login()

@when("i go to the product page")
def step_impl(context):
    context.product_page = ProductPage()
    context.product_page.open()

@when("add the product to my wishlist")
def step_impl(context):
    context.wishlist = Wishlist()
    context.product_page.add_to_wishlist()
    context.wishlist.open()

@then("the product is added to my wishlist")
def step_impl(context):
    assert context.product_page.product_on_wishlist()
```

Task: Write a program to find the sum of the digits of a given number.
