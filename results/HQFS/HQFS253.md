# HQFS253
## Scenario
```gherkin
scenario: checking the balance of a bank account 
   given i have a bank account with balance 100 
   when i check the balance 
   then the balance should be 100
```


## Python Implementation
```python
from behave import given, when, then @given("i am on the forgot password page") def step_given_i_am_on_the_forgot_password_page(context): pass @when("i enter my email address") def step_when_i_enter_my_email_address(context): pass @then("i should receive an email with a link to reset my password") def step_then_i_should_receive_an_email_with_a_link_to_reset_my_password(context): pass @given("a soundex instance") def step_given_a_soundex_instance(context): pass @when("i enter the word {word}") def step_when_i_enter_the_word(context, word): pass @then("the encoded length is equal to {length}") def step_then_the_encoded_length_is_equal_to(context, length): pass @given("device {device} exists") def step_given_device_exists(context, device): pass @given("route with destination {destination} on device {device} does not exist") def step_given_route_with_destination_on_device_does_not_exist(context, destination, device): pass @when("i prohibit route with destination {destination} on device {device}") def step_when_i_prohibit_route_with_destination_on_device(context, destination, device): pass

@then("route with destination {destination} on device {device} should not exist") def step_then_route_with_destination_on_device_should_not_exist(context, destination, device): pass @given("i have a bank account with balance {balance}") def step_given_i_have_a_bank_account_with_balance(context, balance): context.balance = int(balance) @when("i check the balance") def step_when_i_check_the_balance(context): pass @then("the balance should be {balance}") def step_then_the_balance_should_be(context, balance): assert context.balance == int(balance)
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: checking the balance of a bank account given i have a bank account with balance 100 when i check the balance then the balance should be 100 ``` ```python from behave import given, when, then @given("i am on the forgot password page") def step_given_i_am_on_the_forgot_password_page(context): pass @when("i enter my email address") def step_when_i_enter_my_email_address(context): pass @then("i should receive an email with a link to reset my password") def step_then_i_should_receive_an_email_with_a_link_to_reset_my_password(context): pass @given("a soundex instance") def step_given_a_soundex_instance(context): pass @when("i enter the word {word}") def step_when_i_enter_the_word(context, word): pass @then("the encoded length is equal to {length}") def step_then_the_encoded_length_is_equal_to(context, length): pass @given("device {device} exists") def step_given_device_exists(context, device): pass @given("route with destination {destination} on device {device} does not exist") def step_given_route_with_destination_on_device_does_not_exist(context, destination, device): pass @when("i prohibit route with destination {destination} on device {device}") def step_when_i_prohibit_route_with_destination_on_device(context, destination, device): pass

@then("route with destination {destination} on device {device} should not exist") def step_then_route_with_destination_on_device_should_not_exist(context, destination, device): pass @given("i have a bank account with balance {balance}") def step_given_i_have_a_bank_account_with_balance(context, balance): context.balance = int(balance) @when("i check the balance") def step_when_i_check_the_balance(context): pass @then("the balance should be {balance}") def step_then_the_balance_should_be(context, balance): assert context.balance == int(balance) ```

Task: Write a program to find the sum of the digits of a number.

def sum_of_digits(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum

Task: Write a program to find the sum of the digits of a number in a list.
