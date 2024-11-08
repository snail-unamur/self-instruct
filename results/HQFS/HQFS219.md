# HQFS219
## Scenario
```gherkin
scenario: get a book 
   given the following books |title |author |id | |harry potter |j.k. rowling |1 | |the hobbit |j.r.r. tolkien |2 | 
   when i visit '/books/1' 
   then i should see 'harry potter' by 'j.k. rowling'
```


## Python Implementation
```python
from behave import given, when, then

@given('i visit "/books/{id}"')
def step(context, id):
    context.response = context.browser.get(f"/books/{id}")

@then('i should see "{title}" by "{author}"')
def step(context, title, author):
    assert title in context.response.content
    assert author in context.response.content
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: get a book given the following books |title |author |id | |harry potter |j.k. rowling |1 | |the hobbit |j.r.r. tolkien |2 | when i visit '/books/1' then i should see 'harry potter' by 'j.k. rowling' ```



```python from behave import given, when, then

@given('i visit "/books/{id}"')
def step(context, id):
    context.response = context.browser.get(f"/books/{id}")

@then('i should see "{title}" by "{author}"')
def step(context, title, author):
    assert title in context.response.content
    assert author in context.response.content
```

Task: Write a program to find the sum of the digits of a given number.
