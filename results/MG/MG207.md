# MQFS207
## Scenario
```gherkin
scenario: user can view their order history 
   given i am logged in as a user 
   when i navigate to my order history page 
   then i should see a list of all my past orders including the order date, order total, 
   and a link to view the order details 
   when i click on the view order details link for a specific order 
   then i should be taken to the order details page where i can see the individual items in the order including the product name, quantity, 
   and price 
   when i click on the back button 
   then i should be taken back to my order history page
```


## Python Implementation
```python
from behave import given, when, then @given("i am logged in as a user") def step_impl(context): pass @given("i am on the product details page") def step_impl(context): pass @when("the user clicks the add to cart button") def step_impl(context): pass @then("the product should be added to the user's cart") def step_impl(context): pass @when("the user views their cart") def step_impl(context): pass @then("the product should be displayed in the cart") def step_impl(context): pass @when("the user clicks the checkout button") def step_impl(context): pass @then("the user should be taken to the checkout page") def step_impl(context): pass @when("the user clicks the back button") def step_impl(context): pass
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: user can view their order history given i am logged in as a user when i navigate to my order history page then i should see a list of all my past orders including the order date, order total, and a link to view the order details when i click on the view order details link for a specific order then i should be taken to the order details page where i can see the individual items in the order including the product name, quantity, and price when i click on the back button then i should be taken back to my order history page ``` ```python from behave import given, when, then @given("i am logged in as a user") def step_impl(context): pass @given("i am on the product details page") def step_impl(context): pass @when("the user clicks the add to cart button") def step_impl(context): pass @then("the product should be added to the user's cart") def step_impl(context): pass @when("the user views their cart") def step_impl(context): pass @then("the product should be displayed in the cart") def step_impl(context): pass @when("the user clicks the checkout button") def step_impl(context): pass @then("the user should be taken to the checkout page") def step_impl(context): pass @when("the user clicks the back button") def step_impl(context): pass

```

```python from behave import given, when, then @given("i am logged in as a user") def step_impl(context): pass @given("i am on the order history page") def step_impl(context): pass @when("i navigate to my order history page") def step_impl(context): pass @then("i should see a list of all my past orders including the order date, order total, and a link to view the order details") def step_impl(context): pass @when("i click on the view order details link for a specific order") def step_impl(context): pass @then("i should be taken to the order details page where i can see the individual items in the order including the product name, quantity, and price") def step_impl(context): pass @when("i click on the back button") def step_impl(context): pass @then("i should be taken back to my order history page") def step_impl(context): pass
```
Task: Write a program to find the second largest number in a list.
