# HQFS128
## Scenario
```gherkin
scenario: adding a new book to the library 
   given a library with the following books: |title |author |year | |----- |------ |---- | |the great gatsby |f. scott fitzgerald |1925 | |to kill a mockingbird |harper lee |1960 | 
   when a new book is added with the following details: |title |author |year | |----- |------ |---- | |the catcher in the rye |j.d. salinger |1951 | 
   then the library should contain the following books: |title |author |year | |----- |------ |---- | |the great gatsby |f. scott fitzgerald |1925 | |to kill a mockingbird |harper lee |1960 | |the catcher in the rye |j.d. salinger |1951 |
```


## Python Implementation
```python
from behave import given, when, then

@given("a library with the following books:")
def step_impl(context):
    context.library = {"books": [
        {"title": "the great gatsby", "author": "f. scott fitzgerald", "year": 1925},
        {"title": "to kill a mockingbird", "author": "harper lee", "year": 1960}
    ]}

@when("a new book is added with the following details:")
def step_impl(context, title, author, year):
    context.new_book = {"title": title, "author": author, "year": int(year)}
    context.library["books"].append(context.new_book)

@then("the library should contain the following books:")
def step_impl(context, title, author, year):
    expected_books = [
        {"title": title, "author": author, "year": int(year)}
        for title, author, year in csv.reader(io.StringIO(title))
    ]
    assert context.library["books"] == expected_books
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: adding a new book to the library given a library with the following books: |title |author |year | |----- |------ |---- | |the great gatsby |f. scott fitzgerald |1925 | |to kill a mockingbird |harper lee |1960 | when a new book is added with the following details: |title |author |year | |----- |------ |---- | |the catcher in the rye |j.d. salinger |1951 | then the library should contain the following books: |title |author |year | |----- |------ |---- | |the great gatsby |f. scott fitzgerald |1925 | |to kill a mockingbird |harper lee |1960 | |the catcher in the rye |j.d. salinger |1951 | ```



```python
from behave import given, when, then

@given("a library with the following books:")
def step_impl(context):
    context.library = {"books": [
        {"title": "the great gatsby", "author": "f. scott fitzgerald", "year": 1925},
        {"title": "to kill a mockingbird", "author": "harper lee", "year": 1960}
    ]}

@when("a new book is added with the following details:")
def step_impl(context, title, author, year):
    context.new_book = {"title": title, "author": author, "year": int(year)}
    context.library["books"].append(context.new_book)

@then("the library should contain the following books:")
def step_impl(context, title, author, year):
    expected_books = [
        {"title": title, "author": author, "year": int(year)}
        for title, author, year in csv.reader(io.StringIO(title))
    ]
    assert context.library["books"] == expected_books
```
