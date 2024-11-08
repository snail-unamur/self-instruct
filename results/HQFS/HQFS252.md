# HQFS252
## Scenario
```gherkin
scenario: i can view my cart 
   given i have added books to my cart 
   when i click on the cart icon 
   then i should see the books in my cart
```


## Python Implementation
```python
from behave import given, when, then

@given("i have added books to my cart")
def step_given_i_have_added_books_to_my_cart(context):
    context.books = ["Python", "Java", "C++"]
    context.cart = context.books.copy()

@when("i click on the cart icon")
def step_when_i_click_on_the_cart_icon(context):
    context.view = context.cart.copy()

@then("i should see the books in my cart")
def step_then_i_should_see_the_books_in_my_cart(context):
    assert context.view == context.cart
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: i can view my cart given i have added books to my cart when i click on the cart icon then i should see the books in my cart ```



```python from behave import given, when, then

@given("i have added books to my cart")
def step_given_i_have_added_books_to_my_cart(context):
    context.books = ["Python", "Java", "C++"]
    context.cart = context.books.copy()

@when("i click on the cart icon")
def step_when_i_click_on_the_cart_icon(context):
    context.view = context.cart.copy()

@then("i should see the books in my cart")
def step_then_i_should_see_the_books_in_my_cart(context):
    assert context.view == context.cart
```

Task: Write a program to find the sum of the digits of a given number.
