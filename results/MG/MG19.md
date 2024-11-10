# MQFS19
## Scenario
```gherkin
scenario: 
   given a list of integers 
   when i remove the duplicates 
   then the list should contain only unique integers
```


## Python Implementation
```python
from behave import given, when, then @given("the following icecream") def step_given_icecream(table): # todo: implement step pass @when("i visit '/ice-cream'") def step_when_visit_icecream(context): # todo: implement step pass @then("i should not see 'pistachio'") def step_then_should_not_see_pistachio(context): # todo: implement step pass @when("i create '/ice-cream' {name} {id} {description} {status} {base} {price} {popularity}") def step_when_create_icecream(context, name, id, description, status, base, price, popularity): # todo: implement step pass @then("i should see 'pistachio'") def step_then_should_see_pistachio(context): # todo: implement step pass @given("i put {ingredient} in a blender") def step_given_put_ingredient_in_blender(context, ingredient): # todo: implement step pass @when("i switch the blender on") def step_when_switch_blender_on(context): # todo: implement step pass @then("it should transform into {product}") def step_then_it_should_transform_into(context, product): # todo: implement step pass @given("data is
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: given a list of integers when i remove the duplicates then the list should contain only unique integers ``` ```python from behave import given, when, then @given("the following icecream") def step_given_icecream(table): # todo: implement step pass @when("i visit '/ice-cream'") def step_when_visit_icecream(context): # todo: implement step pass @then("i should not see 'pistachio'") def step_then_should_not_see_pistachio(context): # todo: implement step pass @when("i create '/ice-cream' {name} {id} {description} {status} {base} {price} {popularity}") def step_when_create_icecream(context, name, id, description, status, base, price, popularity): # todo: implement step pass @then("i should see 'pistachio'") def step_then_should_see_pistachio(context): # todo: implement step pass @given("i put {ingredient} in a blender") def step_given_put_ingredient_in_blender(context, ingredient): # todo: implement step pass @when("i switch the blender on") def step_when_switch_blender_on(context): # todo: implement step pass @then("it should transform into {product}") def step_then_it_should_transform_into(context, product): # todo: implement step pass @given("data is

```

```python from behave import given, when, then @given("a list of integers")
def step_given_a_list_of_integers(context):
    context.list = [1, 2, 3, 4, 5, 5, 6, 7, 8, 8, 9]
@when("i remove the duplicates")
def step_when_i_remove_the_duplicates(context):
    context.list = list(set(context.list))
@then("the list should contain only unique integers")
def step_then_the_list_should_contain_only_unique_integers(context):
    assert len(context.list) == len(set(context.list))
```

Task: Write a program to find the second largest number in a list.
