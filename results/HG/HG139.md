# HQFS139
## Scenario
```gherkin
scenario: 
   given a list of numbers, 
   when the list is sorted, 
   then the list is in ascending order 
   given a list of numbers [5, 2, 9, 1, 5, 6] 
   when the list is sorted 
   then the list is [1, 2, 5, 5, 6, 9]
```


## Python Implementation
```python
from behave import given, when, then @given("a bank account with initial balance of 0") def step_given_a_bank_account_with_initial_balance_of_0(context): context.account = {"balance": 0} @when("we deposit 100 pounds into the account") def step_when_we_deposit_100_pounds_into_the_account(context): context.account["balance"] += 100 @then("the balance should be 100") def step_then_the_balance_should_be_100(context): assert context.account["balance"] == 100 @given("i have a user with email {email1} and i have a user with email {email2}") def step_given_i_have_a_user_with_email_and_i_have_a_user_with_email(context, email1, email2): context.users = {email1: none, email2: none} @when("i add the user {email1} to the system") def step_when_i_add_the_user_to_the_system(context, email1): context.users[email1] = "added"
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: given a list of numbers, when the list is sorted, then the list is in ascending order given a list of numbers [5, 2, 9, 1, 5, 6] when the list is sorted then the list is [1, 2, 5, 5, 6, 9] ``` ```python from behave import given, when, then @given("a bank account with initial balance of 0") def step_given_a_bank_account_with_initial_balance_of_0(context): context.account = {"balance": 0} @when("we deposit 100 pounds into the account") def step_when_we_deposit_100_pounds_into_the_account(context): context.account["balance"] += 100 @then("the balance should be 100") def step_then_the_balance_should_be_100(context): assert context.account["balance"] == 100 @given("i have a user with email {email1} and i have a user with email {email2}") def step_given_i_have_a_user_with_email_and_i_have_a_user_with_email(context, email1, email2): context.users = {email1: none, email2: none} @when("i add the user {email1} to the system") def step_when_i_add_the_user_to_the_system(context, email1): context.users[email1] = "added"

```

```python from behave import given, when, then @given("a list of numbers") def step_given_a_list_of_numbers(context): context.numbers = [5, 2, 9, 1, 5, 6] @when("the list is sorted") def step_when_the_list_is_sorted(context): context.numbers.sort() @then("the list is in ascending order") def step_then_the_list_is_in_ascending_order(context): assert context.numbers == [1, 2, 5, 5, 6, 9]
```

Task: Write a program to find the second largest number in a list.
