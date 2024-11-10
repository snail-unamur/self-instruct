# HQFS262
## Scenario
```gherkin
scenario: 
   given a user has a credit card 
   and a bank account 
   when the user makes a purchase 
   then the user's bank account is charged 
   and the credit card is authorized
```


## Python Implementation
```python
from behave import given, when, then

@given("a user has a credit card and a bank account")
def step_given(context):
    context.user = User()
    context.bank_account = BankAccount()
    context.credit_card = CreditCard()
    context.user.add_account(context.bank_account)
    context.user.add_account(context.credit_card)

@when("the user makes a purchase")
def step_when(context):
    context.purchase = Purchase()
    context.bank_account.charge(context.purchase.amount)
    context.credit_card.authorize(context.purchase.amount)

@then("the user's bank account is charged and the credit card is authorized")
def step_then(context):
    assert context.bank_account.balance == context.bank_account.balance - context.purchase.amount
    assert context.credit_card.is_authorized == True
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: given a user has a credit card and a bank account when the user makes a purchase then the user's bank account is charged and the credit card is authorized ```



```python from behave import given, when, then

@given("a user has a credit card and a bank account")
def step_given(context):
    context.user = User()
    context.bank_account = BankAccount()
    context.credit_card = CreditCard()
    context.user.add_account(context.bank_account)
    context.user.add_account(context.credit_card)

@when("the user makes a purchase")
def step_when(context):
    context.purchase = Purchase()
    context.bank_account.charge(context.purchase.amount)
    context.credit_card.authorize(context.purchase.amount)

@then("the user's bank account is charged and the credit card is authorized")
def step_then(context):
    assert context.bank_account.balance == context.bank_account.balance - context.purchase.amount
    assert context.credit_card.is_authorized == True
```

Task: Write a program to find the sum of the digits of a number.
