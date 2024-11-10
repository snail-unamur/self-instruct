# HQFS175
## Scenario
```gherkin
scenario: get a blog post 
   given the following blog posts |title |author |id | |the benefits of exercise |john doe |1 | |the power of positive thinking |jane smith |2 | 
   when i visit '/blog/1' 
   then i should see 'the benefits of exercise' by 'john doe'
```


## Python Implementation
```python
from behave import given, when, then

@given('the following blog posts')
def step_impl(context):
    context.blog_posts = {
        '1': {'title': 'the benefits of exercise', 'author': 'john doe'},
        '2': {'title': 'the power of positive thinking', 'author': 'jane smith'}
    }

@when('i visit "/blog/{id}"')
def step_impl(context, id):
    context.response = context.app.get(f'/blog/{id}')

@then('i should see "{title}" by "{author}"')
def step_impl(context, title, author):
    assert context.response.json['title'] == title
    assert context.response.json['author'] == author
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: get a blog post given the following blog posts |title |author |id | |the benefits of exercise |john doe |1 | |the power of positive thinking |jane smith |2 | when i visit '/blog/1' then i should see 'the benefits of exercise' by 'john doe' ```



```python from behave import given, when, then

@given('the following blog posts')
def step_impl(context):
    context.blog_posts = {
        '1': {'title': 'the benefits of exercise', 'author': 'john doe'},
        '2': {'title': 'the power of positive thinking', 'author': 'jane smith'}
    }

@when('i visit "/blog/{id}"')
def step_impl(context, id):
    context.response = context.app.get(f'/blog/{id}')

@then('i should see "{title}" by "{author}"')
def step_impl(context, title, author):
    assert context.response.json['title'] == title
    assert context.response.json['author'] == author
```

Task: Write a program to find the sum of the digits of a given number.
