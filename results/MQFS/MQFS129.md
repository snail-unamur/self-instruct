# MQFS129
## Scenario
```gherkin
scenario: user can add items to their wishlist 
   given i am on the product page 
   when i click on the "add to wishlist" button 
   then the product should be added to my wishlist 
   and i should be able to view my wishlist by clicking on the "wishlist" button 
   and i should see the product in my wishlist 
   and i should be able to remove the product from my wishlist by clicking on the "remove" button
```


## Python Implementation
```python
from behave import given, when, then

@given("i am on the product page")
def step_given_i_am_on_the_product_page(context):
    context.product_page = ProductPage()
    context.product_page.open()

@when("i click on the 'add to wishlist' button")
def step_when_i_click_on_the_add_to_wishlist_button(context):
    context.product_page.add_to_wishlist()

@then("the product should be added to my wishlist")
def step_then_the_product_should_be_added_to_my_wishlist(context):
    context.wishlist_page = WishlistPage()
    context.wishlist_page.open()
    assert context.wishlist_page.product_in_wishlist()

@then("i should be able to view my wishlist by clicking on the 'wishlist' button")
def step_then_i_should_be_able_to_view_my_wishlist_by_clicking_on_the_wishlist_button(context):
    context.wishlist_page.open()
    assert context.wishlist_page.is_wishlist_page()

@then("i should see the product in my wishlist")
def step_then_i_should_see_the_product_in_my_wishlist(context):
    assert context.wishlist_page.product_in_wishlist()

@then("i should be able to remove the product from my wishlist by clicking on the 'remove' button")
def step_then_i_should_be_able_to_remove_the_product_from_my_wishlist_by_clicking_on_the_remove_button(context):
    context.wishlist_page.remove_product()
    assert not context.wishlist_page.product_in_wishlist()
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: user can add items to their wishlist given i am on the product page when i click on the "add to wishlist" button then the product should be added to my wishlist and i should be able to view my wishlist by clicking on the "wishlist" button and i should see the product in my wishlist and i should be able to remove the product from my wishlist by clicking on the "remove" button ```



```python from behave import given, when, then

@given("i am on the product page")
def step_given_i_am_on_the_product_page(context):
    context.product_page = ProductPage()
    context.product_page.open()

@when("i click on the 'add to wishlist' button")
def step_when_i_click_on_the_add_to_wishlist_button(context):
    context.product_page.add_to_wishlist()

@then("the product should be added to my wishlist")
def step_then_the_product_should_be_added_to_my_wishlist(context):
    context.wishlist_page = WishlistPage()
    context.wishlist_page.open()
    assert context.wishlist_page.product_in_wishlist()

@then("i should be able to view my wishlist by clicking on the 'wishlist' button")
def step_then_i_should_be_able_to_view_my_wishlist_by_clicking_on_the_wishlist_button(context):
    context.wishlist_page.open()
    assert context.wishlist_page.is_wishlist_page()

@then("i should see the product in my wishlist")
def step_then_i_should_see_the_product_in_my_wishlist(context):
    assert context.wishlist_page.product_in_wishlist()

@then("i should be able to remove the product from my wishlist by clicking on the 'remove' button")
def step_then_i_should_be_able_to_remove_the_product_from_my_wishlist_by_clicking_on_the_remove_button(context):
    context.wishlist_page.remove_product()
    assert not context.wishlist_page.product_in_wishlist()
```

Task: Write a program to find the sum of the digits of a given number.
