# HQFS235
## Scenario
```gherkin
scenario: 
   given a list of numbers, 
   when i find the sum of the numbers, 
   then the sum should be correct 
   given a list of numbers [1, 2, 3, 4, 5] 
   when i find the sum of the numbers 
   then the sum should be 15
```


## Python Implementation
```python
# 1. from behave import given, when, then @given("a list of items with a delete button for each item") def step_given_a_list_of_items_with_a_delete_button_for_each_item(context): context.items = [{"name": f"item{i}"} for i in range(5)] context.ui = {"delete_button": {}} @when("i press the delete button for an item") def step_when_i_press_the_delete_button_for_an_item(context): item_index = int(context.text) del context.items[item_index] context.ui["delete_button"].pop(item_index) @then("the item should be removed from the list") def step_then_the_item_should_be_removed_from_the_list(context): assert context.items == [{"name": f"item{i}"} for i in range(len(context.items))] # 2. import hashlib from behave import given, when, then @given("a json message for a granule with {file_type:d} files") def step_given_a_json_message_for_a_granule_with_files(

context, file_type
): context.json_message = {
"granule": {
"files": [
{"name": f"file{i}.{file_type}"} for i in range(1, 4)
],
"granule_id": "20220801T000000_000001",
"product": "MOD09GA",
"version": "006",
},
"ingest": {"timestamp": "2022-08-01T12:00:00Z"},
} @when("i compute the hash of the json message") def step_when_i_compute_the_hash_of_the_json_message(context): context.hash = hashlib.sha256(
str(context.json_message).encode()
).hexdigest() @then("the hash should be unique for the json message") def step_then_the_hash_should_be_unique_for_the_json_message(context): assert context.hash != "0000000000000000000000000000000000000000000000000000000000000000"
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: given a list of numbers, when i find the sum of the numbers, then the sum should be correct given a list of numbers [1, 2, 3, 4, 5] when i find the sum of the numbers then the sum should be 15 ``` ```python # 1. from behave import given, when, then @given("a list of items with a delete button for each item") def step_given_a_list_of_items_with_a_delete_button_for_each_item(context): context.items = [{"name": f"item{i}"} for i in range(5)] context.ui = {"delete_button": {}} @when("i press the delete button for an item") def step_when_i_press_the_delete_button_for_an_item(context): item_index = int(context.text) del context.items[item_index] context.ui["delete_button"].pop(item_index) @then("the item should be removed from the list") def step_then_the_item_should_be_removed_from_the_list(context): assert context.items == [{"name": f"item{i}"} for i in range(len(context.items))] # 2. import hashlib from behave import given, when, then @given("a json message for a granule with {file_type:d} files") def step_given_a_json_message_for_a_granule_with_files(

context, file_type
): context.json_message = {
"granule": {
"files": [
{"name": f"file{i}.{file_type}"} for i in range(1, 4)
],
"granule_id": "20220801T000000_000001",
"product": "MOD09GA",
"version": "006",
},
"ingest": {"timestamp": "2022-08-01T12:00:00Z"},
} @when("i compute the hash of the json message") def step_when_i_compute_the_hash_of_the_json_message(context): context.hash = hashlib.sha256(
str(context.json_message).encode()
).hexdigest() @then("the hash should be unique for the json message") def step_then_the_hash_should_be_unique_for_the_json_message(context): assert context.hash != "0000000000000000000000000000000000000000000000000000000000000000" ```

```python # 1. from behave import given, when, then @given("a list of numbers") def step_given_a_list_of_numbers(context): context.numbers = [1, 2, 3, 4, 5] @when("i find the sum of the numbers") def step_when_i_find_the_sum_of_the_numbers(context): context.sum = sum(context.numbers) @then("the sum should be {sum:d}") def step_then_the_sum_should_be(context, sum): assert context.sum == sum

# 2. from behave import given, when, then @given("a json message for a granule with {file_type:d} files") def step_given_a_json_message_for_a_granule_with_
