# HQFS136
## Scenario
```gherkin
scenario: the user can edit an address in their account 
   given the user is logged in 
   when the user navigates to the "addresses" page 
   then the user should see a list of their addresses 
   when the user clicks the "edit" button next to an address 
   then the user should be taken to a page to edit the address 
   when the user edits the address 
   and clicks "save" 
   then the address should be updated in the user's account
```


## Python Implementation
```python
from behave import given, when, then

@given("the user is logged in")
def step_impl(context):
    context.user = User()
    context.user.login()

@when("the user navigates to the 'addresses' page")
def step_impl(context):
    context.page = AddressesPage(context.driver)
    context.page.load()

@then("the user should see a list of their addresses")
def step_impl(context):
    assert context.page.addresses_exist()

@when("the user clicks the 'edit' button next to an address")
def step_impl(context):
    context.address = context.page.get_first_address()
    context.edit_page = context.page.click_edit_address(context.address)

@then("the user should be taken to a page to edit the address")
def step_impl(context):
    assert isinstance(context.edit_page, AddressEditPage)

@when("the user edits the address and clicks 'save'")
def step_impl(context):
    context.edited_address = context.edit_page.edit(context.address)
    context.edit_page.save()

@then("the address should be updated in the user's account")
def step_impl(context):
    assert context.page.get_address_by_id(context.edited_address.id) == context.edited_address
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: the user can edit an address in their account given the user is logged in when the user navigates to the "addresses" page then the user should see a list of their addresses when the user clicks the "edit" button next to an address then the user should be taken to a page to edit the address when the user edits the address and clicks "save" then the address should be updated in the user's account ```



```python from behave import given, when, then

@given("the user is logged in")
def step_impl(context):
    context.user = User()
    context.user.login()

@when("the user navigates to the 'addresses' page")
def step_impl(context):
    context.page = AddressesPage(context.driver)
    context.page.load()

@then("the user should see a list of their addresses")
def step_impl(context):
    assert context.page.addresses_exist()

@when("the user clicks the 'edit' button next to an address")
def step_impl(context):
    context.address = context.page.get_first_address()
    context.edit_page = context.page.click_edit_address(context.address)

@then("the user should be taken to a page to edit the address")
def step_impl(context):
    assert isinstance(context.edit_page, AddressEditPage)

@when("the user edits the address and clicks 'save'")
def step_impl(context):
    context.edited_address = context.edit_page.edit(context.address)
    context.edit_page.save()

@then("the address should be updated in the user's account")
def step_impl(context):
    assert context.page.get_address_by_id(context.edited_address.id) == context.edited_address
```

Task: Write a program to find the sum of the digits of a number.
