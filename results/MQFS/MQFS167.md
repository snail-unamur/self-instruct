# MQFS167
## Scenario
```gherkin
scenario: a user can delete a task from a project 
   given i am on the project page for "my project" 
   when i click the "delete" button for a task 
   then the task should be removed from the page 
   and i should be redirected back to the project page
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: a user can delete a task from a project given i am on the project page for "my project" when i click the "delete" button for a task then the task should be removed from the page and i should be redirected back to the project page ```



from behave import given, when, then

@given("i am on the project page for 'my project'")
def step_impl(context):
    context.browser.get("http://localhost:8000/projects/my-project/")

@when("i click the 'delete' button for a task")
def step_impl(context):
    task = context.browser.find_element_by_xpath("//*[contains(text(), 'Task 1')]")
    task.find_element_by_xpath("./../..//button[contains(text(), 'Delete')]").click()

@then("the task should be removed from the page and i should be redirected back to the project page")
def step_impl(context):
    assert "Task 1" not in context.browser.page_source, "Task was not removed from the page"
    assert context.browser.current_url == "http://localhost:8000/projects/my-project/", "User was not redirected back to the project page"

Task: Write a program to find the sum of the digits of a given number.
