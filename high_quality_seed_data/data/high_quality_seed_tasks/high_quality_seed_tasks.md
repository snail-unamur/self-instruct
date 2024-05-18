id : seed_task_0
name : weaker opponent
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: Weaker opponent
	Given the ninja has a third level black-belt
	When attacked by a samurai
	Then the ninja should engage the opponent
```
input = ""
output:
```python
from behave import given, when, then
from hamcrest import assert_that, equal_to
from ninja_module import NinjaFight

@given('the ninja has a {achievement_level}')
def step_the_ninja_has_a(context, achievement_level):
	context.ninja_fight = NinjaFight(achievement_level)

@when('attacked by a {opponent_role}')
def step_attacked_by_a(context, opponent_role):
	context.ninja_fight.opponent = opponent_role

@then('the ninja should {reaction}')
def step_the_ninja_should(context, reaction):
	assert_that(reaction, equal_to(context.ninja_fight.decision()))
```

id : seed_task_1
name : stronger opponent
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: Stronger opponent
	Given the ninja has a third level black-belt
	When attacked by Chuck Norris
	Then the ninja should run for his life
```
input = ""
output:
```python
from behave import given, when, then
from hamcrest import assert_that, equal_to
from ninja_module import NinjaFight

@given('the ninja has a {achievement_level}')
def step_the_ninja_has_a(context, achievement_level):
	context.ninja_fight = NinjaFight(achievement_level)

@when('attacked by {opponent}')
def step_attacked_by(context, opponent):
	context.ninja_fight.opponent = opponent

@then('the ninja should {reaction}')
def step_the_ninja_should(context, reaction):
	assert_that(reaction, equal_to(context.ninja_fight.decision()))
```

id : seed_task_2
name : blenders
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework : 
```gherkin
Scenario: Blenders
	Given I put "apples" in a blender
	When I switch the blender on
	Then it should transform into "apple juice"
```
input = ""
output:
```python
from behave import given, when, then
from hamcrest import assert_that, equal_to
from blender_module import Blender

@given('I put "{thing}" in a blender')
def step_given_put_thing_into_blender(context, thing):
	context.blender = Blender()
	context.blender.add(thing)

@when('I switch the blender on')
def step_when_switch_blender_on(context):
	context.blender.switch_on()

@then('it should transform into "{other_thing}"')
def step_then_should_transform_into(context, other_thing):
	assert_that(context.blender.result, equal_to(other_thing))
```

id : seed_task_3
name : blenders
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework : 
```gherkin
Scenario: Blenders
	Given I put "<thing>" in a blender
	When I switch the blender on
	Then it should transform into "<other thing>"

    Examples: Amphibians
	|thing	      |other thing|
	|Red Tree Frog|mush       |
	|apples       |apple juice|

    Examples: Consumer Electronics
	|thing       |other thing|
	|iPhone	     |toxic waste|
	|Galaxy Nexus|toxic waste|
```
input = ""
output:
```python
from behave import given, when, then
from hamcrest import assert_that, equal_to
from blender_module import Blender

@given('I put "{thing}" in a blender')
def step_given_put_thing_into_blender(context, thing):
	context.blender = Blender()
	context.blender.add(thing)

@when('I switch the blender on')
def step_when_switch_blender_on(context):
	context.blender.switch_on()

@then('it should transform into "{other_thing}"')
def step_then_should_transform_into(context, other_thing):
	assert_that(context.blender.result, equal_to(other_thing))
```

id : seed_task_4
name : some scenario
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework : 
```gherkin
Scenario: Frobulator
	Given a sample text loaded into the frobulator:
	"""
	Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
	"""
	When we activate the frobulator
	Then we will find it similar to English
```
input = ""
output:
```python
from behave import given, when, then
from hamcrest import assert_that, equal_to
from frobulator import Frobulator

@given('a sample text loaded into the frobulator')
def step_impl(context):
	frobulator = getattr(context, "frobulator", None)
	if not frobulator:
		context.frobulator = Frobulator()
	context.frobulator.text = context.text  #< STEP-DATA from context.text

@when('we activate the frobulator')
def step_impl(context):
	context.frobulator.activate()

@then('we will find it similar to {language}')
def step_impl(context, language):
	assert_that(language, equal_to(context.frobulator.seems_like_language()))
```

id : seed_task_5
name : setup table
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework : 
```gherkin
Scenario: Setup Table
	Given a set of specific users:
	|name	  |department |
	|Barry	  |Beer Cans  |
	|Pudey	  |Silly Walks|
	|Two-Lumps|Silly Walks|
	When we count the number of people in each department
	Then we will find two people in "Silly Walks"
	But we will find one person in "Beer Cans"
```
input = ""
output:
```python
from behave import given, when, then
from hamcrest import assert_that, equal_to
from my_company import CompanyModel
from number_module import NamedNumber

@given('a set of specific users')
def step_impl(context):
	model = getattr(context, "model", None)
	if not model:
		context.model = CompanyModel()
	for row in context.table:
	    context.model.add_user(row["name"], deparment=row["department"])

@when('we count the number of people in each department')
def step_impl(context):
	context.model.count_persons_per_department()

@then('we will find {count} people in "{department}"')
def step_impl(context, count, department):
	count_ = NamedNumber.from_string(count)
	assert_that(count_, equal_to(context.model.get_headcount_for(department)))

@then('we will find one person in "{department}"')
def step_impl(context, department):
	assert_that(1, equal_to(context.model.get_headcount_for(department)))
```

id : seed_task_6
name : unordered result
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: Unordered Result Table Comparison (RowFixture Table)
	Given a set of specific users:
	|name  |department |
	|Alice |Beer Cans  |
	|Bob   |Beer Cans  |
	|Charly|Silly Walks|
	|Dodo  |Silly Walks|
	Then we will have the following people in "Silly Walks":
	|name  |
	|Charly|
	|Dodo  |
	And we will have the following people in "Beer Cans":
	|name |
	|Bob  |
	|Alice|
```
input = ""
output:
```python
from behave import given, then
from hamcrest import assert_that, contains_inanyorder
from my_company import CompanyModel

@given('a set of specific users')
def step_impl(context):
	model = getattr(context, "model", None)
	if not model:
		context.model = CompanyModel()
	for row in context.table:
		context.model.add_user(row["name"], deparment=row["department"])

@then('we will have the following people in "{department}"')
def step_impl(context, department):
	"""
	Compares expected with actual persons in a department.
	NOTE: Unordered comparison (ordering is not important).
	"""
	department_ = context.model.departments.get(department, None)
	if not department_:
		assert_that(False, "Department %s is unknown" % department)
		# -- NORMAl-CASE:
	expected_persons = [ row["name"]  for row in context.table ]
	actual_persons   = department_.members

	# -- UNORDERED TABLE-COMPARISON (using: pyhamcrest)
	assert_that(contains_inanyorder(*expected_persons), actual_persons)
```

id : seed_task_7
name : subset result
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: Subset Result Table Comparison
	Given a set of specific users:
	|name |department      |
	|Alice|Super-sonic Cars|
	|Bob  |Super-sonic Cars|
	Then we will have at least the following people in "Super-sonic Cars":
	|name |
	|Alice|
```
input = ""
output:
```python
from behave import given, then
from hamcrest import assert_that, has_items
from my_company import CompanyModel

@given('a set of specific users')
def step_impl(context):
	model = getattr(context, "model", None)
	if not model:
		context.model = CompanyModel()
	for row in context.table:
		context.model.add_user(row["name"], deparment=row["department"])

@then('we will have at least the following people in "{department}"')
def step_impl(context, department):
	"""
	Compares subset of persons with actual persons in a department.
	NOTE: Unordered subset comparison.
	"""
	department_ = context.model.departments.get(department, None)
	if not department_:
		assert_that(False, "Department %s is unknown" % department)
		# -- NORMAl-CASE:
	expected_persons = [ row["name"]  for row in context.table ]
	actual_persons   = department_.members

	# -- TABLE-SUBSET-COMPARISON (using: pyhamcrest)
	assert_that(has_items(*expected_persons), actual_persons)
```

id : seed_task_8
name : step by step
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: Step by Step
	Given I start a new game
	When I press the big red button
	And I duck
	Then I reach the next level
```
input = ""
output:
```python
from behave import given, when, then
from hamcrest import assert_that, greater_than

@given('I start a new game')
def step_impl(context):
	context.duck_count = 0
	context.red_button_pressed = 0

@when('I press the big red button')
def step_impl(context):
	context.red_button_pressed += 1

@when('I duck')
def step_impl(context):
	context.duck_count += 1

@then('I reach the next level')
def step_impl(context):
	assert_that(context.duck_count, greater_than(0))
	assert_that(context.red_button_pressed, greater_than(0))
```

id : seed_task_9
name : multiple steps
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: Execute multiple Steps in middle Step
	Given I start a new game
	When I do the same thing as before
	Then I reach the next level
```
input = ""
output:
```python
from behave import given, when, then
from hamcrest import assert_that, greater_than

@given('I start a new game')
def step_impl(context):
	context.duck_count = 0
	context.red_button_pressed = 0

@when('I press the big red button')
def step_impl(context):
	context.red_button_pressed += 1

@when('I duck')
def step_impl(context):
	context.duck_count += 1
    
@when('I do the same thing as before')
def step_impl(context):
	context.execute_steps(u"""
	when I press the big {button_color} button
	and I duck
	""".format(button_color="red"))

@then('I reach the next level')
def step_impl(context):
	assert_that(context.duck_count, greater_than(0))
	assert_that(context.red_button_pressed, greater_than(0))
```

id : seed_task_10
name : calculator
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: Calculator
	Given I have a calculator
	When I add "<x>" and "<y>"
	Then the calculator returns "<sum>"

	Examples:
	| x | y | sum |
	| 1 | 1 |  2  |
	| 1 | 2 |  3  |
	| 2 | 1 |  3  |
	| 2 | 7 |  9  |
```
input = ""
output:
```python
from behave import given, when, then
from hamcrest import assert_that, equal_to
from my_calculator import Calculator

@given('I have a calculator')
def step_impl(context):
	context.calculator = Calculator()

@when('I add "{x}" and "{y}"')
def step_impl(context, x, y):
	assert isinstance(x, int)
	assert isinstance(y, int)
	context.calculator.add2(x, y)

@then('the calculator returns "{expected}"')
def step_impl(context, expected):
	assert isinstance(expected, int)
	assert_that(context.calculator.result, equal_to(expected))
```

id : seed_task_11
name : add two numbers
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: Addition
	Given I take the calculator
	When I add 2 and 3
	Then the result should be 5
```
input = ""
output:
```python
from behave import given, when, then
@given ('I take the calculator')
def step_impl(context):
    context.current_value = 0

@when('I add {first_value:d} and {second_value:d}')
def step_impl(context, first_value, second_value):
	context.current_value = first_value + second_value

@then('the result should be {expected_value:d}')
def step_impl(context, expected_value):
	assert context.current_value == expected_value
```

id : seed_task_12
name : subtract two numbers
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: Subtraction
	Given I take the calculator
	When I subtract 5 and 3
	Then the result should be 2
```
input = ""
output:
```python
from behave import given, when, then
@given ('I take the calculator')
def step_impl(context):
	context.current_value = 0

@when('I subtract {first_value:d} and {second_value:d}')
def step_impl(context, first_value, second_value):
	context.current_value = first_value - second_value

@then('the result should be {expected_value:d}')
def step_impl(context, expected_value):
	assert context.current_value == expected_value
```

id : seed_task_13
name : multiply two numbers
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: Multiplication
	Given I take the calculator
	When I multiply 1 and 3
	Then the result should be 3
```
input = ""
output:
```python
from behave import given, when, then
@given ('I take the calculator')
def step_impl(context):
	context.current_value = 0

@when('I multiply {first_value:d} and {second_value:d}')
def step_impl(context, first_value, second_value):
	context.current_value = first_value * second_value

@then('the result should be {expected_value:d}')
def step_impl(context, expected_value):
	assert context.current_value == expected_value
```

id : seed_task_14
name : divide two numbers
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: Division
	Given I take the calculator
	When I divide 6 and 2
	Then the result should be 3
```
input = ""
output:
```python
from behave import given, when, then
@given ('I take the calculator')
def step_impl(context):
	context.current_value = 0

@when('I divide {first_value:d} and {second_value:d}')
def step_impl(context, first_value, second_value):
	context.current_value = first_value / second_value

@then('the result should be {expected_value:d}')
def step_impl(context, expected_value):
	assert context.current_value == expected_value
```

id : seed_task_15
name : potential two numbers
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: Potential
	Given I take the calculator
	When I potentiate <base> and <potence>
	Then the result should be <result>
	Examples:
	|base|potence|result|
	|6   |2      |36    |
```
input = ""
output:
```python
from behave import given, when, then
@given ('I take the calculator')
def step_impl(context):
	context.current_value = 0

@when("I potentiate {first_value:d} and {second_value:d}")
def step_impl(context, first_value, second_value):
	context.current_value = first_value ** second_value

@then('the result should be {expected_value:d}')
def step_impl(context, expected_value):
	assert context.current_value == expected_value
```

id : seed_task_16
name : deposit money
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: deposit money to empty account
	Given a bank account with initial balance of 0
	When we deposit 100 pounds into the account
	Then the balance should be 100
```
input = ""
output:
```python
from behave import given, when, then
from bank_system import BankAccount

@given('a bank account with initial balance of 0')
def step_given_empty_account(context):
	context.bank_account = BankAccount(0)

@when('we deposit 100 pounds into the account')
def step_when_deposit(context):
	context.bank_account.deposit(100)

@then('the balance should be 100')
def step_then_balance(context):
	assert context.bank_account.balance == 100
```

id : seed_task_17
name : withdraw money
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: withdraw money from a bank account
	Given a bank account with initial balance of 1000
	When we withdraw 100 pounds from the account
	Then the balance should be 900
```
input = ""
output:
```python
from behave import given, when, then
from bank_company import BankAccount

@given('a bank account with initial balance of 1000')
def step_given_balance_1000(context):
	context.bank_account = BankAccount(1000)

@when('we withdraw 100 pounds from the account')
def step_when_withdraw_100(context):
	context.bank_account.withdraw(100)

@then('the balance should be 900')
def step_then_balance_is_900(context):
	assert context.bank_account.balance == 900
```

id : seed_task_18
name : create canvas
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: Creating a canvas
	Given c = canvas(10, 20)
	Then c.width == 10
	And c.height == 20
	And every pixel of c is color(0, 0, 0)
```
input = ""
output:
```python
from behave import given, then
from canvas_module import canvas
from tuples_module import tuples
import itertools

@given('c = canvas({h:d}, {w:d})')
def step_impl(context, h, w):
	context.c = canvas.Canvas(h, w)

@then('c.width == {width:d}')
def step_impl(context, width):
	assert context.c.width == width

@then('c.height == {height:d}')
def step_impl(context, height):
	assert context.c.height == height
	
@then('every pixel of c is color({r:d}, {g:d}, {b:d})')
def step_impl(context, r, g, b):
	every_pixel = tuples.Color(r, g, b)
	assert False not in [tuples.t_eq(every_pixel, this_pixel) for this_pixel in itertools.chain(*context.c.pixels)]
```

id : seed_task_19
name : write pixels
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: Writing pixles to a canvas
	Given c = canvas(10, 20)
	And red = color(1.0, 0.0, 0.0)
	When write_pixel(c, 2, 3, red)
	Then pixel_at(c, 2, 3) == red
```
input = ""
output:
```python
from behave import given, when, then
from canvas_module import canvas
from tuples_module import tuples

@given('c = canvas({width:d}, {height:d})')
def step_impl(context, width, height):
	context.c = canvas.Canvas(width, height)

@given('red = color({r:f}, {g:f}, {b:f})')
def step_impl(context, r, g, b):
	context.red = tuples.Color(r, g, b)

@when('write_pixel({can:w}, {h:d}, {w:d}, {color:w})')
def step_impl(context, can, h, w, color):
	canvas.write_pixel(getattr(context, can), h, w, getattr(context, color))

@then('pixel_at({can:w}, {h:d}, {w:d}) == {color:w}')
def step_impl(context, can, h, w, color):
	assert canvas.pixel_at(getattr(context, can), h, w) == getattr(context, color)
```

id : seed_task_20
name : ppm header
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: Add Product to Cart
    Given I am on the Blouse product page
    When I click add to cart
    Then the product should be added to the cart
```
input = ""
output:
```python
from behave import given, when, then
from product_pages import ProductPageActions

@given(u'I am on the Blouse product page')
def step_impl(context):
    context.page_object = ProductPageActions(context.driver)
    assert context.page_object.is_product_page_displayed(), "Product page is not displayed"

@when(u'I click add to cart')
def step_impl(context):
    context.page_object.click_on_add_to_cart()

@then(u'the product should be added to the cart')
def step_impl(context):
    assert context.page_object.is_product_added_to_cart(), "Product is not added to cart"
```

id : seed_task_21
name : ppm pixel data
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: Converting Canvas to PPM
    Given a canvas with pixels written
    When the canvas is converted to PPM format
    Then the generated PPM lines match the expected values
```
input = ""
output:
```python
from behave import given, when, then
from canvas_module import canvas

@given('a canvas with pixels written')
def step_impl(context):
    context.canvas = canvas.Canvas(5, 3)
    canvas.write_pixel(context.canvas, 0, 0, context.c1)
    canvas.write_pixel(context.canvas, 2, 1, context.c2)
    canvas.write_pixel(context.canvas, 4, 2, context.c3)

@when('the canvas is converted to PPM format')
def step_impl(context):
    context.generated_ppm = list(canvas.canvas_to_ppm(context.canvas))

@then('the generated PPM lines match the expected values')
def step_impl(context):
    expected_ppm_lines = context.text.split('\n')
    generated_ppm_lines = context.generated_ppm[4:6]  # Lines 4-6 from generated PPM
    assert expected_ppm_lines == generated_ppm_lines
```

id : seed_task_22
name : default folder
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: Creates project in default features folder
	The application creates the project in a default features folder when no directory is specifies as parameter.
	Given br-init is run with no parameters
	When the application executes
	Then the project is created at features folder
```
input = ""
output:
```python
import os
import filecmp
from behave import given, when, then
from hamcrest import assert_that
import app

@given('br-init is run with {location}')
def step_impl(context, location):
	context.location_param = None if location == 'no parameters' else location
	project_folder = context.location_param or 'features'
	context.project_created_dir = os.path.join(os.getcwd(), project_folder)

@when('the application executes')
def step_impl(context):
	try:
		app.BrInitApp().init_project(context.location_param)
	except Exception as err:
		context.exception_raised = err

@then('the project is created at {folder} folder')
def step_impl(context, folder):
	result = filecmp.dircmp(context.project_src_dir, context.project_created_dir)
	assert_that(result.diff_files).is_empty()
```

id : seed_task_23
name : specified location
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: Creates project in specified location
	The application creates the project at the location specifies as parameter.
	Given br-init is run with project_dir
	When the application executes
	Then the project is created at project_dir folder
```
input = ""
output:
```python
import os
import filecmp
from behave import given, when, then
from hamcrest import assert_that
import app

@given('br-init is run with {location}')
def step_impl(context, location):
	context.location_param = None if location == 'no parameters' else location
	project_folder = context.location_param or 'features'
	context.project_created_dir = os.path.join(os.getcwd(), project_folder)

@when('the application executes')
def step_impl(context):
	try:
		app.BrInitApp().init_project(context.location_param)
	except Exception as err:
		context.exception_raised = err

@then('the project is created at {folder} folder')
def step_impl(context, folder):
	result = filecmp.dircmp(context.project_src_dir, context.project_created_dir)
	assert_that(result.diff_files).is_empty()
```

id : seed_task_24
name : exception
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: An exception is raised if specified folder exists
	The user specifies a folder that already exists, in which case the application raises an exception as exits with an error code
	Given br-init is run with existent
	When the application executes
	Then an exception is raised
```
input = ""
output:
```python
import os
from behave import given, when, then, fail
import app

@given('br-init is run with {location}')
def step_impl(context, location):
	context.location_param = None if location == 'no parameters' else location
	project_folder = context.location_param or 'features'
	context.project_created_dir = os.path.join(os.getcwd(), project_folder)

@when('the application executes')
def step_impl(context):
	try:
		app.BrInitApp().init_project(context.location_param)
	except Exception as err:
		context.exception_raised = err

@then('an exception is raised')
def step_impl(context):
	if not 'exception_raised' in context:
		fail('Exception not raised')
```

id : seed_task_25
name : stealthy approach
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: Stealthy Approach
	Given the spy is equipped with a silenced pistol
	When approaching a guard from behind
	Then the spy should incapacitate the guard silently
```
input = ""
output:
```python
from behave import given, when, then
from secret_service import Spy

@given('the spy is equipped with a silenced pistol')
def step_spy_equipped_with_pistol(context):
	context.spy = Spy(equipment="silenced pistol")

@when('approaching a guard from behind')
def step_approaching_guard(context):
	context.result = context.spy.approach_guard()

@then('the spy should incapacitate the guard silently')
def step_incapacitate_guard(context):
	assert context.result == "incapacitated"
```

id : seed_task_26
name : data encryption
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: Data Encryption
	Given a message to be sent securely
	When encrypting the message with AES-256
	Then the encrypted message should be unreadable without the key
```
input = ""
output:
```python
from behave import given, when, then
from crypto_module import encrypt, decrypt

@given('a message to be sent securely')
def step_given_message(context):
	context.message = "This is a secret message."

@when('encrypting the message with AES-256')
def step_encrypt_message(context):
	context.encrypted_message = encrypt(context.message, key="AES-256")

@then('the encrypted message should be unreadable without the key')
def step_check_encryption(context):
	assert decrypt(context.encrypted_message, key="AES-256") == context.message
```

id : seed_task_27
name : data backup
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: Database Backup
	Given a database containing critical data
	When initiating a backup process
	Then the backup should be stored securely in an offsite location
```
input = ""
output:
```python
from behave import given, when, then
from main_system import Database

@given('a database containing critical data')
def step_given_critical_data(context):
	context.database = Database()

@when('initiating a backup process')
def step_initiate_backup(context):
	context.backup_result = context.database.backup()

@then('the backup should be stored securely in an offsite location')
def step_check_backup(context):
	assert context.backup_result == "stored securely"
```

id : seed_task_28
name : new profil
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: Creating a new user profile
	Given a user wants to create a new profile
	When they provide their name, email, and password
	And they click on the 'Create Profile' button
	Then a new profile should be created successfully
```
input = ""
output:
```python
from behave import given, when, then
from my_app import User

@given('a user wants to create a new profile')
def step_given_user_wants_to_create_new_profile(context):
	context.user = User()

@when('they provide their name, email, and password')
def step_provide_user_info(context):
	context.user.set_info(name="John Doe", email="john@example.com", password="password123")

@when('they click on the {button} button')
def step_click_create_button(context, button):
	context.user.create_profile()

@then('a new profile should be created successfully')
def step_new_profile_created_successfully(context):
	assert context.user.profile_created() == True
```

id : seed_task_29
name : valid login
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: Logging in with valid credentials
	Given a user has a registered account
	When they provide the correct email and password
	And they click on the 'Login' button
	Then they should be logged into their account
```
input = ""
output:
```python
from behave import given, when, then
from my_app import User

@given('a user has a registered account')
def step_given_registered_account(context):
	context.user = User()

@when('they provide the correct email and password')
def step_provide_correct_credentials(context):
	context.user.login(email="john@example.com", password="password123")

@when('they click on the {button} button')
def step_click_login_button(context, button):
	context.user.click_login()

@then('they should be logged into their account')
def step_logged_into_account(context):
	assert context.user.logged_in() == True
```

id : seed_task_30
name : point
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: 'Point' describes tuples with w=1
	Given p is a Point of "4.0", "-4.0", "3.0"
	Then p = tuple "4.0", "-4.0", "3.0", "1.0"
```
input = ""
output:
```python
from behave import given, then
from math_elements import tuples

@given('p is a Point of "{x:f}", "{y:f}", "{z:f}"')
def step_impl(context, x, y, z):
	context.p = tuples.Point(x, y, z)

@then(u'p = tuple "{x:f}", "{y:f}", "{z:f}", "{w:f}"')
def step_impl(context, x, y, z, w):
	assert tuples.t_eq(context.p, (x, y, z, w))
```

id : seed_task_31
name : vector
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: 'Vector' describes tuples with w=0
	Given v is a Vector of "4.0", "-4.0", "3.0"
	Then v = tuple "4.0", "-4.0", "3.0", "0.0"
```
input = ""
output:
```python
from behave import given, then
from math_elements import tuples

@given('v is a Vector of "{x:f}", "{y:f}", "{z:f}"')
def step_impl(context, x, y, z):
	context.p = tuples.Vector(x, y, z)

@then(u'v = tuple "{x:f}", "{y:f}", "{z:f}", "{w:f}"')
def step_impl(context, x, y, z, w):
	assert tuples.t_eq(context.p, (x, y, z, w))
```

id : seed_task_32
name : add tuples
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: Adding two tuples
	Given a1 is a tuple of "3.0", "-2.0", "5.0", "1.0"
	And a2 is a tuple of "-2.0", "3.0", "1.0", "0.0"
	Then a1 + a2 is a tuple of "1.0", "1.0", "6.0", "1.0"
```
input = ""
output:
```python
from behave import given, when, then
from math_elements import tuples

@given('a1 is a tuple of "{x:f}", "{y:f}", "{z:f}", "{w:f}"')
def step_impl(context, x, y, z, w):
	context.a1 = (x, y, z, w)

@given(u'a2 is a tuple of "{x:f}", "{y:f}", "{z:f}", "{w:f}"')
def step_impl(context, x, y, z, w):
	context.a2 = (x, y, z, w)

@then('a1 + a2 is a tuple of "{x:f}", "{y:f}", "{z:f}", "{w:f}"')
def step_impl(context, x, y, z, w):
	result = tuples.t_add(context.a1, context.a2)
	assert tuples.t_eq(result, (x, y, z, w))
```

id : seed_task_33
name : initial cards
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: Deal initial cards
	Given a dealer
	When round starts
	Then the dealer gives itself two cards
```
input = ""
output:
```python
from behave import given, when, then
from poker_game import Dealer

@given("a dealer")
def step_impl(context):
	context.dealer = Dealer()

@when("round starts")
def step_impl(context):
	context.dealer.new_round()

@then("the dealer gives itself two cards")
def step_impl(context):
	assert len(context.dealer.hand) == 2
```

id : seed_task_34
name : sum cards
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario Outline:
	Given a <hand>
	When the dealer sums the cards
	Then the <total> is correct

	Examples: hands
	|hand |total|
	|5,7  |12   |
	|5,Q  |15   |
	|Q,Q,A|21   |
	|Q,A  |21   |
	|A,A,A|13   |
```
input = ""
output:
```python
from behave import given, when, then
from poker_game import Dealer

@given("a {hand}")
def step_impl(context, hand):
	context.dealer = Dealer()
	context.dealer.hand = hand.split(',')

@when("the dealer sums the cards")
def step_impl(context):
	context.dealer_total = context.dealer.get_hand_total()

@then("the {total:d} is correct")
def step_impl(context, total):
	assert (context.dealer_total == total)
```

id : seed_task_35
name : determine play
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario Outline: Dealer plays by the rules
	Given  a hand <total>
	When  the dealer determines a play
	Then the <play> is correct

	Examples: Hands
	|total|play |
	|10   |hit  |
	|15   |hit  |
	|16   |hit  |
	|17   |stand|
	|18   |stand|
	|19   |stand|
	|20   |stand|
	|21   |stand|
	|22   |stand|
```
input = ""
output:
```python
from behave import given, when, then
from poker_game import Dealer

@given("a hand {total:d}")
def step_impl(context, total):
	context.dealer = Dealer()
	context.total = total

@when('the dealer determines a play')
def step_impl(context):
	context.dealer_play = context.dealer.determine_play(context.total)

@then('the {play} is correct')
def steP_impl(context, play):
	assert context.dealer_play == play
```

id : seed_task_36
name : always play
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: A Dealer can always play
	Given a dealer
	When round starts
	Then the dealer chooses a play
```
input = ""
output:
```python
from behave import given, when, then
from poker_game import Dealer

@given("a dealer")
def step_impl(context):
	context.dealer = Dealer()

@when("round starts")
def step_impl(context):
	context.dealer.new_round()

@then("the dealer chooses a play")
def step_impl(context):
	assert context.dealer.make_play() in ['hit' ,'stand']
```

id : seed_task_37
name : icecream
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: Get an icecream
	Given the following icecream
		|name   |id|
		|Vanilla|4 |
	When I visit '/ice-cream/4'
	Then I should see 'Vanilla'
```
input = ""
output:
```python
from behave import given, when, then
from store import icecream

@given(u'the following icecream')
def step_impl(context):
	icecream.data_reset()
	flavors = {}
	for row in context.table:
		flavors[row['id']] = {'name': row['name'], 'id': row['id']}
	context.icecream.flavors = flavors

@when(u'I visit \'{url}\'')
def step_impl(context, url):
	context.resp = context.app.get(url)
	assert context.resp.status_code == 200

@then(u'I should see \'{name}\'')
def step_impl(context, name):
	assert name in context.resp.data
```

id : seed_task_38
name : age comparison 1
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: Exact month day
	Given birthdate "2000-01-01" and evaldate "2010-01-01"
	When evaluate the difference
	Then the result should be equal to "10"
```
input = ""
output:
```python
from behave import given, when, then
from calculator import agecalc

@given('birthdate "{birthdate:ti}" and evaldate "{evaldate:ti}"')
def step_impl(context, birthdate, evaldate):
	context.birthdate = birthdate.date()
	context.evaldate = evaldate.date()

@when('evaluate the difference')
def step_impl(context):
	try:
		context.result = agecalc.calculate(context.birthdate, context.evaldate)
	except Exception as e:
		context.e = e

@then('the result should be equal to "{expected:d}"')
def step_impl(context, expected):
	assert context.result == expected
```

id : seed_task_39
name : age comparison 2
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: Greater month day
	Given birthdate "2000-01-01" and evaldate "2010-02-01"
	When evaluate the difference
	Then the result should be equal to "10"
```
input = ""
output:
```python
from behave import given, when, then
from demographic_system import agecalc

@given('birthdate "{birthdate:ti}" and evaldate "{evaldate:ti}"')
def step_impl(context, birthdate, evaldate):
	context.birthdate = birthdate.date()
	context.evaldate = evaldate.date()

@when('evaluate the difference')
def step_impl(context):
	try:
		context.result = agecalc.calculate(context.birthdate, context.evaldate)
	except Exception as e:
		context.e = e

@then('the result should be equal to "{expected:d}"')
def step_impl(context, expected):
	assert context.result == expected
```

id : seed_task_40
name : age comparison 3
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: Smaller month day
	Given birthdate "2000-01-02" and evaldate "2010-01-01"
	When evaluate the difference
	Then the result should be equal to "9"
```
input = ""
output:
```python
from behave import given, when, then
from demographic_system import agecalc

@given('birthdate "{birthdate:ti}" and evaldate "{evaldate:ti}"')
def step_impl(context, birthdate, evaldate):
	context.birthdate = birthdate.date()
	context.evaldate = evaldate.date()

@when('evaluate the difference')
def step_impl(context):
	try:
		context.result = agecalc.calculate(context.birthdate, context.evaldate)
	except Exception as e:
		context.e = e

@then('the result should be equal to "{expected:d}"')
def step_impl(context, expected):
	assert context.result == expected
```

id : seed_task_41
name : age error
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: Evaldate < brithdate raise ValueError
	Given birthdate "2000-01-01" and evaldate "1999-01-01"
	When evaluate the difference
	Then it should raise ValueError
```
input = ""
output:
```python
from behave import given, when, then
from demographic_system import agecalc

@given('birthdate "{birthdate:ti}" and evaldate "{evaldate:ti}"')
def step_impl(context, birthdate, evaldate):
	context.birthdate = birthdate.date()
	context.evaldate = evaldate.date()

@when('invoked')
def step_impl(context):
	try:
		context.result = agecalc.calculate(context.birthdate, context.evaldate)
	except Exception as e:
		context.e = e

@then('it should raise ValueError')
def step_impl(context):
	assert isinstance(context.e, ValueError)
```

id : seed_task_42
name : soundex encoded
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario Outline: A word is given to soundex algorithm
	Given A soundex instance
	When I enter a word as "<word>"
	Then it is encoded to "<encoded>"

	# the word is the given word
	# encoded is the expected encoded value
	Examples:
	  |word|encoded|
	  |A   |A000   |
	  |I   |I000   |
	  |Ab  |A100   |
	  |Ac  |A200   |
	  |Ad  |A300   |
	  |Ax  |A200   |
	  |A#  |A000   |
	  |Acdl|A234   |
```
input = ""
output:
```python
from behave import given, when, then
from hamcrest import assert_equals
from soundex import MySoundex

@given("A soundex instance")
def step_impl(context):
	"""
	:type context: behave.runner.Context
	"""
	context.soundex = MySoundex()
	print("given_a_soundex_instance ", "\n")

@when('I enter a word as "(?P<word>.+)"')
def step_impl(context, word):
	"""
	:type context: behave.runner.Context
	:type word: str
	"""
	print("when_i_enter_a_word_as ", word, "\n")
	context.encoded = context.soundex.encode(word)

@then('it is encoded to "(?P<encoded>.+)"')
def step_impl(context, encoded):
	"""
	:type context: behave.runner.Context
	:type encoded: str
	"""
	print("then_it_is_encoded_to ", encoded,  "\n",  "\n")
	assert_equals(encoded, context.encoded)
```

id : seed_task_43
name : soundex length
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: A word is given to soundex algorithm
	Given A soundex instance
	When I enter the word "Dcdlb"
	Then the encoded length is equal to "4"
```
input = ""
output:
```python
from behave import given, when, then
from hamcrest import assert_equals
from soundex import MySoundex

@given("A soundex instance")
def step_impl(context):
	"""
	:type context: behave.runner.Context
	"""
	context.soundex = MySoundex()
	print("given_a_soundex_instance ", "\n")

@when('I enter the word "([^\"]*)"')
def step_impl(context, word):
	"""
	:type context: behave.runner.Context
	"""
	print("when_i_enter_the_word_as ", word, "\n")
	context.encoded = context.soundex.encode(word)

@then('the encoded length is equal to "([^\"]*)"')
def step_impl(context, length):
	"""
	:type context: behave.runner.Context
	"""
	print("then_the_encoded_length_is_equal_to ", length, "\n")
	assert_equals(int(length), len(context.encoded))
```

id : seed_task_44
name : soundex first letter
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: A word is given to soundex algorithm with lower case letter
	Given A soundex instance
	When I enter the lower case word "abcd"
	Then the encoded first letter is equal to "A"
```
input = ""
output:
```python
from behave import given, when, then
from hamcrest import assert_equals
from soundex import MySoundex

@given("A soundex instance")
def step_impl(context):
	"""
	:type context: behave.runner.Context
	"""
	context.soundex = MySoundex()
	print("given_a_soundex_instance ", "\n")

@when('I enter the lower case word "([^\"]*)"')
def step_impl(context, word):
	"""
	:type context: behave.runner.Context
	"""
	print("when_i_enter_the_lower_case_word ", word, "\n")
	context.encoded = context.soundex.encode(word)

@then('the encoded first letter is equal to "([^\"]*)"')
def step_impl(context, letter):
	"""
	:type context: behave.runner.Context
	"""
	print("then_the_encoded_first_letter_is_equal_to", letter, "\n")
	assert_equals(letter, context.encoded[0])
```

id : seed_task_45
name : soundex character
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario Outline: A word is given to soundex algorithm
	Given A soundex instance
	When I enter the character "<character>"
	Then it is equal to other encoded character "<other_character>"
	Examples:
	  |character|other_character|
	  |b        |f              |
	  |c        |g              |
	  |d        |t              |
```
input = ""
output:
```python
from behave import given, when, then
from hamcrest import assert_equals
from soundex import MySoundex

@given("A soundex instance")
def step_impl(context):
	"""
	:type context: behave.runner.Context
	"""
	context.soundex = MySoundex()
	print("given_a_soundex_instance ", "\n")

@when('I enter the character "(?P<character>.+)"')
def step_impl(context, character):
	"""
	:type context: behave.runner.Context
	:type character: str
	"""
	print("when_i_enter_the_character ", character, "\n")
	context.encoded = context.soundex.encoded_digit(character)

@then('it is equal to other encoded character "(?P<other_character>.+)"')
def step_impl(context, other_character):
	"""
	:type context: behave.runner.Context
	:type other_character: str
	"""
	print("then_it_is_equal_to_other_encoded_character ", other_character, "\n")
	other_encoded_char = context.soundex.encoded_digit(other_character)
	assert_equals(context.encoded, other_encoded_char)
```

id : seed_task_46
name : soundex string
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario Outline: A word is given to soundex algorithm
	Given A soundex instance
	When I enter the string "<string>"
	Then it is equal to other encoded string "<other_string>"
	Examples:
	  |string|other_string|
	  |BCDL  |Bcdl        |
```
input = ""
output:
```python
from behave import given, when, then
from hamcrest import assert_equals
from soundex import MySoundex

@given("A soundex instance")
def step_impl(context):
	"""
	:type context: behave.runner.Context
	"""
	context.soundex = MySoundex()
	print("given_a_soundex_instance ", "\n")

@when('I enter the string "(?P<string>.+)"')
def step_impl(context, string):
	"""
	:type context: behave.runner.Context
	:type string: str
	"""
	print("when_i_enter_the_string ", string, "\n")
	context.encoded = context.soundex.encode(string)

@then('it is equal to other encoded string "(?P<other_string>.+)"')
def step_impl(context, other_string):
	"""
	:type context: behave.runner.Context
	:type other_string: str
	"""
	print("then_it_is_equal_to_other_encoded_string ", other_string, "\n")
	other_encoded_string = context.soundex.encode(other_string)
	assert_equals(context.encoded, other_encoded_string)
```

id : seed_task_47
name : full calculator
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario Outline: Perform simple arithmetic operations 1 5 x
	Given I have two number <param1> and <param2> into the calculator
	When I perform <operator>
	Then the result should be <expected_result> on the screen
	Examples:
	|param1|param2|operator      |expected_result|
	|12    |6     |division	     |2              |
	|6     |12    |division	     |0.5            |
	|1.5   |2     |multiplication|3              |
	|25    |10    |multiplication|250            |
	|-5    |-2    |subtraction   |-3             |
	|25.5  |10    |subtraction   |15.5           |
	|-5    |-3    |addition      |-8             |
	|10.5  |10    |addition      |20.5           |
```
input = ""
output:
```python
from behave import given, when, then
from various_calculator import SimpleCalculator
@given("I have two number (.*) and (.*) into the calculator")
def step_impl(context,param1, param2):
	global var1
	global var2
	var1 = float(param1)
	var2 = float(param2)

@when("I perform (addition|subtraction|multiplication|division)")
def step_impl(context,operator):
	global var1
	global var2
	global actual_result
	calc = SimpleCalculator(var1, var2)
	if operator == 'addition':
		actual_result = calc.addition()
	if operator == 'subtraction':
		actual_result = calc.subtraction()
	if operator == 'multiplication':
		actual_result = calc.multiplication()
	if operator == 'division':
		actual_result = calc.division()

@then("the result should be (.*) on the screen")
def step_impl(context,expected_result):
	global actual_result
	assert (actual_result == float(expected_result)) is True
```

id : seed_task_48
name : webdriver 1
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: The attribute "role" of a element should be "note"
	Given I open the site "/"
	Then I expect that the attribute "role" from element "#attributeComparison" is "note"
```
input = ""
output:
```python
from behave import given, then
from urllib.parse import urljoin

@given('I open the site "([^"]*)?"')
def open_site(context, url):
	base_url = getattr(context, 'base_url', 'http://localhost:8000')
	destination = urljoin(base_url, url)
	context.behave_driver.open_url(destination)

@then('I expect that the( css)* attribute "([^"]*)?" from element "([^"]*)?" is( not)* "([^"]*)?"')
def check_element_attribute(context, is_css, attr, element, negative, value):
	if is_css:
		attribute_value, value = context.behave_driver.get_element_attribute(element, attr, is_css, value)
	else:
		attribute_value = context.behave_driver.get_element_attribute(element, attr)

	if negative:
		assert attribute_value != value, 'Attribute value was "{}"'.format(attribute_value)
	else:
		assert attribute_value == value, 'Attribute value was "{}"'.format(attribute_value)
```

id : seed_task_49
name : webdriver 2
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: The attribute "role" of a element should not be "main"
	Given I open the site "/"
	Then I expect that the attribute "role" from element "#attributeComparison" is not "main"
```
input = ""
output:
```python
from behave import given, when, then
from urllib.parse import urljoin

@given('I open the site "([^"]*)?"')
def open_site(context, url):
	base_url = getattr(context, 'base_url', 'http://localhost:8000')
	destination = urljoin(base_url, url)
	context.behave_driver.open_url(destination)

@then('I expect that the( css)* attribute "([^"]*)?" from element "([^"]*)?" is( not)* "([^"]*)?"')
def check_element_attribute(context, is_css, attr, element, negative, value):
	if is_css:
		attribute_value, value = context.behave_driver.get_element_attribute(element, attr, is_css, value)
	else:
		attribute_value = context.behave_driver.get_element_attribute(element, attr)

	if negative:
		assert attribute_value != value, 'Attribute value was "{}"'.format(attribute_value)
	else:
		assert attribute_value == value, 'Attribute value was "{}"'.format(attribute_value)
```

id : seed_task_50
name : webdriver 3
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: The CSS attribute "color" of a element should not be "blue"
	Given I open the site "/"
	Then I expect that the css attribute "color" from element "#cssAttributeComparison" is not " rgba(0, 255, 0, 1)"
```
input = ""
output:
```python
from behave import given, when, then
from urllib.parse import urljoin

@given('I open the site "([^"]*)?"')
def open_site(context, url):
	base_url = getattr(context, 'base_url', 'http://localhost:8000')
	destination = urljoin(base_url, url)
	context.behave_driver.open_url(destination)

@then('I expect that the( css)* attribute "([^"]*)?" from element "([^"]*)?" is( not)* "([^"]*)?"')
def check_element_attribute(context, is_css, attr, element, negative, value):
	if is_css:
		attribute_value, value = context.behave_driver.get_element_attribute(element, attr, is_css, value)
	else:
		attribute_value = context.behave_driver.get_element_attribute(element, attr)

	if negative:
		assert attribute_value != value, 'Attribute value was "{}"'.format(attribute_value)
	else:
		assert attribute_value == value, 'Attribute value was "{}"'.format(attribute_value)
```

id : seed_task_51
name : webdriver 4
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: Change the base url to http://127.0.0.1:8000/
	Given the base url is "http://127.0.0.1:8000/"
	When I open the site "/page.html"
	Then I expect that the url is "http://127.0.0.1:8000/page.html"
	And I expect that the url is not "http://localhost:8000/page.html"
```
input = ""
output:
```python
from behave import given, when, then
from urllib.parse import urljoin

@given('the base url is "([^"]*)?"')
def set_base_url(context, url):
	if url.endswith('/'):
		url = url[:-1]
	context.base_url = url

@when('I open the site "([^"]*)?"')
def open_site(context, url):
	base_url = getattr(context, 'base_url', 'http://localhost:8000')
	destination = urljoin(base_url, url)
	context.behave_driver.open_url(destination)

@then('I expect that the url is( not)* "([^"]*)?"')
def check_url(context, negative, value):
	current_url = context.behave_driver.current_url
	if negative:
		assert current_url != value, 'The url was "{}"'.format(current_url)
	else:
		assert current_url == value, 'Expected url to be "{}", but saw the url was "{}"'.format(value, current_url)
```

id : seed_task_52
name : webdriver 5
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: Test if element responds to button press
	Given I open the site "/"
	And the element "#testKeyResponse" not contains any text
	When I press "a"
	Then I expect that element "#testKeyResponse" contains the text "65"
```
input = ""
output:
```python
from behave import given, when, then
from urllib.parse import urljoin

@given('I open the site "([^"]*)?"')
def open_site(context, url):
	base_url = getattr(context, 'base_url', 'http://localhost:8000')
	destination = urljoin(base_url, url)
	context.behave_driver.open_url(destination)

@given('the element "([^"]*)?" contains( not)* the same text as element "([^"]*)?"')
@then('I expect that element "([^"]*)?"( not)* contains the same text as element "([^"]*)?"')
def elements_same_text(context, first_element, negative, second_element):
	first_elem_text = context.behave_driver.get_element_text(first_element)
	second_elem_text = context.behave_driver.get_element_text(second_element)
	same = first_elem_text == second_elem_text
	if negative:
		assert not same, 'Element "{}" text "{}" is same as element "{}"'.format(first_element, first_elem_text, second_element)
	else:
		assert same, 'Element "{}" text "{}" is not same as element "{}" text "{}"'.format(first_element, first_elem_text, second_element, second_elem_text)

@when('I press "{key}"')
def press_button(context, key):
	context.behave_driver.press_button(key)
```

id : seed_task_53
name : webdriver 6
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: Navigate to the Product Page
    Given I am on Home Page
    When I click on Blouse
    Then I should see the Blouse product page
```
input = ""
output:
```python
from behave import given, when, then
from page_objects.home_actions import HomeActions
from page_objects.product_page_actions import ProductPageActions

@given(u'I am on Home Page')
def step_impl(context):
    context.page_object = HomeActions(context.driver)
    context.page_object.open_application(context.base_url)

@when(u'I click on Blouse')
def step_impl(context):
    context.page_object = HomeActions(context.driver)
    context.page_object.click_on_blouse()

@then(u'I should see the Blouse product page')
def step_impl(context):
    context.page_object = ProductPageActions(context.driver)
    assert context.page_object.is_product_page_displayed(), "Product page is not displayed"
```

id : seed_task_54
name : webdriver 7
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: Is not Google
	Given I open the site "/"
	Then I expect that the title is not "Google"
```
input = ""
output:
```python
from behave import given, then
from urllib.parse import urljoin

@given('I open the site "([^"]*)?"')
def open_site(context, url):
	base_url = getattr(context, 'base_url', 'http://localhost:8000')
	destination = urljoin(base_url, url)
	context.behave_driver.open_url(destination)

@then('I expect that the title is( not)* "([^"]*)?"')
def title(context, negative, value):
	if negative:
		assert context.behave_driver.title != value, 'Title was "{}"'.format(context.behave_driver.title)
	else:
		assert context.behave_driver.title == value, 'Title was "{}"'.format(context.behave_driver.title)
```

id : seed_task_55
name : webdriver 8
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: Is correct
	Given I open the site "/"
	Then I expect that the title is "DEMO APP"
```
input = ""
output:
```python
from behave import given, then
from urllib.parse import urljoin

@given('I open the site "([^"]*)?"')
def open_site(context, url):
	base_url = getattr(context, 'base_url', 'http://localhost:8000')
	destination = urljoin(base_url, url)
	context.behave_driver.open_url(destination)

@then('I expect that the title is( not)* "([^"]*)?"')
def title(context, negative, value):
	if negative:
		assert context.behave_driver.title != value, 'Title was "{}"'.format(context.behave_driver.title)
	else:
		assert context.behave_driver.title == value, 'Title was "{}"'.format(context.behave_driver.title)
```

id : seed_task_56
name : chess 1
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: Starting the game
	Given you are starting a game of chess
	When you start a game
	Then the board exists
	And it is the correct size
	And there is the correct number of pieces
	And the score is set to zero
```
input = ""
output:
```python
from behave import given, when, then
from logic_game import Chess

@given(u'you are starting a game of chess')
def step_impl(context):
	context.chess = Chess()

@when(u'you start a game')
def step_impl(context):
	context.chess.start_new_game()
	assert context.chess.game_active == True

@then(u'the board exists')
def step_impl(context):
	assert context.chess.board is not None

@then(u'it is the correct size')
def step_impl(context):
	assert len(context.chess.board) == 8
	for board_row in context.chess.board:
		assert len(board_row) == 8

@then(u'there is the correct number of pieces')
def step_impl(context):
	rules = context.chess.Rules
	expected_pieces = [8, 2, 2, 2, 1, 1]
	for piece in rules.list_of_pieces:
		for number in expected_pieces:
			pass

@then(u'the score is set to zero')
def step_impl(context):
	assert(context.chess.score == 0)
```

id : seed_task_57
name : chess 2
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: Setting up the board
	Given that you have a set of pieces
	When the game is about to start
	Then all of the pieces are put in their correct places
	And none of the pieces are in wrong places
```
input = ""
output:
```python
from behave import given, when, then
from logic_game import Chess
from logic_game.pieces import PiecesSet

@given(u'that you have a set of pieces')
def step_impl(context):
	context.chess = Chess()
	set_of_pieces = PiecesSet()
	assert(len(set_of_pieces.full_set()) == 32)
	assert(len(set_of_pieces.full_set("Pawns")) == 16)
	assert(len(set_of_pieces.full_set("Pawns", "White")) == 8)

@when(u'the game is about to start')
def step_impl(context):
	raise NotImplementedError(u'STEP: When the game is about to start')

@then(u'all of the pieces are put in their correct places')
def step_impl(context):
	raise NotImplementedError(u'STEP: Then all of the pieces are put in their correct places')

@then(u'none of the pieces are in wrong places')
def step_impl(context):
	raise NotImplementedError(u'STEP: Then none of the pieces are in wrong places')
```

id : seed_task_58
name : chess 3
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: Moving a piece
	Given a piece is on the board
	When you move it to a valid position
	Then it changes positions
	And your turn ends
```
input = ""
output:
```python
from behave import given, when, then
from logic_game import Chess

@given(u'a piece is on the board')
def step_impl(context):
	context.chess = Chess()
	piece = context.chess.piece("b", 8)
	assert(piece["color"] == "Black")
	assert(piece["type"] == "Pawn")

@when(u'you move it to a valid position')
def step_impl(context):
	raise NotImplementedError(u'STEP: you move it to a valid position')

@then(u'it changes positions')
def step_impl(context):
	raise NotImplementedError(u'STEP: Then it changes positions')

@then(u'your turn ends')
def step_impl(context):
	raise NotImplementedError(u'STEP: Then your turn ends')
```

id : seed_task_59
name : chess 4
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: Taking a piece
	Given two pieces
	When one piece takes another
	Then the defender's space is occupied by the attacker
	And the defending piece is removed from play
	And your turn ends
```
input = ""
output:
```python
from behave import given, when, then
from games import Game

@given('two pieces')
def given_two_pieces(context):
    context.game = Game()
    context.game.add_piece("attacker", "attacker_position")
    context.game.add_piece("defender", "defender_position")

@when('one piece takes another')
def when_one_piece_takes_another(context):
    attacker_position = "attacker_position"
    defender_position = "defender_position"
    attacker = context.game.board.get(attacker_position)
    defender = context.game.board.get(defender_position)
    if attacker and defender:
        context.game.remove_piece(defender_position)
        context.game.add_piece("attacker", defender_position)

@then("the defender's space is occupied by the attacker")
def then_defender_space_occupied(context):
    attacker_position = "defender_position"
    assert context.game.board.get(attacker_position) == "attacker"

@then("the defending piece is removed from play")
def then_defending_piece_removed(context):
    defender_position = "defender_position"
    assert context.game.board.get(defender_position) is None

@then("your turn ends")
def then_turn_ends(context):
    assert context.game.current_player != "attacker"
```

id : seed_task_60
name : coin
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: Vending Machine accepts quarters
	Given I have a "Quarter"
	When I insert a "Quarter" into the vending machine
	Then the vending machine accepts the "Quarter"
```
input = ""
output:
```python
from behave import given, when, then
from my_services.vending_machine import VendingMachine 
from my_services.product import Product
from my_services.coin_validator import CoinValidator
from my_services.coin import Coin

@given('I have a "{coin}"')
def step_impl(context, coin):
	context.coin = coins.get(coin)
	print(context.coin)

@when('I insert a "{payment}" into the vending machine')
def step_impl(context, payment):
	product = Product('item', context.coin.value)
	context.vending_machine = VendingMachine(product, CoinValidator(), product.price)
	coin = Coin(context.coin.weight, context.coin.diameter)
	context.vending_machine.insert_coins(coin)

@then('the vending machine accepts the "{coin}"')
def step_impl(context, coin):
	assert context.vending_machine.DISPLAY == THANK_YOU

@then("the vending machine does not accepts the coin")
def step_impl(context):
	assert context.vending_machine.DISPLAY == INSERT_COINS
```

id : seed_task_61
name : payment 1
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: Customer orders an item
	Given I am a client
	When I go to order an item
	Then the displays says "Insert Coins"
```
input = ""
output:
```python
from behave import given, when, then
import nose.tools as nt
from ordering_service import order_item

@given('I am a client')
def step_impl(context):
	pass

@when("I go to order an item")
def step_impl(context):
	order_item(context, 1.00)

@then('the displays says "{msg}"')
def step_impl(context, msg):
	nt.assert_equals(context.vending_machine.DISPLAY, msg)
```

id : seed_task_62
name : payment 2
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: Customer pays for item
	Given I am a client
	And order an item for ".25" dollar
	When I insert ".25"
	Then the displays says "Thank you"
```
input = ""
output:
```python
from behave import given, when, then
import nose.tools as nt
from ordering_service import order_item
from vending_machine import create_coin

@given('I am a client')
def step_impl(context):
	pass

@given('order an item for "{price}" dollar')
def step_impl(context, price):
	order_item(context, price)

@when('I insert "{payment}"')
def step_impl(context, payment):
	coin = create_coin(payment)
	print(coin)
	context.change = context.vending_machine.insert_coins(coin)

@then('the displays says "{msg}"')
def step_impl(context, msg):
	nt.assert_equals(context.vending_machine.DISPLAY, msg)
```

id : seed_task_63
name : payment 3
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: Customer pays for item
	Given I am a client
	And order an item for ".50" dollar
	When I insert ".25"
	Then the displays says "Insert Coins"
```
input = ""
output:
```python
from behave import given, when, then
import nose.tools as nt
from ordering_service import order_item
from vending_machine import create_coin

@given('I am a client')
def step_impl(context):
	pass

@given('order an item for "{price}" dollar')
def step_impl(context, price):
	order_item(context, price)

@when('I insert "{payment}"')
def step_impl(context, payment):
	coin = create_coin(payment)
	print(coin)
	context.change = context.vending_machine.insert_coins(coin)

@then('the displays says "{msg}"')
def step_impl(context, msg):
	nt.assert_equals(context.vending_machine.DISPLAY, msg)
```

id : seed_task_64
name : payment 4
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: Customer pays for item
	Given I purchase an item for ".50"
	And I have inserted ".30"
	And display says "Insert Coins"
	When I insert another ".25"
	Then the displays says "Thank you"
	And ".05" cents is returned
```
input = ""
output:
```python
from behave import given, when, then
import nose.tools as nt
from ordering_service import order_item
from vending_machine import create_coin

@given('I purchase an item for "{price}"')
def step_impl(context, price):
	order_item(context, price)

@given('I have inserted "{payment}"')
def step_impl(context, payment):
	context.vending_machine.PAYMENT = float(payment)

@given('display says "Insert Coins"')
def step_impl(context):
	pass

@when('I insert another "{payment}"')
def step_impl(context, payment):
	coin = create_coin(payment)
	context.change = context.vending_machine.insert_coins(coin)

@then('the displays says "{msg}"')
def step_impl(context, msg):
	nt.assert_equals(context.vending_machine.DISPLAY, msg)

@then('"{change}" cents is returned')
def step_impl(context, change):
	nt.assert_equals(context.change, float(change))
```

id : seed_task_65
name : product
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: Customer orders Chips
	Given I order "Chips" for ".50"
	When I select the respective button
	And I have inserted "2" "Quarter"
	Then the product is dispensed
	And the machine displays "Thank you"
```
input = ""
output:
```python
from behave import given, when, then
import nose.tools as nt
from vending_machine import Product, Coin, VendingMachine, CoinValidator

@given('I order "{product}" for "{price}"')
def step_impl(context, product, price):
	product = Product(product, float(price))
	validator = CoinValidator()
	context.vending_machine = VendingMachine(product, validator, product.price)

@when("I select the respective button")
def step_impl(context):
	pass

@when('I have inserted "{amount:d}" "{coin_type}"')
def step_impl(context, amount, coin_type):
	coin = Coin(COINS[coin_type]['weight'], COINS[coin_type]['diameter'])
	for x in range(amount):
		context.vending_machine.insert_coins(coin)

@then("the product is dispensed")
def step_impl(context):
	pass

@then('the machine displays "{msg}"')
def step_impl(context, msg):
	nt.assert_equals(context.vending_machine.DISPLAY, msg)
```

id : seed_task_66
name : account 1
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: open first page
	Given I am on home page
	When the page is loaded
	Then first name tag exists
```
input = ""
output:
```python
from behave import given, when, then
@given("I am on home page")
def step_impl(context):
	context.tester.load_first_page()

@when("the page is loaded")
def step_impl(context):
	print(context.tester.first_page_loaded())
	assert (context.tester.first_page_loaded() == True)

@then("first name tag exists")
def step_impl(context):
	print(context.tester.first_name_tag_exists())
	assert (context.tester.first_name_tag_exists() == True)
```

id : seed_task_67
name : account 2
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: enter first name
	Given the page is loaded
	When first name tag found
	Then enter first name
```
input = ""
output:
```python
from behave import given, when, then
@given("the page is loaded")
def step_impl(context):
	assert (context.tester.first_name_tag_exists() == True)

@when("first name tag found")
def step_impl(context):
	context.tester.get_first_name_tag()

@then("enter first name")
def step_impl(context):
	context.tester.fill_first_name()
```

id : seed_task_68
name : account 3
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: enter last name
	Given last name tag exists
	When last name tag found
	Then enter last name
```
input = ""
output:
```python
from behave import given, when, then
@given("last name tag exists")
def step_impl(context):
	assert(context.tester.last_name_tag_exists() == True)

@when("last name tag found")
def step_impl(context):
	context.tester.get_last_name_tag()

@then("enter last name")
def step_impl(context):
	context.tester.fill_last_name()
```

id : seed_task_69
name : account 4
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: Confirm Checkout
    Given I am on the shipping page
    When I confirm the proceed to checkout
    Then I should be redirected to the authentication page
```
input = ""
output:
```python
from behave import given, when, then
from page_objects.shipping_page import ShippingPageActions
from page_objects.authentication import AuthenticationActions

@given(u'I am on the shipping page')
def step_impl(context):
    context.page_object = ShippingPageActions(context.driver)
    assert context.page_object.is_shipping_page_displayed(), "Shipping page is not displayed"

@when(u'I confirm the proceed to checkout')
def step_impl(context):
    context.page_object.confirm_proceed_to_checkout()

@then(u'I should be redirected to the authentication page')
def step_impl(context):
    context.page_object = AuthenticationActions(context.driver)
    assert context.page_object.is_authentication_page_displayed(), "Authentication page is not displayed"
```

id : seed_task_70
name : account 5
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: click on first page complete button
	Given first step complete button exists
	Then I can click on first step complete button
```
input = ""
output:
```python
from behave import given, then
@given("first step complete button exists")
def step_impl(context):
	assert (context.tester.first_step_complete_button_exists() == True)

@then("I can click on first step complete button")
def step_impl(context):
	context.tester.click_on_first_step_complete_button()
```

id : seed_task_71
name : usage info 1
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: User asks for usage info
	Given the license-generator package is installed on the system
	When I run the license-generator "help" command
	Then I see its usage info
```
input = ""
output:
```python
from behave import given, when, then
import os
import subprocess
from license-generator import package_usage_info

@given(u'the license-generator package is installed on the system')
def step_impl(context):
	os.chdir(context.base_path)
	subprocess.check_output(
		'python {setup_package} develop'.format(
			setup_package=os.path.join(context.base_path, 'setup.py')
		),
		shell=True
	)
	context.assert_license_generator_existence()
	os.chdir(context.testing_ground_path)

@when(u'I run the license-generator "{command_name}" command')
def step_impl(context, command_name):
	context.assert_license_generator_existence()
	context.run_command('license-generator {command}'.format(command=command_name))

@then(u'I see its usage info')
def step_impl(context):
	context.assert_command_output_presence()
	assert (context.command_output.strip() == package_usage_info)
```

id : seed_task_72
name : usage info 2
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: User doesn't send any command
    Given the license-generator package is installed on the system
	When I run the license-generator
	Then I see its usage info
```
input = ""
output:
```python
from behave import given, when, then
import os
import subprocess
from license-generator import package_usage_info

@given(u'the license-generator package is installed on the system')
def step_impl(context):
	os.chdir(context.base_path)
	subprocess.check_output(
		'python {setup_package} develop'.format(
			setup_package=os.path.join(context.base_path, 'setup.py')
		),
		shell=True
	)
	context.assert_license_generator_existence()
	os.chdir(context.testing_ground_path)

@when(u'I run the license-generator')
def step_impl(context):
	context.assert_license_generator_existence()
	context.run_command('license-generator')

@then(u'I see its usage info')
def step_impl(context):
	context.assert_command_output_presence()
	assert (context.command_output.strip() == package_usage_info)
```

id : seed_task_73
name : license 1
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario Outline: It generates licenses based on their name
	Given the license-generator package is installed on the system
	When I run the license-generator "generate" command with "<license_type>" as argument
	Then the "LICENSE" file is generated
	And the generated "LICENSE" file contains the "<license_type_code>" license

	Examples:
	  |license_type|license_type_code|
	  |AGPLv3      |agpl30           |
	  |agplv3      |agpl30           |
	  |AGPL30      |agpl30           |
	  |agpl30      |agpl30           |
	  |APACHE20    |apache20         |
	  |apache20    |apache20         |
	  |GPL30       |gpl30            |
	  |gpl30       |gpl30            |
	  |LGPL30      |lgpl30           |
	  |lgpl30      |lgpl30           |
	  |MIT         |mit              |
	  |mit         |mit              |
	  |MPL20       |mpl20            |
	  |mpl20       |mpl20            |
	  |UNLICENSE   |unlicense        |
	  |unlicense   |unlicense        |
```
input = ""
output:
```python
from behave import given, when, then
import os
import subprocess
from license-generator import package_usage_info

@given(u'the license-generator package is installed on the system')
def step_impl(context):
	os.chdir(context.base_path)
	subprocess.check_output(
		'python {setup_package} develop'.format(
			setup_package=os.path.join(context.base_path, 'setup.py')
		),
		shell=True
	)
	context.assert_license_generator_existence()
	os.chdir(context.testing_ground_path)

@when(u'I run the license-generator "{command_name}" command with "{command_parameter}" as argument')
def step_impl(context, command_name, command_parameter):
	context.assert_license_generator_existence()
	subprocess.check_output(
		'license-generator {command_name} {command_parameter}'.format(
		command_name=command_name,
		command_parameter=command_parameter
		),
		shell=True
	)

@then(u'I see its usage info')
def step_impl(context):
	context.assert_command_output_presence()
	assert (context.command_output.strip() == package_usage_info)
```

id : seed_task_74
name : license 2
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: Generate command fails if no license is specified
	Given the license-generator package is installed on the system
	When I run the license-generator "generate" command with no arguments
	Then I will be reminded to specify a license name
	And the program will exit with an error code
```
input = ""
output:
```python
from behave import given, when, then
import os
import subprocess
from license-generator import no_license_generated_message

@given(u'the license-generator package is installed on the system')
def step_impl(context):
	os.chdir(context.base_path)
	subprocess.check_output(
		'python {setup_package} develop'.format(
			setup_package=os.path.join(context.base_path, 'setup.py')
		),
		shell=True
	)
	context.assert_license_generator_existence()
	os.chdir(context.testing_ground_path)

@when(u'I run the license-generator "{command_name}" command with no arguments')
def step_impl(context, command_name):
	context.assert_license_generator_existence()
	try:
		context.run_command('license-generator {command}'.format(command=command_name))
	except Exception as e:
		if hasattr(e, 'returncode'):
			context.returncode = e.returncode
		if hasattr(e, 'output'):
			context.command_output = e.output

@then(u'I will be reminded to specify a license name')
def step_impl(context):
	context.assert_command_output_presence()
	assert (context.command_output.strip() == no_license_generated_message)

@then(u'the program will exit with an error code')
def step_impl(context):
	if not context.returncode:
		raise RuntimeError('No returncode attribute was set in the context object.')
	assert (context.returncode != 0)
```

id : seed_task_75
name : license 3
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: It generates the license at specified location
	Given the license-generator package is installed on the system
	And the directory "some/project" exists
	When I run "license-generator generate MIT --destination-dir 'some/project'
	Then the "some/project/LICENSE" file is generated
	And the generated "some/project/LICENSE" file contains the "mit" license
```
input = ""
output:
```python
from behave import given, when, then
import os
import subprocess
from license-generator import FileGenerationError
from license-generator import readfile

@given(u'the license-generator package is installed on the system')
def step_impl(context):
	os.chdir(context.base_path)
	subprocess.check_output(
		'python {setup_package} develop'.format(
			setup_package=os.path.join(context.base_path, 'setup.py')
		),
		shell=True
	)
	context.assert_license_generator_existence()
	os.chdir(context.testing_ground_path)

@given(u'the directory "{directory_path}" exists')
def step_impl(context, directory_path):
	directory_path = os.path.join(context.testing_ground_path, directory_path)
	os.makedirs(name=directory_path)
	assert (os.path.exists(directory_path) == True)

@when(u'I run "{command}')
def step_impl(context, command):
	context.run_command(command)

@then(u'the "{license_filename}" file is generated')
def step_impl(context, license_filename):
	license_file = os.path.join(context.testing_ground_path, license_filename)
	if not os.path.isfile(license_file):
		raise FileGenerationError(
			'{license_file} file was not generated'.format(license_file=license_file)
		)

@then(u'the generated "{license_filename}" file contains the "{license_type}" license')
def step_impl(context, license_filename, license_type):
	generated_license_content = readfile(
		os.path.join(context.testing_ground_path, license_filename)
	)
	builtin_license_content = readfile(
		os.path.join(context.base_path, 'license_generator', 'licenses', license_type.lower())
	)
	assert (builtin_license_content == generated_license_content)
```

id : seed_task_76
name : sql attack
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: Execute an sql attack for the setup Windows-Jboss-Benchmark
	Given a setup Windows-Jboss-Benchmark
	When sql attack is performed
	Then sql attack is detected and appropriate status is available
```
input = ""
output:
```python
from behave import given, when, then
@given('a setup Windows-Jboss-Benchmark')
def step_impl(context):
	pass

@when('sql attack is performed')
def step_impl(context):
	assert True is not False

@then('sql attack is detected and appropriate status is available')
def step_impl(context):
	assert context.failed is True
```

id : seed_task_77
name : active tag 1
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: Tag logic with one active tag
	Given I setup the current values for active tags with:
	  |category|value|
	  |foo	   |xxx  |
	Then the following active tag combinations are enabled:
	  |tags                      |enabled?|
	  |@active.with_foo=xxx      |yes     |
	  |@active.with_foo=other    |no      |
	  |@not_active.with_foo=xxx  |no      |
	  |@not_active.with_foo=other|yes     |
	And the following active tag combinations are enabled:
	  |tags                 |enabled?|
	  |@use.with_foo=xxx    |yes     |
	  |@use.with_foo=other  |no      |
	  |@only.with_foo=xxx   |yes     |
	  |@only.with_foo=other |no      |
	  |@not.with_foo=xxx    |no      |
	  |@not.with_foo=other  |yes     |
```
input = ""
output:
```python
from behave import given, then
from hamcrest import assert_that, equal_to
from tag_app import ActiveTagMatcher, parse_bool, normalize_tags

@given('I setup the current values for active tags with')
def step_given_setup_the_current_values_for_active_tags_with(context):
	assert context.table, "REQUIRE: table"
	context.table.require_columns(["category", "value"])

	active_values = getattr(context, "active_value_provider", None)
	if active_values is None:
		# -- SETUP DATA:
		context.active_value_provider = active_values = {}

	for row in context.table.rows:
		category = row["category"]
		value = row["value"]
		active_values[category] = value

@then('the following active tag combinations are enabled')
def step_then_following_active_tags_combinations_are_enabled(context):
	assert context.table, "REQUIRE: table"
	assert context.active_value_provider, "REQUIRE: active_value_provider"
	context.table.require_columns(["tags", "enabled?"])
	ignore_unknown_categories = getattr(context,
		"active_tags_ignore_unknown_categories",
		ActiveTagMatcher.ignore_unknown_categories)

	table = context.table
	annotate_column_id = 0
	active_tag_matcher = ActiveTagMatcher(context.active_value_provider)
	active_tag_matcher.ignore_unknown_categories = ignore_unknown_categories
	mismatched_rows = []
	for row_index, row in enumerate(table.rows):
		tags = normalize_tags(row["tags"].split())
		expected_enabled = parse_bool(row["enabled?"])
		actual_enabled = active_tag_matcher.should_run_with(tags)

		if actual_enabled != expected_enabled:
			# -- ANNOTATE MISMATCH IN EXTRA COLUMN:
			if annotate_column_id == 0:
				annotate_column_id = table.ensure_column_exists("MISMATCH!")
			row.cells[annotate_column_id] = "= %s" % actual_enabled
			mismatched_rows.append(row_index)

	# -- FINALLY: Ensure that there are no mismatched rows.
	assert_that(mismatched_rows, equal_to([]), "No mismatched rows:")
```

id : seed_task_78
name : active tag 2
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: Tag logic with unknown categories (case: ignored)
	Given I setup the current values for active tags with:
	  |category|value|
	  |foo     |xxx  |
	When unknown categories are ignored in active tags
	Then the following active tag combinations are enabled:
	  |tags                 |enabled?|
	  |@use.with_unknown=xxx|yes     |
	  |@use.with_unknown=zzz|yes     |
	  |@not.with_unknown=xxx|yes     |
	  |@not.with_unknown=zzz|yes     |
```
input = ""
output:
```python
from behave import given, then
from hamcrest import assert_that, equal_to
from tag_app import ActiveTagMatcher, parse_bool, normalize_tags

@given('I setup the current values for active tags with')
def step_given_setup_the_current_values_for_active_tags_with(context):
	assert context.table, "REQUIRE: table"
	context.table.require_columns(["category", "value"])
	active_values = getattr(context, "active_value_provider", None)
	if active_values is None:
		# -- SETUP DATA:
		context.active_value_provider = active_values = {}
	for row in context.table.rows:
		category = row["category"]
		value = row["value"]
		active_values[category] = value

@when('unknown categories are ignored in active tags')
def step_unknown_categories_are_ignored_in_active_tags(context):
	context.active_tags_ignore_unknown_categories = True

@then('the following active tag combinations are enabled')
def step_then_following_active_tags_combinations_are_enabled(context):
	assert context.table, "REQUIRE: table"
	assert context.active_value_provider, "REQUIRE: active_value_provider"
	context.table.require_columns(["tags", "enabled?"])
	ignore_unknown_categories = getattr(context, "active_tags_ignore_unknown_categories", ActiveTagMatcher.ignore_unknown_categories)
	table = context.table
	annotate_column_id = 0
	active_tag_matcher = ActiveTagMatcher(context.active_value_provider)
	active_tag_matcher.ignore_unknown_categories = ignore_unknown_categories
	mismatched_rows = []
	for row_index, row in enumerate(table.rows):
		tags = normalize_tags(row["tags"].split())
		expected_enabled = parse_bool(row["enabled?"])
		actual_enabled = active_tag_matcher.should_run_with(tags)
		if actual_enabled != expected_enabled:
			# -- ANNOTATE MISMATCH IN EXTRA COLUMN:
			if annotate_column_id == 0:
				annotate_column_id = table.ensure_column_exists("MISMATCH!")
			row.cells[annotate_column_id] = "= %s" % actual_enabled
			mismatched_rows.append(row_index)
	# -- FINALLY: Ensure that there are no mismatched rows.
	assert_that(mismatched_rows, equal_to([]), "No mismatched rows:")
```

id : seed_task_79
name : tuto
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: run a simple test
	Given we have behave installed
	When we implement a test
	Then behave will test it for us!
```
input = ""
output:
```python
from behave import given, when, then
@given('we have behave installed')
def step_impl(context):
	pass

@when('we implement a test')
def step_impl(context):
	assert True is not False

@then('behave will test it for us!')
def step_impl(context):
	assert context.failed is False
```

id : seed_task_80
name : background
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: the stuff should be set up
	Given I am testing stuff
	And some stuff is set up
	And stuff has been set up
	Then it will work
```
input = ""
output:
```python
from behave import given, then
@given("I am testing stuff")
def step_impl(context):
	context.testing_stuff = True

@given("some stuff is set up")
def step_impl(context):
	context.stuff_set_up = True

@given("stuff has been set up")
def step_impl(context):
	assert context.testing_stuff is True
	assert context.stuff_set_up is True

@then("it will work")
def step_impl(context):
	pass
```

id : seed_task_81
name : outline
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario Outline: run scenarios with one example table
	Given Some text <prefix>
	When we add some text <suffix>
	Then we should get the <combination>

	Examples: some simple examples
	|prefix|suffix |combination |
	|go    |ogle   |google      |
	|onomat|opoeia |onomatopoeia| 
	|comb  |ination|combination |
```
input = ""
output:
```python
from behave import given, when, then
@given("some text {prefix}")
def step_impl(context, prefix):
	context.prefix = prefix

@when('we add some text {suffix}')
def step_impl(context, suffix):
	context.combination = context.prefix + suffix

@then('we should get the {combination}')
def step_impl(context, combination):
	assert context.combination == combination
```

id : seed_task_82
name : parsing
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: basic parsing
	Given a string with an argument
	Then we get "with" parsed
```
input = ""
output:
```python
from behave import given, then
@given('a string {argument} an argument')
def step_impl(context, argument):
	context.argument = argument

@then('we get "{argument}" parsed')
def step_impl(context, argument):
	assert context.argument == argument
```

id : seed_task_83
name : text
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: step with text
	Given some body of text
	"""
	Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
	Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
	"""
	Then the text is as expected
```
input = ""
output:
```python
from behave import given, then
@given('some body of text')
def step_impl(context):
	assert context.text
	context.saved_text = context.text

TEXT = '''Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.'''
@then('the text is as expected')
def step_impl(context):
	assert context.saved_text, 'context.saved_text is %r!!' % (context.saved_text, )
	context.saved_text.assert_equals(TEXT)
```

id : seed_task_84
name : data
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: step with a table
	Given some initial data
		|name	  |department |
		|Barry    |Beer Cans  |
		|Pudey 	  |Silly Walks|
		|Two-Lumps|Silly Walks| 
	Then we will have the expected data
```
input = ""
output:
```python
from behave import given, then
@given('some initial data')
def step_impl(context):
	assert context.table
	context.saved_table = context.table

TABLE_DATA = [
	dict(name='Barry', department='Beer Cans'),
	dict(name='Pudey', department='Silly Walks'),
	dict(name='Two-Lumps', department='Silly Walks'),
]
@then('we will have the expected data')
def step_impl(context):
	assert context.saved_table, 'context.saved_table is %r!!' % (context.saved_table, )
	for expected, got in zip(TABLE_DATA, iter(context.saved_table)):
		assert expected['name'] == got['name']
		assert expected['department'] == got['department']
```

id : seed_task_85
name : substituted text
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario Outline: step with text and subtitution
	Given some body of text
	"""
	Lorem <ipsum> dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
	Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
	"""
	Then the text is substituted as expected

	Examples:
	| ipsum |
	| spam  |
	| ham   |
```
input = ""
output:
```python
from behave import given, then
@given('some body of text')
def step_impl(context):
	assert context.text
	context.saved_text = context.text

TEXT = '''Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.'''

@then('the text is substituted as expected')
def step_impl(context):
	assert context.saved_text, 'context.saved_text is %r!!' % (context.saved_text, )
	expected = TEXT.replace('ipsum', context.active_outline['ipsum'])
	context.saved_text.assert_equals(expected)
```

id : seed_task_86
name : alarm 1
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: Alarm
	Given smartHome, alarm turned off, touch not pressed, button not pressed
	When touch is pressed
	Then sound the alarm
```
input = ""
output:
```python
from behave import given, when, then
from malyDomek import malyDomek

@given('smartHome, alarm off, touch not pressed, button not pressed')
def step_impl(context):
	context.malyDom = malyDomek()

@when('touch is pressed')
def step_impl(context):
	context.malyDom.Out()

@then('sound the alarm')
def step_impl(context):
	assert context.malyDom.alarmInProgress is True
```

id : seed_task_87
name : alarm 2
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: Alarm
	Given smartHome, alarm disarmed, button not pressed
	When the button is pressed
	Then arm the alarm
```
input = ""
output:
```python
from behave import given, when, then
from malyDomek import malyDomek

@given('smartHome, alarm disarmed, button not pressed')
def step_impl(context):
	context.malyDom = malyDomek()

@when('the button is pressed')
def step_impl(context):
	context.malyDom.Arm()

@then('arm the alarm')
def step_impl(context):
	assert context.malyHome.armed is True
	assert context.malyDom.wlasnieUzbroilem is True
```

id : seed_task_88
name : alarm 3
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: Alarm
	Given smartHome
	When the sensor reads the temperature below 15
	Then turn on the white LED
```
input = ""
output:
```python
from behave import given, when, then
from malyDomek import malyDomek

@given('smartHome')
def step_impl(context):
	context.malyDom = malyDomek()

@when('the sensor reads the temperature below 15')
def step_impl(context):
	t=300
	context.malyDom.CheckTemperature(t)

@then('turn on the white LED')
def step_impl(context):
	assert context.malyDom.diodaBiala.read() is 1
	assert context.malyDom.diodaZielona.read() is 0
	assert context.malyDom.diodaCzerwona.read() is 0
```

id : seed_task_89
name : alarm 4
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: Alarm
	Given smartHome
	When the sensor reads the temperature between 16 and 25
	Then turn on the green LED
```
input = ""
output:
```python
from behave import given, when, then
from malyDomek import malyDomek

@given('smartHome')
def step_impl(context):
	context.malyDom = malyDomek()

@when('the sensor reads the temperature between 16 and 25')
def step_impl(context):
	t=400
	context.malyDom.CheckTemperature(t)

@then('turn on the green LED')
def step_impl(context):
	assert context.malyDom.diodaBiala.read() is 0
	assert context.malyDom.diodaZielona.read() is 1
	assert context.malyDom.diodaCzerwona.read() is 0
```

id : seed_task_90
name : alarm 5
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: Alarm
	Given smartHome
	When the sensor reads the temperature between 26 and 50
	Then turn on the red LED
```
input = ""
output:
```python
from behave import given, when, then
from malyDomek import malyDomek

@given('smartHome')
def step_impl(context):
	context.malyDom = malyDomek()

@when('the sensor reads the temperature between 26 and 50')
def step_impl(context):
	t=600
	context.malyDom.CheckTemperature(t)

@then('turn on the red LED')
def step_impl(context):
	assert context.malyDom.diodaBiala.read() is 0
	assert context.malyDom.diodaZielona.read() is 0
	assert context.malyDom.diodaCzerwona.read() is 1
```

id : seed_task_91
name : joke
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: Jokes can be read from CLI
	Given CLI jokes tool is installed
	When I execute "joke"
	Then I should see "Setup"
	And I should see "Punchline"
```
input = ""
output:
```python
from behave import given, when, then
import pexpect

@given(u'CLI jokes tool is installed')
def step_impl(context):
	execute('./joke/install')

@when(u'I execute "{cmd}"')
def step_impl(context, cmd):
	out = execute(cmd)
	context.out = out

@then(u'I should see "{expected_text}"')
def step_impl(context, expected_text):
	assert expected_text in context.out

def execute(cmd):
	output, status = pexpect.run(cmd, withexitstatus=1, timeout=600)
	return output
```

id : seed_task_92
name : login
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: Login
	Given I am on the login page
	And my account has already been created
	When I fill in the user signin form
	Then I should be on my console page
	And I should see "Login successful!"
```
input = ""
output:
```python
from behave import given, when, then
from selenium import webdriver

@given('I am on the login page')
def given_on_login_page(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://example.com/login")

@given('my account has already been created')
def given_account_created(context):
    pass

@when('I fill in the user signin form')
def when_fill_user_signin_form(context):
    username_field = context.driver.find_element_by_id("username")
    username_field.send_keys("username")
    password_field = context.driver.find_element_by_id("password")
    password_field.send_keys("password12345")
    signin_button = context.driver.find_element_by_id("signin-button")
    signin_button.click()

@then('I should be on my console page')
def then_on_console_page(context):
    assert "console" in context.driver.current_url

@then('I should see "{expected_text}"')
def then_should_see_text(context, expected_text):
    page_source = context.driver.page_source
    assert expected_text in page_source

def after_scenario(context, scenario):
    if hasattr(context, 'driver'):
        context.driver.quit()
```

id : seed_task_93
name : landing
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: Landing Page
	Given I have a browser open
	When I enter the site url
	Then I should be on the landing page
```
input = ""
output:
```python
from behave import given, when, then
from selenium import webdriver

@given(u'I have a browser open')
def step_impl(context):
	context.browser = webdriver.Firefox()
	context.browser.implicitly_wait(3)

@when(u'I enter the site url')
def step_impl(context):
	context.browser.get('http://localhost:8000/')

@then(u'I should be on the landing page')
def step_impl(context):
	assert('Cloudonyms' in context.browser.title)
	context.browser.quit()
```

id : seed_task_94
name : query 1
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: query-age-gender-health-expenditures
	Given a client
	When the client queries "age_and_gender" for "age_group:total" returning all "years"
	Then from the "age_and_gender" result the "2002" value is greater than "10"
	Then from the "age_and_gender" result the "2010" value is greater than "10"
```
input = ""
output:
```python
from behave import given, when, then
import api
import time
from users_data import check_results

@given(u'a client')
def step_impl(context):
	context.client = api.create()
	for i in range(10):
		try:
			status = context.client.status()
			if status == "OK":
				break
		except:
			pass
		time.sleep(1.5)

@when(u'the client queries "{table}" for "{attribute}" returning all "{values}"')
def step_impl(context, table, attribute, values):
	result = context.client.query(table, attribute, values)
	context.results[table].append(result)

@then(u'from the "{table}" result the "{key}" value is greater than "{value}"')
def step_impl(context, table, key, value):
	def check(check_val):
		assert(int(check_val) > int(value))
	check_results(context, table, key, check)
```

id : seed_task_95
name : query 2
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: Query Invalid Table for Males in 2010
	Given a client
	When the client queries "invalid_table" for "gender:males" returning all "2010"
	Then the "invalid_table" result is empty
	And the "invalid_table" result is an error
```
input = ""
output:
```python
from behave import given, when, then
import api
import time

@given(u'a client')
def step_impl(context):
	context.client = api.create()
	for i in range(10):
		try:
			status = context.client.status()
			if status == "OK":
				break
		except:
			pass
		time.sleep(1.5)

@when(u'the client queries "{table}" for "{attribute}" returning all "{values}"')
def step_impl(context, table, attribute, values):
	result = context.client.query(table, attribute, values)
	context.results[table].append(result)

@then(u'the "{table}" result is empty')
def step_impl(context, table):
	q_result = context.results[table][0]
	results = q_result.get('results', [])
	assert(not results)

@then(u'the "{table}" result is an error')
def step_impl(context, table):
	q_result = context.results[table][0]
	assert('error' in q_result)
```

id : seed_task_96
name : find postcode
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: I can find house prices by postcode
	Given a house price search engine with July 2016 data
	And I am on the search page
	When I enter the post code GL5 4TT
	And I click the search button
	Then all house prices should be in GL5
```
input = ""
output:
```python
from behave import given, when, then
from hamcrest import assert_that, starts_with

@given('a house price search engine with July 2016 data')
def step_impl(context):
	pass

@given('I am on the search page')
def step_impl(context):
	context.browser.visit("http://192.168.99.100:8080/")

@when('I enter the post code {postcode}')
def step_impl(context, postcode):
	context.browser.fill("query", postcode)

@when('I click the search button')
def step_impl(context):
	context.browser.find_by_name("search").click()

@then('all house prices should be in {postcode}')
def step_impl(context, postcode):
	elements = context.browser.find_by_css(".result")
	for element in elements:
		assert_that(element.value, starts_with(postcode))
```

id : seed_task_97
name : find date
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: I can find house prices by date
	Given a house price search engine with July 2016 data
	And I am on the search page
	When I enter the start date of 14 July
	And I enter an end date of 21 July
	And I click the search button
	Then all house prices should be for sales between 14 July and 21 July
```
input = ""
output:
```python
from behave import given, when, then
from dateutil.parser import parse as parse_date
from hamcrest import assert_that, is_greater_than, is_less_than

@given('a house price search engine with July 2016 data')
def step_impl(context):
	pass

@given('I an on the search page')
def step_impl(context):
	context.browser.visit("http://192.168.99.100:8080/")

@when('I enter a start date of {startdate}')
def step_impl(context, startdate):
	context.browser.fill("startdate", startdate)

@when('I enter an end date of {enddate}')
def step_impl(context, enddate):
	context.browser.fill("enddate", enddate)

@when('I click the search button')
def step_impl(context):
	context.browser.find_by_name("search").click

@then('all house prices should be for sales between {startdate} and {enddate}')
def step_impl(context, startdate, enddate):
	startdate = parse_date(startdate)
	enddate = parse_date(enddate)
	elements = context.browser.find_by_css(".result")
	for element in elements:
		date = parse_date(element.value)
		assert_that(date, is_greater_than(startdate))
		assert_that(date, is_less_than(enddate))
```

id : seed_task_98
name : peers 1
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: basic startup of 3 validating peers
	Given we compose "docker-compose-3.yml"
	When requesting "/chain" from "vp0"
	Then I should get a JSON response with "height" = "1"
```
input = ""
output:
```python
from behave import given, when, then
import bdd_compose_util
import bdd_test_util
import requests
from my_app import buildUrl, getAttributeFromJSON

@given(u'we compose "{composeYamlFile}"')
def step_impl(context, composeYamlFile):
	context.compose_yaml = composeYamlFile
	fileArgsToDockerCompose = bdd_compose_util.getDockerComposeFileArgsFromYamlFile(context.compose_yaml)
	context.compose_output, context.compose_error, context.compose_returncode = bdd_test_util.cli_call(["docker-compose"] + fileArgsToDockerCompose + ["up","--force-recreate", "-d"], expect_success=True)
	assert context.compose_returncode == 0, "docker-compose failed to bring up {0}".format(composeYamlFile
	bdd_compose_util.parseComposeOutput(context)
	timeoutSeconds = 15
	assert bdd_compose_util.allContainersAreReadyWithinTimeout(context, timeoutSeconds), "Containers did not come up within {} seconds, aborting".format(timeoutSeconds)

@when(u'requesting "{path}" from "{containerName}"')
def step_impl(context, path, containerName):
	ipAddress = bdd_test_util.ipFromContainerNamePart(containerName, context.compose_containers)
	request_url = buildUrl(context, ipAddress, path)
	resp = requests.get(request_url, headers={'Accept': 'application/json'}, verify=False)
	assert resp.status_code == 200, "Failed to GET url %s:  %s" % (request_url,resp.text)
	context.response = resp

@then(u'I should get a JSON response containing "{attribute}" attribute')
def step_impl(context, attribute):
	getAttributeFromJSON(attribute, context.response.json(), "Attribute not found in response (%s)" %(attribute))
```

id : seed_task_99
name : peers 2
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: Peers list test, single peer issue #827
	Given we compose "docker-compose-1.yml"
	When requesting "/network/peers" from "vp0"
	Then I should get a JSON response with array "peers" contains "1" elements
```
input = ""
output:
```python
from behave import given, when, then
import bdd_compose_util
import bdd_test_util
import requests
from my_app import buildUrl, getAttributeFromJSON

@given(u'we compose "{composeYamlFile}"')
def step_impl(context, composeYamlFile):
	context.compose_yaml = composeYamlFile
	fileArgsToDockerCompose = bdd_compose_util.getDockerComposeFileArgsFromYamlFile(context.compose_yaml)
	context.compose_output, context.compose_error, context.compose_returncode = bdd_test_util.cli_call(["docker-compose"] + fileArgsToDockerCompose + ["up","--force-recreate", "-d"], expect_success=True)
	assert context.compose_returncode == 0, "docker-compose failed to bring up {0}".format(composeYamlFile
	bdd_compose_util.parseComposeOutput(context)
	timeoutSeconds = 15
	assert bdd_compose_util.allContainersAreReadyWithinTimeout(context, timeoutSeconds), "Containers did not come up within {} seconds, aborting".format(timeoutSeconds)

@when(u'requesting "{path}" from "{containerName}"')
def step_impl(context, path, containerName):
	ipAddress = bdd_test_util.ipFromContainerNamePart(containerName, context.compose_containers)
	request_url = buildUrl(context, ipAddress, path)
	resp = requests.get(request_url, headers={'Accept': 'application/json'}, verify=False)
	assert resp.status_code == 200, "Failed to GET url %s:  %s" % (request_url,resp.text)
	context.response = resp

@then(u'I should get a JSON response with array "{attribute}" contains "{expectedValue}" elements')
def step_impl(context, attribute, expectedValue):
	foundValue = getAttributeFromJSON(attribute, context.response.json(), "Attribute not found in response (%s)" %(attribute))
	assert (len(foundValue) == int(expectedValue)), "For attribute %s, expected array of size (%s), instead found (%s)" % (attribute, expectedValue, len(foundValue))
```

id : seed_task_100
name : peers 3
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: List Peers when two are up
	Given we compose "docker-compose-2.yml"
	When I execute "peer network list" in container "vp0"
	Then the command should complete successfully
	And stdout should contain JSON with "Peers" array of length 1
```
input = ""
output:
```python
from behave import given, when, then
import bdd_compose_util
import bdd_test_util

from bdd_test_util import executeCommandInContainer, commandCompletedSuccessfully
from main_module import assertIsJson, decodeJson, getAttribute, assertLength

@given(u'we compose "{composeYamlFile}"')
def step_impl(context, composeYamlFile):
    context.compose_yaml = composeYamlFile
    fileArgsToDockerCompose = bdd_compose_util.getDockerComposeFileArgsFromYamlFile(context.compose_yaml)
    context.compose_output, context.compose_error, context.compose_returncode = bdd_test_util.cli_call(["docker-compose"] + fileArgsToDockerCompose + ["up","--force-recreate", "-d"], expect_success=True)
    assert context.compose_returncode == 0, "docker-compose failed to bring up {0}".format(composeYamlFile)
    bdd_compose_util.parseComposeOutput(context)
    timeoutSeconds = 15
    assert bdd_compose_util.allContainersAreReadyWithinTimeout(context, timeoutSeconds), "Containers did not come up within {} seconds, aborting".format(timeoutSeconds)

@when(u'I execute "{command}" in container {containerName}')
def step_impl(context, command, containerName):
    executeCommandInContainer(context, command, containerName)

@then(u'the command should complete successfully')
def step_impl(context):
    assert commandCompletedSuccessfully(context)

@then(u'{stream} should contain JSON with "{attribute}" array of length {length}')
def step_impl(context, stream, attribute, length):
    data = context.command[stream]
    assertIsJson(data)
    json = decodeJson(data)
    array = getAttribute(attribute, json)
    assertLength(array, int(length))
```

id : seed_task_101
name : peers 4
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: 1 peer and 1 membersrvc, query transaction certs with query parameter count
	Given we compose "docker-compose-rest.yml"
	And I use the following credentials for querying peers:
	  |peer|username  |secret      |
	  |vp0 |test_user0|MS9qrN8hFjlE|
	And I register with CA supplying username "test_user0" and secret "MS9qrN8hFjlE" on peers:
	  |vp0|
	When I request transaction certs with query parameters on "vp0"
	  |key  |value|
	  |count|1    |
	Then I should get a JSON response with "1" different transaction certs
```
input = ""
output:
```python
from behave import given, when, then
from main_system import bdd_compose_util, bdd_test_util, buildUrl, getAttributeFromJSON
import requests

@given(u'we compose "{composeYamlFile}"')
def step_impl(context, composeYamlFile):
	context.compose_yaml = composeYamlFile
	fileArgsToDockerCompose = bdd_compose_util.getDockerComposeFileArgsFromYamlFile(context.compose_yaml)
	context.compose_output, context.compose_error, context.compose_returncode = bdd_test_util.cli_call(["docker-compose"] + fileArgsToDockerCompose + ["up","--force-recreate", "-d"], expect_success=True)
	assert context.compose_returncode == 0, "docker-compose failed to bring up {0}".format(composeYamlFile
	bdd_compose_util.parseComposeOutput(context)
	timeoutSeconds = 15
	assert bdd_compose_util.allContainersAreReadyWithinTimeout(context, timeoutSeconds), "Containers did not come up within {} seconds, aborting".format(timeoutSeconds)

@when(u'I request transaction certs with query parameters on "{containerName}"')
def step_impl(context, containerName):
	assert 'table' in context, "table (of query parameters) not found in context"
	assert 'userName' in context, "userName not found in context"
	assert 'compose_containers' in context, "compose_containers not found in context"
	ipAddress = bdd_test_util.ipFromContainerNamePart(containerName, context.compose_containers)
	request_url = buildUrl(context, ipAddress, "/registrar/{0}/tcert".format(context.userName))
	queryParams = {}
	for row in context.table.rows:
		key, value = row['key'], row['value']
		queryParams[key] = value
	resp = requests.get(request_url, params=queryParams, headers={'Accept': 'application/json'}, verify=False)
	assert resp.status_code == 200, "Failed to GET to %s:  %s" % (request_url, resp.text)
	context.response = resp

@then(u'I should get a JSON response with "{expectedValue}" different transaction certs')
def step_impl(context, expectedValue):
	foundValue = getAttributeFromJSON("OK", context.response.json(), "Attribute not found in response (OK)")
	assert (len(set(foundValue)) == int(expectedValue)), "For attribute OK, expected different transaction cert of size (%s), instead found (%s)" % (expectedValue, len(set(foundValue)))
```

id : seed_task_102
name : create employee
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: Create employee - post with token
	Given I prepare environment for tests run
	When I register an employee with name "morpheus" and job "leader"
	Then I verify that status code is "201"
	And I verify that response contains "morpheus" as "name" attribute
	And I verify that response contains "leader" as "job" attribute
```
input = ""
output:
```python
from behave import given, when, then
from hamcrest import assert_that, is_
from company_employees import generate_data_file, post

@given(u'I prepare environment for tests run')
def step_impl(context):
	context.execute_steps('''
		Given I register an user with email "eve.holt@reqres.in" and "cityslicka"
		And I login with email "eve.holt@reqres.in" and "cityslicka"
	''')

@when(u'I register an employee with name {name} and job {job}')
def step_impl(context, name, job):
	data = generate_data_file(name=name, job=job)
	context.response = post(context.base_url + "users", context.token, data)

@then(u'I verify that status code is "{status_code}"')
def step_impl(context, status_code):
	assert_that(context.response.status_code, is_(int(status_code)))

@then(u'I verify that response contains "{response}" as "{attribute}" attribute')
def step_impl(context, response, attribute):
	text = context.response.json()
	assert_that(text[str(attribute)], is_(str(response)))
```

id : seed_task_103
name : change employee
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: Change employee- put with token
	Given I prepare environment for tests run
	And I register an employee with name "morpheus" and job "leader"
	When I change an employee 1 with name "morpheus" and job "zion resident"
	Then I verify that status code is "200"
	And I verify that response contains "zion resident" as "job" attribute
```
input = ""
output:
```python
from behave import given, when, then
from hamcrest import assert_that, is_
from company_employees import generate_data_file, post, put

@given(u'I prepare environment for tests run')
def step_impl(context):
	context.execute_steps('''
		Given I register an user with email "eve.holt@reqres.in" and "cityslicka"
		And I login with email "eve.holt@reqres.in" and "cityslicka"
	''')

@given(u'I register an employee with name {name} and job {job}')
def step_impl(context, name, job):
	data = generate_data_file(name=name, job=job)
	context.response = post(context.base_url + "users", context.token, data)

@when(u'I change an employee {employee_id} with name "{name}" and job "{job}"')
def step_impl(context, employee_id, name, job):
	data = generate_data_file(name=name, job=job)
	context.response = put(context.base_url + "users/" + employee_id, token=context.token, data=data)

@then(u'I verify that status code is "{status_code}"')
def step_impl(context, status_code):
	assert_that(context.response.status_code, is_(int(status_code)))

@then(u'I verify that response contains "{response}" as "{attribute}" attribute')
def step_impl(context, response, attribute):
	text = context.response.json()
	assert_that(text[str(attribute)], is_(str(response)))
```

id : seed_task_104
name : delete employee
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: Delete employee- delete with token
	Given I prepare environment for tests run
	And I register an employee with name "morpheus" and job "leader"
	When I delete the employee 1
	Then I verify that status code is "204"
```
input = ""
output:
```python
from behave import given, when, then
from hamcrest import assert_that, is_
from company_employees import generate_data_file, post, delete

@given(u'I prepare environment for tests run')
def step_impl(context):
	context.execute_steps('''
		Given I register an user with email "eve.holt@reqres.in" and "cityslicka"
		And I login with email "eve.holt@reqres.in" and "cityslicka"
	''')

@given(u'I register an employee with name {name} and job {job}')
def step_impl(context, name, job):
	data = generate_data_file(name=name, job=job)
	context.response = post(context.base_url + "users", context.token, data)

@when(u'I delete the employee {employee_id}')
def step_impl(context, employee_id):
	context.response = delete(context.base_url + "users/" + employee_id, token=context.token)

@then(u'I verify that status code is "{status_code}"')
def step_impl(context, status_code):
	assert_that(context.response.status_code, is_(int(status_code)))
```

id : seed_task_105
name : search employee
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: Search employee- search with token
	Given I prepare environment for tests run
	And I register an employee with name "morpheus" and job "leader"
	When I search the employee 1
	Then I verify that status code is "200"

```
input = ""
output:
```python
from behave import given, when, then
from hamcrest import assert_that, is_
from company_employees import generate_data_file, post, get

@given(u'I prepare environment for tests run')
def step_impl(context):
	context.execute_steps('''
		Given I register an user with email "eve.holt@reqres.in" and "cityslicka"
		And I login with email "eve.holt@reqres.in" and "cityslicka"
	''')

@given(u'I register an employee with name {name} and job {job}')
def step_impl(context, name, job):
	data = generate_data_file(name=name, job=job)
	context.response = post(context.base_url + "users", context.token, data)

@when(u'I search the employee {employee_id}')
def step_impl(context, employee_id):
	context.response = get(context.base_url + "users/" + employee_id, token=context.token)

@then(u'I verify that status code is "{status_code}"')
def step_impl(context, status_code):
	assert_that(context.response.status_code, is_(int(status_code)))
```

id : seed_task_106
name : try search
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: Try to search an employee that does not exist
	Given I prepare environment for tests run
	When I search the employee -1
	Then I verify that status code is "404"
```
input = ""
output:
```python
from behave import given, when, then
from hamcrest import assert_that, is_
from company_employees import get

@given(u'I prepare environment for tests run')
def step_impl(context):
	context.execute_steps('''
		Given I register an user with email "eve.holt@reqres.in" and "cityslicka"
		And I login with email "eve.holt@reqres.in" and "cityslicka"
	''')

@when(u'I search the employee {employee_id}')
def step_impl(context, employee_id):
	context.response = get(context.base_url + "users/" + employee_id, token=context.token)

@then(u'I verify that status code is "{status_code}"')
def step_impl(context, status_code):
	assert_that(context.response.status_code, is_(int(status_code)))
```

id : seed_task_107
name : try create
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: Try to create an user without using a password
	Given I prepare environment for tests run
	When I try to register an user using only email "kea@gmail.com"
	Then I verify that status code is "400"
	And I verify that response contains "Missing password" as "error" attribute
```
input = ""
output:
```python
from behave import given, when, then
from hamcrest import assert_that, is_
from company_employees import generate_data_file, post

@given(u'I prepare environment for tests run')
def step_impl(context):
	context.execute_steps('''
		Given I register an user with email "eve.holt@reqres.in" and "cityslicka"
		And I login with email "eve.holt@reqres.in" and "cityslicka"
	''')

@when(u'I try to register an user using only email "{email}"')
def step_impl(context, email):
	data = generate_data_file(email=email)
	context.response = post(context.base_url + "register", data=data)

@then(u'I verify that status code is "{status_code}"')
def step_impl(context, status_code):
	assert_that(context.response.status_code, is_(int(status_code)))

@then(u'I verify that response contains "{response}" as "{attribute}" attribute')
def step_impl(context, response, attribute):
	text = context.response.json()
	assert_that(text[str(attribute)], is_(str(response)))
```

id : seed_task_108
name : search list
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: Search employee list - search with token
	Given I prepare environment for tests run
	And I register an employee with name <name> and job <job>
	When I get employee list with page <page>
	Then I verify that status code is \"200\"
	Example: Platinum Client
	|name    |job          |page|
	|Morpheus|leader       |2   |
	|John    |zion resident|3   |
	|Maven   |Engineer     |4   |
	|Jack    |leader       |5   |
	|Lit     |zion resident|6   |
	|Marvel  |Engineer     |7   |
```
input = ""
output:
```python
from behave import given, when, then
from hamcrest import assert_that, is_
from company_employees import generate_data_file, post, get

@given(u'I prepare environment for tests run')
def step_impl(context):
    context.execute_steps('''\n\t\tGiven I register an user with email \"eve.holt@reqres.in\" and \"cityslicka\"\n\t\tAnd I login with email \"eve.holt@reqres.in\" and \"cityslicka\"\n\t''')
    
@given(u'I register an employee with name {name} and job {job}')
def step_impl(context, name, job):
    data = generate_data_file(name=name, job=job)
    context.response = post(context.base_url + "users", context.token, data)

@when(u'I get employee list with page {page}')
def step_impl(context, page):
    context.response = get(context.base_url + "users", token=context.token, page=page)
           
@then(u'I verify that status code is \"{status_code}\"')
def step_impl(context, status_code):
    assert_that(context.response.status_code, is_(int(status_code)))
```

id : seed_task_109
name : login ok
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: Login successful - post without token
	Given I register a user with email following data
		|email                                 |password|
		|mauricio.chaves.junior@live.com       |123456  |
		|mauricio.chaves.silva.junior@gmail.com|123456  |
	When I login with email "eve.holt@reqres.in" and "cityslicka"
	Then I verify that status code is "200"
```
input = ""
output:
```python
from behave import given, when, then
from hamcrest import assert_that, is_
from my_app import generate_data_file, post

@given(u'I register a user with email following data')
def step_impl(context ):
	for row in context.table:
		data = generate_data_file(email=row['email'], password=row['password'])
		context.response = post(context.base_url + "register", data=data)

@when(u'I login with email "{email}" and "{password}"')
def step_impl(context, email, password):
	data = generate_data_file(email=email, password=password)
	context.response = post(context.base_url + "login", data=data)
	context.token = context.response.json()['token']

@then(u'I verify that status code is "{status_code}"')
def step_impl(context, status_code):
	assert_that(context.response.status_code, is_(int(status_code)))
```

id : seed_task_110
name : login ko
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: Login unsuccessful
	Given I register a user with email following data
		|email                                 |password|
		|mauricio.chaves.junior@live.com       |123456  |
		|mauricio.chaves.silva.junior@gmail.com|123456  |
	When I login only with email "mauricio.chaves.silva.junior@gmail.com"
	Then I verify that status code is "400"
	And I verify that response contains "Missing password" as "error" attribute 
```
input = ""
output:
```python
from behave import given, when, then
from behave import given, when, then
from hamcrest import assert_that, is_
from my_app import generate_data_file, post

@given(u'I register a user with email following data')
def step_impl(context ):
	for row in context.table:
		data = generate_data_file(email=row['email'], password=row['password'])
		context.response = post(context.base_url + "register", data=data)

@when(u'I login only with email "{email}"')
def step_impl(context, email):
	data = generate_data_file(email=email)
	context.response = post(context.base_url + "login", data=data)

@then(u'I verify that status code is "{status_code}"')
def step_impl(context, status_code):
	assert_that(context.response.status_code, is_(int(status_code)))

@then(u'I verify that response contains "{response}" as "{attribute}" attribute')
def step_impl(context, response, attribute):
	text = context.response.json()
	assert_that(text[str(attribute)], is_(str(response)))
```

id : seed_task_111
name : buy
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: Proceed to Checkout
    Given I have added a product to the cart
    When I click proceed to checkout
    Then I should be directed to the shipping page
```
input = ""
output:
```python
from behave import given, when, then
from store import ShippingPageActions
@given(u'I have added a product to the cart')
def step_impl(context):
    # Assuming product is added to cart in previous steps
    assert context.page_object.is_product_added_to_cart(), "Product is not added to cart"

@when(u'I click proceed to checkout')
def step_impl(context):
    context.page_object.click_on_proceed_to_checkout()

@then(u'I should be directed to the shipping page')
def step_impl(context):
    context.page_object = ShippingPageActions(context.driver)
    assert context.page_object.is_shipping_page_displayed(), "Shipping page is not displayed"
```

id : seed_task_112
name : login try
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: When I try to login
	Given I am on Home Page
	And I click on sign in
	When I fill in the email field with the "mcsj123@teste.com" who is not registered
	Then System should display the message "Password is required."
```
input = ""
output:
```python
from behave import given, when, then
from hamcrest import assert_that, equal_to
from full_app import HomeActions, AuthenticationActions

@given(u'I am on Home Page')
def step_impl(context):
	context.page_object = HomeActions(context.driver)
	context.page_object.open_application(context.base_url)

@given(u'I click on sign in')
def step_impl(context):
	context.page_object.click_on_sign_in()

@when(u'I fill in the email field with the "{email}" who is not registered')
def step_impl(context, email):
	context.page_object = AuthenticationActions(context.driver)
	context.page_object.email_in(email)
	context.page_object.click_on_sign_in()

@then(u'System should display the message "{mensage}"')
def step_impl(context, mensage):
	assert_that(context.page_object.get_alert(), equal_to(mensage))
```

id : seed_task_113
name : forgot password
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: When I forget my username or password
	Given I clicked on the option I forgot my password
	When I click send without informing a user
	Then system should display the message "Informe o usuário"
	Then the title of the page should be "Esqueci minha senha"
	Then Help information "Preencha a informação abaixo para recuperar sua senha." should be displayed
```
input = ""
output:
```python
from behave import given, when, then
from hamcrest import assert_that, equal_to
from full_site_app import HomeActions, ForgotPasswordActions

@given(u'I clicked on the option I forgot my password')
def step_impl2(context):
	context.page_object = HomeActions(context.driver)
	context.page_object.click_on_forgot_password()

@when(u'I click send without informing a user')
def step_when2(context):
	context.page_object = ForgotPasswordActions(context.driver)
	context.page_object.click_on_send_button()

@then(u'system should display the message "{mensage}"')
def step_then2(context, mensage):
	context.page_object = ForgotPasswordActions(context.driver)
	assert_that(context.page_object.get_error_user(), equal_to(mensage))

@then(u'the title of the page should be "{mensage}"')
def step_when3(context, mensage):
	context.page_object = ForgotPasswordActions(context.driver)
	assert_that(context.page_object.get_title(), equal_to(mensage))

@then(u'Help information "{mensage}" should be displayed')
def step_when4(context, mensage):
	context.page_object = ForgotPasswordActions(context.driver)
	assert_that(context.page_object.get_help_mensage(), equal_to(mensage))
```

id : seed_task_114
name : json granule
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario Outline:
	Given a JSON message for a granule
	"""
	{
		"submission_id": 123,
		"files": [
			{
				"id": "tests/data/test_binary_file",
				"checksum": {
					"type": "MD5",
					"hash": "bacfc108148ce83e4c05d4c5b4f969e2"
				},
				"stored": false,
				"type": "SCIENCE"
			},
			{
				"id": "tests/data/test_text_file.txt",
				"checksum": {
					  "type": "MD5",
					"hash": "675c9d875973335dcdbb51bedd6e5ef5"
				},
				"stored": false,
				"type": "METADATA"
			}
		]
	}
	"""
	When we validate the <file_type> files in the granule against their checksums
	Then the granule validation will return a status of True
	And a message for <file> of "Success"
	Examples:
	  | file_type | file						  |
	  | SCIENCE   | tests/data/test_binary_file   |
	  | METADATA  | tests/data/test_text_file.txt |
```
input = ""
output:
```python
from behave import given, when, then
import json
from my_app.file import check_granule_files_of_type

@given("a JSON message for a granule")
def step_impl(context):
	context.granule = json.loads(context.text)

@when("we validate the {file_type} files in the granule against their checksums")
def step_impl(context, file_type):
	context.granule_status, context.file_statuses = check_granule_files_of_type(context.granule, file_type)

@then("the granule validation will return a status of True")
def step_impl(context):
	assert context.granule_status

@then('a message for {file} of "Success"')
def step_impl(context, file):
	assert file in context.file_statuses
	assert context.file_statuses[file] == (True, "Success")
```

id : seed_task_115
name : file checksum
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario Outline: Check a file against a checksum
	Given a file with path <file_path>
	And a checksum <checksum> of type <checksum_type>
	When we validate the contents of the file against the checksum
	Then the validation will return <status>
	And a message matching "<status_message_re>"

  Examples: MD5 Successes
	|file_path                    |checksum_type|status|status_message_re|checksum                        |
	|tests/data/test_text_file.txt|md5          |True  |Success          |675c9d875973335dcdbb51bedd6e5ef5|
	|tests/data/test_binary_file  |md5          |True  |Success          |bacfc108148ce83e4c05d4c5b4f969e2|

  Examples: SHA256 Successes
	|file_path                    |checksum_type|status|status_message_re|checksum                                                        |
	|tests/data/test_text_file.txt|sha256	    |True  |Success          |c364b31ba54903fb2c9ae4ab4ed3d9941b49b4185f6579c5a5959bbd77ddbde6|
	|tests/data/test_binary_file  |sha256	    |True  |Success          |71f9ebf3b491fb844934350e203ba31cd64d86a3dffdbe3aa5444df0d0b6d5a0|

  Examples: MD5 Failures
	|file_path                    |checksum_type|status|status_message_re                                    |checksum                        |
	|tests/data/test_text_file.txt|md5          |False |Computed checksum .*? does not match .*? for file .*?|aaa9d875973335dcdbb51bedd6e5ef5 |
	|tests/data/test_binary_file  |md5          |False |Computed checksum .*? does not match .*? for file .*?|aaafc108148ce83e4c05d4c5b4f969e2|
```
input = ""
output:
```python
from behave import given, when, then
import re
from crypto_app import check_file

@given('a file with path {file_path}')
def step_impl(context, file_path):
	context.file = file_path

@given('a checksum {checksum} of type {checksum_type}')
def step_impl(context, checksum, checksum_type):
	context.checksum = checksum
	context.checksum_type = checksum_type

@when('we validate the contents of the file against the checksum')
def step_impl(context):
	status, message = check_file(context.file, context.checksum_type, context.checksum)
	context.status = status
	context.status_message = message

@then('the validation will return {status}')
def step_impl(context, status):
	assert str(context.status) == status

@then('a message matching "{status_message_re}"')
def step_impl(context, status_message_re):
	assert re.match(status_message_re, context.status_message)
```

id : seed_task_116
name : non--existing route
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: Manage non existing route addition
	Given device "eth2" exists
	And route with destination "1.2.3.4/30" on device "eth2" does not exist
	When I add route with destination "1.2.3.4/30" on device "eth2"
	Then route with destination "1.2.3.4/30" on device "eth2" exists
	And no exception is raised
```
input = ""
output:
```python
from behave import given, when, then
from navigation_module import Device, Route

@given(u'device "{device_name}" exists')
def step_impl(context, device_name):
	device = None
	for dev in Device.discover():
		if dev.name == device_name:
			device = dev
	assert device is not None
	context.device = device

@given(u'route with destination "{destination}" on device "{device}" does not exist')
def step_impl(context, destination, device):
	route = Route(destination, device)
	if route.exists():
		route.delete()

@when(u'I add route with destination "{destination}" on device "{device}"')
def step_impl(context, destination, device):
	route = Route(destination, device)
	try:
		route.create()
	except Exception as e:
		context.exception = e

@then(u'route with destination "{destination}" on device "{device}" exists')
def step_impl(context, destination, device):
	route = Route(destination, device)
	assert route.exists()

@then(u'no exception is raised')
def step_impl(context):
	assert not hasattr(context, 'exception')
```

id : seed_task_117
name : existing route
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: Manage existing route addition
	Given device "eth2" exists
	And route with destination "1.2.3.4/30" on device "eth2" exists
	When I add route with destination "1.2.3.4/30" on device "eth2"
	Then an ObjectAlreadyExistsException is raised
```
input = ""
output:
```python
from behave import given, when, then
from navigation_module import Device, Route
from navigation_module.exception import ObjectAlreadyExistsException

@given(u'device "{device_name}" exists')
def step_impl(context, device_name):
	device = None
	for dev in Device.discover():
		if dev.name == device_name:
			device = dev
	assert device is not None   # TODO: create the device if necessary
	context.device = device

@given(u'route with destination "{destination}" on device "{device}" exists')
def step_impl(context, destination, device):
	route = Route(destination, device)
	if route not in Route.discover():
		route.create()

@when(u'I add route with destination "{destination}" on device "{device}"')
def step_impl(context, destination, device):
	route = Route(destination, device)
	try:
		route.create()
	except Exception as e:
		context.exception = e

@then(u'an ObjectAlreadyExistsException is raised')
def step_impl(context):
	assert isinstance(context.exception, ObjectAlreadyExistsException)
```

id : seed_task_118
name : n-e-route prohibition
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: Manage non existing route prohibition
	Given device "eth2" exists
	And route with destination "1.2.3.4/30" on device "eth2" does not exist
	When I prohibit route with destination "1.2.3.4/30" on device "eth2"
	Then route with destination "1.2.3.4/30" on device "eth2" exists
	And the route with destination "1.2.3.4/30" on device "eth2" is prohibited
	And no exception is raised
```
input = ""
output:
```python
import os
from behave import given, when, then
from navigation_module import Device, Route

@given(u'device "{device_name}" exists')
def step_impl(context, device_name):
	device = None
	for dev in Device.discover():
		if dev.name == device_name:
			device = dev
	assert device is not None   # TODO: create the device if necessary
	context.device = device

@given(u'route with destination "{destination}" on device "{device}" does not exist')
def step_impl(context, destination, device):
	route = Route(destination, device)
	if route.exists():
		route.delete()

@when(u'I prohibit route with destination "{destination}" on device "{device}"')
def step_impl(context, destination, device):
	route = Route(destination, device)
	try:
		route.prohibit()
	except Exception as e:
		context.exception = e

@then(u'the route with destination "{destination}" on device "{device}" is prohibited')
def step_impl(context, destination, device):
	route = Route(destination, device)
	route.refresh()
	assert route.is_prohibited()
	response = None
	try:
		response = os.system('ping -c 1 %s  2>/dev/null' % destination.split('/')[0])
	except:
		assert response == 2
	assert response is not None

@then(u'no exception is raised')
def step_impl(context):
	assert not hasattr(context, 'exception')
```

id : seed_task_119
name : e-route prohibition
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: Manage existing route prohibition
	Given device "eth2" exists
	And route with destination "1.2.3.4/30" on device "eth2" exists
	When I prohibit route with destination "1.2.3.4/30" on device "eth2"
	Then an ObjectAlreadyExistsException is raised
```
input = ""
output:
```python
from behave import given, when, then
from navigation_module import Device, Route
from navigation_module.exception import ObjectAlreadyExistsException

@given(u'device "{device_name}" exists')
def step_impl(context, device_name):
	device = None
	for dev in Device.discover():
		if dev.name == device_name:
			device = dev
	assert device is not None   # TODO: create the device if necessary
	context.device = device

@given(u'route with destination "{destination}" on device "{device}" exists')
def step_impl(context, destination, device):
	route = Route(destination, device)
	if route not in Route.discover():
		route.create()

@when(u'I prohibit route with destination "{destination}" on device "{device}"')
def step_impl(context, destination, device):
	route = Route(destination, device)
	try:
		route.prohibit()
	except Exception as e:
		context.exception = e

@then(u'an ObjectAlreadyExistsException is raised')
def step_impl(context):
	assert isinstance(context.exception, ObjectAlreadyExistsException)
```

id : seed_task_120
name : n-e-route unreachable
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: Manage non existing route unreachable
	Given device "eth2" exists
	And route with destination "1.2.3.4/30" on device "eth2" does not exist
	When I unreachable route with destination "1.2.3.4/30" on device "eth2"
	Then route with destination "1.2.3.4/30" on device "eth2" exists
	And the route with destination "1.2.3.4/30" on device "eth2" is unreachable
	And no exception is raised
```
input = ""
output:
```python
from behave import given, when, then
from navigation_module import Device, Route
from navigation_module.exception import ObjectAlreadyExistsException

@given(u'device "{device_name}" exists')
def step_impl(context, device_name):
	device = None
	for dev in Device.discover():
		if dev.name == device_name:
			device = dev
	assert device is not None
	context.device = device

@given(u'route with destination "{destination}" on device "{device}" does not exist')
def step_impl(context, destination, device):
	route = Route(destination, device)
	if route.exists():
		route.delete()

@when(u'I unreachable route with destination "{destination}" on device "{device}"')
def step_impl(context, destination, device):
	route = Route(destination, device)
	try:
		route.unreachable()
	except Exception as e:
		context.exception = e

@then(u'route with destination "{destination}" on device "{device}" exists')
def step_impl(context, destination, device):
	route = Route(destination, device)
	assert route.exists()

@then(u'the route with destination "{destination}" on device "{device}" is unreachable')
def step_impl(context, destination, device):
	route = Route(destination, device)
	route.refresh()
	assert not route.is_reachable()
	response = None
	try:
		response = os.system('ping -c 1 %s  2>/dev/null' % destination.split('/')[0])
	except:
		assert response == 2
	assert response is not None

@then(u'no exception is raised')
def step_impl(context):
	assert not hasattr(context, 'exception')
```

id : seed_task_121
name : e-route unreachable
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: Manage existing route unreachable
	Given device "eth2" exists
	And route with destination "1.2.3.4/30" on device "eth2" exists
	When I unreachable route with destination "1.2.3.4/30" on device "eth2"
	Then an ObjectAlreadyExistsException is raised
```
input = ""
output:
```python
from behave import given, when, then
from navigation_module import Device, Route
from navigation_module.exception import ObjectAlreadyExistsException

@given(u'device "{device_name}" exists')
def step_impl(context, device_name):
	device = None
	for dev in Device.discover():
		if dev.name == device_name:
			device = dev
	assert device is not None   # TODO: create the device if necessary
	context.device = device

@given(u'route with destination "{destination}" on device "{device}" exists')
def step_impl(context, destination, device):
	route = Route(destination, device)
	if route not in Route.discover():
		route.create()

@when(u'I unreachable route with destination "{destination}" on device "{device}"')
def step_impl(context, destination, device):
	route = Route(destination, device)
	try:
		route.unreachable()
	except Exception as e:
		context.exception = e

@then(u'an ObjectAlreadyExistsException is raised')
def step_impl(context):
	assert isinstance(context.exception, ObjectAlreadyExistsException)
```

id : seed_task_122
name : namespace creation 1
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: Manage non existing namespaces creation
	Given namespace "creation" does not exist
	When I create a namespace "creation"
	Then namespace "creation" exists
	And no exception is raised
```
input = ""
output:
```python
from behave import given, when, then
from my_application.namespace import Namespace

@given(u'namespace "{namespace_name}" does not exist')
def step_impl(context, namespace_name):
	namespace = Namespace(namespace_name)
	if namespace in Namespace.discover():
		namespace.delete()

@when(u'I create a namespace "{namespace_name}"')
def step_impl(context, namespace_name):
	namespace = Namespace(namespace_name)
	try:
		namespace.create()
	except Exception as e:
		context.exception = e

@then(u'namespace "{namespace_name}" exists')
def step_impl(context, namespace_name):
	namespace = Namespace(namespace_name)
	assert namespace.exists()

@then(u'no exception is raised')
def step_impl(context):
	assert not hasattr(context, 'exception')
```

id : seed_task_123
name : namespace creation 2
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: Manage existing namespaces creation
	Given namespace "creation" exists
	When I create a namespace "creation"
	Then an ObjectAlreadyExistsException is raised
```
input = ""
output:
```python
from behave import given, when, then
from my_application.namespace import Namespace
from my_application.exceptions import ObjectAlreadyExistsException

@given(u'namespace "{namespace_name}" exists')
def step_impl(context, namespace_name):
	namespace = Namespace(namespace_name)
	if namespace not in Namespace.discover():
		namespace.create()

@when(u'I create a namespace "{namespace_name}"')
def step_impl(context, namespace_name):
	namespace = Namespace(namespace_name)
	try:
		namespace.create()
	except Exception as e:
		context.exception = e

@then(u'an ObjectAlreadyExistsException is raised')
def step_impl(context):
	assert isinstance(context.exception, ObjectAlreadyExistsException)
```

id : seed_task_124
name : delete namespace
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: Manage existing namespaces deletion
	Given namespace "deletion" exists
	When I delete namespace "deletion"
	Then namespace "deletion" does not exist
```
input = ""
output:
```python
from behave import given, when, then
from my_application.namespace import Namespace

@given(u'namespace "{namespace_name}" exists')
def step_impl(context, namespace_name):
	namespace = Namespace(namespace_name)
	if namespace not in Namespace.discover():
		namespace.create()

@when(u'I delete namespace "{namespace_name}"')
def step_impl(context, namespace_name):
	namespace = Namespace(namespace_name)
	try:
		namespace.delete()
	except Exception as e:
		context.exception = e

@then(u'namespace "{namespace_name}" does not exist')
def step_impl(context, namespace_name):
	namespace = Namespace(namespace_name)
	assert not namespace.exists()
```

id : seed_task_125
name : delete fail
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: Manage non existing namespaces deletion
	Given namespace "deletion" does not exist
	When I delete namespace "deletion"
	Then an ObjectNotFoundException is raised
```
input = ""
output:
```python
from behave import given, when, then
from my_application.namespace import Namespace
from my_application.exceptions import ObjectNotFoundException

@given(u'namespace "{namespace_name}" does not exist')
def step_impl(context, namespace_name):
	namespace = Namespace(namespace_name)
	if namespace in Namespace.discover():
		namespace.delete()

@when(u'I delete namespace "{namespace_name}"')
def step_impl(context, namespace_name):
	namespace = Namespace(namespace_name)
	try:
		namespace.delete()
	except Exception as e:
		context.exception = e

@then(u'an ObjectNotFoundException is raised')
def step_impl(context):
	assert isinstance(context.exception, ObjectNotFoundException)
```

id : seed_task_126
name : namespace discovery
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: Manage namespace discovery
	Given namespace "namespace1" exists
	And namespace "namespace2" exists
	When I discover namespaces
	Then discovered namespaces contains "namespace1"
	And discovered namespaces contains "namespace2"
	And discovered namespaces contains default namespace
```
input = ""
output:
```python
from behave import given, when, then
from my_application.namespace import Namespace

@given(u'namespace "{namespace_name}" exists')
def step_impl(context, namespace_name):
	namespace = Namespace(namespace_name)
	if namespace not in Namespace.discover():
		namespace.create()

@when(u'I discover namespaces')
def step_impl(context):
	context.discovered = Namespace.discover()

@then(u'discovered namespaces contains "{namespace_name}"')
def step_impl(context, namespace_name):
	assert Namespace(namespace_name) in context.discovered

@then(u'discovered namespaces contains default namespace')
def step_impl(context):
	assert Namespace('') in context.discovered
```

id : seed_task_127
name : landing screen
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: Landing Screen
	Given I am on the page with relative url "/"
	Then I should be directly redirected to the page with relative url "/landing/"
```
input = ""
output:
```python
import time
from urllib.parse import urljoin
from behave import given, then

@given('I am on (?:the )?page with relative url "(?P<url>.*)"')
def step_impl(context, url):
	full_url = urljoin(context.config.server_url, url)
	context.browser.visit(full_url)

@then('I should be directly redirected to the page with relative url "(?P<url>.*)"')
def step_impl(context, not_, url):
	time.sleep(1)
	full_url = urljoin(context.config.server_url, url)
	if not_:
		assert not context.browser.url == full_url, "Expected not to be on page %s, instead got %s" % (full_url, context.browser.url)
	else:
		assert context.browser.url == full_url, "Expected to be on page %s, instead got %s" % (full_url, context.browser.url)
```

id : seed_task_128
name : api screen
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: API Home Screen
	Given I am on the page with relative url "/api/"
	Then I should see the text "Api Root"
```
input = ""
output:
```python
from urllib.parse import urljoin
from behave import given, then

@given('I am on (?:the )?page with relative url "(?P<url>.*)"')
def step_impl(context, url):
	full_url = urljoin(context.config.server_url, url)
	context.browser.visit(full_url)

@then('I should (?P<not_>not )?see (?:the )?text "(?P<text>.*)"')
def step_impl(context, not_, text):
	if not_:
		assert not context.browser.is_text_present(text)
	else:
		assert context.browser.is_text_present(text)
```

id : seed_task_129
name : select text
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: User picks a text
	Given user is on page with lists of texts
	When user clicks on a text
	Then user is redirected to the first page containing incorrect words
```
input = ""
output:
```python
from behave import given, when, then

@given('user is on page with lists of texts')
def step_impl(context):
    context.browser.get("http://localhost:8000/edit")

@when('user clicks on a text')
def step_impl(context):
    context.browser.find_element_by_id('text_to_click').click()

@then('user is redirected to the first page containing incorrect words')
def step_impl(context):
    # This assertion ensures that at least one incorrect word is present on the page
    assert context.browser.find_element_by_css_selector('.incorrect-word'), "No incorrect words found on the page"
```

id : seed_task_130
name : server 1
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: Http server responds through proxy
	Given server started with '--workers=1 0 proxy web:80'
	When client connects
	And client sends 'GET / HTTP/1.0\r\n\r\n'
	Then client receives 'Hello, this is a web server'
```
input = ""
output:
```python
import subprocess
import re
import shlex
import select
import socket
from behave import given, when, then

@given(u'server started with \'{cmd}\'')
def step_impl(context, cmd):
	context.server = subprocess.Popen(shlex.split('./malunas ' + cmd), stdout = subprocess.PIPE, stderr = subprocess.PIPE, bufsize = 1)
	poller = select.poll()
	poller.register(context.server.stderr, select.POLLIN)
	poll_result = poller.poll(TIMEOUT)
	if poll_result:
		line = context.server.stderr.readline()
		m = re.compile(r'^malunas: Listening on 0.0.0.0:(?P<port>\d+)').match(line) 
		context.port = int(m.group('port'))
	assert(context.server.poll() is None), 'server died: %s' % context.server.stderr.read(100) 

@when(u'client connects')
def step_impl(context):
	context.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server_address = ('localhost', context.port)
	context.client.connect(server_address)

@when(u'client sends \'{msg}\'')
def step_impl(context, msg):
	context.client.send(msg.decode('unicode-escape'))

@then(u'client receives \'{msg}\'')
def step_impl(context, msg):
	context.client.settimeout(TIMEOUT)
	resp = ''
	while True:
		part = context.client.recv(100)
		if not part:
			break
		resp = resp + part
	found  = re.search(msg, resp) is not None
	assert(found), "Response does not match '%s', in '%s'" % (msg, resp)
```

id : seed_task_131
name : server 2
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: one worker can only serve one client at a time
	Given server started with '--workers=1 0 exec python scripts/program.py'
	When client connects
	And second client connects
	And program handles the request
	Then program does not handle request
```
input = ""
output:
```python
import subprocess
import re
import shlex
import select
import socket
from behave import given, when, then

@given(u'server started with \'{cmd}\'')
def step_impl(context, cmd):
	context.server = subprocess.Popen(shlex.split('./malunas ' + cmd), stdout = subprocess.PIPE, stderr = subprocess.PIPE, bufsize = 1)
	poller = select.poll()
	poller.register(context.server.stderr, select.POLLIN)
	poll_result = poller.poll(TIMEOUT)
	if poll_result:
		line = context.server.stderr.readline()
		m = re.compile(r'^malunas: Listening on 0.0.0.0:(?P<port>\d+)').match(line) 
		context.port = int(m.group('port'))
	assert(context.server.poll() is None), 'server died: %s' % context.server.stderr.read(100) 

@when(u'client connects')
def step_impl(context):
	context.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server_address = ('localhost', context.port)
	context.client.connect(server_address)

@when(u'second client connects')
def step_impl(context):
	context.second_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server_address = ('localhost', context.port)
	context.second_client.connect(server_address)

@when(u'program handles the request')
def step_impl(context):
	connection, client_address = context.pm.accept()
	context.control_socket = connection

@then(u'program does not handle request')
def step_impl(context):
	try:
		connection, client_address = context.pm.accept()
		context.control_socket = connection
	except socket.timeout:
		return
	assert(False), 'A program handles a request but that is not expected'
```

id : seed_task_132
name : kalibro configuration
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: one kalibro configuration
	Given I have a kalibro configuration with name "Java"
	When I get all the kalibro configurations
	Then I should get a list with the given kalibro configuration
```
input = ""
output:
```python
from kalibro.models import KalibroConfigurationFactory, KalibroConfiguration
from nose.tools import assert_in
from behave import given, when, then

@given(u'I have a kalibro configuration with name "{}"')
def step_impl(context, kalibro_configuration_name):
	context.kalibro_configuration = KalibroConfigurationFactory.build(name=kalibro_configuration_name)
	context.kalibro_configuration.save()

@when(u'I get all the kalibro configurations')
def step_impl(context):
	context.all_kalibro_configurations = KalibroConfiguration.all()

@then(u'I should get a list with the given kalibro configuration')
def step_impl(context):
	assert_in(context.kalibro_configuration, context.all_kalibro_configurations)
```

id : seed_task_133
name : kalibro destruction
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: destroying a kalibro configuration
	Given I have a kalibro configuration with name "Java"
	When I destroy the kalibro configuration
	Then the kalibro configuration should no longer exist
```
input = ""
output:
```python
from kalibro.models import KalibroConfigurationFactory, KalibroConfiguration
from behave import given, when, then

@given(u'I have a kalibro configuration with name "{}"')
def step_impl(context, kalibro_configuration_name):
	context.kalibro_configuration = KalibroConfigurationFactory.build(name=kalibro_configuration_name)
	context.kalibro_configuration.save()

@when(u'I destroy the kalibro configuration')
def step_impl(context):
	context.kalibro_configuration.delete()

@then(u'the kalibro configuration should no longer exist')
def step_impl(context):
	assert(not KalibroConfiguration.exists(context.kalibro_configuration.id))
```

id : seed_task_134
name : kalibro metric
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: one metric configuration
	Given I have a kalibro configuration with name "Java"
	And the kalibro configuration has a metric configuration
	When I list all the metric configurations of the kalibro configuration
	Then I should get a list with the given metric configuration
```
input = ""
output:
```python
from behave import given, when, then
from nose.tools import assert_in
from kalibro.metrics import MetricConfigurationFactory

@given(u'the kalibro configuration has a metric configuration')
def step_impl(context):
	context.metric_configuration = MetricConfigurationFactory.build(kalibro_configuration_id=context.kalibro_configuration.id)
	context.metric_configuration.save()

@when(u'I list all the metric configurations of the kalibro configuration')
def step_impl(context):
	context.metric_configurations = context.kalibro_configuration.metric_configurations()

@then(u'I should get a list with the given metric configuration')
def step_impl(context):
	assert_in(context.metric_configuration, context.metric_configurations)
```

id : seed_task_135
name : kalibro hotspot
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin 
Scenario: get a list of all hotspot metric configurations of some kalibro configuration
	Given I have a kalibro configuration with name "Kalibro for Java"
	And I have a hotspot metric configuration within the given kalibro configuration
	When I request for hotspot_metric_configurations of the given kalibro configuration
	Then I should get a list with the given HotspotMetricConfiguration
```
input = ""
output:
```python
from behave import given, when, then
from nose.tools import assert_in
from kalibro.models import KalibroConfigurationFactory, HotspotMetricFactory, MetricConfigurationFactory

@given(u'I have a kalibro configuration with name "{}"')
def step_impl(context, kalibro_configuration_name):
	context.kalibro_configuration = KalibroConfigurationFactory.build(name=kalibro_configuration_name)
	context.kalibro_configuration.save()

@given(u'I have a hotspot metric configuration within the given kalibro configuration')
def step_impl(context):
	context.metric = HotspotMetricFactory.build()
	context.hotspot_metric_configuration = MetricConfigurationFactory.build(kalibro_configuration_id=context.kalibro_configuration.id, metric=context.metric)
	context.hotspot_metric_configuration.save()

@when(u'I request for hotspot_metric_configurations of the given kalibro configuration')
def step_impl(context):
	context.hotspot_metric_configurations = context.kalibro_configuration.hotspot_metric_configurations()

@then(u'I should get a list with the given HotspotMetricConfiguration')
def step_impl(context):
	assert_in(context.hotspot_metric_configuration, context.hotspot_metric_configurations)
```

id : seed_task_136
name : kalibro tree-metric
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: get a list of all metric configurations of some kalibro configuration
	Given I have a kalibro configuration with name "Kalibro for Java"
	And I have a reading group with name "Group"
	And I have a tree metric configuration within the given kalibro configuration
	When I request for tree_metric_configurations of the given kalibro configuration
	Then I should get a list with the given TreeMetricConfiguration
```
input = ""
output:
```python
from behave import given, when, then
from nose.tools import assert_in
from kalibro.models import KalibroConfigurationFactory, ReadingGroupFactory

@given(u'I have a kalibro configuration with name "{}"')
def step_impl(context, kalibro_configuration_name):
	context.kalibro_configuration = KalibroConfigurationFactory.build(name=kalibro_configuration_name)
	context.kalibro_configuration.save()

@given(u'I have a reading group with name "{}"')
def step_impl(context, reading_group_name):
	context.reading_group = ReadingGroupFactory.build(name=reading_group_name)
	context.reading_group.save()

@given(u'I have a tree metric configuration within the given kalibro configuration')
def step_impl(context):
	context.execute_steps(u'Given I have a loc configuration within the given kalibro configuration')
	context.tree_metric_configuration = context.metric_configuration

@when(u'I request for tree_metric_configurations of the given kalibro configuration')
def step_impl(context):
	context.tree_metric_configurations = context.kalibro_configuration.tree_metric_configurations()

@then(u'I should get a list with the given TreeMetricConfiguration')
def step_impl(context):
	assert_in(context.tree_metric_configuration, context.tree_metric_configurations)
```

id : seed_task_137
name : find range
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: find a valid range
	Given I have a kalibro configuration with name "Java" with metric configuration
	And I have a reading group with name "Group"
	And I have a reading and a range within the given reading group
	When I search a range with the same id of the given range
	Then it should return the same range as the given one
```
input = ""
output:
```python
from behave import given, when, then
from kalibro.models import (
    KalibroConfigurationFactory,
    ReadingGroupFactory,
    MetricConfigurationFactory,
    KalibroRangeFactory,
    ReadingFactory,
    KalibroRange
)
from hamcrest import assert_that, equal_to

@given(u'I have a kalibro configuration with name "{}" with metric configuration')
def step_impl(context, kalibro_configuration_name):
	context.kalibro_configuration = KalibroConfigurationFactory.build(name=kalibro_configuration_name)
	context.kalibro_configuration.save()
    context.metric_configuration = MetricConfigurationFactory.build(kalibro_configuration_id=context.kalibro_configuration.id)
	context.metric_configuration.save()

@given(u'I have a reading group with name "{}"')
def step_impl(context, reading_group_name):
	context.reading_group = ReadingGroupFactory.build(name=reading_group_name)
	context.reading_group.save()

@given(u'I have a reading and a range within the given reading group')
def step_impl(context):
	context.reading = ReadingFactory.build(reading_group_id=context.reading_group.id
	context.reading.save()
    context.range = KalibroRangeFactory.build(reading_id=context.reading.id, metric_configuration_id=context.metric_configuration.id, beginning=1.1, end=5.1)

@when(u'I search a range with the same id of the given range')
def step_impl(context):
	context.found_range = KalibroRange.find(int(context.range.id))

@then(u'it should return the same range as the given one')
def step_impl(context):
	assert_that(context.found_range, equal_to(context.range))
```

id : seed_task_138
name : inexistent range
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin 
Scenario: With an inexistent range
	Given I have a kalibro configuration with name "Java"
	And I have a reading group with name "Group"
	And I have a metric configuration within the given kalibro configuration
	When I ask ranges of the given metric configuration
	Then I should get an empty list
```
input = ""
output:
```python
from behave import given, when, then
from kalibro.models import (
    KalibroConfigurationFactory,
    ReadingGroupFactory,
    MetricConfigurationFactory,
    KalibroRangeFactory,
    ReadingFactory,
    KalibroRange
)
from hamcrest import assert_that, equal_to

@given(u'I have a kalibro configuration with name "{}"')
def step_impl(context, kalibro_configuration_name):
	context.kalibro_configuration = KalibroConfigurationFactory.build(name=kalibro_configuration_name)
	context.kalibro_configuration.save()

@given(u'I have a reading group with name "{}"')
def step_impl(context, reading_group_name):
	context.reading_group = ReadingGroupFactory.build(name=reading_group_name)
	context.reading_group.save()

@given(u'I have a metric configuration within the given kalibro configuration')
def step_impl(context):
	context.metric_configuration = MetricConfigurationFactory.build(kalibro_configuration_id=context.kalibro_configuration.id)
	context.metric_configuration.save()

@when(u'I ask ranges of the given metric configuration')
def step_impl(context):
	context.response = KalibroRange.ranges_of(context.metric_configuration.id)

@then(u'I should get an empty list')
def step_impl(context):
    assert_that(len(context.response), equal_to(0))
```

id : seed_task_139
name : list metric
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: get a list of all metric configurations of some kalibro configuration
	Given I have a kalibro configuration with name "Kalibro for Java"
	And I have a reading group with name "Group"
	And I have a metric configuration within the given kalibro configuration
	When I request all metric configurations of the given kalibro configuration
	Then I should get a list of its metric configurations
```
input = ""
output:
```python
from behave import given, when, then
from kalibro.models import KalibroConfigurationFactory, ReadingGroupFactory, MetricConfigurationFactory, MetricConfiguration
from nose.tools import assert_in

@given(u'I have a kalibro configuration with name "{}"')
def step_impl(context, kalibro_configuration_name):
	context.kalibro_configuration = KalibroConfigurationFactory.build(name=kalibro_configuration_name)
	context.kalibro_configuration.save()

@given(u'I have a reading group with name "{}"')
def step_impl(context, reading_group_name):
	context.reading_group = ReadingGroupFactory.build(name=reading_group_name)
	context.reading_group.save()

@given(u'I have a metric configuration within the given kalibro configuration')
def step_impl(context):
	context.metric_configuration = MetricConfigurationFactory.build(kalibro_configuration_id=context.kalibro_configuration.id)
	context.metric_configuration.save()

@when(u'I request all metric configurations of the given kalibro configuration')
def step_impl(context):
	context.metric_configurations = MetricConfiguration.metric_configurations_of(context.kalibro_configuration.id)

@then(u'I should get a list of its metric configurations')
def step_impl(context):
	assert_in(context.metric_configuration, context.metric_configurations)
```

id : seed_task_140
name : inexistent metric
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: get an empty list for a kalibro configuration without metric configurations
	Given I have a kalibro configuration with name "Kalibro for Java"
	When I request all metric configurations of the given kalibro configuration
	Then I should get an empty list of metric configurations
```
input = ""
output:
```python
from behave import given, when, then
from kalibro.models import KalibroConfigurationFactory, MetricConfiguration
from nose.tools import assert_equal

@given(u'I have a kalibro configuration with name "{}"')
def step_impl(context, kalibro_configuration_name):
	context.kalibro_configuration = KalibroConfigurationFactory.build(name=kalibro_configuration_name)
	context.kalibro_configuration.save()

@when(u'I request all metric configurations of the given kalibro configuration')
def step_impl(context):
	context.metric_configurations = MetricConfiguration.metric_configurations_of(context.kalibro_configuration.id)

@then(u'I should get an empty list of metric configurations')
def step_impl(context):
	assert_equal(len(context.metric_configurations), 0)
```

id : seed_task_141
name : project
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: one project
	Given I have a project with name "Kalibro"
	When I ask for all the projects
	Then I should get a list with the given project
```
input = ""
output:
```python
from behave import given, when, then
from kalibro.models import Project
from nose.tools import assert_in

@given(u'I have a project with name "{}"')
def step_impl(context, project_name):
	context.execute_steps(u'When I create the project with name "{}"'.format(project_name))

@when(u'I ask for all the projects')
def step_impl(context):
	context.all_projects = Project.all()

@then(u'I should get a list with the given project')
def step_impl(context):
	assert_in(context.project, context.all_projects)
```

id : seed_task_142
name : project destruction
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: destroy an existing project
	Given I have a project with name "Kalibro"
	When I destroy the project with the same id of the given project
	Then the project should no longer exist
```
input = ""
output:
```python
from behave import given, when, then
from kalibro.models import Project

@given(u'I have a project with name "{}"')
def step_impl(context, project_name):
	context.execute_steps(u'When I create the project with name "{}"'.format(project_name))

@when(u'I destroy the project with the same id of the given project')
def step_impl(context):
	context.found_project = Project.find(context.project.id)
	context.found_project.delete()

@then(u'the project should no longer exist')
def step_impl(context):
	assert(not Project.exists(context.found_project.id))
```

id : seed_task_143
name : cancel processing
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin 
Scenario: With one repository
	Given I have a project with name "Kalibro"
	And I have a kalibro configuration with name "Conf"
	And the given project has the following Repositories:
	  |name   |scm_type|address                                        |
	  |Kalibro|GIT     |https://github.com/mezuro/kalibro_processor.git|
	When I call the process method for the given repository
	And I call the cancel_process method for the given repository
	Then I should get success
```
input = ""
output:
```python
from behave import given, when, then
from kalibro.models import KalibroConfigurationFactory, RepositoryFactory

@given(u'I have a project with name "{}"')
def step_impl(context, project_name):
	context.execute_steps(u'When I create the project with name "{}"'.format(project_name))

@given(u'I have a kalibro configuration with name "{}"')
def step_impl(context, kalibro_configuration_name):
	context.kalibro_configuration = KalibroConfigurationFactory.build(name=kalibro_configuration_name)
	context.kalibro_configuration.save()

@given(u'the given project has the following Repositories')
def step_impl(context):
	row = dict(zip(context.table.headings, context.table[0].cells))
	context.repository = RepositoryFactory.build(project_id=context.project.id, kalibro_configuration_id=context.kalibro_configuration.id, **row)
	context.repository.save()

@when(u'I call the processing method for the given repository')
def step_impl(context):
	context.response = context.repository.processing()

@when(u'I call the cancel_process method for the given repository')
def step_impl(context):
	context.response = context.repository.cancel_processing_of_a_repository()

@then(u'I should get success')
def step_impl(context):
	assert("errors" not in context.response)
```

id : seed_task_144
name : ghpages
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin 
Scenario: Make ghpages
	Given a configured git repo with a Kramdown draft
	When make "ghpages" is run
	Then it succeeds
	And a branch is created called "gh-pages" containing "index.html"
	And documents are added to gh-pages
```
input = ""
output:
```python
from behave import given, when, then
from subprocess import call, check_output
from contextlib import contextmanager
import os
from glob import glob

@contextmanager
def cd(newdir):
    prevdir = os.getcwd()
    os.chdir(os.path.expanduser(newdir))
    try:
        yield
    finally:
        os.chdir(prevdir)

def run_with_capture(context, command):
    context.result = call(command)

@given(u'a configured git repo with a Kramdown draft')
def step_impl(context):
	context.execute_steps(u'Given a git repo with a single Kramdown draft')
	with cd(context.working_dir):
		context.result = call(["make", "-f", "lib/setup.mk"])

@when(u'make "{target}" is run')
def step_impl(context, target):
	run_with_capture(context, ["make", target])

@then(u'it succeeds')
def step_impl(context):
	assert context.result == 0

@then(u'a branch is created called "{branch}" containing "{filename}"')
def step_impl(context, branch, filename):
	with cd(context.working_dir):
		files = check_output(["git", "ls-tree", branch, "--name-only", "-r"] ).decode("utf-8")
	assert filename in files

@then(u'documents are added to gh-pages')
def step_impl(context):
	with cd(context.working_dir):
		md_files = glob("draft-*.md")
		ghpages_files = check_output(["git", "ls-tree", "gh-pages", "--name-only", "-r"] ).decode("utf-8")
		for md in md_files:
			txt_file = md.replace(".md", ".txt")
			html_file = md.replace(".md", ".html")
			assert txt_file in ghpages_files
			assert html_file in ghpages_files
```

id : seed_task_145
name : pre-commit blocked
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: Git pre-commit hook blocks broken drafts
	Given a configured git repo with a Kramdown draft
	When the draft is broken
	And git commit is run
	Then it fails
```
input = ""
output:
```python
from behave import given, when, then
from subprocess import call
from glob import glob
import fileinput
from git_module import git_commit, run_with_capture, cd

@given(u'a configured git repo with a Kramdown draft')
def step_impl(context):
	context.execute_steps(u'Given a git repo with a single Kramdown draft')
	with cd(context.working_dir):
		context.result = call(["make", "-f", "lib/setup.mk"])

@when(u'the draft is broken')
def step_impl(context):
	with cd(context.working_dir):
		break_this_file = glob("draft-*.md")[0]
		with fileinput.input(files=break_this_file, inplace=True) as inFile:
			for line in inFile:
				if "RFC2119:" not in line:
					print(line, end='')
		context.broken_file = break_this_file

@when(u'git commit is run')
def step_impl(context):
	with cd(context.working_dir):
		run_with_capture(context, git_commit + ["-am", "Committing broken draft"])

@then(u'it fails')
def step_impl(context):
	assert context.result != 0
```

id : seed_task_146
name : pre-commit unblocked
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: git pre-commit hook does not block other drafts
	Given a configured git repo with multiple Kramdown drafts
	When the draft is broken
	And a non-broken draft is committed
	Then it succeeds
```
input = ""
output:
```python
from behave import given, when, then
from subprocess import call
from glob import glob
import fileinput
from git_module import git_commit, run_with_capture, cd

@given(u'a configured git repo with a Kramdown draft')
def step_impl(context):
	context.execute_steps(u'Given a git repo with a single Kramdown draft')
	with cd(context.working_dir):
		context.result = call(["make", "-f", "lib/setup.mk"])

@when(u'the draft is broken')
def step_impl(context):
	with cd(context.working_dir):
		break_this_file = glob("draft-*.md")[0]
		with fileinput.input(files=break_this_file, inplace=True) as inFile:
			for line in inFile:
				if "RFC2119:" not in line:
					print(line, end='')
		context.broken_file = break_this_file

@when(u'a non-broken draft is committed')
def step_impl(context):
	with cd(context.working_dir):
		drafts = glob("draft-*.md")
		drafts.remove(context.broken_file)
		commit_this_file = drafts[0]
		with open(commit_this_file, "a") as update:
			update.write("# One more appendix\n\nCan you see me?\n")
		call(["git", "add", commit_this_file])
		run_with_capture(context, git_commit + ["-m", "Only the non-broken file"])
```

id : seed_task_147
name : no draft
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: Run setup script on directory with no draft
	Given an empty git repo
	And lib is cloned in
	When the setup script is run
	Then it fails
	And generates a message "Create a draft file"
```
input = ""
output:
```python
from behave import given, when, then
import os
from tempfile import mkdtemp
from subprocess import call
from manager_system import cd, run_with_capture

@given(u'an empty git repo')
def step_impl(context):
	context.test_dir = os.getcwd()
	context.working_dir = mkdtemp()
	context.origin_dir = mkdtemp()
	with cd(context.origin_dir):
		call(["git", "init"])
		# Need to checkout another branch so that pushes to master work.
		call(["git", "checkout", "-b", "testing"])
	with cd(context.working_dir):
		call(["git", "clone", context.origin_dir, "."])
		call(["git", "config", "user.name", "Behave Tests"])
		call(["git", "config", "user.email", "behave@example.com"])

@given(u'lib is cloned in')
def step_impl(context):
	with cd(context.working_dir):
		call(["ln", "-s", context.test_dir, "lib"])

@when(u'the setup script is run')
def step_impl(context):
	run_with_capture(context, ["make", "-f", "lib/setup.mk"])

@then(u'it fails')
def step_impl(context):
	assert context.result != 0

@then(u'generates a message "{text}"')
def step_impl(context, text):
	assert context.error.find(text) != -1
```

id : seed_task_148
name : no origin remote
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: Run setup script on directory with no origin remote
	Given a git repo with no origin
	And lib is cloned in
	And a Kramdown draft is created
	When the setup script is run
	Then it fails
	And generates a message "remote"
```
input = ""
output:
```python
from behave import given, when, then
import os
import random
from tempfile import mkdtemp
from subprocess import call
from manager_system import cd, run_with_capture

@given(u'a git repo with no origin')
def step_impl(context):
	context.test_dir = os.getcwd()
	context.working_dir = mkdtemp()
	with cd(context.working_dir):
		call(["git", "init"])
		call(["git", "config", "user.name", "Behave Tests"])
		call(["git", "config", "user.email", "behave@example.com"])

@given(u'lib is cloned in')
def step_impl(context):
	with cd(context.working_dir):
		call(["ln", "-s", context.test_dir, "lib"])

@given(u'a Kramdown draft is created')
def step_impl(context):
	with cd(context.working_dir):
		random_string = ''.join(random.SystemRandom().choice(string.ascii_lowercase) for n in range(8))
		draft_name = "draft-behave-" + random_string
		file_name = draft_name + ".md"
		with open(file_name, "wb") as newFile:
			call(["sed", "-e", "s/draft-hartke-xmpp-stupid/{}/".format(draft_name), "lib/doc/example.md"], stdout=newFile)
		call(["git", "add", file_name])
		call(["git", "commit", "-am", "Initial commit of {}".format(draft_name)])

@when(u'the setup script is run')
def step_impl(context):
	run_with_capture(context, ["make", "-f", "lib/setup.mk"])

@then(u'it fails')
def step_impl(context):
	assert context.result != 0

@then(u'generates a message "{text}"')
def step_impl(context, text):
	assert context.error.find(text) != -1
```

id : seed_task_149
name : log management 1
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: An authenticated user creates a new log
	Given that the user has valid credentials
	And the user makes a POST request to /login
	When the user tries to create a new log
	Then the log should be available at the returned url
	And the log should be listed at the /logs endpoint
```
input = ""
output:
```python
import requests
from behave import given, when, then
@given(u'that the user has valid credentials')
def step_impl(context):
	global TEST_USER_CREATED
	if not TEST_USER_CREATED:
		#Create a user and store the credentials
		response = requests.post(BASE_URL + '/users/', json={
			'captcha_token': '123',
			'username': 'agos',
			'display_name': 'Cary Agos',
			'password': 'startanotherfirm',
		})
		assert response.ok
		TEST_USER_CREATED = True
	context.username = 'agos'
	context.password = 'startanotherfirm'

@given(u'the user makes a POST request to /login')
def step_impl(context):
	response = requests.post(BASE_URL + '/login/', json={
		'username': context.username,
		'password': context.password,
	})
	if response.ok:
		access_token = response.json().get('access_token')
		context.access_token = access_token
	else:
		context.access_token = None

@when(u'the user tries to create a new log')
def step_impl(context):
	response = requests.post(BASE_URL + '/logs/', headers={'Authorization': 'tinylog ' + context.access_token, }, json={'name': 'Project named partner', 'description': 'My attempts to found my own firm',},)
	assert response.ok
	context.log_url = response.json().get('_link')

@then(u'the log should be available at the returned url')
def step_impl(context):
	response = requests.get(context.log_url, headers={'Authorization': 'tinylog ' + context.access_token,})
	assert response.ok
	expected_response = {'_link': context.log_url, 'name': 'Project named partner', 'description': 'My attempts to found my own firm', 'entries': [],}
	actual_response = response.json()
	assert expected_response == actual_response

@then(u'the log should be listed in the parent log object')
def step_impl(context):
	response = requests.get(context.log_url, headers={'Authorization': 'tinylog ' + context.access_token,})
	assert any([entry['_link'] == context.entry_url for entry in response.json().get('entries')])
```

id : seed_task_150
name : log management 2
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: An authenticated user creates a new log entry
	Given that the user has valid credentials
	And the user makes a POST request to /login
	And the user tries to create a new log
	When the user tries to create a new log entry
	Then the log entry should be available at the returned url
	And the log should be listed in the parent log object
```
input = ""
output:
```python
import os
import requests
from behave import given, when, then
@given(u'that the user has valid credentials')
def step_impl(context):
	global TEST_USER_CREATED
	if not TEST_USER_CREATED:
		#Create a user and store the credentials
		response = requests.post(BASE_URL + '/users/', json={
			'captcha_token': '123',
			'username': 'agos',
			'display_name': 'Cary Agos',
			'password': 'startanotherfirm',
		})
		assert response.ok
		TEST_USER_CREATED = True
	context.username = 'agos'
	context.password = 'startanotherfirm'

@given(u'the user makes a POST request to /login')
def step_impl(context):
	response = requests.post(BASE_URL + '/login/', json={
		'username': context.username,
		'password': context.password,
	})
	if response.ok:
		access_token = response.json().get('access_token')
		context.access_token = access_token
	else:
		context.access_token = None

@given(u'the user tries to create a new log')
def step_impl(context):
	response = requests.post(BASE_URL + '/logs/', headers={'Authorization': 'tinylog ' + context.access_token, }, json={'name': 'Project named partner', 'description': 'My attempts to found my own firm',},)
	assert response.ok
	context.log_url = response.json().get('_link')

@when(u'the user tries to create a new log entry')
def step_impl(context):
    response = requests.post(
        os.path.join(context.log_url, 'entries/'),
        headers={
            'Authorization': 'tinylog ' + context.access_token,
        },
        json={
            'title': 'Brick Walls',
            'description': 'Check out that old t-shirt factory',
        },
    )
    assert response.ok
    context.entry_url = response.json().get('_link')

@then(u'the log should be available at the returned url')
def step_impl(context):
	response = requests.get(context.log_url, headers={'Authorization': 'tinylog ' + context.access_token,})
	assert response.ok
	expected_response = {'_link': context.log_url, 'name': 'Project named partner', 'description': 'My attempts to found my own firm', 'entries': [],}
	actual_response = response.json()
	assert expected_response == actual_response

@then(u'the log should be listed in the parent log object')
def step_impl(context):
	response = requests.get(context.log_url, headers={'Authorization': 'tinylog ' + context.access_token,})
	assert any([
		entry['_link'] == context.entry_url 
		for entry in response.json().get('entries')
	])
```

id : seed_task_151
name : logout
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: A currently logged in user logs out
	Given that the user has valid credentials
	And the user makes a POST request to /login
	When the user makes a POST request to /logout
	Then the access token should not be valid
```
input = ""
output:
```python
import requests
from behave import given, when, then
@given(u'that the user has valid credentials')
def step_impl(context):
	global TEST_USER_CREATED
	if not TEST_USER_CREATED:
		#Create a user and store the credentials
		response = requests.post(BASE_URL + '/users/', json={
			'captcha_token': '123',
			'username': 'agos',
			'display_name': 'Cary Agos',
			'password': 'startanotherfirm',
		})
		assert response.ok
		TEST_USER_CREATED = True
	context.username = 'agos'
	context.password = 'startanotherfirm'

@given(u'the user makes a POST request to /login')
def step_impl(context):
	response = requests.post(BASE_URL + '/login/', json={
		'username': context.username,
		'password': context.password,
	})
	if response.ok:
		access_token = response.json().get('access_token')
		context.access_token = access_token
	else:
		context.access_token = None
@when(u'the user makes a POST request to /logout')
def step_impl(context):
	response = requests.post(BASE_URL + '/logout/', headers={'Authorization': 'tinylog ' + context.access_token,})
	assert response.ok

@then(u'the access token should not be valid')
def step_impl(context):
	response = requests.get(BASE_URL + '/current-user/', headers={'Authorization': 'tinylog ' + context.access_token,})
	assert not response.ok
```

id : seed_task_152
name : account creation
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: A new user account is successfully created
	Given that no account with the desired username exists
	And the client has correctly solved the captcha
	When a post request is made to the /users resource
	Then the new user should be listed under the /users resource
	And the new user should be available at their /user/<username> url
```
input = ""
output:
```python
import requests
from behave import given, when, then
@given(u'that no account with the desired username exists')
def step_impl(context):
	pass # No need to do anything here

@given(u'the client has correctly solved the captcha')
def step_impl(context):
	captcha_challenge = requests.get(BASE_URL + '/captcha-challenge').json()
	assert len(captcha_challenge) > 0

@when(u'a post request is made to the /users resource')
def step_impl(context):
	# Normally, this would be given by the captcha provider on success but when testing a dummy token is used since, by design, the captcha cannot be solved automatically!
	captcha_token = "DUMMY_CAPTCHA_TOKEN"
	response = requests.post(BASE_URL + '/users/', json={
		'captcha_token': captcha_token,
		'username': 'pflorrick',
		'display_name': 'Old Pete',
		'password': 'onthecampaigntrail',
	})
	assert response.ok

@then(u'the new user should be listed under the /users resource')
def step_impl(context):
	response = requests.get(BASE_URL + '/users/')
	assert response.ok
	assert any([
		user['username'] == 'pflorrick'
		for user in response.json().get('users', [])
	])

@then(u'the new user should be available at their /user/<username> url')
def step_impl(context):
	response = requests.get(BASE_URL + '/users/pflorrick/')
	assert response.ok
	expected_response = {
		"_link": BASE_URL + "/users/pflorrick", 
		"display_name": "Old Pete", 
		"username": "pflorrick"
	}
	actual_response = response.json()
	assert expected_response == actual_response
```

id : seed_task_153
name : fix 1
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: rdopkg fix - did not add description of changes
	Given a distgit repository exists
	When I execute the rdopkg command "fix"
	Then the rdopkg state file should be generated
```
input = ""
output:
```python
import os
from behave import given, when, then
from rdopkg import run

@given('a distgit repository exists')
def step_impl(context):
	context.execute_steps(u'Given a distgit at Version 1.2.3 and Release 2')

@when('I execute the rdopkg command {args}')
def step_impl(context, args):
	# proper argument parsing might be needed
	cmd = ['rdopkg'] + args.split(' ')
	context.command_output = run(*cmd, fatal=False, log_fail=False)

@then(u'the rdopkg state file should be generated')
def step_check_for_rdopkg_state_file_not_present(context):
	assert os.path.exists(os.path.join(context.distgitdir, STATE_FILE_FN))
```

id : seed_task_154
name : fix 2
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: rdopkg fix - Normal semver nvr bumps consistently
	Given a distgit at Version 2.0.0 and Release 0.1
	When I run rdopkg "fix"
	Then .spec file tag Release is 0.2%{?dist}
```
input = ""
output:
```python
from behave import given, when, then
from rdopkg import run, _create_distgit, specfile

@given('a distgit at Version {version} and Release {release}')
def step_impl(context, version, release):
	_create_distgit(context, version, release)

@when('I run rdopkg {args}')
def step_impl(context, args):
	# proper argument parsing might be needed
	cmd = ['rdopkg'] + args.split(' ')
	context.command_output = run(*cmd, fatal=False, log_fail=False)

@then('.spec file tag {tag} is {value}')
def step_impl(context, tag, value):
	spec = specfile.Spec()
	assert spec.get_tag(tag) == value, "{0} != {1}".format(spec.get_tag(tag), value)
```

id : seed_task_155
name : show dataset
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin 
Scenario: 1-step showing dataset
	Given a dataset is available
	When the show command is called
	Then an image should pop up
```
input = ""
output:
```python
from behave import given, when, then
from my_app.models import DataArray, Scene
from unittest.mock import patch

@given("a dataset is available")
def step_impl_create_scene_one_dataset(context):
	"""Create a Scene with a fake dataset for testing.
	Args: context (behave.runner.Context): Test context
	"""
	from xarray import DataArray
	from satpy import Scene
	scn = Scene()
	scn["MyDataset"] = DataArray([[1, 2], [3, 4]], dims=["y", "x"])
	context.scene = scn

@when("the show command is called")
def step_impl_scene_show(context):
	"""Call the Scene.show method.
	Args: context (behave.runner.Context): Test context
	"""
	with patch("trollimage.xrimage.XRImage.show") as mock_show:
		context.scene.show("MyDataset")
		mock_show.assert_called_once_with()

@then("an image should pop up")
def step_impl_image_pop_up(context):
	"""Check that a image window pops up (no-op currently).
	Args: context (behave.runner.Context): Test context
	"""
```

id : seed_task_156
name : save dataset
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: 1-step saving dataset
	Given a dataset is available
	When the save_dataset command is called
	Then a file should be saved on disk
```
input = ""
output:
```python
from behave import given, when, then
from my_app.models import DataArray, Scene

@given("a dataset is available")
def step_impl_create_scene_one_dataset(context):
	"""Create a Scene with a fake dataset for testing.
	Args: context (behave.runner.Context): Test context
	"""
	from xarray import DataArray
	from satpy import Scene
	scn = Scene()
	scn["MyDataset"] = DataArray([[1, 2], [3, 4]], dims=["y", "x"])
	context.scene = scn

@when("the save_dataset command is called")
def step_impl_save_dataset_to_png(context):
	"""Run Scene.save_dataset to create a PNG image.
	Args: context (behave.runner.Context): Test context
	"""
	context.filename = "/tmp/test_dataset.png"
	context.scene.save_dataset("MyDataset", context.filename)

@then("a file should be saved on disk")
def step_impl_file_exists_and_remove(context):
	"""Check that a file exists on disk and then remove it.
	Args: context (behave.runner.Context): Test context
	"""
	import os
	assert os.path.exists(context.filename)
	os.remove(context.filename)
```

id : seed_task_157
name : save datasets
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: 1-step saving all datasets
	Given a bunch of datasets are available
	When the save_datasets command is called
	Then a bunch of files should be saved on disk
```
input = ""
output:
```python
from behave import given, when, then
from my_app.models import DataArray, Scene

@given("a bunch of datasets are available")
def step_impl_create_scene_two_datasets(context):
	"""Create a Scene with two fake datasets for testing.
	Args: context (behave.runner.Context): Test context
	"""
	from xarray import DataArray
	from satpy import Scene
	scn = Scene()
	scn["MyDataset"] = DataArray([[1, 2], [3, 4]], dims=["y", "x"])
	scn["MyDataset2"] = DataArray([[5, 6], [7, 8]], dims=["y", "x"])
	context.scene = scn

@when("the save_datasets command is called")
def step_impl_save_datasets(context):
	"""Run Scene.save_datsets to create PNG images.
	Args: context (behave.runner.Context): Test context
	"""
	context.scene.save_datasets(writer="simple_image", filename="{name}.png")

@then("a bunch of files should be saved on disk")
def step_impl_check_two_pngs_exist(context):
	"""Check that two PNGs exist.
	Args: context (behave.runner.Context): Test context
	"""
	import os
	for filename in ["MyDataset.png", "MyDataset2.png"]:
		assert os.path.exists(filename)
		os.remove(filename)
```

id : seed_task_158
name : load dataset
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: 1-step data loading
	Given data is available
	When user loads the data without providing a config file
	Then the data is available in a scene object
```
input = ""
output:
```python
from behave import given, when, then
import os
from urllib.request import urlopen
from my_app.models import DataArray, Scene
from datetime import datetime
from satpy import Scene, find_files_and_readers

@given(u"data is available")
def step_impl_data_available(context):
	if not os.path.exists("/tmp/SVM02_npp_d20150311_t1122204_e1123446_b17451_c20150311113206961730_cspp_dev.h5"):
		response = urlopen("https://zenodo.org/record/16355/files/"
				"SVM02_npp_d20150311_t1122204_e1123446_b17451_c20150311113206961730_cspp_dev.h5")
		with open("/tmp/SVM02_npp_d20150311_t1122204_e1123446_b17451_c20150311113206961730_cspp_dev.h5", mode="w") as fp:
			fp.write(response.read())
	if not os.path.exists("/tmp/GMTCO_npp_d20150311_t1122204_e1123446_b17451_c20150311113205873710_cspp_dev.h5"):
		response = urlopen("https://zenodo.org/record/16355/files/"
				"GMTCO_npp_d20150311_t1122204_e1123446_b17451_c20150311113205873710_cspp_dev.h5")
		with open("/tmp/GMTCO_npp_d20150311_t1122204_e1123446_b17451_c20150311113205873710_cspp_dev.h5", mode="w") as fp:
			fp.write(response.read())

@when(u"user loads the data without providing a config file")
def step_impl_user_loads_no_config(context):
	from datetime import datetime
	from satpy import Scene, find_files_and_readers
	os.chdir("/tmp/")
	readers_files = find_files_and_readers(sensor="viirs", start_time=datetime(2015, 3, 11, 11, 20), end_time=datetime(2015, 3, 11, 11, 26))
	scn = Scene(filenames=readers_files)
	scn.load(["M02"])
	context.scene = scn

@then(u"the data is available in a scene object")
def step_impl_data_available_in_scene(context):
	assert context.scene["M02"] is not None
	assert context.scene.get("M01") is None
```

id : seed_task_159
name : meta data missing
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: No crash when metadata is missing
	Given data is available
	When user loads the data without providing a config file
	And some items are not available
	Then the data is available in a scene object
```
input = ""
output:
```python
from behave import given, when, then
import os
from urllib.request import urlopen
from my_app.models import DataArray, Scene
from datetime import datetime
from satpy import Scene, find_files_and_readers

@given(u"data is available")
def step_impl_data_available(context):
	if not os.path.exists("/tmp/SVM02_npp_d20150311_t1122204_e1123446_b17451_c20150311113206961730_cspp_dev.h5"):
		response = urlopen("https://zenodo.org/record/16355/files/"
				"SVM02_npp_d20150311_t1122204_e1123446_b17451_c20150311113206961730_cspp_dev.h5")
		with open("/tmp/SVM02_npp_d20150311_t1122204_e1123446_b17451_c20150311113206961730_cspp_dev.h5", mode="w") as fp:
			fp.write(response.read())
	if not os.path.exists("/tmp/GMTCO_npp_d20150311_t1122204_e1123446_b17451_c20150311113205873710_cspp_dev.h5"):
		response = urlopen("https://zenodo.org/record/16355/files/"
				"GMTCO_npp_d20150311_t1122204_e1123446_b17451_c20150311113205873710_cspp_dev.h5")
		with open("/tmp/GMTCO_npp_d20150311_t1122204_e1123446_b17451_c20150311113205873710_cspp_dev.h5", mode="w") as fp:
			fp.write(response.read())

@when(u"user loads the data without providing a config file")
def step_impl_user_loads_no_config(context):
	from datetime import datetime
	from satpy import Scene, find_files_and_readers
	os.chdir("/tmp/")
	readers_files = find_files_and_readers(sensor="viirs", start_time=datetime(2015, 3, 11, 11, 20), end_time=datetime(2015, 3, 11, 11, 26))
	scn = Scene(filenames=readers_files)
	scn.load(["M02"])
	context.scene = scn

@when(u"some items are not available")
def step_impl_items_not_available(context):
	context.scene.load(["M01"])

@then(u"the data is available in a scene object")
def step_impl_data_available_in_scene(context):
	assert context.scene["M02"] is not None
	assert context.scene.get("M01") is None
```

id : seed_task_160
name : data explorable
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: Data is explorable
	Given data is available
	When user wants to know what data is available
	Then available datasets is returned
```
input = ""
output:
```python
from behave import given, when, then
import os
from urllib.request import urlopen
from my_app.models import DataArray, Scene
from datetime import datetime
from satpy import Scene, find_files_and_readers

@given(u"data is available")
def step_impl_data_available(context):
	if not os.path.exists("/tmp/SVM02_npp_d20150311_t1122204_e1123446_b17451_c20150311113206961730_cspp_dev.h5"):
		response = urlopen("https://zenodo.org/record/16355/files/"
				"SVM02_npp_d20150311_t1122204_e1123446_b17451_c20150311113206961730_cspp_dev.h5")
		with open("/tmp/SVM02_npp_d20150311_t1122204_e1123446_b17451_c20150311113206961730_cspp_dev.h5", mode="w") as fp:
			fp.write(response.read())
	if not os.path.exists("/tmp/GMTCO_npp_d20150311_t1122204_e1123446_b17451_c20150311113205873710_cspp_dev.h5"):
		response = urlopen("https://zenodo.org/record/16355/files/"
				"GMTCO_npp_d20150311_t1122204_e1123446_b17451_c20150311113205873710_cspp_dev.h5")
		with open("/tmp/GMTCO_npp_d20150311_t1122204_e1123446_b17451_c20150311113205873710_cspp_dev.h5", mode="w") as fp:
			fp.write(response.read())

@when(u"user wants to know what data is available")
def step_impl_user_checks_availability(context):
	from datetime import datetime
	from satpy import Scene, find_files_and_readers
	os.chdir("/tmp/")
	reader_files = find_files_and_readers(sensor="viirs", start_time=datetime(2015, 3, 11, 11, 20), end_time=datetime(2015, 3, 11, 11, 26))
	scn = Scene(filenames=reader_files)
	context.available_dataset_ids = scn.available_dataset_ids()

@then(u"available datasets are returned")
def step_impl_available_datasets_are_returned(context):
	assert (len(context.available_dataset_ids) >= 5)
```

id : seed_task_161
name : accessing data
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: Accessing datasets by name prefers less modified datasets
	Given datasets with the same name
	When a dataset is retrieved by name
	Then the least modified version of the dataset is returned
```
input = ""
output:
```python
from behave import given, when, then

@given("datasets with the same name")
def step_impl_datasets_with_same_name(context):
	from xarray import DataArray
	from satpy import Scene
	from satpy.tests.utils import make_dataid
	scn = Scene()
	scn[make_dataid(name="ds1", calibration="radiance")] = DataArray([[1, 2], [3, 4]])
	scn[make_dataid(name="ds1", resolution=500, calibration="reflectance")] = DataArray([[5, 6], [7, 8]])
	scn[make_dataid(name="ds1", resolution=250, calibration="reflectance")] = DataArray([[5, 6], [7, 8]])
	scn[make_dataid(name="ds1", resolution=1000, calibration="reflectance")] = DataArray([[5, 6], [7, 8]])
	scn[make_dataid(name="ds1", resolution=500, calibration="radiance", modifiers=("mod1",))] = \
	DataArray([[5, 6], [7, 8]])
	ds_id = make_dataid(name="ds1", resolution=1000, calibration="radiance", modifiers=("mod1", "mod2"))
	scn[ds_id] = DataArray([[5, 6], [7, 8]])
	context.scene = scn

@when("a dataset is retrieved by name")
def step_impl_dataset_retrieved_by_name(context):
	context.returned_dataset = context.scene["ds1"]

@then("the least modified version of the dataset is returned")
def step_impl_least_modified_dataset_returned(context):
	assert len(context.returned_dataset.attrs["modifiers"]) == 0
```

id : seed_task_162
name : basic scoring
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: Basic scoring
	Given we have an initialized game with two teams
	And the current ball color is white
	When the team 1 scores a goal
	Then the team 1 should have a score of 1 points
	And the team 2 should have a score of 0 points
```
input = ""
output:
```python
from behave import given, when, then
from game.models import Team, Ball, Game

@given(u'we have an initialized game with two teams')
def step_impl(context):
	player_list = ['Player ' + str(i) for i in range(1,5)]
	team1 = Team(*player_list[0:2])
	team2 = Team(*player_list[2:4])
	context.game = Game(team1, team2)

@given(u'the current ball color is {ball_color}')
def step_impl(context, ball_color):
	context.game.set_current_ball(Ball.from_color(ball_color))

@when(u'the team {team_id:d} scores a goal')
def step_impl(context, team_id):
	context.game.score_goal(team_id)

@then(u'the team {team_id:d} should have a score of {points:d} points')
def step_impl(context, team_id, points):
	if team_id == 1:
		assert context.game.score.team1 == points
	else:
		assert context.game.score.team2 == points
```

id : seed_task_163
name : advanced scoring
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: Advanced scoring with single color ball
	Given we have an initialized game with two teams
	And the next sequence of score actions:
	  | team | ball   |
	  | 1	 | white  |
	  | 2	 | white  |
	  | 1	 | white  |
	Then the team 1 should have a score of 2 points
	And the team 2 should have a score of 1 points
```
input = ""
output:
```python
from behave import given, then
from game.models import Team, Ball, Game

@given(u'we have an initialized game with two teams')
def step_impl(context):
	player_list = ['Player ' + str(i) for i in range(1,5)]
	team1 = Team(*player_list[0:2])
	team2 = Team(*player_list[2:4])
	context.game = Game(team1, team2)

@given(u'the next sequence of score actions')
def step_impl(context):
	for row in context.table:
		context.game.set_current_ball(Ball.from_color(row['ball']))
		context.game.score_goal(int(row['team']))

@then(u'the team {team_id:d} should have a score of {points:d} points')
def step_impl(context, team_id, points):
	if team_id == 1:
		assert context.game.score.team1 == points
	else:
		assert context.game.score.team2 == points
```

id : seed_task_164
name : game completion
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: Game completion
	Given we have an initialized game with two teams
	And the team 1 has a score of 9 points
	And the team 2 has a score of 9 points
	When the team 1 scores a goal
	Then the game is over
	And the winner team is the team 1
```
input = ""
output:
```python
from behave import given, when, then
from game.models import Team, Game

@given(u'we have an initialized game with two teams')
def step_impl(context):
	player_list = ['Player ' + str(i) for i in range(1,5)]
	team1 = Team(*player_list[0:2])
	team2 = Team(*player_list[2:4])
	context.game = Game(team1, team2)

@given(u'the team {team:d} has a score of {points:d} points')
def step_impl(context, team, points):
	if team == 1:
		context.game.score.team1 = points
	else:
		context.game.score.team2 = points

@when(u'the team {team_id:d} scores a goal')
def step_impl(context, team_id):
	context.game.score_goal(team_id)

@then(u'the game is over')
def step_impl(context):
	assert context.game.is_over()

@then(u'the winner team is the team {team:d}')
def step_impl(context, team):
	assert context.game.get_winner() == team
```

id : seed_task_165
name : stop scoring
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: Stop scoring when ten goals reached
	Given we have an initialized game with two teams
	And the team 1 has a score of 9 points
	And the team 2 has a score of 0 points
	When the team 1 scores a goal
	And the team 1 scores a goal
	Then the game is over
	And the team 1 should have a score of 10 points
```
input = ""
output:
```python
from behave import given, when, then
from game.models import Team, Game

@given(u'we have an initialized game with two teams')
def step_impl(context):
	player_list = ['Player ' + str(i) for i in range(1,5)]
	team1 = Team(*player_list[0:2])
	team2 = Team(*player_list[2:4])
	context.game = Game(team1, team2)

@given(u'the team {team:d} has a score of {points:d} points')
def step_impl(context, team, points):
	if team == 1:
		context.game.score.team1 = points
	else:
		context.game.score.team2 = points

@when(u'the team {team_id:d} scores a goal')
def step_impl(context, team_id):
	context.game.score_goal(team_id)

@then(u'the game is over')
def step_impl(context):
	assert context.game.is_over()

@then(u'the team {team_id:d} should have a score of {points:d} points')
def step_impl(context, team_id, points):
	if team_id == 1:
		assert context.game.score.team1 == points
	else:
		assert context.game.score.team2 == points
```

id : seed_task_166
name : blue ball
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: Auto goal with a blue ball
	Given we have an initialized game with two teams
	And the team 1 has a score of 1 points
	And the current ball color is blue
	When the team 1 scores an autogoal
	Then the team 1 should have a score of -1 points
```
input = ""
output:
```python
from behave import given, when, then
from game.models import Team, Ball, Game

@given(u'we have an initialized game with two teams')
def step_impl(context):
	player_list = ['Player ' + str(i) for i in range(1,5)]
	team1 = Team(*player_list[0:2])
	team2 = Team(*player_list[2:4])
	context.game = Game(team1, team2)

@given(u'the team {team:d} has a score of {points:d} points')
def step_impl(context, team, points):
	if team == 1:
		context.game.score.team1 = points
	else:
		context.game.score.team2 = points

@given(u'the current ball color is {ball_color}')
def step_impl(context, ball_color):
	context.game.set_current_ball(Ball.from_color(ball_color))

@when(u'the team {team:d} scores an autogoal')
def step_impl(context, team):
	context.game.score_goal(team, auto_goal=True)

@then(u'the team {team_id:d} should have a score of {points:d} points')
def step_impl(context, team_id, points):
	if team_id == 1:
		assert context.game.score.team1 == points
	else:
		assert context.game.score.team2 == points
```

id : seed_task_167
name : create game
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: Game from scratch
	Given we have an empty game
	And the game score is reset
	And we have team 1 with players player1 and player2
	And we have team 2 with players player3 and player4
	When we add the team 1 to the game
	And we add the team 2 to the game
	Then the team 1 should have a score of 0 points
	And the team 2 should have a score of 0 points
```
input = ""
output:
```python
from behave import given, when, then
from game.models import Team, Game

@given(u'we have an empty game')
def step_impl(context):
	context.game = Game()
	context.teams = {}

@given(u'the game score is reset')
def step_impl(context):
	context.game.reset_score()

@given(u'we have team {team_id:d} with players {player1} and {player2}')
def step_impl(context, team_id, player1, player2):
	if team_id == 1:
		context.team1 = Team(player1, player2)
	elif team_id == 2:
		context.team2 = Team(player1, player2)
	else:
		raise ValueError("team_id should be 1 or 2")

@when(u'we add the team {team_id:d} to the game')
def step_impl(context, team_id):
	if team_id == 1:
		context.game.set_team1(context.team1)
	elif team_id == 2:
		context.game.set_team2(context.team2)
	else:
		raise ValueError("team_id should be 1 or 2")

@then(u'the team {team_id:d} should have a score of {points:d} points')
def step_impl(context, team_id, points):
	if team_id == 1:
		assert context.game.score.team1 == points
	else:
		assert context.game.score.team2 == points
```

id : seed_task_168
name : mopa detection
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: Simple mopa detection
	Given we have an initialized game with two teams
	And the team 1 has a score of 9 points
	And the team 2 has a score of 0 points
	When the team 1 scores a goal
	Then the game is over
	And the winner team is the team 1
	And the team 1 is mopper
	And the team 2 is mopped
	And the game is a mopa
```
input = ""
output:
```python
from behave import given, when, then
from game.models import Team, Game

@given(u'we have an initialized game with two teams')
def step_impl(context):
	player_list = ['Player ' + str(i) for i in range(1,5)]
	team1 = Team(*player_list[0:2])
	team2 = Team(*player_list[2:4])
	context.game = Game(team1, team2)

@given(u'the team {team:d} has a score of {points:d} points')
def step_impl(context, team, points):
	if team == 1:
		context.game.score.team1 = points
	else:
		context.game.score.team2 = points

@when(u'the team {team_id:d} scores a goal')
def step_impl(context, team_id):
	context.game.score_goal(team_id)

@then(u'the game is over')
def step_impl(context):
	assert context.game.is_over()

@then(u'the winner team is the team {team:d}')
def step_impl(context, team):
	assert context.game.get_winner() == team

@then(u'the team {team:d} is mopped')
def step_impl(context, team):
	if team == 1:
		assert context.game.score.team1 == 0 and context.game.score.team2 == 10
	else:
		assert context.game.score.team1 == 10 and context.game.score.team2 == 0

@then(u'the game is a mopa')
def step_impl(context):
	assert context.game.is_mopa()
```

id : seed_task_169
name : validate links
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: Social network validation
	Given that I'm on the home page
	When I click on Contact
	Then I validate the social media links
```
input = ""
output:
```python
from behave import given, when, then
import time

@given(u'that I'm on the home page')
def step_impl(context):
	url = 'http://localhost:8000/'
	context.browser.visit(url)
	time.sleep(3)

@when(u'I click on Contact')
def step_impl(context):
	context.browser.find_by_css(CONTACT).click()
	time.sleep(2)

@then(u'I validate social media links')
def step_impl(context):
	context.browser.find_by_css(FACEBOOK).visible
	context.browser.find_by_css(TWITTER).visible
	context.browser.find_by_css(INSTAGRAM).visible
	context.browser.find_by_css(BEHANCE).visible
	context.browser.find_by_css(DRIBBBLE).visible
```

id : seed_task_170
name : standard info
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario Outline: print information to standard output in verbose mode
	Given I start dummy-brightnessd
	And I have a directory "device"
	And I have a file "device/in_illuminance_input" with the content "<ambient>"
	When I run ambientlightd with the device "device" and argument "--verbose"
	Then I expect the string "read ambient value <ambient>" on stdout from ambientlightd
	And I expect the string "write brightness value <brightness>" on stdout from ambientlightd
	Examples:
		|ambient|brightness|
		|  25000|       100|
		|      1|        10|
		| 100000|       100|
		|  10000|        46|
		|   1000|        14|
		|      0|        10|
```
input = ""
output:
```python
import os
from behave import given, when, then
from main_system import startApplication, waitForDbusService, writeFileContent, output

@given(u'I start dummy-brightnessd')
def step_impl(context):
	path = os.path.dirname(os.path.realpath(__file__))
	context.brightnessd = startApplication(context, ['python', path + '/dummy-brightnessd.py'])
	waitForDbusService()

@given(u'I have a directory "{directory}"')
def step_impl(context, directory):
	os.makedirs(context.tmpdir + '/' + directory)

@given(u'I have a file "{filename}" with the content ""')
def step_impl(context, filename):
	writeFileContent(context, filename, "")

@when(u'I run ambientlightd with the device "{device}" and argument "{arg1}"')
def step_impl(context, device, arg1):
	device = context.tmpdir + '/' + device
	context.ambientlightd = startApplication(context, ['ambientlightd', '--session', '--single', '--device=' + device, arg1])
	context.ambientlightd.wait()
	context.stdout = context.ambientlightd.stdout.read()
	context.stderr = context.ambientlightd.stderr.read()

@then(u'I expect the string "{text}" on stderr from ambientlightd')
def step_impl(context, text):
	assert context.stderr.find(text) != -1, 'expected to see "' + text + '", got: \n' + output
```

id : seed_task_171
name : print error
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: ambientlightd prints an error when the ambient light sensor is not available
	Given I start dummy-brightnessd
	When I run ambientlightd with the argument "--device=/sys/not-here"
	Then I expect the string "file "/sys/not-here/in_illuminance_input" not found" on stderr from ambientlightd
```
input = ""
output:
```python
import os
from behave import given, when, then
from main_system import startApplication, waitForDbusService, output

@given(u'I start dummy-brightnessd')
def step_impl(context):
	path = os.path.dirname(os.path.realpath(__file__))
	context.brightnessd = startApplication(context, ['python', path + '/dummy-brightnessd.py'])
	waitForDbusService()

@when(u'I run ambientlightd with the argument "{arg1}"')
def step_impl(context, arg1):
	context.ambientlightd = startApplication(context, ['ambientlightd', '--session', arg1])
	context.ambientlightd.wait()
	context.stdout = context.ambientlightd.stdout.read()
	context.stderr = context.ambientlightd.stderr.read()

@then(u'I expect the string "{text}" on stderr from ambientlightd')
def step_impl(context, text):
	assert context.stderr.find(text) != -1, 'expected to see "' + text + '", got: \n' + output
```

id : seed_task_172
name : brightness
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario Outline: actual and requested brightness are equal
	Given I have a directory "/sys/test/backlight"
	And I have a file "/sys/test/backlight/brightness" with the content "<expected>"
	And I have a file "/sys/test/backlight/actual_brightness" with the content "<actual>"
	When I run checkbrightness with the device "/sys/test/backlight" and argument "--command=false"
	Then I expect no output on stderr from checkbrightness
	And I expect no output on stdout from checkbrightness
	And checkbrightness exits with the error code 0
	Examples:
		|expected|actual|
		|       0|     0|
		|      27|    27|
		|     100|   100|
		|   65432| 65432|
```
input = ""
output:
```python
from behave import given, when, then
import os
from main_system import startApplication

@given(u'I have a directory "{directory}"')
def step_impl(context, directory):
	os.makedirs(context.tmpdir + '/' + directory)

@given(u'I have a file "{filename}" with the content "{content}"')
def writeFileContent(context, filename, content):
	filename = context.tmpdir + '/' + filename
	file = open(filename, 'w+')
	file.write(content)
	file.close()

@when(u'I run checkbrightness with the device "{device}" and argument "{arg1}"')
def step_impl(context, device, arg1):
	device = context.tmpdir + '/' + device
	context.checkbrightness = startApplication(context, ['checkbrightness', '--device=' + device, arg1])
	context.checkbrightness.wait()

@then(u'I expect no output on stdout from brightnessd')
def step_impl(context):
	output = context.brightnessd_stdout
	assert output == "", 'expected not putput, got: \n' + output

@then(u'I expect no output on stderr from checkbrightness')
def step_impl(context):
	output = context.checkbrightness.stderr.read()
	assert output == "", 'expected not putput, got: \n' + output

@then(u'checkbrightness exits with the error code {expected:d}')
def step_impl(context, expected):
	code = context.checkbrightness.returncode
	assert code == expected, 'expected to see "' + str(expected) + '", got: ' + str(code)
```

id : seed_task_173
name : birth date
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: enter date of birth
	Given date of birth tag exists
	When date of birth tag found
	Then I can enter date of birth
```
input = ""
output:
```python
from behave import given, when, then
@given("date of birth tag exists")
def step_impl(context):
	assert (context.tester.date_of_birth_tag_exists() == True)

@when("date of birth tag found")
def step_impl(context):
	context.tester.get_date_of_birth_tag()

@then("I can enter date of birth")
def step_impl(context):
	context.tester.fill_date_of_birth_tag()
```

id : seed_task_174
name : contact error
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: Invalid email validation
	Given as long as I am in Contact
	When I fill in the invalid email
	Then I validate the error message
```
input = ""
output:
```python
from behave import given, when, then
import time

@given(u'that I am in Contact')
def step_impl(context):
	url = 'http://localhost:8000/#contact'
	context.browser.visit(url)

@when(u'fill in invalid email')
def step_impl(context):
	email = 'teste@a.com'
	context.browser.find_by_css(EMAIL).fill(email)
	context.browser.find_by_css(SUBMIT).click()
	time.sleep(2)

@then(u'validate the error message')
def step_impl(context):
	message = 'is an invalid email address and cannot be imported.'
	assert message in context.browser.find_by_css(MSG).value
```
