# MQFS110
## Scenario
```gherkin
scenario: query invalid table for males in 2011 
   given a client 
   when the client queries "invalid_table" for "gender:males" returning all "2011" 
   then the "invalid_table" result is not empty 
   and the "invalid_table" result is a table with 1 row 
   and the "invalid_table" result has a column "gender" with value "males" 
   and the "invalid_table" result has a column "year" with value "2011" 
   and the "invalid_table" result has a column "count" with value "1"
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: query invalid table for males in 2011 given a client when the client queries "invalid_table" for "gender:males" returning all "2011" then the "invalid_table" result is not empty and the "invalid_table" result is a table with 1 row and the "invalid_table" result has a column "gender" with value "males" and the "invalid_table" result has a column "year" with value "2011" and the "invalid_table" result has a column "count" with value "1" ```



```python from behave import given, then, when

@given("a client")
def step_given_a_client(context):
    context.client = Client()

@when("the client queries {table_name} for {gender} returning all {year}")
def step_when_the_client_queries_table_for_gender_returning_all_year(context, table_name, gender, year):
    context.result = context.client.query(table_name, gender, year)

@then("the {table_name} result is not empty")
def step_then_the_table_result_is_not_empty(context, table_name):
    assert context.result, f"{table_name} result is empty"

@then("the {table_name} result is a table with 1 row")
def step_then_the_table_result_is_a_table_with_1_row(context, table_name):
    assert len(context.result) == 1, f"{table_name} result has {len(context.result)} rows, expected 1"

@then("the {table_name} result has a column {column} with value {value}")
def step_then_the_table_result_has_a_column_with_value(context, table_name, column, value):
    assert context.result[0][column] == value, f"{table_name} result column {column} does not have value {value}"

@then("the {table_name} result has a column {column1} with value {value1} and the {table_name} result has a column {column2} with value {value2}")
def step_then_the_table_result_has_a_column_with_value_and_the_table_result_has_a_column_with_value(context, table_name, column1, value1, column2, value2):
    assert context.result[0][column1] == value1, f"{table_name} result column {column1} does not have value {value1}"
    assert context.result[0][column2] == value2, f"{table
