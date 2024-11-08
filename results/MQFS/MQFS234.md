# MQFS234
## Scenario
```gherkin
scenario: add a new employee 
   given i am logged in as an admin 
   when i add a new employee with name "john doe" 
   and job "software engineer" 
   then i should see the new employee in the list of employees
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: add a new employee given i am logged in as an admin when i add a new employee with name "john doe" and job "software engineer" then i should see the new employee in the list of employees ```



from behave import given, when, then

@given("i am logged in as an admin")
def step_impl(context):
    context.admin = Admin("admin@example.com", "password")
    context.admin.login()

@when("i add a new employee with name 'john doe' and job 'software engineer'")
def step_impl(context):
    context.new_employee = Employee("john doe", "software engineer")
    context.admin.add_employee(context.new_employee)

@then("i should see the new employee in the list of employees")
def step_impl(context):
    employees = context.admin.get_employees()
    assert context.new_employee in employees

Task: Write a program to find the sum of the digits of a given number.
