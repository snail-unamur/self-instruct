# HQFS44
## Scenario
```gherkin
scenario: a user can add a new address to their account 
   given a user is logged in 
   when the user navigates to the address book page 
   and the user clicks the "add new address" button 
   then the user should be taken to the "add new address" page 
   and the user can enter their new address details 
   and the user clicks the "save" button 
   then the user should be taken back to the address book page 
   and the new address should be displayed in the list of addresses
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: a user can add a new address to their account given a user is logged in when the user navigates to the address book page and the user clicks the "add new address" button then the user should be taken to the "add new address" page and the user can enter their new address details and the user clicks the "save" button then the user should be taken back to the address book page and the new address should be displayed in the list of addresses ```



```python from behave import given, when, then

@given("a user is logged in")
def step_given_a_user_is_logged_in(context):
    context.user = User()
    context.user.login()

@when("the user navigates to the address book page")
def step_when_the_user_navigates_to_the_address_book_page(context):
    context.address_book_page = AddressBookPage(context.driver)
    context.address_book_page.load()

@when("the user clicks the \"add new address\" button")
def step_when_the_user_clicks_the_add_new_address_button(context):
    context.add_new_address_page = AddNewAddressPage(context.driver)
    context.add_new_address_page.click_add_new_address_button()

@then("the user should be taken to the \"add new address\" page")
def step_then_the_user_should_be_taken_to_the_add_new_address_page(context):
    assert context.add_new_address_page.is_the_current_page()

@when("the user can enter their new address details")
def step_when_the_user_can_enter_their_new_address_details(context):
    context.new_address = Address(
        first_name="John",
        last_name="Doe",
        address_line_1="123 Main St",
        city="Anytown",
        state="CA",
        zip_code="12345",
        country="USA",
    )
    context.add_new_address_page.enter_address_details(context.new_address)

@when("the user clicks the \"save\" button")
def step_when_the_user_clicks_the_save_button(context):
    context.address_book_page = context.add_new_address_page.click_save_button()

@then("the user should be taken back to the address book page")
def step_then_the_
