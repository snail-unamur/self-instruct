# MQFS244
## Scenario
```gherkin
scenario: a user can add a new payment method 
   given i am on my dashboard page 
   when i click on the add payment method button 
   then i should be taken to the add payment method page 
   and i should see a form with the following fields: - card number - expiration date - cvv - billing address - zip code - country 
   when i fill out the form 
   and submit it 
   then i should see a confirmation message 
   and i should see the new payment method in my payment methods
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: a user can add a new payment method given i am on my dashboard page when i click on the add payment method button then i should be taken to the add payment method page and i should see a form with the following fields: - card number - expiration date - cvv - billing address - zip code - country when i fill out the form and submit it then i should see a confirmation message and i should see the new payment method in my payment methods ```



```python from behave import given, when, then

@given("i am on my dashboard page")
def step_given_i_am_on_my_dashboard_page(context):
    context.driver.get("http://localhost:8000/dashboard")

@when("i click on the add payment method button")
def step_when_i_click_on_the_add_payment_method_button(context):
    add_payment_method_button = context.driver.find_element_by_id("add-payment-method-button")
    add_payment_method_button.click()

@then("i should be taken to the add payment method page")
def step_then_i_should_be_taken_to_the_add_payment_method_page(context):
    assert context.driver.current_url == "http://localhost:8000/add-payment-method"

@then("i should see a form with the following fields: - card number - expiration date - cvv - billing address - zip code - country")
def step_then_i_should_see_a_form_with_the_following_fields(context):
    assert context.driver.find_element_by_name("card_number")
    assert context.driver.find_element_by_name("expiration_date")
    assert context.driver.find_element_by_name("cvv")
    assert context.driver.find_element_by_name("billing_address")
    assert context.driver.find_element_by_name("zip_code")
    assert context.driver.find_element_by_name("country")

@when("i fill out the form and submit it")
def step_when_i_fill_out_the_form_and_submit_it(context):
    context.driver.find_element_by_name("card_number").send_keys("1234567890123456")
    context.driver.find_element_by_name("expiration_date").send_keys("12/25")
    context.driver.find_element_by_name
