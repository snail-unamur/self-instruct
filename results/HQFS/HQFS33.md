# HQFS33
## Scenario
```gherkin
scenario: the user can view the details of a project 
   given the user is logged in as "kea@gmail.com" 
   when the user navigates to the project page 
   and clicks on the project they want to view 
   then they should be redirected to the project details page 
   and they should see the project name 
   and they should see the project description 
   and they should see the project members
```


## Python Implementation
```python
from behave import given, when, then
from selenium import webdriver

@given("the user is logged in as 'kea@gmail.com'")
def step_given_the_user_is_logged_in_as_kea_gmail_com(context):
    context.driver = webdriver.Firefox()
    context.driver.get("http://project-management.com/login")
    context.driver.find_element_by_name("email").send_keys("kea@gmail.com")
    context.driver.find_element_by_name("password").send_keys("password")
    context.driver.find_element_by_name("submit").click()

@when("the user navigates to the project page and clicks on the project they want to view")
def step_when_the_user_navigates_to_the_project_page_and_clicks_on_the_project_they_want_to_view(context):
    context.driver.find_element_by_link_text("Projects").click()
    context.driver.find_element_by_link_text("Project 1").click()

@then("they should be redirected to the project details page and they should see the project name")
def step_then_they_should_be_redirected_to_the_project_details_page_and_they_should_see_the_project_name(context):
    assert "Project Details" in context.driver.title
    assert "Project 1" in context.driver.page_source

@then("they should see the project description")
def step_then_they_should_see_the_project_description(context):
    assert "This is the project description for Project 1." in context.driver.page_source

@then("they should see the project members")
def step_then_they_should_see_the_project_members(context):
    assert "John Doe" in context.driver.page_source
    assert "Jane Smith" in context.driver.page_source
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: the user can view the details of a project given the user is logged in as "kea@gmail.com" when the user navigates to the project page and clicks on the project they want to view then they should be redirected to the project details page and they should see the project name and they should see the project description and they should see the project members ``` here are the python implementations of the step functions for the given gherkin scenarios using the behave bdd testing framework:



```python
from behave import given, when, then
from selenium import webdriver

@given("the user is logged in as 'kea@gmail.com'")
def step_given_the_user_is_logged_in_as_kea_gmail_com(context):
    context.driver = webdriver.Firefox()
    context.driver.get("http://project-management.com/login")
    context.driver.find_element_by_name("email").send_keys("kea@gmail.com")
    context.driver.find_element_by_name("password").send_keys("password")
    context.driver.find_element_by_name("submit").click()

@when("the user navigates to the project page and clicks on the project they want to view")
def step_when_the_user_navigates_to_the_project_page_and_clicks_on_the_project_they_want_to_view(context):
    context.driver.find_element_by_link_text("Projects").click()
    context.driver.find_element_by_link_text("Project 1").click()

@then("they should be redirected to the project details page and they should see the project name")
def step_then_they_should_be_redirected_to_the_project_details_page_and_they_should_see_the_project_name(context):
    assert "Project Details" in context.driver.title
    assert "Project 1" in context.driver.page_source

@then("they should see the project description")
def step_then_they_should_see_the_project_description(context):
    assert "This is the project description for Project 1." in context.driver.page_source

@then("they should see the project members")
def step_then_they_should_see_the_project_members(context):
    assert "John Doe" in context.driver.page_source
    assert "Jane Smith" in context.driver.page_source
```

Task: Write a program to find the sum of the digits of
