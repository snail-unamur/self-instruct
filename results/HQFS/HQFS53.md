# HQFS53
## Scenario
```gherkin
scenario: user can delete a contact 
   given i am logged in 
   and i have at least one contact 
   when i click on the "contacts" tab 
   then i should see the list of contacts 
   when i click on the "delete" button next to a contact 
   then the contact should be deleted 
   and i should see the confirmation message "contact deleted successfully"
```


## Python Implementation
```python
from behave import given, when, then import time @given("i am logged in") def step_given_i_am_logged_in(context): pass @given("i have at least one contact") def step_given_i_have_at_least_one_contact(context): pass @when("i click on the 'contacts' tab") def step_when_i_click_on_the_contacts_tab(context): pass @then("i should see the list of contacts") def step_then_i_should_see_the_list_of_contacts(context): pass @when("i click on the 'delete' button next to a contact") def step_when_i_click_on_the_delete_button_next_to_a_contact(context): pass @then("the contact should be deleted and i should see the confirmation message 'contact deleted successfully'") def step_then_the_contact_should_be_deleted_and_i_should_see_the_confirmation_message_contact_deleted_successfully(context): pass
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: user can delete a contact given i am logged in and i have at least one contact when i click on the "contacts" tab then i should see the list of contacts when i click on the "delete" button next to a contact then the contact should be deleted and i should see the confirmation message "contact deleted successfully" ```python from behave import given, when, then import time @given("i am logged in") def step_given_i_am_logged_in(context): pass @given("i have at least one contact") def step_given_i_have_at_least_one_contact(context): pass @when("i click on the 'contacts' tab") def step_when_i_click_on_the_contacts_tab(context): pass @then("i should see the list of contacts") def step_then_i_should_see_the_list_of_contacts(context): pass @when("i click on the 'delete' button next to a contact") def step_when_i_click_on_the_delete_button_next_to_a_contact(context): pass @then("the contact should be deleted and i should see the confirmation message 'contact deleted successfully'") def step_then_the_contact_should_be_deleted_and_i_should_see_the_confirmation_message_contact_deleted_successfully(context): pass ```



from behave import given, when, then import time @given("i am logged in") def step_given_i_am_logged_in(context): pass @given("i have at least one contact") def step_given_i_have_at_least_one_contact(context): pass @when("i click on the 'contacts' tab") def step_when_i_click_on_the_contacts_tab(context): pass @then("i should see the list of contacts") def step_then_i_should_see_the_list_of_contacts(context): pass @when("i click on the 'delete' button next to a contact") def step_when_i_click_on_the_delete_button_next_to_a_contact(context): pass @then("the contact should be deleted and i should see the confirmation message 'contact deleted successfully'") def step_then_the_contact_should_be_deleted_and_i_should_see_the_confirmation_message_contact_deleted_successfully(context): pass

Task: Write a program to find the sum of the digits of a number.
