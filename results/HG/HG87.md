# HQFS87
## Scenario
```gherkin
scenario: adding two numbers 
   given i have two numbers, a 
   and b 
   when i add a 
   and b 
   then i should get the sum of a 
   and b
```


## Python Implementation
```python
# 1. fizzbuzz from behave import given, when, then @given("a list of numbers from 1 to 100") def step_given_a_list_of_numbers(context): context.numbers = list(range(1, 101)) @when("iterating through the list") def step_when_iterating_through_the_list(context): for i in range(len(context.numbers)): if context.numbers[i] % 3 == 0 and context.numbers[i] % 5 == 0: context.numbers[i] = "fizzbuzz" elif context.numbers[i] % 3 == 0: context.numbers[i] = "fizz" elif context.numbers[i] % 5 == 0: context.numbers[i] = "buzz" @then("replace numbers divisible by 3 with 'fizz'") def step_then_replace_numbers_divisible_by_3_with_fizz(context): for num in context.numbers: if num % 3 == 0 and num != "fizz" and num != "fizzbuzz": assert false @then("replace numbers divisible by 5 with 'buzz'") def step_then_replace_numbers_divisible_by_5_with_buzz(context):
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: adding two numbers given i have two numbers, a and b when i add a and b then i should get the sum of a and b ``` ```python # 1. fizzbuzz from behave import given, when, then @given("a list of numbers from 1 to 100") def step_given_a_list_of_numbers(context): context.numbers = list(range(1, 101)) @when("iterating through the list") def step_when_iterating_through_the_list(context): for i in range(len(context.numbers)): if context.numbers[i] % 3 == 0 and context.numbers[i] % 5 == 0: context.numbers[i] = "fizzbuzz" elif context.numbers[i] % 3 == 0: context.numbers[i] = "fizz" elif context.numbers[i] % 5 == 0: context.numbers[i] = "buzz" @then("replace numbers divisible by 3 with 'fizz'") def step_then_replace_numbers_divisible_by_3_with_fizz(context): for num in context.numbers: if num % 3 == 0 and num != "fizz" and num != "fizzbuzz": assert false @then("replace numbers divisible by 5 with 'buzz'") def step_then_replace_numbers_divisible_by_5_with_buzz(context):

```

```gherkin scenario: adding two numbers given i have two numbers, a and b when i add a and b then i should get the sum of a and b ``` ```python # 1. adding two numbers from behave import given, when, then @given("i have two numbers, a and b") def step_given_i_have_two_numbers(context): context.a = 5 context.b = 7 @when("i add a and b") def step_when_i_add_a_and_b(context): context.sum = context.a + context.b @then("i should get the sum of a and b") def step_then_i_should_get_the_sum_of_a_and_b(context): assert context.sum == 12 ```
