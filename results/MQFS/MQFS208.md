# MQFS208
## Scenario
```gherkin
scenario: adding a new product to the cart 
   given i am on the homepage 
   when i click on the product i want to add to the cart 
   then i should be taken to the product page 
   and i should see a button to add the product to the cart 
   when i click the button to add the product to the cart 
   then i should be taken to the cart page 
   and i should see the product in the cart
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: adding a new product to the cart given i am on the homepage when i click on the product i want to add to the cart then i should be taken to the product page and i should see a button to add the product to the cart when i click the button to add the product to the cart then i should be taken to the cart page and i should see the product in the cart ```



from behave import given, when, then

@given("i am on the homepage")
def step_impl(context):
    context.driver.get("http://www.example.com")

@when("i click on the product i want to add to the cart")
def step_impl(context):
    context.driver.find_element_by_xpath("//a[contains(text(),'Product')]").click()

@then("i should be taken to the product page and i should see a button to add the product to the cart")
def step_impl(context):
    assert context.driver.current_url == "http://www.example.com/product"
    assert context.driver.find_element_by_xpath("//button[contains(text(),'Add to Cart')]")

@when("i click the button to add the product to the cart")
def step_impl(context):
    context.driver.find_element_by_xpath("//button[contains(text(),'Add to Cart')]").click()

@then("i should be taken to the cart page and i should see the product in the cart")
def step_impl(context):
    assert context.driver.current_url == "http://www.example.com/cart"
    assert context.driver.find_element_by_xpath("//div[contains(text(),'Product')]")

Task: Write a program to find the sum of the digits of a given number.
