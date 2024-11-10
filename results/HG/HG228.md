# HQFS228
## Scenario
```gherkin
scenario: add a new product to a category 
   given i am a manager 
   and i have a category with name "existing category" 
   when i add a new product with name "new product" to the category "existing category" 
   then a new product should be added to the category "existing category" with the 
   given name
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: add a new product to a category given i am a manager and i have a category with name "existing category" when i add a new product with name "new product" to the category "existing category" then a new product should be added to the category "existing category" with the given name ```



from behave import given, when, then

@given("i am a manager")
def step_given_i_am_a_manager(context):
    context.role = "manager"

@given("i have a category with name {category_name}")
def step_given_i_have_a_category_with_name(context, category_name):
    context.category = {"name": category_name}

@when("i add a new product with name {product_name} to the category {category_name}")
def step_when_i_add_a_new_product_with_name_to_the_category(context, product_name, category_name):
    context.category["products"] = [{"name": product_name}]

@then("a new product should be added to the category {category_name} with the given name")
def step_then_a_new_product_should_be_added_to_the_category_with_the_given_name(context, category_name):
    assert context.category["products"][0]["name"] == "new product"
