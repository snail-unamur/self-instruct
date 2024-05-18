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
	When  I switch the blender on
	Then  it should transform into "apple juice"
```
input = ""
output:
```python
from behave import given, when, then
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
name : ko_3
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework :
```gherkin
Scenario: Authorization verification
	When action target not found
	Then it should fail when action target not found
	When action target found
	Then it should fail when target type not matching
	When deny role found
	When deny role found once
	Then it should fail when principal match the deny role definition
	Then it should fail when principal and extra info match the deny role definition
	Then it should succeed when principal does not match every deny role definition in a set
	Then it should fail when principal match every deny role definition in a set
	Then it should fail when a matching deny role definition does not define a "contains" method
	Then it should fail when a matching deny role definition has a "contains" method that does not take at least one parameter
	Then it should fail when a matching deny role definition has a "contains" method that does not return a boolean value
	When deny role found more than once
	Then it should fail when principal and any extra info match any deny role definition
	Then it should fail when principal and any extra info match any contained deny role definition
	Then it should fail when principal and any extra info match any deny role definition in an embedded container action
	When deny role not found
	When allow role not found
	Then it should fail when allow role not found
	When allow role found
	When allow role found once
	Then it should succeed when principal match an allow role definition
	Then it should succeed when principal and extra info match an allow role definition
	Then it should fail when principal does not match every allow role definition in a set
	Then it should succeed when principal does match every allow role definition in a set
	Then it should fail when a matching allow role definition does not define a "contains" method
	Then it should fail when a matching allow role definition has a "contains" method that does not take at least one parameter
	Then it should fail when a matching allow role definition has a "contains" method that does not return a boolean value
	When allow role found more than once
	Then it should succeed when principal and any extra info match any allow role definition
	Then it should fail when principal and any extra info do not match any allow role definition
	Then it should succeed when principal and any extra info match any contained allow role definition
	Then it should succeed when principal and any extra info match any allow role definition in an embedded container action
```
input = ""
output:
```python
from behave import when, then

@when('action target not found')
def step_impl(context):
	pass

@then('it should fail when action target not found')
def step_impl(context):
	result = context.ae(Create(SomeClass)).is_allowing(PrincipalClass('commiter'))
	assert_that(calling(context.ae(Create(SomeClass)).verify).with_args(PrincipalClass('commiter')), raises(AuthorizationException))
	assert_that(result.is_failure)

@when('action target found')
def step_impl(context):
	pass

@then('it should fail when target type not matching')
def step_impl(context):
	result = context.ae(Read(OtherSomeOtherClass)).is_allowing(PrincipalClass('supervisor'))
	assert_that(calling(context.ae(Read(OtherSomeOtherClass)).verify).with_args(PrincipalClass('supervisor')), raises(AuthorizationException))
	assert_that(result.is_failure)

@when('deny role found')
def step_impl(context):
	pass

@when('deny role found once')
def step_impl(context):
	pass

@then('it should fail when principal match the deny role definition')
def step_impl(context):
	result = context.ae(Read()).is_allowing(OtherPrincipalClass('contributor'))
	assert_that(calling(context.ae(Read()).verify).with_args(OtherPrincipalClass('contributor')), raises(AuthorizationException))
	assert_that(result.is_failure)

@then('it should fail when principal and extra info match the deny role definition')
def step_impl(context):
	result = context.ae(Read(SomeClass)).is_allowing(PrincipalClass('reader'), 1234)
	assert_that(calling(context.ae(Read(SomeClass)).verify).with_args(PrincipalClass('reader'), 1234), raises(AuthorizationException))
	assert_that(result.is_failure)

@then('it should succeed when principal does not match every deny role definition in a set')
def step_impl(context):
	result = context.ae(Create()).is_allowing(PrincipalClass('commiter'))
	context.ae(Create()).verify(PrincipalClass('commiter'))
	assert_that(result.is_success)

@then('it should fail when principal match every deny role definition in a set')
def step_impl(context):
	result = context.ae(Create()).is_allowing(PrincipalClass('supervisor-commiter'))
	assert_that(calling(context.ae(Create()).verify).with_args(PrincipalClass('supervisor-commiter')), raises(AuthorizationException))
	assert_that(result.is_failure)

@then('it should fail when a matching deny role definition does not define a "contains" method')
def step_impl(context):
	assert_that(calling(context.ae(Update(OtherSomeOtherClass)).is_allowing).with_args(PrincipalClass('supervisor')), raises(NotImplementedError))
	assert_that(calling(context.ae(Update(OtherSomeOtherClass)).verify).with_args(PrincipalClass('supervisor')), raises(NotImplementedError))

@then('it should fail when a matching deny role definition has a "contains" method that does not take at least one parameter')
def step_impl(context):
	assert_that(calling(context.ae(Update(SomeOtherClass)).is_allowing).with_args(PrincipalClass('commiter')), raises(NotImplementedError))
	assert_that(calling(context.ae(Update(SomeOtherClass)).verify).with_args(PrincipalClass('commiter')), raises(NotImplementedError))

@then('it should fail when a matching deny role definition has a "contains" method that does not return a boolean value')
def step_impl(context):
	assert_that(calling(context.ae(Update(OtherClass)).is_allowing).with_args(PrincipalClass('commiter')), raises(NotImplementedError))
	assert_that(calling(context.ae(Update(OtherClass)).verify).with_args(PrincipalClass('commiter')), raises(NotImplementedError))

@when('deny role found more than once')
def step_impl(context):
	pass

@then('it should fail when principal and any extra info match any deny role definition')
def step_impl(context):
	result = context.ae(Read()).is_allowing(OtherPrincipalClass('contributor'))
	assert_that(calling(context.ae(Read()).verify).with_args(OtherPrincipalClass('contributor')), raises(AuthorizationException))
	assert_that(result.is_failure)

@then('it should fail when principal and any extra info match any contained deny role definition')
def step_impl(context):
	result = context.ae(Patch()).is_allowing(OtherPrincipalClass('contributor'))
	assert_that(calling(context.ae(Patch()).verify).with_args(OtherPrincipalClass('contributor')), raises(AuthorizationException))
	assert_that(result.is_failure)

@then('it should fail when principal and any extra info match any deny role definition in an embedded container action')
def step_impl(context):
	result = context.ae(Delete()).is_allowing(OtherPrincipalClass('contributor'))
	assert_that(calling(context.ae(Delete()).verify).with_args(OtherPrincipalClass('contributor')), raises(AuthorizationException))
	assert_that(result.is_failure)

@when('deny role not found')
def step_impl(context):

@when('allow role not found')
def step_impl(context):
	pass

@then('it should fail when allow role not found')
def step_impl(context):
	result = context.ae(Read(SomeClass)).is_allowing(PrincipalClass('laura'))
	assert_that(calling(context.ae(Read(SomeClass)).verify).with_args(PrincipalClass('laura')), raises(AuthorizationException))
	assert_that(result.is_failure)

@when('allow role found')
def step_impl(context):
	pass

@when('allow role found once')
def step_impl(context):
	pass

@then('it should succeed when principal match an allow role definition')
def step_impl(context):
	result = context.ae(Read(SomeOtherClass)).is_allowing(OtherPrincipalClass('contributor'))
	context.ae(Read(SomeOtherClass)).verify(OtherPrincipalClass('contributor'))
	assert_that(result.is_success)

@then('it should succeed when principal and extra info match an allow role definition')
def step_impl(context):
	result = context.ae(Read(OtherSomeOtherClass)).is_allowing(OtherPrincipalClass('reader'), 1234, "1234")
	context.ae(Read(OtherSomeOtherClass)).verify(OtherPrincipalClass('reader'), 1234, "1234")
	assert_that(result.is_success)

@then('it should fail when principal does not match every allow role definition in a set')
def step_impl(context):
	result = context.ae(Read(SomeClass)).is_allowing(PrincipalClass('commiter'))
	assert_that(calling(context.ae(Read(SomeClass)).verify).with_args(PrincipalClass('commiter')), raises(AuthorizationException))
	assert_that(result.is_failure)

@then('it should succeed when principal does match every allow role definition in a set')
def step_impl(context):
	result = context.ae(Read(SomeClass)).is_allowing(PrincipalClass('supervisor-commiter'))
	context.ae(Read(SomeClass)).verify(PrincipalClass('supervisor-commiter'))
	assert_that(result.is_success)

@then('it should fail when a matching allow role definition does not define a "contains" method')
def step_impl(context):
	assert_that(calling(context.ae(Delete(OtherSomeOtherClass)).is_allowing).with_args(PrincipalClass('supervisor')), raises(NotImplementedError))
	assert_that(calling(context.ae(Delete(OtherSomeOtherClass)).verify).with_args(PrincipalClass('supervisor')), raises(NotImplementedError))

@then('it should fail when a matching allow role definition has a "contains" method that does not take at least one parameter')
def step_impl(context):
	assert_that(calling(context.ae(Delete(SomeOtherClass)).is_allowing).with_args(PrincipalClass('commiter')), raises(NotImplementedError))
	assert_that(calling(context.ae(Delete(SomeOtherClass)).verify).with_args(PrincipalClass('commiter')), raises(NotImplementedError))

@then('it should fail when a matching allow role definition has a "contains" method that does not return a boolean value')
def step_impl(context):
	assert_that(calling(context.ae(Delete(OtherClass)).is_allowing).with_args(PrincipalClass('commiter')), raises(NotImplementedError))
	assert_that(calling(context.ae(Delete(OtherClass)).verify).with_args(PrincipalClass('commiter')), raises(NotImplementedError))

@when('allow role found more than once')
def step_impl(context):
	pass

@then('it should succeed when principal and any extra info match any allow role definition')
def step_impl(context):
	result = context.ae(Read(SomeClass)).is_allowing(PrincipalClass('supervisor'))
	context.ae(Read(SomeClass)).verify(PrincipalClass('supervisor'))
	assert_that(result.is_success)

@then('it should fail when principal and any extra info do not match any allow role definition')
def step_impl(context):
	result = context.ae(Create(OtherSomeOtherClass)).is_allowing(PrincipalClass('commiter'))
	assert_that(calling(context.ae(Create(OtherSomeOtherClass)).verify).with_args(PrincipalClass('commiter')), raises(AuthorizationException))
	assert_that(result.is_failure)

@then('it should succeed when principal and any extra info match any contained allow role definition')
def step_impl(context):
	result = context.ae(Patch(SomeOtherClass)).is_allowing(PrincipalClass('admin'))
	context.ae(Patch(SomeOtherClass)).verify(PrincipalClass('admin'))
	assert_that(result.is_success)

@then('it should succeed when principal and any extra info match any allow role definition in an embedded container action')
def step_impl(context):
	result = context.ae(Delete(SomeOtherClass)).is_allowing(PrincipalClass('admin'))
	context.ae(Delete(SomeOtherClass)).verify(PrincipalClass('admin'))
	assert_that(result.is_success)
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
name : ko_5
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework : 
```gherkin
Scenario: Сheck login with valid user
	Given website "http://qa_dashboard.test.thinkmobiles.com:8085"
	When enter email which was registered
	When enter password '123456'
	When click on button SignIn
	Then user 'Oleg Stasiv' was login successfully
```
input = ""
output:
```python
@given('website "{url}"')
def step(context, url):
	context.browser.get(url)

@when("enter email which was registered")
def step(context):
	context.browser.find_element(*LoginPageLocator.EMAIL_FIELD).send_keys(_existing_email())
	time.sleep(2)

@when("enter password '{text}'")
def step(context, text):
	context.browser.find_element(*LoginPageLocator.PASSWORD_FIELD).send_keys(text)

@when("click on button SignIn")
def step(context):
	context.browser.find_element(*LoginPageLocator.SIGNIN_BUTTON).click()

@then("user '{text}' was login successfully")
def step(context, text):
	username = context.browser.find_element(*HomePageLocator.FULLNAME_USER).text
	assert username == text
```

id : seed_task_6
name : ko_6
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework : 
```gherkin
Scenario: Forgot Password
	Given website "http://qa_dashboard.test.thinkmobiles.com:8085"
	When click on Forgot link
	Then appears Forgot field
	When enter existing email
	When click on Restore button
	Then email was send on your mail box
	When click on reset link
	Then appears Password restore fields
	When enter new password '123456'
	When click on Change my password button
	Then should redirect on Login screen
	Given website "http://qa_dashboard.test.thinkmobiles.com:8085"
	When enter email which was registered
	When enter password '123456'
	When click on button SignIn
	Then user 'Oleg Stasiv' was login successfully
```
input = ""
output:
```python
@given('website "{url}"')
def step(context, url):
    context.browser.get(url)

@when("click on Forgot link")
def step(context):
    time.sleep(1)
    context.browser.find_element(*LoginPageLocator.FORGOT_LINK).click()
    time.sleep(1)

@then("appears Forgot field")
def step(context):
	assert _is_element_present(context, *LoginPageLocator.EMAIL_FIELD) == True

@when ("enter existing email")
def step(context):
	context.browser.find_element(*LoginPageLocator.EMAIL_FIELD).send_keys(_existing_email())
	time.sleep(1)

@when ("click on Restore button")
def step(context):
	context.browser.find_element(*LoginPageLocator.RESTORE_BUTTON).click()

@then ("email was send on your mail box")
def step(context):
	assert _check_email_box() == True

@when ("click on reset link")
def step(context):
	f = open("token_list.txt", "r")
	restore_url = f.readline()
	f.close()
	context.browser.get(restore_url)

@then ("appears Password restore fields")
def step(context):
	_is_element_present(context, *LoginPageLocator.PASSWORD_FIELD)

@when ("enter new password '{psw}'")
def step(context, psw):
	context.browser.find_element(*LoginPageLocator.PASSWORD_FIELD).send_keys(psw)
	context.browser.find_element(*LoginPageLocator.CONFIRM_PASSWORD).send_keys(psw)

@when("click on Change my password button")
def step(context):
	time.sleep(1)
	context.browser.find_element(*LoginPageLocator.CHANGE_MY_PASSWORD_BUTTON).click()

@then ("should redirect on Login screen")
def step(context):
	time.sleep(1)
	_is_element_present(context, *LoginPageLocator.EMAIL_FIELD)

@given('website "{url}"')
def step(context, url):
	context.browser.get(url)

@when("enter email which was registered")
def step(context):
	context.browser.find_element(*LoginPageLocator.EMAIL_FIELD).send_keys(_existing_email())
	time.sleep(2)

@when("enter password '{text}'")
def step(context, text):
	context.browser.find_element(*LoginPageLocator.PASSWORD_FIELD).send_keys(text)

@when("click on button SignIn")
def step(context):
	context.browser.find_element(*LoginPageLocator.SIGNIN_BUTTON).click()

@then("user '{text}' was login successfully")
def step(context, text):
	username = context.browser.find_element(*HomePageLocator.FULLNAME_USER).text
	assert username == text
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
from behave import given, when, then
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
	When  I press the big red button
	And  I duck
	Then  I reach the next level
```
input = ""
output:
```python
from behave import given, when, then
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
name : ko_9
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework : 
```gherkin
Scenario: Сheck login with invalid user
	Given website "http://qa_dashboard.test.thinkmobiles.com:8085"
	When enter email which was registered
	When enter password 'yana2468975311'
	When click on button SignIn
	Then appear validation message 'Invalid Email or password.'
```
input = ""
output:
```python
@given('website "{url}"')
def step(context, url):
	context.browser.get(url)

@when("enter email which was registered")
def step(context):
	context.browser.find_element(*LoginPageLocator.EMAIL_FIELD).send_keys(_existing_email())
	time.sleep(2)

@when("enter password '{text}'")
def step(context, text):
	context.browser.find_element(*LoginPageLocator.PASSWORD_FIELD).send_keys(text)

@when("click on button SignIn")
def step(context):
	context.browser.find_element(*LoginPageLocator.SIGNIN_BUTTON).click()

@then("user '{text}' was login successfully")
def step(context, text):
	username = context.browser.find_element(*HomePageLocator.FULLNAME_USER).text
	assert username == text

@then("appear validation message '{text}'")
def step(context, text):
	username = context.browser.find_element(*LoginPageLocator.VALIDATION_MESSAGE).text
	time.sleep(2)
	assert username == text
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
	|  x  |  y | sum |
	|  1  |  1 |  2  |
	|  1  |  2 |  3  |
	|  2  |  1 |  3  |
	|  2  |  7 |  9  |
```
input = ""
output:
```python
from behave import given, when, then
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
name : ko_12
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework : 
```gherkin
Scenario: Create organization
	Given website "http://qa_dashboard.test.thinkmobiles.com:8085"
	When login ass owner
	Then user 'Behave Organization' was login successfully
	When click on My_organization button
	Then appear button Create_new_organization button
	When click on button 'Create_new_organization'
	When click on "Add New Organization"
	Then appear validation message "can't be blank"
	When create organization "Test one" and Description "Test description"
	Then My organization list contain "Test one" organization
```
input = ""
output:
```python
@given('website "{url}"')
def step(context, url):
	context.browser.get(url)

@when("login ass owner")
def step(context):
	time.sleep(2)
	general_methods.login(context,email=username, password=psw)
	time.sleep(1)

@then("user '{text}' was login successfully")
def step(context, text):
	username = context.browser.find_element(*HomePageLocator.FULLNAME_USER).text
	assert username == text

@when("click on My_organization button")
def step(context):
	time.sleep(2)
	context.browser.find_element(*HomePageLocator.My_organizations_btn).click()
	time.sleep(1)

@then("appear button Create_new_organization button")
def step(context):
	btn = context.browser.find_element(*HomePageLocator.Create_new_organization_btn)
	assertTrue(btn)

@when("click on button 'Create_new_organization'")
def step_impl(context):
	context.browser.find_element(*HomePageLocator.Create_new_organization_btn).click()
	time.sleep(5)

@when('click on "Add New Organization"')
def step_impl(context):
	context.browser.find_element(*HomePageLocator.Add_new_organization_btn).click()

@then('appear validation message "{text1}"')
def step_impl(context, text1):
	valid_message = context.browser.find_element(*LoginPageLocator.VALIDATION_MESSAGE).text
	time.sleep(0.5)
	assert valid_message == text1

@when('create organization "{text1}" and Description "{text2}"')
def step_impl(context, text1, text2):
	time.sleep(2)
	context.browser.find_element(*OrganizationPopup.TITLE).send_keys(text1)
	context.browser.find_element(*OrganizationPopup.DESC).send_keys(text2)
	context.browser.find_element(*OrganizationPopup.SUBMIT).click()
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
name : ko_14
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework : 
```gherkin
Scenario: Add user to organization
	Given website "http://qa_dashboard.test.thinkmobiles.com:8085"
	When login ass owner
	When click on My_organization button
	When clear all organization
	When create organization "Test one edit"
	When click on organization "Test one edit"
	When click on "Organization Members" button in left menu
	When click on "Add Members" button
	Then appears popup window "Add Organization Members"
```
input = ""
output:
```python
@given('website "{url}"')
def step(context, url):
	context.browser.get(url)

@when("login ass owner")
def step(context):
	time.sleep(2)
	general_methods.login(context,email=username, password=psw)
	time.sleep(1)

@when("click on My_organization button")
def step(context):
	time.sleep(2)
	context.browser.find_element(*HomePageLocator.My_organizations_btn).click()
	time.sleep(1)

@when("clear all organization")
def step_impl(context):
	general_methods.clear_organizations(context)

@when('create organization "Test one edit"')
def step_impl(context):
	general_methods.create_organization(context, "Test one edit")

@when('click on organization "{text}"')
def step_impl(context, text):
	time.sleep(1)
	context.browser.find_element(By.XPATH, ".//a[text() = '{}']".format(text)).click()

@when('click on "{text}" button in left menu')
def step_impl(context,text):
	context.browser.find_element(By.XPATH, ".//span[text()='{}']".format(text)).click()

@when('click on "{text}" button')
def step_impl(context,text):
	context.browser.find_element(By.XPATH, ".//a[text()='{}']".format(text)).click()

@then('appears popup window "{text}"')
def step_impl(context, text):
	title = context.browser.find_element(By.CSS_SELECTOR, ".title-main>h3").text
	time.sleep(2)
	assertTrue(text, title)
```

id : seed_task_15
name : ko_15
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework : 
```gherkin
Scenario: With one repository
	Given I have a project with name \"Kalibro\"
	And I have a kalibro configuration with name \"Conf\"
	And the given project has the following Repositories:
	  |   name\t| scm_type |\t\t\t\t\t   address\t\t\t\t\t|\n\t  |  Kalibro  |\tGIT   | https://github.com/mezuro/kalibro_processor.git  |
	When I call the process method for the given repository
	And I call the cancel_process method for the given repository
	Then I should get success
```
input = ""
output:
```python
from behave import given, when, then
@given(u'I have a project with name \"{}\"')
def step_impl(context, project_name):
    context.execute_steps(u'When I create the project with name \"{}\"'.format(project_name))
    
@given(u'I have a kalibro configuration with name \"{}\"')
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
    assert_true("errors" not in context.response)
```

id : seed_task_16
name : ko_16
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework : 
```gherkin
Scenario: find a valid range
	Given I have a kalibro configuration with name "Java"
	And I have a reading group with name "Group"
	And I have a metric configuration within the given kalibro configuration
	And I have a reading within the given reading group
	And I have a range within the given reading
	Then the range should exist
```
input = ""
output:
```python
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

@given(u'I have a reading within the given reading group')
def step_impl(context):
	context.reading = ReadingFactory.build(reading_group_id=context.reading_group.id)
	context.reading.save()

@given(u'I have a range within the given reading')
def step_impl(context):
	context.range = KalibroRangeFactory.build(reading_id=context.reading.id, metric_configuration_id=context.metric_configuration.id, beginning=1.1, end=5.1)
	context.range.save()

@then(u'the range should exist')
def step_impl(context):
	assert_true(KalibroRange.exists(context.range.id))
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
name : ko_18
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework : 
```gherkin
Scenario: Constructing the PPM header
	Given c = canvas(5, 3)
	When ppm = canvas_to_ppm(c)
	Then lines 1-3 of ppm are
	"""
	P3
	5 3
	255
	"""
```
input = ""
output:
```python
from behave import given, when, then
@given('c = canvas({width:d}, {height:d})')
def step_impl(context, width, height):
	context.c = canvas.Canvas(width, height)

@when('ppm = canvas_to_ppm(c)')
def step_impl(context):
	context.ppm = list(canvas.canvas_to_ppm(context.c))

@then('lines 1-3 of ppm are')
def step_impl(context):
	print(f'{"".join(context.ppm[0:3])}')
	print(f'{context.text}')
	assert "".join(context.ppm[0:3]) == context.text"
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
name : ko_20
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework : 
```gherkin
Scenario: two workers can serve two clients at time  
	Given server started with '--workers=2 0 exec python scripts/program.py' 
	When client connects  
	And second client connects
	And program handles the request
	And second program handles the request
	Then program does not handle request
	When program writes 'hello'
	When program flushes output
	Then client receives 'hello' 
	When second program writes 'hello'
	When second program flushes
	Then second client receives 'hello'
```
input = ""
output:
```python
@given(u'server started with \'{cmd}\'')
def step_impl(context, cmd):
	context.server = subprocess.Popen(shlex.split('./malunas ' + cmd), stdout = subprocess.PIPE, stderr = subprocess.PIPE, bufsize = 1)
	poller = select.poll()
	poller.register(context.server.stderr, select.POLLIN)
	poll_result = poller.poll(TIMEOUT)
	if poll_result:
		line = context.server.stderr.readline()
		print(line)
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

@when(u'second program handles the request')
def step_impl(context):
	connection, client_address = context.pm.accept()
	context.second_control_socket = connection

@then(u'program does not handle request')
def step_impl(context):
	try:
		connection, client_address = context.pm.accept()
		context.control_socket = connection
	except socket.timeout:
		return
	assert(False), 'A program handles a request but that is not expected'

@when(u'program writes \'hello\'')
def step_impl(context):
	context.control_socket.send('WRITE hello\n')

@when(u'program flushes output')
def step_impl(context):
	context.control_socket.send('FLUSH\n')

@then(u'client receives \'hello\'')
def step_impl(context):
	context.client.settimeout(TIMEOUT)
	line = context.client.recv(10)
	assert("hello" == line.strip()), "Message not received by client, but received: '%s'" % line

@when(u'second program writes \'hello\'')
def step_impl(context):
	context.second_control_socket.send('WRITE hello\n')

@when(u'second program flushes')
def step_impl(context):
	context.second_control_socket.send('FLUSH\n')

@then(u'second client receives \'hello\'')
def step_impl(context):
	context.second_client.settimeout(TIMEOUT)
	line = context.second_client.recv(10)
	assert("hello" == line.strip()), "Message not received by client, but received: '%s'" % line
```

id : seed_task_21
name : ko_21
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework : 
```gherkin
Scenario: Without TTY client sees response immediately if program flushes
	Given server started with '--workers=1 0 exec python scripts/program.py' 
	When client connects
	And program handles the request
	Then program recognizes that it does not run in TTY
	When program writes 'hello'
	And program flushes output
	Then client receives 'hello'
```
input = ""
output:
```python
@given(u'server started with \'{cmd}\'')
def step_impl(context, cmd):
	context.server = subprocess.Popen(shlex.split('./malunas ' + cmd), stdout = subprocess.PIPE, stderr = subprocess.PIPE, bufsize = 1)
	poller = select.poll()
	poller.register(context.server.stderr, select.POLLIN)
	poll_result = poller.poll(TIMEOUT)
	if poll_result:
		line = context.server.stderr.readline()
        	print(line)
		m = re.compile(r'^malunas: Listening on 0.0.0.0:(?P<port>\d+)').match(line) 
        	context.port = int(m.group('port'))
	assert(context.server.poll() is None), 'server died: %s' % context.server.stderr.read(100) 

@when(u'client connects')
def step_impl(context):
	context.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server_address = ('localhost', context.port)
	context.client.connect(server_address)

@when(u'program handles the request')
def step_impl(context):
	connection, client_address = context.pm.accept()
	context.control_socket = connection

@then(u'program recognizes that it does not run in TTY')
def step_impl(context):
    context.control_socket.send('ISTTY?\n')
    line = context.control_socket.recv(10) 
    assert("TTY=0" == line.strip()), 'program cannot confirm that it does not run in a TTY'

@when(u'program writes \'hello\'')
def step_impl(context):
	context.control_socket.send('WRITE hello\n')

@when(u'program flushes output')
def step_impl(context):
	context.control_socket.send('FLUSH\n')

@then(u'client receives \'hello\'')
def step_impl(context):
	context.client.settimeout(TIMEOUT)
	line = context.client.recv(10)
	assert("hello" == line.strip()), "Message not received by client, but received: '%s'" % line
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
from behave import given, when, then
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
name : ko_23
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework : 
```gherkin
Scenario: Http server responds through proxy 
	Given server started with '--workers=1 0 proxy web:80'
	When client connects
	When client sends 'GET / HTTP/1.0\r\n\r\n'
	Then client receives 'Hello, this is a web server'
```
input = ""
output:
```python
@given(u'server started with \'{cmd}\'')
def step_impl(context, cmd):
	context.server = subprocess.Popen(shlex.split('./malunas ' + cmd), stdout = subprocess.PIPE, stderr = subprocess.PIPE, bufsize = 1)
	poller = select.poll()
	poller.register(context.server.stderr, select.POLLIN)
	poll_result = poller.poll(TIMEOUT)
	if poll_result:
		line = context.server.stderr.readline()
        	print(line)
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
from behave import given, when, then
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
name : ko_26
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework : 
```gherkin
Scenario Outline: test chaincode to chaincode invocation
	Given we compose "<ComposeFile>"
	And I wait "5" seconds
	And I register with CA supplying username "binhn" and secret "7avZQLwcUe9q" on peers:
	   | vp0  |
	And I register with CA supplying username "alice" and secret "CMS10pEQlB16" on peers:
	   | vp0  |
	And I use the following credentials for querying peers:
	   | peer |   username  |    secret    |
	   | vp0  |  test_user0 | MS9qrN8hFjlE |
	   | vp1  |  test_user1 | jGlNl6ImkuDo |
	   | vp2  |  test_user2 | zMflqOKezFiA |
	   | vp3  |  test_user3 | vWdLCE00vJy0 |

	When requesting "/chain" from "vp0"
	Then I should get a JSON response with "height" = "1"

	# Deploy the first chaincode
	When user "binhn" deploys chaincode "github.com/hyperledger/fabric/examples/chaincode/go/chaincode_example02" aliased as "chaincode_example02" with ctor "init" and args
			  | arg1 |  arg2 | arg3 | arg4 |
			  |  a   |  100  |  b   |  200 |
	Then I should have received a chaincode name
	Then I wait up to "<WaitTime>" seconds for transaction to be committed to peers:
		     | vp0  | vp1 | vp2 | vp3 |
	And "binhn"'s last transaction should have succeeded

	# Deploy the second chaincode
	When user "binhn" deploys chaincode "github.com/hyperledger/fabric/examples/chaincode/go/chaincode_example05" aliased as "chaincode_example05" with ctor "init" and args
			  | arg1  |  arg2 |
			  | sum   |   0   |
	Then I should have received a chaincode name
	Then I wait up to "<WaitTime>" seconds for transaction to be committed to peers:
		     | vp0  | vp1 | vp2 | vp3 |
	And "binhn"'s last transaction should have succeeded


	# Invoke chaincode_example05 which in turn will invoke chaincode_example02.  NOTE: Binhn must pass a reference to the first chaincode
	Given user "binhn" stores a reference to chaincode "chaincode_example02" as "cc1"
	When user "binhn" invokes chaincode "chaincode_example05" function name "invoke" with args
		  |  arg1   |  arg2  |
		  | {cc1}   |  sum   |
	Then I should have received a transactionID
	Then I wait up to "60" seconds for transaction to be committed to peers:
	   | vp0  | vp1 | vp2 | vp3 |
      And "binhn"'s last transaction should have succeeded


    Examples: Consensus Options
	  |	    ComposeFile			 |   WaitTime   |
	  |   docker-compose-4-consensus-batch.yml |	60	|
```
input = ""
output:
```python
@given(u'we compose "{composeYamlFile}"')
def step_impl(context, composeYamlFile):
	context.compose_yaml = composeYamlFile
	fileArgsToDockerCompose = bdd_compose_util.getDockerComposeFileArgsFromYamlFile(context.compose_yaml)
	context.compose_output, context.compose_error, context.compose_returncode = \
		bdd_test_util.cli_call(["docker-compose"] + fileArgsToDockerCompose + ["up","--force-recreate", "-d"], expect_success=True)
	assert context.compose_returncode == 0, "docker-compose failed to bring up {0}".format(composeYamlFile)

	bdd_compose_util.parseComposeOutput(context)

	timeoutSeconds = 15
	assert bdd_compose_util.allContainersAreReadyWithinTimeout(context, timeoutSeconds), \
		"Containers did not come up within {} seconds, aborting".format(timeoutSeconds)

@given(u'I wait "{seconds}" seconds')
def step_impl(context, seconds):
	time.sleep(float(seconds))

@given(u'I register with CA supplying username "{userName}" and secret "{secret}" on peers')
def step_impl(context, userName, secret):
	assert 'compose_containers' in context, "compose_containers not found in context"
	assert 'table' in context, "table (of peers) not found in context"

	# Get list of IPs to login to
	aliases =  context.table.headings
	containerDataList = bdd_test_util.getContainerDataValuesFromContext(context, aliases, lambda containerData: containerData)

	secretMsg = {
		"enrollId": userName,
		"enrollSecret" : secret
	}

	# Login to each container specified
	for containerData in containerDataList:
		request_url = buildUrl(context, containerData.ipAddress, "/registrar")
		print("{0} POSTing path = {1}".format(currentTime(), request_url))

		resp = requests.post(request_url, headers={'Content-type': 'application/json'}, data=json.dumps(secretMsg), verify=False)
		assert resp.status_code == 200, "Failed to POST to %s:  %s" %(request_url, resp.text)
		context.response = resp
		print("message = {0}".format(resp.json()))

		# Create new User entry
		bdd_test_util.registerUser(context, secretMsg, containerData.composeService)

	# Store the username in the context
	context.userName = userName
	# if we already have the chaincodeSpec, change secureContext
	if 'chaincodeSpec' in context:
		context.chaincodeSpec["secureContext"] = context.userName

@given(u'I use the following credentials for querying peers')
def step_impl(context):
	assert 'compose_containers' in context, "compose_containers not found in context"
	assert 'table' in context, "table (of peers, username, secret) not found in context"

	peerToSecretMessage = {}

	# Login to each container specified using username and secret
	for row in context.table.rows:
		peer, userName, secret = row['peer'], row['username'], row['secret']
		secretMsg = {
			"enrollId": userName,
			"enrollSecret" : secret
		}

		ipAddress = bdd_test_util.ipFromContainerNamePart(peer, context.compose_containers)
		request_url = buildUrl(context, ipAddress, "/registrar")
		print("POSTing to service = {0}, path = {1}".format(peer, request_url))

		resp = requests.post(request_url, headers={'Content-type': 'application/json'}, data=json.dumps(secretMsg), verify=False)
		assert resp.status_code == 200, "Failed to POST to %s:  %s" %(request_url, resp.text)
		context.response = resp
		print("message = {0}".format(resp.json()))
		peerToSecretMessage[peer] = secretMsg
	context.peerToSecretMessage = peerToSecretMessage

@when(u'requesting "{path}" from "{containerName}"')
def step_impl(context, path, containerName):
	ipAddress = bdd_test_util.ipFromContainerNamePart(containerName, context.compose_containers)
	request_url = buildUrl(context, ipAddress, path)
	print("Requesting path = {0}".format(request_url))
	resp = requests.get(request_url, headers={'Accept': 'application/json'}, verify=False)
	assert resp.status_code == 200, "Failed to GET url %s:  %s" % (request_url,resp.text)
	context.response = resp
	print("")

@then(u'I should get a JSON response containing "{attribute}" attribute')
def step_impl(context, attribute):
	getAttributeFromJSON(attribute, context.response.json(), "Attribute not found in response (%s)" %(attribute))

@when(u'user "{enrollId}" deploys chaincode "{chaincodePath}" aliased as "{ccAlias}" with ctor "{ctor}" and args')
def step_impl(context, enrollId, chaincodePath, ccAlias, ctor):
	bdd_grpc_util.deployChaincode(context, enrollId, chaincodePath, ccAlias, ctor)

@then(u'I should have received a chaincode name')
def step_impl(context):
	if 'chaincodeSpec' in context:
		assert context.chaincodeSpec['chaincodeID']['name'] != ""
		# Set the current transactionID to the name passed back
		context.transactionID = context.chaincodeSpec['chaincodeID']['name']
	elif 'grpcChaincodeSpec' in context:
		assert context.grpcChaincodeSpec.chaincodeID.name != ""
		# Set the current transactionID to the name passed back
		context.transactionID = context.grpcChaincodeSpec.chaincodeID.name
	else:
		fail('chaincodeSpec not in context')

@then(u'I wait up to "{seconds}" seconds for transaction to be committed to all peers')
def step_impl(context, seconds):
	assert 'transactionID' in context, "transactionID not found in context"
	assert 'compose_containers' in context, "compose_containers not found in context"

	# Build map of "containerName" : resp.statusCode
	respMap = {container.containerName:0 for container in context.compose_containers}

	# Set the max time before stopping attempts
	maxTime = datetime.now() + timedelta(seconds = int(seconds))
	for container in context.compose_containers:
		ipAddress = container.ipAddress
		request_url = buildUrl(context, ipAddress, "/transactions/{0}".format(context.transactionID))

		# Loop unless failure or time exceeded
		while (datetime.now() < maxTime):
			print("{0} GETing path = {1}".format(currentTime(), request_url))
			resp = requests.get(request_url, headers={'Accept': 'application/json'}, verify=False)
			if resp.status_code == 404:
				# Pause then try again
				respMap[container.containerName] = 404
				time.sleep(1)
				continue
			elif resp.status_code == 200:
				# Success, continue
				respMap[container.containerName] = 200
				break
			else:
				raise Exception("Error requesting {0}, returned result code = {1}".format(request_url, resp.status_code))
		else:
			raise Exception("Max time exceeded waiting for transactions with current response map = {0}".format(respMap))
	print("Result of request to all peers = {0}".format(respMap))
    print("")

@then(u'"{enrollId}"\'s last transaction should have succeeded')
def step_impl(context, enrollId):
	txResult = bdd_grpc_util.getTxResult(context, enrollId)
	assert txResult.errorCode == 0, "Expected success (errorCode == 0), instead found errorCode={0}, error={1}".format(txResult.errorCode, txResult.error
```

id : seed_task_27
name : ko_27
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework : 
```gherkin
Scenario: UTXO chaincode test
	Given we compose "docker-compose-1.yml"
	And I wait "1" seconds
	When requesting "/chain" from "vp0"
	Then I should get a JSON response with "height" = "1"
	When I deploy chaincode "github.com/openblockchain/obc-peer/examples/chaincode/go/utxo" with ctor "init" to "vp0"
	||
	||

	Then I should have received a chaincode name
	Then I wait up to "60" seconds for transaction to be committed to all peers

	When requesting "/chain" from "vp0"
	Then I should get a JSON response with "height" = "2"

	When I invoke chaincode "map" function name "execute" on "vp0"
	  | arg1 |
	  | AQAAAAEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP////9NBP//AB0BBEVUaGUgVGltZXMgMDMvSmFuLzIwMDkgQ2hhbmNlbGxvciBvbiBicmluayBvZiBzZWNvbmQgYmFpbG91dCBmb3IgYmFua3P/////AQDyBSoBAAAAQ0EEZ4r9sP5VSCcZZ/GmcTC3EFzWqCjgOQmmeWLg6h9h3rZJ9rw/TO84xPNVBOUewRLeXDhN97oLjVeKTHAra/EdX6wAAAAA |
	Then I should have received a transactionID
	Then I wait up to "25" seconds for transaction to be committed to all peers

	When requesting "/chain" from "vp0"
	Then I should get a JSON response with "height" = "3"
```
input = ""
output:
```python
@given(u'we compose "{composeYamlFile}"')
def step_impl(context, composeYamlFile):
	context.compose_yaml = composeYamlFile
	fileArgsToDockerCompose = bdd_compose_util.getDockerComposeFileArgsFromYamlFile(context.compose_yaml)
	context.compose_output, context.compose_error, context.compose_returncode = \
		bdd_test_util.cli_call(["docker-compose"] + fileArgsToDockerCompose + ["up","--force-recreate", "-d"], expect_success=True)
	assert context.compose_returncode == 0, "docker-compose failed to bring up {0}".format(composeYamlFile)

	bdd_compose_util.parseComposeOutput(context)

	timeoutSeconds = 15
	assert bdd_compose_util.allContainersAreReadyWithinTimeout(context, timeoutSeconds), \
		"Containers did not come up within {} seconds, aborting".format(timeoutSeconds)

@given(u'I wait "{seconds}" seconds')
def step_impl(context, seconds):
	time.sleep(float(seconds))

@when(u'requesting "{path}" from "{containerName}"')
def step_impl(context, path, containerName):
	ipAddress = bdd_test_util.ipFromContainerNamePart(containerName, context.compose_containers)
	request_url = buildUrl(context, ipAddress, path)
	print("Requesting path = {0}".format(request_url))
	resp = requests.get(request_url, headers={'Accept': 'application/json'}, verify=False)
	assert resp.status_code == 200, "Failed to GET url %s:  %s" % (request_url,resp.text)
	context.response = resp
	print("")

@when(u'I invoke chaincode "{chaincodeName}" function name "{functionName}" on "{containerName}"')
def step_impl(context, chaincodeName, functionName, containerName):
	assert 'chaincodeSpec' in context, "chaincodeSpec not found in context"
	invokeChaincode(context, "invoke", functionName, containerName)

@then(u'I should get a JSON response containing "{attribute}" attribute')
def step_impl(context, attribute):
	getAttributeFromJSON(attribute, context.response.json(), "Attribute not found in response (%s)" %(attribute))

@when(u'user "{enrollId}" deploys chaincode "{chaincodePath}" aliased as "{ccAlias}" with ctor "{ctor}" and args')
def step_impl(context, enrollId, chaincodePath, ccAlias, ctor):
	bdd_grpc_util.deployChaincode(context, enrollId, chaincodePath, ccAlias, ctor)

@then(u'I should have received a chaincode name')
def step_impl(context):
	if 'chaincodeSpec' in context:
		assert context.chaincodeSpec['chaincodeID']['name'] != ""
		# Set the current transactionID to the name passed back
		context.transactionID = context.chaincodeSpec['chaincodeID']['name']
	elif 'grpcChaincodeSpec' in context:
		assert context.grpcChaincodeSpec.chaincodeID.name != ""
		# Set the current transactionID to the name passed back
		context.transactionID = context.grpcChaincodeSpec.chaincodeID.name
	else:
		fail('chaincodeSpec not in context')

@then(u'I wait up to "{seconds}" seconds for transaction to be committed to all peers')
def step_impl(context, seconds):
	assert 'transactionID' in context, "transactionID not found in context"
	assert 'compose_containers' in context, "compose_containers not found in context"

	# Build map of "containerName" : resp.statusCode
	respMap = {container.containerName:0 for container in context.compose_containers}

	# Set the max time before stopping attempts
	maxTime = datetime.now() + timedelta(seconds = int(seconds))
	for container in context.compose_containers:
		ipAddress = container.ipAddress
		request_url = buildUrl(context, ipAddress, "/transactions/{0}".format(context.transactionID))

		# Loop unless failure or time exceeded
		while (datetime.now() < maxTime):
			print("{0} GETing path = {1}".format(currentTime(), request_url))
			resp = requests.get(request_url, headers={'Accept': 'application/json'}, verify=False)
			if resp.status_code == 404:
				# Pause then try again
				respMap[container.containerName] = 404
				time.sleep(1)
				continue
			elif resp.status_code == 200:
				# Success, continue
				respMap[container.containerName] = 200
				break
			else:
				raise Exception("Error requesting {0}, returned result code = {1}".format(request_url, resp.status_code))
		else:
			raise Exception("Max time exceeded waiting for transactions with current response map = {0}".format(respMap))
	print("Result of request to all peers = {0}".format(respMap))
	print("")

@then(u'"{enrollId}"\'s last transaction should have succeeded')
def step_impl(context, enrollId):
	txResult = bdd_grpc_util.getTxResult(context, enrollId)
	assert txResult.errorCode == 0, "Expected success (errorCode == 0), instead found errorCode={0}, error={1}".format(txResult.errorCode, txResult.error)

@then(u'I should have received a transactionID')
def step_impl(context):
	assert 'transactionID' in context, 'transactionID not found in context'
	assert context.transactionID != ""
	pass
```

id : seed_task_28
name : ko_28
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework : 
```gherkin
Scenario: Create an account sending all mandatory information
	Given I am on Home Page
	And I click on sign in
	When I fill my email "keaaaa@keaaaaa.com.br" on create an account field
	And I click on create an account
	Then I should go to "YOUR PERSONAL INFORMATION" screen
	When I click on Mr title
	And I type "keakea" on first name
	And I type "Junior" on last name
	And I type "123456" on password
	And I type "Seattle" on my address first name
	And I type "Los Angeles" on my address last name
	And I type "Barão de Bonito" on address
	And I type "Recife" on city
	And I select "California" on state
	And I type "00000" on zip code
	And I type "9999999999" on mobile phone
	And I type "kea" on address alias
	And I click on register
	Then I should see my account information 
```
input = ""
output:
```python
@step(u'I am on Home Page')
def step_impl(context):
	context.page_object = HomeActions(context.driver)
	context.page_object.open_application(context.base_url)

@step(u'I click on sign in')
def step_impl(context):
	context.page_object.click_on_sign_in()

@step(u'I fill my email "{email}" on create an account field')
def step_impl(context, email):
	context.page_object = AuthenticationActions(context.driver)
	context.page_object.email_in_create_account(email)

@step(u'I click on create an account')
def step_impl(context):
	context.page_object.click_on_create_account()

@step(u'I should go to "{screen}" screen')
def step_impl(context,screen):
	assert_that(context.page_object.get_personal_info(), equal_to(screen))

@step(u'I click on Mr title')
def step_impl(context):
	context.page_object.click_on_mr_title()

@step(u'I type "{first_name}" on first name')
def step_impl(context, first_name):
	context.page_object.type_in_first_name(first_name)

@step(u'I type "{last_name}" on last name')
def step_impl(context, last_name):
	context.page_object.type_in_last_name(last_name)

@step(u'I type "{password}" on password')
def step_impl(context, password):
	context.page_object.type_in_password(password)

@step(u'I type "{address_fn}" on my address first name')
def step_impl(context, address_fn):
	context.page_object.type_in_address_first_name(address_fn)

@step(u'I type "{address_ln}" on my address last name')
def step_impl(context, address_ln):
	context.page_object.type_in_address_last_name(address_ln)

@step(u'I type "{address}" on address')
def step_impl(context, address):
	context.page_object.type_in_address(address)

@step(u'I type "{city}" on city')
def step_impl(context, city):
	context.page_object.type_in_city(city)

@step(u'I type "{zipcode}" on zip code')
def step_impl(context, zipcode):
	context.page_object.type_in_zip_code(zipcode)

@step(u'I select "{state}" on state') 
def step_impl(context,state):
	context.page_object.select_in_combo_box(state)

@step(u'I type "{phone}" on mobile phone')
def step_impl(context, phone):
	context.page_object.type_in_mobile_phone(phone)

@step(u'I type "{alias}" on address alias')
def step_impl(context, alias):
	context.page_object.type_in_address_alias(alias)

@step(u'I click on register')
def step_impl(context):
	context.page_object.click_on_register()

@step(u'I should see my account information')
def step_impl(context):
	assert_that(context.page_object.get_my_account_info(), equal_to("MY ACCOUNT"))
	context.page_object.click_on_sign_out()
```

id : seed_task_29
name : ko_29
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework : 
```gherkin
Scenario: Create an account - without typing first name
	Given I am on Home Page
	And I click on sign in
	When I fill my email "keaa@keaaaaaaaa.com.br" on create an account field
	And I click on create an account
	Then I should go to "YOUR PERSONAL INFORMATION" screen
	When I click on Mr title
	And I type "Junior" on last name
	And I type "123456" on password
	And I type "Seattle" on my address first name
	And I type "Los Angeles" on my address last name
	And I type "Barão de Bonito" on address
	And I type "Recife" on city
	And I select "California" on state
	And I type "00000" on zip code
	And I type "9999999999" on mobile phone
	And I type "kea" on address alias
	And I click on register
	Then System should display the message "firstname is required."
```
input = ""
output:
```python
@step(u'I am on Home Page')
def step_impl(context):
	context.page_object = HomeActions(context.driver)
	context.page_object.open_application(context.base_url)

@step(u'I click on sign in')
def step_impl(context):
	context.page_object.click_on_sign_in()

@step(u'I fill my email "{email}" on create an account field')
def step_impl(context, email):
	context.page_object = AuthenticationActions(context.driver)
	context.page_object.email_in_create_account(email)

@step(u'I click on create an account')
def step_impl(context):
	context.page_object.click_on_create_account()

@step(u'I should go to "{screen}" screen')
def step_impl(context,screen):
	assert_that(context.page_object.get_personal_info(), equal_to(screen))

@step(u'I click on Mr title')
def step_impl(context):
	context.page_object.click_on_mr_title()

@step(u'I type "{last_name}" on last name')
def step_impl(context, last_name):
	context.page_object.type_in_last_name(last_name)

@step(u'I type "{password}" on password')
def step_impl(context, password):
	context.page_object.type_in_password(password)

@step(u'I type "{address_fn}" on my address first name')
def step_impl(context, address_fn):
	context.page_object.type_in_address_first_name(address_fn)

@step(u'I type "{address_ln}" on my address last name')
def step_impl(context, address_ln):
	context.page_object.type_in_address_last_name(address_ln)

@step(u'I type "{address}" on address')
def step_impl(context, address):
	context.page_object.type_in_address(address)

@step(u'I type "{city}" on city')
def step_impl(context, city):
	context.page_object.type_in_city(city)

@step(u'I type "{zipcode}" on zip code')
def step_impl(context, zipcode):
	context.page_object.type_in_zip_code(zipcode)

@step(u'I select "{state}" on state') 
def step_impl(context,state):
	context.page_object.select_in_combo_box(state)

@step(u'I type "{phone}" on mobile phone')
def step_impl(context, phone):
	context.page_object.type_in_mobile_phone(phone)

@step(u'I type "{alias}" on address alias')
def step_impl(context, alias):
	context.page_object.type_in_address_alias(alias)

@step(u'I click on register')
def step_impl(context):
	context.page_object.click_on_register()

@step(u'I should see my account information')
def step_impl(context):
	assert_that(context.page_object.get_my_account_info(), equal_to("MY ACCOUNT"))
	context.page_object.click_on_sign_out()
```

id : seed_task_30
name : ko_30
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework : 
```gherkin
Scenario: Create an account - without typing last name
	Given I am on Home Page
	And I click on sign in
	When I fill my email "keaa@keaaaaaaaa.com.br" on create an account field
	And I click on create an account
	Then I should go to "YOUR PERSONAL INFORMATION" screen
	When I click on Mr title	
	And I type "keakea" on first name
	And I type "123456" on password
	And I type "Seattle" on my address first name
	And I type "Los Angeles" on my address last name
	And I type "Barão de Bonito" on address
	And I type "Recife" on city
	And I select "California" on state
	And I type "00000" on zip code
	And I type "9999999999" on mobile phone
	And I type "kea" on address alias
	And I click on register
	Then System should display the message "lastname is required."
```
input = ""
output:
```python
@step(u'I am on Home Page')
def step_impl(context):
	context.page_object = HomeActions(context.driver)
	context.page_object.open_application(context.base_url)

@step(u'I click on sign in')
def step_impl(context):
	context.page_object.click_on_sign_in()

@step(u'I fill my email "{email}" on create an account field')
def step_impl(context, email):
	context.page_object = AuthenticationActions(context.driver)
	context.page_object.email_in_create_account(email)

@step(u'I click on create an account')
def step_impl(context):
	context.page_object.click_on_create_account()

@step(u'I should go to "{screen}" screen')
def step_impl(context,screen):
	assert_that(context.page_object.get_personal_info(), equal_to(screen))

@step(u'I click on Mr title')
def step_impl(context):
	context.page_object.click_on_mr_title()

@step(u'I type "{first_name}" on first name')
def step_impl(context, first_name):
	context.page_object.type_in_first_name(first_name)

@step(u'I type "{password}" on password')
def step_impl(context, password):
	context.page_object.type_in_password(password)

@step(u'I type "{address_fn}" on my address first name')
def step_impl(context, address_fn):
	context.page_object.type_in_address_first_name(address_fn)

@step(u'I type "{address_ln}" on my address last name')
def step_impl(context, address_ln):
	context.page_object.type_in_address_last_name(address_ln)

@step(u'I type "{address}" on address')
def step_impl(context, address):
	context.page_object.type_in_address(address)

@step(u'I type "{city}" on city')
def step_impl(context, city):
	context.page_object.type_in_city(city)

@step(u'I type "{zipcode}" on zip code')
def step_impl(context, zipcode):
	context.page_object.type_in_zip_code(zipcode)

@step(u'I select "{state}" on state') 
def step_impl(context,state):
	context.page_object.select_in_combo_box(state)

@step(u'I type "{phone}" on mobile phone')
def step_impl(context, phone):
	context.page_object.type_in_mobile_phone(phone)

@step(u'I type "{alias}" on address alias')
def step_impl(context, alias):
	context.page_object.type_in_address_alias(alias)

@step(u'I click on register')
def step_impl(context):
	context.page_object.click_on_register()

@step(u'I should see my account information')
def step_impl(context):
	assert_that(context.page_object.get_my_account_info(), equal_to("MY ACCOUNT"))
	context.page_object.click_on_sign_out()
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
from behave import given, when, then
@given('v is a Vector of "{x:f}", "{y:f}", "{z:f}"')
def step_impl(context, x, y, z):
	context.p = tuples.Vector(x, y, z)

@then(u'v = tuple "{x:f}", "{y:f}", "{z:f}", "{w:f}"')
def step_impl(context, x, y, z, w):
	assert tuples.t_eq(context.p, (x, y, z, w))
```

id : seed_task_32
name : ko_32
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework : 
```gherkin
Scenario: Create an account - without typing password
	Given I am on Home Page
	And I click on sign in
	When I fill my email "keaa@keaaaaaaaa.com.br" on create an account field
	And I click on create an account
	Then I should go to "YOUR PERSONAL INFORMATION" screen
	When I click on Mr title
	And I type "keakea" on first name
	And I type "Junior" on last name
	And I type "Seattle" on my address first name
	And I type "Los Angeles" on my address last name
	And I type "Barão de Bonito" on address
	And I type "Recife" on city
	And I select "California" on state
	And I type "00000" on zip code
	And I type "9999999999" on mobile phone
	And I type "kea" on address alias
	And I click on register
	Then System should display the message "passwd is required."
```
input = ""
output:
```python
@step(u'I am on Home Page')
def step_impl(context):
	context.page_object = HomeActions(context.driver)
	context.page_object.open_application(context.base_url)

@step(u'I click on sign in')
def step_impl(context):
	context.page_object.click_on_sign_in()

@step(u'I fill my email "{email}" on create an account field')
def step_impl(context, email):
	context.page_object = AuthenticationActions(context.driver)
	context.page_object.email_in_create_account(email)

@step(u'I click on create an account')
def step_impl(context):
	context.page_object.click_on_create_account()

@step(u'I should go to "{screen}" screen')
def step_impl(context,screen):
	assert_that(context.page_object.get_personal_info(), equal_to(screen))

@step(u'I click on Mr title')
def step_impl(context):
	context.page_object.click_on_mr_title()

@step(u'I type "{first_name}" on first name')
def step_impl(context, first_name):
	context.page_object.type_in_first_name(first_name)

@step(u'I type "{last_name}" on last name')
def step_impl(context, last_name):
	context.page_object.type_in_last_name(last_name)

@step(u'I type "{address_fn}" on my address first name')
def step_impl(context, address_fn):
	context.page_object.type_in_address_first_name(address_fn)

@step(u'I type "{address_ln}" on my address last name')
def step_impl(context, address_ln):
	context.page_object.type_in_address_last_name(address_ln)

@step(u'I type "{address}" on address')
def step_impl(context, address):
	context.page_object.type_in_address(address)

@step(u'I type "{city}" on city')
def step_impl(context, city):
	context.page_object.type_in_city(city)

@step(u'I type "{zipcode}" on zip code')
def step_impl(context, zipcode):
	context.page_object.type_in_zip_code(zipcode)

@step(u'I select "{state}" on state') 
def step_impl(context,state):
	context.page_object.select_in_combo_box(state)

@step(u'I type "{phone}" on mobile phone')
def step_impl(context, phone):
	context.page_object.type_in_mobile_phone(phone)

@step(u'I type "{alias}" on address alias')
def step_impl(context, alias):
	context.page_object.type_in_address_alias(alias)

@step(u'I click on register')
def step_impl(context):
	context.page_object.click_on_register()

@step(u'I should see my account information')
def step_impl(context):
	assert_that(context.page_object.get_my_account_info(), equal_to("MY ACCOUNT"))
	context.page_object.click_on_sign_out()
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
name : ko_34
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework : 
```gherkin
Scenario: Buy a product
	Given I am on Home Page
	And I click on sign in
	And I logged in
	And I go to home page 
	When I click on Blouse
	And I click add to cart
	And I click proceed to checkout
	And I confirm the proceed to checkout 
	And I click on proceed to checkout on address screen
	And I click on proceed to checkout on shipping screen
```
input = ""
output:
```python
@step(u'I am on Home Page')
def step_impl(context):
	context.page_object = HomeActions(context.driver)
	context.page_object.open_application(context.base_url)

@step(u'I click on sign in')
def step_impl(context):
	context.page_object.click_on_sign_in()

@step(u'I logged in')
def step_impl(context):
	context.page_object = AuthenticationActions(context.driver)
	context.page_object.email_in('keaaaa@keaaaaa.com.br')
	context.page_object.type_in_password('123456')
	context.page_object.click_on_sign_in()

@step(u'I go to home page')
def step_impl(context):
	context.page_object = HomeActions(context.driver)
	context.page_object.open_application(context.base_url)

@step(u'I click on Blouse')
def step_impl(context):
	context.page_object = HomeActions(context.driver)
	context.page_object.click_on_blouse()

@step(u'I click add to cart')
def step_impl(context):
	context.page_object = ProductPageActions(context.driver)
	context.page_object.click_on_add_to_cart()

@step(u'I click proceed to checkout')
def step_impl(context):
	context.page_object.click_on_proceed_to_checkout()

@step(u'I confirm the proceed to checkout')
def step_impl(context):
	context.page_object = ShippingPageActions(context.driver)
	context.page_object.confirm_proceed_to_checkout()

@step(u'I click on proceed to checkout on address screen')
def step_impl(context):
	context.page_object = ShippingPageActions(context.driver)
	context.page_object.proceed_to_checkout_address()

@step(u'I click on proceed to checkout on shipping screen')
def step_impl(context):
	context.page_object = ShippingPageActions(context.driver)
	context.page_object.click_on_terms_of_service()
	context.page_object.proceed_to_checkout_shipping()
```

id : seed_task_35
name : ko_35
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework : 
```gherkin
Scenario: Manage namespaces unification
	Given at least one docker container is running
	When I discover namespaces
	Then an external namespace exists
	When I remove all docker containers
	And I discover namespaces
	Then no external namespace exists
```
input = ""
output:
```python
@given(u'at least one docker container is running')
def step_impl(context):
	output = subprocess.check_output('docker ps', shell=True)
	lines = [line for line in output.decode('utf-8').split('\n') if line]
	if len(lines) <= 1:
		subprocess.check_output('docker run -d -t progrium/busybox', shell=True)

@when(u'I discover namespaces')
def step_impl(context):
	context.discovered = Namespace.discover()

@then(u'an external namespace exists')
def step_impl(context):
	external_namespaces = [ns for ns in context.discovered if ns.is_external()]
	assert len(external_namespaces) > 0

@when(u'I remove all docker containers')
def step_impl(context):
	subprocess.check_output('docker stop $(docker ps -a -q)', shell=True)

@then(u'no external namespace exists')
def step_impl(context):
	external_namespaces = [ns for ns in context.discovered if ns.is_external()]
	assert len(external_namespaces) == 0
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
name : ko_38
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework : 
```gherkin
Scenario: Constructing the PPM pixel data
	Given c = canvas(5, 3)
	And c1 = color(1.5, 0.0, 0.0)
	And c2 = color(0.0, 0.5, 0.0)
	And c3 = color(-0.5, 0.0, 1.0)
	When write_pixel(c, 0, 0, c1)
	And write_pixel(c, 2, 1, c2)
	And write_pixel(c, 4, 2, c3)
	And ppm2 = canvas_to_ppm(c)
	Then lines 4-6 of ppm2 are
	"""
	255 0 0 0 0 0 0 0 0 0 0 0 0 0 0
	0 0 0 0 0 0 0 128 0 0 0 0 0 0 0
	0 0 0 0 0 0 0 0 0 0 0 0 0 0 255
	"""
```
input = ""
output:
```python
from behave import given, when, then

@given('c = Canvas({width:d}, {height:d})')
def step_impl(context, width, height):
	context.c = canvas.Canvas(width, height)

@given('c1 = Color({r:f}, {g:f}, {b:f})')
def step_impl(context, r, g, b):
	context.c1 = tuples.Color(r, g, b)

@given('c2 = Color({r:f}, {g:f}, {b:f})')
def step_impl(context, r, g, b):
	context.c2 = tuples.Color(r, g, b)

@given('c3 = Color({r:f}, {g:f}, {b:f})')
def step_impl(context, r, g, b):
	context.c3 = tuples.Color(r, g, b)

@when('write_pixel({can:w}, {x:d}, {y:d}, {color:w})')
def step_impl(context, x, y):
	canvas.write_pixel(getattr(context, can), w, h, getattr(context, color))

@when('write_pixel({can:w}, {x:d}, {y:d}, {color:w})')
def step_impl(context, x, y):
	canvas.write_pixel(getattr(context, can), w, h, getattr(context, color))

@when('write_pixel({can:w}, {x:d}, {y:d}, {color:w})')
def step_impl(context, x, y):
	canvas.write_pixel(getattr(context, can), w, h, getattr(context, color))

@when('ppm2 = canvas_to_ppm(c)')
def step_impl(context):
	context.ppm2 = list(canvas.canvas_to_ppm(context.c))

@then('lines 4-6 of ppm2 are')
def step_impl(context):
	print(f'{"".join(context.ppm2[4:6])}')
	print(f'{context.ppm2}')
	print(f'{context.text}')
	assert "".join(context.ppm2[4:6]) == context.text
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
name : ko_40
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework : 
```gherkin
Scenario: Manage device discovery
	When I discover devices
	Then "lo" is found in discovered devices
	And "eth2" is found in discovered devices
	And no exception is raised
```
input = ""
output:
```python
@when(u'I discover devices')
def step_impl(context):
	context.devices = Device.discover()

@then(u'"{device_name}" is found in discovered devices')
def step_impl(context, device_name):
	assert hasattr(context, 'devices')
	found = False
	for device in context.devices:
		if device_name == device.name:
			found = True
	assert found

@then(u'no exception is raised')
def step_impl(context):
	assert not hasattr(context, 'exception')
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
name : ko_43
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework : 
```gherkin
Scenario: When I try to buy a product without being logged in
	Given I am on Home Page
	And I click on Blouse
	And I click add to cart
	And I click proceed to checkout
	When I confirm the proceed to checkout
	Then I should be redirect to authentication page
```
input = ""
output:
```python
from behave import given, when, then
@given(u'I am on Home Page')
def step_impl(context):
    context.page_object = HomeActions(context.driver)
    context.page_object.open_application(context.base_url)

@given(u'I click on Blouse')
def step_impl(context):
    context.page_object = HomeActions(context.driver)
    context.page_object.click_on_blouse()
    
@given(u'I click add to cart')
def step_impl(context):
    context.page_object = ProductPageActions(context.driver)
    context.page_object.click_on_add_to_cart()
    
@given(u'I click proceed to checkout')
def step_impl(context):
    context.page_object.click_on_proceed_to_checkout()
    
@when(u'I confirm the proceed to checkout')
def step_impl(context):
    context.page_object = ShippingPageActions(context.driver)
    context.page_object.confirm_proceed_to_checkout()
    
@then(u'I should be redirect to authentication page')
def step_impl(context):
    context.page_object = AuthenticationActions(context.driver)
    assert_that(context.page_object.get_authentication_text(), equal_to("AUTHENTICATION"))
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
name : ko_46
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework : 
```gherkin
Scenario Outline: Test out logging in via the api-ath and going to the homepage
	Given a super user with username "<user>" and password "<password>"
	And I am on the page with relative url "/api-auth/login"
	When I put "<user>" in the field with name "username"
	And I put "<password>" in the field with name "password"
	And I click the element with name "submit"
	Then I should be on the page with relative url "/accounts/profile/"
	Given I am on the page with relative url "/"
	Then I should be on the page with relative url "/#/"

  Examples:
	|user|password|
	|foo3|bar3	|
```
input = ""
output:
```python
@given('a (?P<super_>super )?user with username "(?P<username>.*)" and password "(?P<password>.*)"')
def step_impl(context, super_, username, password):
	from django.contrib.auth.models import User, Group

	group, _ = Group.objects.get_or_create(name='Users')
	group.save()
	if super_:
		u = User.objects.create_superuser(username=username, email="test@test.com", password=password)
		u.save()
	else:
		u = User(username=username, email='foo@example.com')
		u.set_password(password)
		u.save()

@given('I am on (?:the )?page with relative url "(?P<url>.*)"')
def step_impl(context, url):
	full_url = urljoin(context.config.server_url, url)
	context.browser.visit(full_url)

@when('I put "(?P<value>.*)" in the field with (?P<selector>name|id|css|xpath) "(?P<key>.*)"')
def step_impl(context, value, selector, key):
	if value == "null":
		value = ""  # allows you to put "null" into a field to not fill it in
	if selector == "name":
		context.browser.fill(key, value)
	elif selector == "id":
		context.browser.find_by_id(key).fill(value)
	elif selector == "css":
		context.browser.find_by_css(key).fill(value)
	elif selector == "xpath":
		context.browser.find_by_xpath(key).fill(value)

@when(
	'I (?P<action>click|mouse\wover|right\wclick|double\wclick) the (?:button|element) with (?P<selector>name|id|css|xpath) "(?P<value>.*)"')
def step_impl(context, action, selector, value):
	if action == "click":
		if selector == 'name':
			context.browser.find_by_name(value).click()
		elif selector == 'id':
			context.browser.find_by_id(value).click()
		elif selector == 'css':
			context.browser.find_by_css(value).click()
		elif selector == "xpath":
			context.browser.find_by_xpath(value).click()
	elif action == "mouse over":
		if selector == 'name':
			context.browser.find_by_name(value).mouse_over()
		elif selector == 'id':
			context.browser.find_by_id(value).mouse_over()
		elif selector == 'css':
			context.browser.find_by_css(value).mouse_over()
		elif selector == "xpath":
			context.browser.find_by_xpath(value).mouse_over()
	elif action == "right click":
		if selector == 'name':
			context.browser.find_by_name(value).right_click()
		elif selector == 'id':
			context.browser.find_by_id(value).right_click()
		elif selector == 'css':
			context.browser.find_by_css(value).right_click()
		elif selector == "xpath":
			context.browser.find_by_xpath(value).right_click()
	elif action == "double click":
		if selector == 'name':
			context.browser.find_by_name(value).double_click()
		elif selector == 'id':
			context.browser.find_by_id(value).double_click()
		elif selector == 'css':
			context.browser.find_by_css(value).double_click()
		elif selector == "xpath":
			context.browser.find_by_xpath(value).double_click()

@then('I should (?P<not_>not )?be on (?:the )?page with relative url "(?P<url>.*)"')
def step_impl(context, not_, url):
	time.sleep(1)
	full_url = urljoin(context.config.server_url, url)
	if not_:
		assert not context.browser.url == full_url, "Expected not to be on page %s, instead got %s" % (
			full_url, context.browser.url)
	else:
		assert context.browser.url == full_url, "Expected to be on page %s, instead got %s" % (
			full_url, context.browser.url)
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
name : ko_48
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework : 
```gherkin
Scenario Outline: Test out logging out via the api-ath and going to the homepage
	Given a super user with username "<user>" and password "<password>"
	And I am on the page with relative url "/api-auth/login"
	When I put "<user>" in the field with name "username"
	And I put "<password>" in the field with name "password"
	And I click the element with name "submit"
	Then I should be on the page with relative url "/accounts/profile/"
	Given I am on the page with relative url "/logout/"
	Then I should be on the page with relative url "/login/"

  Examples:
	|user|password|
	|foo4|bar4	|
```
input = ""
output:
```python
@given('a (?P<super_>super )?user with username "(?P<username>.*)" and password "(?P<password>.*)"')
def step_impl(context, super_, username, password):
	from django.contrib.auth.models import User, Group

	group, _ = Group.objects.get_or_create(name='Users')
	group.save()
	if super_:
		u = User.objects.create_superuser(username=username, email="test@test.com", password=password)
		u.save()
	else:
		u = User(username=username, email='foo@example.com')
		u.set_password(password)
		u.save()

@given('I am on (?:the )?page with relative url "(?P<url>.*)"')
def step_impl(context, url):
	full_url = urljoin(context.config.server_url, url)
	context.browser.visit(full_url)

@when('I put "(?P<value>.*)" in the field with (?P<selector>name|id|css|xpath) "(?P<key>.*)"')
def step_impl(context, value, selector, key):
	if value == "null":
		value = ""  # allows you to put "null" into a field to not fill it in
	if selector == "name":
		context.browser.fill(key, value)
	elif selector == "id":
		context.browser.find_by_id(key).fill(value)
	elif selector == "css":
		context.browser.find_by_css(key).fill(value)
	elif selector == "xpath":
		context.browser.find_by_xpath(key).fill(value)

@when('I (?P<action>click|mouse\wover|right\wclick|double\wclick) the (?:button|element) with (?P<selector>name|id|css|xpath) "(?P<value>.*)"')
def step_impl(context, action, selector, value):
	if action == "click":
		if selector == 'name':
			context.browser.find_by_name(value).click()
		elif selector == 'id':
			context.browser.find_by_id(value).click()
		elif selector == 'css':
			context.browser.find_by_css(value).click()
		elif selector == "xpath":
			context.browser.find_by_xpath(value).click()
	elif action == "mouse over":
		if selector == 'name':
			context.browser.find_by_name(value).mouse_over()
		elif selector == 'id':
			context.browser.find_by_id(value).mouse_over()
		elif selector == 'css':
			context.browser.find_by_css(value).mouse_over()
		elif selector == "xpath":
			context.browser.find_by_xpath(value).mouse_over()
	elif action == "right click":
		if selector == 'name':
			context.browser.find_by_name(value).right_click()
		elif selector == 'id':
			context.browser.find_by_id(value).right_click()
		elif selector == 'css':
			context.browser.find_by_css(value).right_click()
		elif selector == "xpath":
			context.browser.find_by_xpath(value).right_click()
	elif action == "double click":
		if selector == 'name':
			context.browser.find_by_name(value).double_click()
		elif selector == 'id':
			context.browser.find_by_id(value).double_click()
		elif selector == 'css':
			context.browser.find_by_css(value).double_click()
		elif selector == "xpath":
			context.browser.find_by_xpath(value).double_click()

@then('I should (?P<not_>not )?be on (?:the )?page with relative url "(?P<url>.*)"')
def step_impl(context, not_, url):
	time.sleep(1)
	full_url = urljoin(context.config.server_url, url)
	if not_:
		assert not context.browser.url == full_url, "Expected not to be on page %s, instead got %s" % (
			full_url, context.browser.url)
	else:
		assert context.browser.url == full_url, "Expected to be on page %s, instead got %s" % (
			full_url, context.browser.url)
```

id : seed_task_49
name : ko_49
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework : 
```gherkin
Scenario Outline: Test Logging in via the login page invalid
	Given an inactive user with username "<user>" and password "<password>"
	And I am on the page with relative url "/login/"
	When I put "<user>" in the field with name "username"
	And I put "<password>" in the field with name "password"
	And I click the element with name "submit"

  Examples:
	| user | password |
	| foo5 | bar5	 |
```
input = ""
output:
```python
@given('an inactive user with username "(?P<username>.*)" and password "(?P<password>.*)"')
def step_impl(context, username, password):
	from django.contrib.auth.models import User

	u = User(username=username, email='foo1@example.com')
	u.set_password(password)
	u.is_active = False
	u.save()

@given('I am on (?:the )?page with relative url "(?P<url>.*)"')
def step_impl(context, url):
	full_url = urljoin(context.config.server_url, url)
	context.browser.visit(full_url)

@when('I put "(?P<value>.*)" in the field with (?P<selector>name|id|css|xpath) "(?P<key>.*)"')
def step_impl(context, value, selector, key):
	if value == "null":
		value = ""  # allows you to put "null" into a field to not fill it in
	if selector == "name":
		context.browser.fill(key, value)
	elif selector == "id":
		context.browser.find_by_id(key).fill(value)
	elif selector == "css":
		context.browser.find_by_css(key).fill(value)
	elif selector == "xpath":
		context.browser.find_by_xpath(key).fill(value)

@when('I (?P<action>click|mouse\wover|right\wclick|double\wclick) the (?:button|element) with (?P<selector>name|id|css|xpath) "(?P<value>.*)"')
def step_impl(context, action, selector, value):
	if action == "click":
		if selector == 'name':
			context.browser.find_by_name(value).click()
		elif selector == 'id':
			context.browser.find_by_id(value).click()
		elif selector == 'css':
			context.browser.find_by_css(value).click()
		elif selector == "xpath":
			context.browser.find_by_xpath(value).click()
	elif action == "mouse over":
		if selector == 'name':
			context.browser.find_by_name(value).mouse_over()
		elif selector == 'id':
			context.browser.find_by_id(value).mouse_over()
		elif selector == 'css':
			context.browser.find_by_css(value).mouse_over()
		elif selector == "xpath":
			context.browser.find_by_xpath(value).mouse_over()
	elif action == "right click":
		if selector == 'name':
			context.browser.find_by_name(value).right_click()
		elif selector == 'id':
			context.browser.find_by_id(value).right_click()
		elif selector == 'css':
			context.browser.find_by_css(value).right_click()
		elif selector == "xpath":
			context.browser.find_by_xpath(value).right_click()
	elif action == "double click":
		if selector == 'name':
			context.browser.find_by_name(value).double_click()
		elif selector == 'id':
			context.browser.find_by_id(value).double_click()
		elif selector == 'css':
			context.browser.find_by_css(value).double_click()
		elif selector == "xpath":
			context.browser.find_by_xpath(value).double_click()
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
name : ko_51
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework : 
```gherkin
Scenario Outline: Test Logging in via the login page
	Given a user with username "<user>" and password "<password>"
	And I am on the page with relative url "/login/"
	When I put "<user>" in the field with name "username"
	And I put "<password>" in the field with name "password"
	And I click the element with name "submit"

  Examples:
	|user|password|
	|foo6|bar6	|
```
input = ""
output:
```python
@given('a (?P<super_>super )?user with username "(?P<username>.*)" and password "(?P<password>.*)"')
def step_impl(context, super_, username, password):
	from django.contrib.auth.models import User, Group

	group, _ = Group.objects.get_or_create(name='Users')
	group.save()
	if super_:
		u = User.objects.create_superuser(username=username, email="test@test.com", password=password)
		u.save()
	else:
		u = User(username=username, email='foo@example.com')
		u.set_password(password)
		u.save()

@given('I am on (?:the )?page with relative url "(?P<url>.*)"')
def step_impl(context, url):
	full_url = urljoin(context.config.server_url, url)
	context.browser.visit(full_url)

@when('I put "(?P<value>.*)" in the field with (?P<selector>name|id|css|xpath) "(?P<key>.*)"')
def step_impl(context, value, selector, key):
	if value == "null":
		value = ""  # allows you to put "null" into a field to not fill it in
	if selector == "name":
		context.browser.fill(key, value)
	elif selector == "id":
		context.browser.find_by_id(key).fill(value)
	elif selector == "css":
		context.browser.find_by_css(key).fill(value)
	elif selector == "xpath":
		context.browser.find_by_xpath(key).fill(value)

@when(
	'I (?P<action>click|mouse\wover|right\wclick|double\wclick) the (?:button|element) with (?P<selector>name|id|css|xpath) "(?P<value>.*)"')
def step_impl(context, action, selector, value):
	if action == "click":
		if selector == 'name':
			context.browser.find_by_name(value).click()
		elif selector == 'id':
			context.browser.find_by_id(value).click()
		elif selector == 'css':
			context.browser.find_by_css(value).click()
		elif selector == "xpath":
			context.browser.find_by_xpath(value).click()
	elif action == "mouse over":
		if selector == 'name':
			context.browser.find_by_name(value).mouse_over()
		elif selector == 'id':
			context.browser.find_by_id(value).mouse_over()
		elif selector == 'css':
			context.browser.find_by_css(value).mouse_over()
		elif selector == "xpath":
			context.browser.find_by_xpath(value).mouse_over()
	elif action == "right click":
		if selector == 'name':
			context.browser.find_by_name(value).right_click()
		elif selector == 'id':
			context.browser.find_by_id(value).right_click()
		elif selector == 'css':
			context.browser.find_by_css(value).right_click()
		elif selector == "xpath":
			context.browser.find_by_xpath(value).right_click()
	elif action == "double click":
		if selector == 'name':
			context.browser.find_by_name(value).double_click()
		elif selector == 'id':
			context.browser.find_by_id(value).double_click()
		elif selector == 'css':
			context.browser.find_by_css(value).double_click()
		elif selector == "xpath":
			context.browser.find_by_xpath(value).double_click()
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
name : ko_53
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework : 
```gherkin
Scenario Outline: Test invalid Logging in via the login page
	Given a user with username "<user>" and password "<password>"
	And I am on the page with relative url "/login/"
	When I put "<user>" in the field with name "username"
	And I put "password" in the field with name "password"
	And I click the element with name "submit"

  Examples:
	|user|password|
	|foo7|bar7	|
```
input = ""
output:
```python
@given('a (?P<super_>super )?user with username "(?P<username>.*)" and password "(?P<password>.*)"')
def step_impl(context, super_, username, password):
	from django.contrib.auth.models import User, Group

	group, _ = Group.objects.get_or_create(name='Users')
	group.save()
	if super_:
		u = User.objects.create_superuser(username=username, email="test@test.com", password=password)
		u.save()
	else:
		u = User(username=username, email='foo@example.com')
		u.set_password(password)
		u.save()

@given('I am on (?:the )?page with relative url "(?P<url>.*)"')
def step_impl(context, url):
	full_url = urljoin(context.config.server_url, url)
	context.browser.visit(full_url)

@when('I put "(?P<value>.*)" in the field with (?P<selector>name|id|css|xpath) "(?P<key>.*)"')
def step_impl(context, value, selector, key):
	if value == "null":
		value = ""  # allows you to put "null" into a field to not fill it in
	if selector == "name":
		context.browser.fill(key, value)
	elif selector == "id":
		context.browser.find_by_id(key).fill(value)
	elif selector == "css":
		context.browser.find_by_css(key).fill(value)
	elif selector == "xpath":
		context.browser.find_by_xpath(key).fill(value)

@when(
	'I (?P<action>click|mouse\wover|right\wclick|double\wclick) the (?:button|element) with (?P<selector>name|id|css|xpath) "(?P<value>.*)"')
def step_impl(context, action, selector, value):
	if action == "click":
		if selector == 'name':
			context.browser.find_by_name(value).click()
		elif selector == 'id':
			context.browser.find_by_id(value).click()
		elif selector == 'css':
			context.browser.find_by_css(value).click()
		elif selector == "xpath":
			context.browser.find_by_xpath(value).click()
	elif action == "mouse over":
		if selector == 'name':
			context.browser.find_by_name(value).mouse_over()
		elif selector == 'id':
			context.browser.find_by_id(value).mouse_over()
		elif selector == 'css':
			context.browser.find_by_css(value).mouse_over()
		elif selector == "xpath":
			context.browser.find_by_xpath(value).mouse_over()
	elif action == "right click":
		if selector == 'name':
			context.browser.find_by_name(value).right_click()
		elif selector == 'id':
			context.browser.find_by_id(value).right_click()
		elif selector == 'css':
			context.browser.find_by_css(value).right_click()
		elif selector == "xpath":
			context.browser.find_by_xpath(value).right_click()
	elif action == "double click":
		if selector == 'name':
			context.browser.find_by_name(value).double_click()
		elif selector == 'id':
			context.browser.find_by_id(value).double_click()
		elif selector == 'css':
			context.browser.find_by_css(value).double_click()
		elif selector == "xpath":
			context.browser.find_by_xpath(value).double_click()
```

id : seed_task_54
name : ko_54
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework : 
```gherkin
Scenario: Start A List For One User
	Given Edith has opened a browser
	When Edith goes to the home page
	Then she notices the page title and header mention to-do lists
	Then she is invited to enter a to-do item straight away
	Then she types "Buy peacock feathers" into the text box and hit's enter
	Then the page now lists "1: Buy peacock feathers" as an item
	And there is still a text box inviting her to add another item.
	Then she types "Use peacock feathers to make a fly" into the text box and hit's enter
	And the page now lists "1: Use peacock feathers to make a fly" as an item
	And the page now lists "2: Buy peacock feathers" as an item
```
input = ""
output:
```python
@given('{name} has opened a browser')
def step_impl(context, name):
	context.name = name
	if hasattr(context, 'browser'):
		context.browser.close()
		context.browser.quit()

	context.browser = Firefox()

	# there is a known bug in selenium, runnign phantomjs as grantchild process, for now let's stick with Firefox...
	# context.browser = PhantomJS()

@when('Edith goes to the home page')
def step_impl(context):
	context.browser.get(context.test.live_server_url)

@then('She notices the page title and header mention to-do lists')
def step_impl(context):
	context.test.assertIn('To-Do', context.browser.title)
	header = context.browser.find_element_by_tag_name("h1").text
	context.test.assertIn('To-Do', header)

@then('She is invited to enter a to-do item straight away')
def step_impl(context):
	inputbox = context.browser.find_element_by_id('id_new_item')
	context.test.assertEqual(
		inputbox.get_attribute('placeholder'),
		'Enter a to-do item'
	)

@then('She types "{text}" into the text box and hit\'s enter')
def step_impl(context, text):
	inputbox = context.browser.find_element_by_id('id_new_item')
	inputbox.send_keys(text)
	inputbox.send_keys(Keys.ENTER)

@then('The page now lists "{idx:d}: {text}" as an item')
def step_impl(context, idx, text):
	wait_for_row_in_list_table(context, '%d: %s' % (idx, text))

@then(u'There is still a text box inviting her to add another item.')
def step_impl(context):
	context.browser.find_element_by_id('id_new_item')
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
from behave import given, when, then
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
name : ko_58
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework : 
```gherkin
Scenario: Multiple users can start lists	
	Given Edith has opened a browser
	When Edith starts a new todo list
	Then She notices that her list has a unique URL
	Given Francis has opened a browser
	When Francis visits the home page, there is no sign of Edith's list
	Then Francis starts a new list by entering a new item.
	And Francis gehts his own unique URL
	And again, there is no trace of Edith's list
```
input = ""
output:
```python
@given('{name} has opened a browser')
def step_impl(context, name):
	context.name = name
	if hasattr(context, 'browser'):
		context.browser.close()
		context.browser.quit()

	context.browser = Firefox()

	# there is a known bug in selenium, runnign phantomjs as grantchild process, for now let's stick with Firefox...
	# context.browser = PhantomJS()

@when('Edith starts a new todo list')
def step_impl(context):
	context.browser.get(context.test.live_server_url)
	inputbox = context.browser.find_element_by_id('id_new_item')
	inputbox.send_keys('Buy peacock feathers')
	inputbox.send_keys(Keys.ENTER)
	wait_for_row_in_list_table(context, '1: Buy peacock feathers')

@then('She notices that her list has a unique URL')
def step_impl(context):
	context.edith_list_url = context.browser.current_url
	context.test.assertRegex(context.edith_list_url, '/lists/.+')

@when('Francis visits the home page, there is no sign of Edith\'s list')
def step_impl(context):
	context.browser.get(context.test.live_server_url)
	page_text = context.browser.find_element_by_tag_name('body').text
	context.test.assertNotIn('Buy peacock feathers', page_text)

@then('Francis starts a new list by entering a new item.')
def step_impl(context):
	inputbox = context.browser.find_element_by_id('id_new_item')
	inputbox.send_keys('Buy milk')
	inputbox.send_keys(Keys.ENTER)
	wait_for_row_in_list_table(context, '1: Buy milk')

@then('Francis gehts his own unique URL')
def step_impl(context):
	context.francis_list_url = context.browser.current_url
	context.test.assertRegex(context.francis_list_url, '/lists/.+')
	context.test.assertNotEqual(context.francis_list_url, context.edith_list_url)

@then('again, there is no trace of Edith\'s list')
def step_impl(context):
	page_text = context.browser.find_element_by_tag_name('body').text
	context.test.assertNotIn('Buy peacock feathers', page_text)
	context.test.assertIn('Buy milk', page_text)
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
@given(u'two pieces')
def step_impl(context):
	raise NotImplementedError(u'STEP: Given two pieces')

@when(u'one piece takes another')
def step_impl(context):
	raise NotImplementedError(u'STEP: When one piece takes another')

@then(u'the defender\'s space is occupied by the attacker')
def step_impl(context):
	raise NotImplementedError(u'STEP: Then the defender\'s space is occupied by the attacker')

@then(u'the defending piece is removed from play')
def step_impl(context):
	raise NotImplementedError(u'STEP: Then the defending piece is removed from play')

@then(u'your turn ends')
def step_impl(context):
	raise NotImplementedError(u'STEP: Then your turn ends')
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
name : ko_63
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework : 
```gherkin
Scneario: user can mark a part of text as pagination
	When
	Then in the right pane option appears to treat this as pagination
```
input = ""
output:
```python
@then('right pane is populated with correction suggestions')
def step_impl(context):
	''' '''
	right_pane = context.browser.find_element_
	
@when('')
def step_impl(context):
	pass
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
name : ko_65
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework : 
```gherkin
Scenario: user cannot find correct version of a word
	Given user is on the page containing incrorrect words
	and uder clicked an incorrect word
	option "none of the above"
	When User clicks on the option
	Then input field appears with greek aplhabet below
	And user can type a word clicking on greek alphabet letters
	And when lenght of the input >2 Save button is enabled
	And user clicks on save button 
	# and in  
	And right pane is emptied
```
input = ""
output:
```python
@given('user is on page with lists of texts')
def step_impl(context):
	context.browser.get("http://localhost:8000/edit")

@when('user clicks on a text')
def step_impl(context):
	''' '''
	context.browser.find_element
@then('user is redirected to the first page contaning incorrect words')
def step_impl(context):
	''' ''' 
	#assert the url is correct
	assert context.browser.current_url ==
	#assert at least one incorrect words
	assert context.browser.find_element_

@given('user is on text page')
def step_impl(context):
	context.execute_steps('''
		given user is on page with lists of texts
		when user clicks on a text
		''')

@when('user click on an incorrect word')
def step_impl(context):
	''' Incorrect word:corr="0" '''
	context.browser.find_element_by() is not None

@then('right pane is populated with correction suggestions')
def step_impl(context):
	''' '''
	right_pane = context.browser.find_element_
	
@when('')
def step_impl(context):
	pass

@when('')
def step_impl(context):
	pass
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
name : ko_67
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework : 
```gherkin
Scenario: Successful checkout of multi-size product
	Given I open Suitsupply website
	And I close cookie bar
	And I close country verification bar
	When I select 'Clothing' from the menu
	And I choose 'Suits' category
	And I select product #'1' from lister
	And I click on 'Select size' dropdown
	And I select size #'4' from dropdown
	And I click on 'ADD TO BAG'
	And I click on 'Secure checkout' on Minicart
	And I click on 'Proceed to purchase' on Cart page
	And I enter user 'test@testtest.nl' on Login page
	And I enter password 'test12345' on Login page
	And I click on 'Login & continue'
	Then Checkout page opens
```
input = ""
output:
```python
@given("I open Suitsupply website")
def step_impl(context):
	context.browser.get("https://eu.suitsupply.com/en/home")

@given("I close cookie bar")
def step_impl(context):
	context.browser.find_element_by_css_selector('.js-cookie-bar-close').click()

@given("I close country verification bar")
def step_impl(context):
	context.browser.find_element_by_css_selector('.js-country-verification-bar-close').click()

@when("I select 'Clothing' from the menu")
def step_impl(context):
	context.browser.find_element_by_css_selector('.sel-clothing').click()

@when("I choose 'Suits' category")
def step_impl(context):
	context.browser.find_element_by_css_selector('.sel-category.sel-suits').click()

@when("I select product #'{prod_num}' from lister")
def step_impl(context, prod_num):
	context.browser.find_element_by_css_selector(f'.js-category-content .sel-product-container:nth-child({prod_num})').click()

@when("I click on 'Select size' dropdown")
def step_impl(context):
	context.browser.find_element_by_css_selector('.sel-size-field').click()

@when("I select size #'{size_num}' from dropdown")
def step_impl(context, size_num):
	context.browser.find_element_by_css_selector(f'.sel-size-field > option:nth-child({size_num})').click()

@when("I click on 'ADD TO BAG'")
def step_impl(context):
	context.browser.find_element_by_css_selector('.sel-controls-container button.js-add-to-bag-btn').click()

@when("I click on 'Secure checkout' on Minicart")
def step_impl(context):
	context.browser.find_element_by_css_selector('.sel-checkout-trigger').click()

@when("I click on 'Proceed to purchase' on Cart page")
def step_impl(context):
	context.browser.find_element_by_css_selector('.js-purchase-btn.sel-checkout-trigger').click()

@when("I enter user '{user}' on Login page")
def step_impl(context, user):
	user_input = context.browser.find_element_by_css_selector('#dwfrm_login_registered_username')
	user_input.clear()
	user_input.send_keys(user)

@when("I enter password '{password}' on Login page")
def step_impl(context, password):
	password_input = context.browser.find_element_by_css_selector('#dwfrm_login_registered_password')
	password_input.clear()
	password_input.send_keys(password)

@when("I click on 'Login & continue'")
def step_impl(context):
	context.browser.find_element_by_css_selector('.sel-login-trigger.sel-login').click()

@then("Checkout page opens")
def step_impl(context):
	assert 'Check out' in context.browser.title, "Wrong page opened"
```

id : seed_task_68
name : ko_68
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework : 
```gherkin
Scenario: rdopkg new-version --bump-only
	Given a distgit at Version 2.0.0 and Release 3
	When I run rdopkg new-version --bump-only -n 2.1.0
	Then command output contains 'Action finished'
        Then .spec file tag Version is 2.1.0
        Then .spec file tag Release is 1%{?dist}
        Then .spec file doesn't contain patches_base
        Then .spec file contains new changelog entry with 1 lines
        Then new commit was created
        Then git is clean
        Then last commit message is:
            """
            foo-bar-2.1.0-1

            Changelog:
            - Update to 2.1.0
            """
```
input = ""
output:
```python
@given('a distgit at Version {version} and Release {release}')
def step_impl(context, version, release):
	_create_distgit(context, version, release)

@when('I run rdopkg {args}')
def step_impl(context, args):
	# proper argument parsing might be needed
	cmd = ['rdopkg'] + args.split(' ')
	context.command_output = run(*cmd, fatal=False, log_fail=False)

@then("command output contains '{rex}'")
def step_impl(context, rex):
	assert re.search(rex, context.command_output), "Did not find [{0}] in command output [{1}]".format(rex, context.command_output.encode('ascii', 'replace'))

@then('.spec file tag {tag} is {value}')
def step_impl(context, tag, value):
	spec = specfile.Spec()
	assert spec.get_tag(tag) == value, "{0} != {1}".format(spec.get_tag(tag), value)

@then('.spec file doesn\'t contain patches_base')
def step_impl(context):
	spec = specfile.Spec()
	assert spec.get_patches_base() == (None, 0)

@then('.spec file contains new changelog entry with {n:n} lines')
def step_impl(context, n):
	spec = specfile.Spec()
	entry = spec.get_last_changelog_entry()
	assert len(entry[1]) == n
	assert entry != context.old_changelog_entry

@then(u'git is clean')
def step_impl(context):
	assert git.is_clean(), git('status').encode('ascii', 'replace')

@then(u'last commit message is')
def step_impl(context):
	msg = git.current_commit_message()	
	assert context.text == msg, exdiff(context.text, msg, header="Commit message differs from expected format:")
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
from behave import given, when, then
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
name : ko_74
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework : 
```gherkin
Scenario: rdopkg new-version with upstream patches
	Given a distgit at Version 0.1 and Release 0.1
	Given a patches branch with 5 patches
	Given a new version 1.0.0 with 2 patches from patches branch
	When I run rdopkg new-version -lntU 1.0.0
	Then command output contains 'Action finished'
	Then .spec file tag Version is 1.0.0
	Then .spec file tag Release is 1%{?dist}
	Then .spec file doesn't contain patches_base
	Then .spec file has 3 patches defined
	Then .spec file contains new changelog entry with 1 lines
	Then new commit was created
	Then git is clean
	Then last commit message is:
	    """
	    foo-bar-1.0.0-1

	    Changelog:
	    - Update to 1.0.0
	    """

```
input = ""
output:
```python
@given('a distgit at Version {version} and Release {release}')
def step_impl(context, version, release):
	_create_distgit(context, version, release)

@given('a patches branch with {n:n} patches')
def step_impl(context, n):
	distgitmagic.create_sample_patches_branch(n)

@given('a new version {version} with {n:n} patches from patches branch')
def step_impl(context, version, n):
	distgitmagic.create_sample_upstream_new_version(version, 9, n)

@when('I run rdopkg {args}')
def step_impl(context, args):
	# proper argument parsing might be needed
	cmd = ['rdopkg'] + args.split(' ')
	context.command_output = run(*cmd, fatal=False, log_fail=False)

@then("command output contains '{rex}'")
def step_impl(context, rex):
	assert re.search(rex, context.command_output), "Did not find [{0}] in command output [{1}]".format(rex, context.command_output.encode('ascii', 'replace'))

@then('.spec file tag {tag} is {value}')
def step_impl(context, tag, value):
	spec = specfile.Spec()
	assert spec.get_tag(tag) == value, "{0} != {1}".format(spec.get_tag(tag), value)

@then('.spec file doesn\'t contain patches_base')
def step_impl(context):
	spec = specfile.Spec()
	assert spec.get_patches_base() == (None, 0)

@then('.spec file has {n:n} patches defined')
def step_impl(context, n):
	spec = specfile.Spec()
	assert spec.get_n_patches() == n

@then('.spec file contains new changelog entry with {n:n} lines')
def step_impl(context, n):
	spec = specfile.Spec()
	entry = spec.get_last_changelog_entry()
	assert len(entry[1]) == n
	assert entry != context.old_changelog_entry

@then('new commit was created')
def step_impl(context):
	new_commit = git.current_commit()
	assert new_commit != context.old_commit

@then(u'git is clean')
def step_impl(context):
	assert git.is_clean(), git('status').encode('ascii', 'replace')

@then(u'last commit message is')
def step_impl(context):
	msg = git.current_commit_message()	
	assert context.text == msg, exdiff(context.text, msg, header="Commit message differs from expected format:")
```

id : seed_task_75
name : ko_75
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework : 
```gherkin
Scenario: User Registration, Login, and Profile Update
	Given I am on the registration page
	When I enter my name, email, and password
	And I click on the submit button
	Then I should be redirected to the login page
	Given I am on the login page
	When I enter my email and password
	And I click on the login button
	Then I should be redirected to my profile page
	Given I am on my profile page
	When I click on the edit profile button
	And I update my name
	And I click on the save changes button
	Then my profile should be updated with the new name
```
input = ""
output:
```python
from your_app import RegistrationPage, LoginPage, ProfilePage

@given("I am on the registration page")
def on_registration_page():
	registration_page = RegistrationPage()
	assert registration_page.is_displayed()

@when("I enter my name, email, and password")
def enter_credentials():
	registration_page.enter_credentials(name="John Doe", email="john@example.com", password="password123")

@when("I click on the submit button")
def click_submit_button():
	registration_page.click_submit_button()

@then("I should be redirected to the login page")
def redirected_to_login():
	login_page = LoginPage()
	assert login_page.is_displayed()

@given("I am on the login page")
def on_login_page():
	login_page = LoginPage()
	assert login_page.is_displayed()

@when("I enter my email and password")
def enter_login_credentials():
	login_page.enter_credentials(email="john@example.com", password="password123")

@when("I click on the login button")
def click_login_button():
	login_page.click_login_button()

@then("I should be redirected to my profile page")
def redirected_to_profile():
	profile_page = ProfilePage()
	assert profile_page.is_displayed()

@given("I am on my profile page")
def on_profile_page():
	profile_page = ProfilePage()
	assert profile_page.is_displayed()

@when("I click on the edit profile button")
def click_edit_profile_button():
	profile_page.click_edit_profile_button()

@when("I update my name")
def update_name():
	profile_page.update_name("Jane Doe")

@when("I click on the save changes button")
def click_save_changes_button():
	profile_page.click_save_changes_button()

@then("my profile should be updated with the new name")
def profile_updated():
	assert profile_page.get_name() == "Jane Doe"
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
name : ko_77
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework : 
```gherkin
Scenario: User Purchase and Check Order History
	Given I am on the product page
	When I select a product and add it to the cart
	And I proceed to checkout
	And I enter my shipping address and payment details
	And I confirm the purchase
	Then I should receive a confirmation email
	And I should be redirected to the order history page
```
input = ""
output:
```python
from your_app import ProductPage, CartPage, CheckoutPage, OrderConfirmationPage, OrderHistoryPage

@given("I am on the product page")
def on_product_page():
	product_page = ProductPage()
	assert product_page.is_displayed()

@when("I select a product and add it to the cart")
def add_product_to_cart():
	product_page.select_product("Product A")
	product_page.add_to_cart()

@when("I proceed to checkout")
def proceed_to_checkout():
	cart_page = CartPage()
	cart_page.proceed_to_checkout()

@when("I enter my shipping address and payment details")
def enter_shipping_and_payment_details():
	checkout_page = CheckoutPage()
	checkout_page.enter_shipping_address(address="123 Main St, City", payment_details="1234 5678 9012 3456")

@when("I confirm the purchase")
def confirm_purchase():
	checkout_page = CheckoutPage()
	checkout_page.confirm_purchase()

@then("I should receive a confirmation email")
def receive_confirmation_email():
	order_confirmation_page = OrderConfirmationPage()
	assert order_confirmation_page.confirmation_email_received()

@then("I should be redirected to the order history page")
def redirected_to_order_history():
	order_history_page = OrderHistoryPage()
	assert order_history_page.is_displayed()
```

id : seed_task_78
name : ko_78
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework : 
```gherkin
Scenario: rdopkg pkgenv basic usage
	Given a distgit at Version 1.0.0 and Release 0.1
	Given a patches branch with 2 patches
	When I run rdopkg pkgenv
	Then command output contains 'Patches style:\s+branch'
	Then command output contains 'Patches base:\s+N/A'
	Then command output contains 'Patches base ref:\s+1.0.0 : existing git tag'
	Then command output contains 'Version:\s+1.0.0'
	Then command output contains 'VR:\s+1:1.0.0-0.1'
	Then command output contains 'Release style:\s+generic'
	Then command output contains 'Rls bump index:\s+last-numeric'
	Then command output contains 'Local patches branch:\s+master-patches : \w+'
	Then no new commit was created
```
input = ""
output:
```python
@given('a distgit at Version {version} and Release {release}')
def step_impl(context, version, release):
	_create_distgit(context, version, release)

@given('a patches branch with {n:n} patches')
def step_impl(context, n):
	distgitmagic.create_sample_patches_branch(n)

@when('I run rdopkg {args}')
def step_impl(context, args):
	# proper argument parsing might be needed
	cmd = ['rdopkg'] + args.split(' ')
	context.command_output = run(*cmd, fatal=False, log_fail=False)

@then("command output contains '{rex}'")
def step_impl(context, rex):
	assert re.search(rex, context.command_output), "Did not find [{0}] in command output [{1}]".format(rex, context.command_output.encode('ascii', 'replace'))

@then(u'no new commit was created')
def step_impl(context):
	new_commit = git.current_commit()
	assert new_commit == context.old_commit
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
name : ko_80
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework : 
```gherkin
Scenario: Create an icecream
	Given the following icecream
		|name	   |id|
		|Vanilla   |4 |
		|Chocolate |6 |
		|Strawberry|7 |
	When I visit '/ice-cream'
	Then I should not see 'Pistachio'
	When I create '/ice-cream'
		|name	 |id|description   |status|base|price|popularity|
		|Pistachio|10|Made from Nuts|melted|milk|$1.00|1/5	   |
	And I visit '/ice-cream/10'
	Then I should see 'Pistachio'
```
input = ""
output:
```python
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

@then(u'I should not see \'{name}\'')
def step_impl(context, name):
	assert name not in context.resp.data

@when(u'I create \'{url}\'')
def step_impl(context, url):
	flavor = {}
	for row in context.table:
		flavor = {'name': row['name'], 'description': row['description'], 'status': row['status'], 'base': row['base'], 'price': row['price'], 'popularity': row['popularity'],'id':row['id']}
		context.resp = context.app.post(url, data=json.dumps(flavor), content_type='application/json')
	print(context.resp)
	assert context.resp.status_code == 201

@when(u'I visit \'{url}\'')
def step_impl(context, url):
	context.resp = context.app.get(url)
	assert context.resp.status_code == 200

@then(u'I should see \'{name}\'')
def step_impl(context, name):
	assert name in context.resp.data
```

id : seed_task_81
name : ko_81
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework : 
```gherkin
Scenario Outline: Square roots
	Given I have a number, <number>
	When I compute the square root
	Then the square root should be returned
	
	Examples: Numbers
	| number						  |
	| 0							      |
	| 1							      |
	| 2							      |
	| 3							      |
	| 4							      |
	| 81							  |
	| 114							  |
	| 144							  |
	| 125348						  |
	| 10000002						  |
	| 100000003						  |
	| 100000000004					  |
	| 1000000000005					  |
	| 10000000000006				  |
	| 100000000000007				  |
	| 1000000000000008				  |
	| 100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000003																				      |
	|10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000003											      |
	|1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000003			      |
	|5486124068793688683255936251187209270074392635932332070112001988456197381759672947165175699536362793613284725337872111744958183862744647903224103718245670299614498700710006264535590197791934024641512541262359795191593953928908168990292758500391456212260452596575509589842140073806143686060649302051520511|
```
input = ""
output:
```python
@given('I have a number, {number}')
def step_impl(context, number):
	context.number = int(number)

@when('I compute the square root')
def step_impl(context):
	context.result = sqrt(context.number)

@then('the square root should be returned')
def step_impl(context):
	result = round(context.result ** 2)
	print 'result {0} {1}'.format(context.number, result)
	assert context.number == result
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
from behave import given, when, then
@given('a string {argument} an argument')
def step_impl(context, argument):
	context.argument = argument

@then('we get "{argument}" parsed')
def step_impl(context, argument):
	assert context.argument == argument
```

id : seed_task_83
name : ko_83
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework : 
```gherkin
Scenario: rdopkg patch --amend
	Given a distgit with Change-Id Ideadbeef1234
	Given a patches branch with 5 patches
	When I run rdopkg patch -l --amend
	Then command return code is 0
	Then .spec file tag Release is 3%{?dist}
	Then .spec file has 5 patches defined
	Then .spec file doesn't contain patches_base
	Then .spec file contains new changelog entry with 5 lines
	Then new commit was created
	Then git is clean
	Then last commit message is:
	    """
	    foo-bar-1.2.3-3

	    Changelog:
	    - Original Patch 5
	    - Original Patch 4
	    - Original Patch 3
	    - Original Patch 2
	    - Original Patch 1

	    Change-Id: Ideadbeef1234
	    """
```
input = ""
output:
```python
@given('a distgit with Change-Id {changeid}')
def step_impl(context, changeid):
	context.execute_steps(u'Given a distgit at Version 1.2.3 and Release 2')
	git('commit', '--amend', '-m',
		context.old_commit + '\n\nChange-Id: %s' % changeid)
	context.old_commit = git.current_commit()

@given('a patches branch with {n:n} patches')
def step_impl(context, n):
	distgitmagic.create_sample_patches_branch(n)

@when('I run rdopkg {args}')
def step_impl(context, args):
	# proper argument parsing might be needed
	cmd = ['rdopkg'] + args.split(' ')
	context.command_output = run(*cmd, fatal=False, log_fail=False)

@then("command return code is {n:n}")
def step_impl(context, n):
	rc = context.command_output.return_code
	assert n == rc, \
		"Command return code is %s but should be %s" % (rc, n)

@then('.spec file tag {tag} is {value}')
def step_impl(context, tag, value):
	spec = specfile.Spec()
	assert spec.get_tag(tag) == value, \
		"{0} != {1}".format(spec.get_tag(tag), value)

@then('.spec file has {n:n} patches defined')
def step_impl(context, n):
	spec = specfile.Spec()
	assert spec.get_n_patches() == n

@then('.spec file doesn\'t contain patches_base')
def step_impl(context):
	spec = specfile.Spec()
	assert spec.get_patches_base() == (None, 0)

then('.spec file contains new changelog entry with {text}')
def step_impl(context, text):
	spec = specfile.Spec()
	entry = spec.get_last_changelog_entry()
	changelog_block = '\n'.join(entry[1])
	assert text in changelog_block, \
		"[{0}] not found in [{1}]".format(text, changelog_block)
	assert entry != context.old_changelog_entry

@then('new commit was created')
def step_impl(context):
	new_commit = git.current_commit()
	assert new_commit != context.old_commit

@then(u'git is clean')
def step_impl(context):
	assert git.is_clean(), git('status').encode('ascii', 'replace')

@then(u'last commit message is')
def step_impl(context):
	msg = git.current_commit_message()
	assert context.text == msg, exdiff(
		context.text, msg,
		header="Commit message differs from expected format:")
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
from behave import given, when, then
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
name : ko_85
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework : 
```gherkin
Scenario: rdopkg patch --no-bump
	Given a distgit at Version 1.20.0 and Release 3
	Given a patches branch with 3 patches
	When I run rdopkg patch --no-bump -l
	Then .spec file tag Release is 3%{?dist}
	Then command return code is 0
	Then .spec file has 3 patches defined
	Then .spec file doesn't contain patches_base
	Then .spec file doesn't contain new changelog entries
	Then .spec file tag Release is 3%{?dist}
	Then new commit was created
	Then git is clean
	Then last commit message is:
	    """
	    Updated patches from master-patches
	    """
```
input = ""
output:
```python
@given('a distgit at Version {version} and Release {release}')
def step_impl(context, version, release):
	_create_distgit(context, version, release)

@given('a patches branch with {n:n} patches')
def step_impl(context, n):
	distgitmagic.create_sample_patches_branch(n)

@when('I run rdopkg {args}')
def step_impl(context, args):
	# proper argument parsing might be needed
	cmd = ['rdopkg'] + args.split(' ')
	context.command_output = run(*cmd, fatal=False, log_fail=False)

@then("command return code is {n:n}")
def step_impl(context, n):
	rc = context.command_output.return_code
	assert n == rc, \
		"Command return code is %s but should be %s" % (rc, n)

@then('.spec file tag {tag} is {value}')
def step_impl(context, tag, value):
	spec = specfile.Spec()
	assert spec.get_tag(tag) == value, \
		"{0} != {1}".format(spec.get_tag(tag), value)

@then('.spec file has {n:n} patches defined')
def step_impl(context, n):
	spec = specfile.Spec()
	assert spec.get_n_patches() == n


@then('.spec file doesn\'t contain patches_base')
def step_impl(context):
	spec = specfile.Spec()
	assert spec.get_patches_base() == (None, 0)

@then('.spec file doesn\'t contain new changelog entries')
def step_impl(context):
	entry = specfile.Spec().get_last_changelog_entry()
	assert entry == context.old_changelog_entry

@then('.spec file tag {tag} is {value}')
def step_impl(context, tag, value):
	spec = specfile.Spec()
	assert spec.get_tag(tag) == value, \
		"{0} != {1}".format(spec.get_tag(tag), value)

@then('new commit was created')
def step_impl(context):
	new_commit = git.current_commit()
	assert new_commit != context.old_commit

@then(u'git is clean')
def step_impl(context):
	assert git.is_clean(), git('status').encode('ascii', 'replace')

@then(u'last commit message is')
def step_impl(context):
	msg = git.current_commit_message()
	assert context.text == msg, exdiff(
		context.text, msg,
		header="Commit message differs from expected format:")
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
@given('smartHome, alarm off, touch not pressed, button not pressed')
def step_impl(context):
	context.malyDom = malyDomek()

@when('touch is pressed')
def step_impl(context):
	context.malyDom.Out()

@then('sound the alarm')
def step_impl(context):
	assert context.malyDom.alarmIn progress is True
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
name : ko_88
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework : 
```gherkin
Scenario: rdopkg fix
	Given a distgit
	When I run rdopkg fix
	When I add description to .spec changelog
	When I run rdopkg --continue
	Then .spec file contains new changelog entry with 1 lines
	Then new commit was created
	Then rdopkg state file is not present
	Then last commit message is:
	    """
	    foo-bar-1.2.3-3

	    Changelog:
	    - Description of a change
	    """
```
input = ""
output:
```python
@given('a distgit')
def step_impl(context):
	context.execute_steps(u'Given a distgit at Version 1.2.3 and Release 2')

@when('I run rdopkg {args}')
def step_impl(context, args):
	# proper argument parsing might be needed
	cmd = ['rdopkg'] + args.split(' ')
	context.command_output = run(*cmd, fatal=False, log_fail=False)

@when('I add description to .spec changelog')
def step_impl(context):
	spec = specfile.Spec()
	spec._txt, n = re.subn('(\n%changelog\n\*[^\n]+\n)\n', '\g<1>- Description of a change\n', spec.txt)
	assert n == 1
	spec.save()

@then('.spec file contains new changelog entry with {n:n} lines')
def step_impl(context, n):
	spec = specfile.Spec()
	entry = spec.get_last_changelog_entry()
	assert len(entry[1]) == n
	assert entry != context.old_changelog_entry

@then('new commit was created')
def step_impl(context):
	new_commit = git.current_commit()
	assert new_commit != context.old_commit

@then(u'rdopkg state file is not present')
def step_check_for_rdopkg_state_file_not_present(context):
	assert not os.path.exists(os.path.join(context.distgitdir, STATE_FILE_FN))

@then(u'last commit message is')
def step_impl(context):
	msg = git.current_commit_message()
	assert context.text == msg, exdiff(
		context.text, msg,
    	header="Commit message differs from expected format:")
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
@given(u'I am on the login page')
def step_impl(context):
	assert False

@given(u'my account has already been created')
def step_impl(context):
	assert False

@when(u'I fill in the user signin form')
def step_impl(context):
	assert False

@then(u'I should be on my console page')
def step_impl(context):
	assert False

@then(u'I should see "Login successful!"')
def step_impl(context):
	assert False
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
@given(u'we compose "{composeYamlFile}"')
def step_impl(context, composeYamlFile):
	context.compose_yaml = composeYamlFile
	fileArgsToDockerCompose = bdd_compose_util.getDockerComposeFileArgsFromYamlFile(context.compose_yaml)
	context.compose_output, context.compose_error, context.compose_returncode = bdd_test_util.cli_call(["docker-compose"] + fileArgsToDockerCompose + ["up","--force-recreate", "-d"], expect_success=True)
	assert context.compose_returncode == 0, "docker-compose failed to bring up {0}".format(composeYamlFile
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
name : ko_103
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework : 
```gherkin
Scenario: rdopkg new-version with patches_ignore filtering
	Given a distgit at Version 0.1 and Release 0.1 with magic comments:
	    """
	    # patches_ignore=DROP-IN-RPM|Wololo
	    # patches_base=0.1
	    """
	Given a patches branch with following patches:
	    """
	    Banana Patch DROP-IN-RPM
	    Mango Patch
	    Wololo Patch
	    Kiwi Patch
	    """
	Given a new version 1.0.0
	When I run rdopkg new-version -ltU 1.0.0
	Then command output contains 'Action finished'
	Then .spec file tag Version is 1.0.0
	Then .spec file tag Release is 1%{?dist}
	Then .spec file has 2 patches defined
	Then .spec file contains patches_base=1.0.0
	Then .spec file contains new changelog entry with 1 lines
	Then new commit was created
	Then git is clean
	Then last commit message is:
	    """
	    foo-bar-1.0.0-1

	    Changelog:
	    - Update to 1.0.0
	    """
```
input = ""
output:
```python
@given('a distgit at Version {version} and Release {release} with magic comments')  # noqa
def step_impl(context, version, release):
	_create_distgit(context, version, release, magic_comments=context.text)

@given('a patches branch with following patches')
def step_impl(context):
	patches = context.text.splitlines()
	distgitmagic.create_sample_patches_branch(patches=patches)

@given('a new version {version}')
def step_impl(context, version):
	context.execute_steps(u'Given a new version %s with 0 patches from patches branch' % version)

@when('I run rdopkg {args}')
def step_impl(context, args):
	# proper argument parsing might be needed
	cmd = ['rdopkg'] + args.split(' ')
	context.command_output = run(*cmd, fatal=False, log_fail=False)

@then("command output contains '{rex}'")
def step_impl(context, rex):
	assert re.search(rex, context.command_output), "Did not find [{0}] in command output [{1}]".format(rex, context.command_output.encode('ascii', 'replace'))

@then('.spec file tag {tag} is {value}')
def step_impl(context, tag, value):
	spec = specfile.Spec()
	assert spec.get_tag(tag) == value, "{0} != {1}".format(spec.get_tag(tag), value)

@when(u'I set .spec file patches_base={base}')
def step_impl(context, base):
	spec = specfile.Spec()
	spec.set_patches_base(base)
	spec.save()

@then('.spec file has {n:n} patches defined')
def step_impl(context, n):
	spec = specfile.Spec()
	assert spec.get_n_patches() == n

@then('.spec file contains new changelog entry with {n:n} lines')
def step_impl(context, n):
	spec = specfile.Spec()
	entry = spec.get_last_changelog_entry()
	assert len(entry[1]) == n
	assert entry != context.old_changelog_entry

@then('new commit was created')
def step_impl(context):
	new_commit = git.current_commit()
	assert new_commit != context.old_commit

@then(u'git is clean')
def step_impl(context):
	assert git.is_clean(), git('status').encode('ascii', 'replace')

@then(u'last commit message is')
def step_impl(context):
	msg = git.current_commit_message()	
	assert context.text == msg, exdiff(context.text, msg, header="Commit message differs from expected format:")
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
name : ko_105
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework : 
```gherkin
Scenario: Action on the ice-cream
	Given I want to melt or freeze an icecream
	When I append melt at the end of the url
	Then I should have 'melted'
	And I should have melted 'Vanilla'
	When I append freeze at the end of the url
	Then I should have 'frozen'
	And I should have frozen 'Vanilla'

```
input = ""
output:
```python
@given('I want to melt or freeze an icecream')
def step_impl(context):
	context.resp = context.app.put('/ice-cream/4/melt')
	assert context.resp.status_code == 200
	context.resp = context.app.put('/ice-cream/4/freeze')
	assert context.resp.status_code == 200

@when('I append melt at the end of the url')
def step_impl(context):
	context.resp = context.app.put('/ice-cream/4/melt')

@then(u'I should have \'melted\'')
def step_impl(context):
	context.resp = context.app.put('/ice-cream/4/melt')
	assert 'melted' in context.resp.data

@then(u'I should have melted \'Vanilla\'')
def step_impl(context):
	context.resp = context.app.put('/ice-cream/4/melt')
	assert 'Vanilla' in context.resp.data

@when(u'I append freeze at the end of the url')
def step_impl(context):
	context.resp = context.app.put('/ice-cream/4/freeze')

@then(u'I should have \'frozen\'')
def step_impl(context):
	context.resp = context.app.put('/ice-cream/4/freeze')
	assert 'frozen' in context.resp.data

@then(u'I should have frozen \'Vanilla\'')
def step_impl(context):
	context.resp = context.app.put('/ice-cream/4/freeze')
	assert 'Vanilla' in context.resp.data
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
name : ko_107
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework : 
```gherkin
Scenario: User Login with Specific Browser
	Given I am using Chrome browser
	When I navigate to the login page
	And I enter my username and password
	And I click on the login button
	Then I should be logged in successfully
	And I should see the homepage displayed in Chrome
```
input = ""
output:
```python
from your_app import LoginPage, HomePage

@given("I am using Chrome browser")
def using_chrome_browser():
	# This step function could potentially be implemented using a WebDriver setup
	pass

@when("I navigate to the login page")
def navigate_to_login_page():
	login_page = LoginPage()
	login_page.navigate()

@when("I enter my username and password")
def enter_credentials():
	login_page = LoginPage()
	login_page.enter_credentials(username="user@example.com", password="password123")

@when("I click on the login button")
def click_login_button():
	login_page = LoginPage()
	login_page.click_login_button()

@then("I should be logged in successfully")
def logged_in_successfully():
	home_page = HomePage()
	assert home_page.is_logged_in()

@then("I should see the homepage displayed in Chrome")
def homepage_displayed_in_chrome():
	# This step may not be practically implemented in the context of the test automation code
	pass
```

id : seed_task_108
name : ko_108
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework : 
```gherkin
Scenario: state file doesn't affect new actions
	Given a distgit at Version 1.1.1
	When I run rdopkg new-version
	When I change .spec file tag Version to 2.2.2
	When I run rdopkg pkgenv
	Then command output contains 'Version:\s+2.2.2'
```
input = ""
output:
```python
@given('a distgit at Version {version}')
def step_impl(context, version):
	step = u'Given a distgit at Version %s and Release 2' % version
	context.execute_steps(step)

@when('I run rdopkg {args}')
def step_impl(context, args):
	# proper argument parsing might be needed
	cmd = ['rdopkg'] + args.split(' ')
	context.command_output = run(*cmd, fatal=False, log_fail=False)

@when('I change .spec file tag {tag} to {value}')
def step_impl(context, tag, value):
	spec = specfile.Spec()
	spec.set_tag(tag, value)
	spec.save()

@then("command output contains '{rex}'")
def step_impl(context, rex):
	assert re.search(rex, context.command_output), \
		"Did not find [{0}] in command output [{1}]".format(
			rex, context.command_output.encode('ascii', 'replace'))
```

id : seed_task_109
name : ko_109
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
name : ko_118
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework : 
```gherkin
Scenario: searching for a book, adding it to the cart, and verifying the final checkout details
	Given the book "all time wonders" costs $20
	When Olivia searches the book
	Then the book is listed in the matching search results
	When she selects the book
	Then the book is added to the cart
	When she checks out the shopping cart
	Then the book is listed in the final checkout
	And the total price of the cart is $20
```
input = ""
output:
```python
from pytest_bdd import given, when, then

@given("the book 'all time wonders' costs $20")
def book_price():
	# Assuming the book price is set to $20
	book_price = 20

@when("Olivia searches the book")
def search_book():
	search_page = SearchPage()
	search_page.search_book("all time wonders")

@then("the book is listed in the matching search results")
def book_listed_in_search_results():
	search_page = SearchPage()
	assert search_page.book_is_listed("all time wonders")

@when("she selects the book")
def select_book():
	search_page = SearchPage()
	search_page.select_book("all time wonders")

@then("the book is added to the cart")
def book_added_to_cart():
	cart_page = CartPage()
	assert cart_page.book_is_added("all time wonders")

@when("she checks out the shopping cart")
def checkout_cart():
	cart_page = CartPage()
	cart_page.checkout()

@then("the book is listed in the final checkout")
def book_listed_in_final_checkout():
	checkout_page = CheckoutPage()
	assert checkout_page.book_is_listed("all time wonders")

@then("the total price of the cart is $20")
def total_price_correct():
	checkout_page = CheckoutPage()
	assert checkout_page.total_price() == 20
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
name : ko_123
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework : 
```gherkin
Scenario: When the update is successful
	Given I have a kalibro configuration with name "Java"
	And I have a reading group with name "Group"
	And I have a metric configuration within the given kalibro configuration
	And I have a reading within the given reading group
	And I have a range within the given reading
	When I change the "beginning" to "-250"
	And I change the "end" to "250"
	And I change the "comments" to "my new range"
	And I ask to update the given range
	Then I should not receive errors
```
input = ""
output:
```python
given(u'I have a kalibro configuration with name "{}"')
def step_impl(context, kalibro_configuration_name):
	context.kalibro_configuration = KalibroConfigurationFactory.build(name=kalibro_configuration_name)
	context.kalibro_configuration.save()

@given(u'I have a reading group with name "{}"')
def step_impl(context, reading_group_name):
	context.reading_group = ReadingGroupFactory.build(name=reading_group_name)
	context.reading_group.save()

@given(u'I have a metric configuration within the given kalibro configuration')
def step_impl(context):
	context.metric_configuration = MetricConfigurationFactory.build(
		kalibro_configuration_id=context.kalibro_configuration.id)
	context.metric_configuration.save()

@given(u'I have a reading within the given reading group')
def step_impl(context):
	context.reading = ReadingFactory.build(
		reading_group_id=context.reading_group.id)
	context.reading.save()

@given(u'I have a range within the given reading')
def step_impl(context):
	context.range = KalibroRangeFactory.build(reading_id=context.reading.id, metric_configuration_id=context.metric_configuration.id, beginning=1.1, end=5.1)
	context.range.save()

@when(u'I change the "{}" to "{}"')
def step_impl(context, attribute, value):
	setattr(context.range, attribute, value)

@then(u'I should not receive errors')
def step_impl(context):
	assert_is_none(context.error)
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
name : ko_125
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework : 
```gherkin
Scenario: when there is a metric result
	Given I have a project with name "Kalibro"
	And I have a sample configuration with MetricFu metrics
	And the given project has the following Repositories:
	  |   name	| scm_type |				   address					|
	  |  Kalibro  |	GIT   | https://github.com/mezuro/kalibro_client.git |
	And I call the process method for the given repository
	And I wait up for a ready processing
	And I call the first_processing method for the given repository
	And I search a metric result with descendant values for the given metric result
	Then I should get a Float list

```
input = ""
output:
```python
@given(u'I have a project with name "{}"')
def step_impl(context, project_name):
	context.execute_steps(u'When I create the project with name "{}"'.format(project_name))

@given(u'I have a sample configuration with MetricFu metrics')
def step_impl(context):
  context.reading_group = ReadingGroupFactory.build()
  context.reading_group.save()
  context.reading = ReadingFactory.build(reading_group_id = context.reading_group.id)
  context.reading.save()

  context.kalibro_configuration = KalibroConfigurationFactory.build()
  context.kalibro_configuration.save()

  context.metric = NativeMetricFactory.build()
  metric_configuration = MetricConfigurationFactory.build(metric=context.metric, reading_group_id=context.reading_group.id, kalibro_configuration_id=context.kalibro_configuration.id)
  metric_configuration.save()

@given(u'the given project has the following Repositories')
def step_impl(context):
	row = dict(zip(context.table.headings, context.table[0].cells))
	context.repository = RepositoryFactory.build(project_id=context.project.id, kalibro_configuration_id=context.kalibro_configuration.id, **row)
	context.repository.save()

@given(u'I call the process method for the given repository')
def step_impl(context):
	context.repository.process()

@given(u'I wait up for a ready processing')
def step_impl(context):
	while not context.repository.has_ready_processing():
		sleep(10)

given(u'I call the first_processing method for the given repository')
def step_impl(context):
	context.execute_steps(u'when I call the first_processing method for the given repository')

@given(u'I search a metric result with descendant values for the given metric result')
def step_impl(context):
	first_module_result = ModuleResult.find(context.response.root_module_result_id)

	metric_results = first_module_result.tree_metric_results()
	context.response = metric_results[0].descendant_values()

@then(u'I should get a Float list')
def step_impl(context):
	assert_is_instance(context.response, list)
	for element in context.response:
		assert_is_instance(element, float)
```

id : seed_task_126
name : ko_126
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework : 
```gherkin
Scenario: Sign up form elements
	Given I am on intu Signup page
	And I focus on signup form
	Then I see form input "First name"
	And I see form input "Last name"
	And I see form input "Email address"
	And I see Birthday part "1"
	And I see Birthday part "2"
	And I see Birthday part "3"
	And I see radio button "Female"
	And I see radio button "Male"
	And I see radio button "Prefer not to say"
	And I see form input "Postcode"
	And I see radio button "Yes"
	And I see radio button "No"
	And I see submit button

```
input = ""
output:
```python
@given('I am on intu Signup Page')
def step_impl(context):
	context.signup_page.navigate(context.driver)
	assert context.signup_page.at()

@given('I focus on signup form')
def step_impl(context):
	context.signup_page.switch_to_frame()

@then('I see form input "{form_field}"')
def step_impl(context, form_field):
	assert context.signup_page.get_form_field(form_field) is not None

@then('I see Birthday part "{idx}"')
def step_impl(context, idx):
	assert context.signup_page.get_birthday_index(idx) is not None

@then('I see radio button "{radio_field}"')
def step_impl(context, radio_field):
	assert context.signup_page.get_radio_field(radio_field) is not None

@then('I see submit button')
def step_impl(context):
	assert context.signup_page.get_submit() is not None
```

id : seed_task_127
name : ko_127
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework : 
```gherkin
Scenario: user has access to UI
	Given user is granted access to text page
	When navigates to the page
	then user can see an image on the left pane
	And text on the right pane
	And UI on the extreme right
	And
	And
```
input = ""
output:
```python
@given('user is on page with lists of texts')
def step_impl(context):
	context.browser.get("http://localhost:8000/edit")

@when('user clicks on a text')
def step_impl(context):
	''' '''
	context.browser.find_element
@then('user is redirected to the first page contaning incorrect words')
def step_impl(context):
	''' ''' 
	#assert the url is correct
	assert context.browser.current_url ==
	#assert at least one incorrect words
	assert context.browser.find_element_

@given('user is on text page')
def step_impl(context):
	context.execute_steps('''
		given user is on page with lists of texts
		when user clicks on a text
		''')

@when('user click on an incorrect word')
def step_impl(context):
	''' Incorrect word:corr="0" '''
	context.browser.find_element_by() is not None

@then('right pane is populated with correction suggestions')
def step_impl(context):
	''' '''
	right_pane = context.browser.find_element_
	
@when('')
def step_impl(context):
	pass

@when('')
def step_impl(context):
	pass
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
from behave import given, when, then
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
name : ko_131
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework : 
```gherkin
Scenario: rdopkg fix - user aborts and reruns
	Given a distgit
	When I run rdopkg fix
	When I run rdopkg fix
	When I undo all changes
	When I run rdopkg --abort
	When I run rdopkg fix
	When I add description to .spec changelog
	When I run rdopkg --continue
	Then .spec file contains new changelog entry with 1 lines
	Then new commit was created
	Then rdopkg state file is not present
	Then last commit message is:
	    """
	    foo-bar-1.2.3-3

	    Changelog:
	    - Description of a change
	    """
```
input = ""
output:
```python
@given('a distgit')
def step_impl(context):
	context.execute_steps(u'Given a distgit at Version 1.2.3 and Release 2')

@when('I run rdopkg {args}')
def step_impl(context, args):
	# proper argument parsing might be needed
	cmd = ['rdopkg'] + args.split(' ')
	context.command_output = run(*cmd, fatal=False, log_fail=False)

@when(u'I undo all changes')
def step_impl(context):
	git("stash")
	assert git.is_clean()

@when('I add description to .spec changelog')
def step_impl(context):
	spec = specfile.Spec()
	spec._txt, n = re.subn('(\n%changelog\n\*[^\n]+\n)\n','\g<1>- Description of a change\n', spec.txt)
	assert n == 1
	spec.save()

@then('.spec file contains new changelog entry with {n:n} lines')
def step_impl(context, n):
	spec = specfile.Spec()
	entry = spec.get_last_changelog_entry()
	assert len(entry[1]) == n
	assert entry != context.old_changelog_entry

@then('new commit was created')
def step_impl(context):
	new_commit = git.current_commit()
	assert new_commit != context.old_commit

@then(u'last commit message is')
def step_impl(context):
	msg = git.current_commit_message()
	assert context.text == msg, exdiff(
		context.text, msg,
		header="Commit message differs from expected format:")

@then(u'rdopkg state file is not present')
def step_check_for_rdopkg_state_file_not_present(context):
	assert not os.path.exists(os.path.join(context.distgitdir, STATE_FILE_FN))
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
name : ko_133
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework : 
```gherkin
Scenario Outline: EULA is accepted
	Given Select language "<languages>"
	"""
	the text of scenario is Username and password fields are empty
	"""
	When Username " " and password " "
	And Stay logged in option is "unchecked"
	And Accept EULA is "checked"
	And Click on Login button
	Then Error appears: "<messages>"
	Examples:
	  |languages||messages															  |
	  |English  ||The username or password is incorrect Please try again.			   |
	  |Deutch   ||Benutzername oder Passwort ist falsch Bitte versuchen Sie es nochmals.|
Scenario Outline: EULA is accepted
	Given Select language "<languages>"
	"""
	the text of scenario is Username and password fields are empty
	"""
	When Username " " and password " "
	And Stay logged in option is "unchecked"
	And Accept EULA is "checked"
	And Click on Login button
	Then Error appears: "<messages>"
	Examples:
	  |languages||messages													    		   |
	  |English  ||The username or password is incorrect Please try again.	    		   |
	  |Deutch   ||Benutzername oder Passwort ist falsch Bitte versuchen Sie es nochmals.   |
```
input = ""
output:
```python
@step('Select language "{language}"')
def step_impl(context, language):
	context.login_page.select_language(language)

@step('Username "{username}" and password "{password}"')
def step_impl(context, username, password):
	context.login_page.type_username_placeholder(username)
	context.login_page.type_password_placeholder(password)

@step('Stay logged in option is "{status}"')
def step_impl(context, status):
	context.login_page.check_autologin(status)

@step('Accept EULA is "{status}"')
def step_impl(context, status):
	context.login_page.check_eula(status)

@step('Click on Login button')
def step_impl(context):
	context.login_page.click_login_button()

@then('Error appears: "{error}"')
def step_impl(context, error):
	assert context.login_page.verify_failed_login(error)
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
name : ko_135
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework : 
```gherkin
Scenario Outline: Expired session with login <status>
	Given Open WebStation login page with timeout
	When Username "ivan.coric91" and password "ICtrader123"
	And Stay logged in option is "<status>"
	And Click on Login button
	And Click on Next button
	Then A "<page>" page will appear

	Examples:
	  |status   |page |
	  |unchecked|Login|
	  |checked  |Home |
```
input = ""
output:
```python
@step('Open WebStation login page with timeout')
def step_impl(context):
	context.selenium_driver.navigate("http://webstationtest3.ttweb.net/WebStation.aspx?timeout=5000")

@step('Username "{username}" and password "{password}"')
def step_impl(context, username, password):
	context.login_page.type_username_placeholder(username)
	context.login_page.type_password_placeholder(password)

@step('Stay logged in option is "{status}"')
def step_impl(context, status):
	context.login_page.check_autologin(status)

@step('Click on Login button')
def step_impl(context):
	context.login_page.click_login_button()

@step('Click on Next button')
def step_impl(context):
	context.login_page.click_on_relog_button()

@then('A "{page}" page will appear')
def step_impl(context, page):
	if page == "Login":
		assert context.login_page.verify_login_button_visible()
	if page == "Home":
		assert context.login_page.verify_home_button_visible()
		context.execute_steps('then Logout')
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
name : ko_137
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework : 
```gherkin
Scenario Outline: test a chaincode showing how to implement role-based access control using TCerts with attributes
	Given we compose "<ComposeFile>"
	And I wait "5" seconds
	And I register with CA supplying username "binhn" and secret "7avZQLwcUe9q" on peers:
		|vp0 |
	And I register with CA supplying username "alice" and secret "8Y7WIrLX0A8G" on peers:
		|vp0 |
	And I use the following credentials for querying peers:
		|peer|username  |secret      |
		|vp0 |test_user0|MS9qrN8hFjlE|
		|vp1 |test_user1|jGlNl6ImkuDo|
		|vp2 |test_user2|zMflqOKezFiA|
		|vp3 |test_user3|vWdLCE00vJy0|
	When requesting "/chain" from "vp0"
	Then I should get a JSON response with "height" = "1"
	When user "binhn" requests a batch of TCerts of size "1" with attributes:
		|role |
		|admin|
	And user "binhn" stores their last result as "BATCH_OF_TCERTS"
	And user "binhn" deploys chaincode "github.com/hyperledger/fabric/examples/chaincode/go/rbac_tcerts_with_attrs" with ctor "init" to "vp0"
            ||
            ||
	Then I should have received a chaincode name
	Then I wait up to "<WaitTime>" seconds for transaction to be committed to peers:
		|vp0|vp1|vp2|vp3|
	When user "alice" requests a new application TCert
	And user "alice" stores their last result as "TCERT_APP_ALICE_1"
	And user "alice" gives stored value "TCERT_APP_ALICE_1" to "binhn"
	When "binhn" uses application TCert "TCERT_APP_ADMIN" to assign role "writer" to application TCert "TCERT_APP_ALICE_1"
	Then I should have received a transactionID
	Then I wait up to "60" seconds for transaction to be committed to peers:
		|vp0|vp1|vp2|vp3|
	When "alice" uses application TCert "TCERT_APP_ALICE_1" to assign role "writer" to application TCert "TCERT_APP_ALICE_1"
	Then I wait up to "60" seconds for transaction to be committed to peers:
		|vp0|vp1|vp2|vp3|
	And transaction should have failed with message "Permission denied"
	Examples: Consensus Options
		|ComposeFile                         |WaitTime|
		|docker-compose-4-consensus-batch.yml|60      |
```
input = ""
output:
```python
@given(u'we compose "{composeYamlFile}"')
def step_impl(context, composeYamlFile):
	context.compose_yaml = composeYamlFile
	fileArgsToDockerCompose = bdd_compose_util.getDockerComposeFileArgsFromYamlFile(context.compose_yaml)
	context.compose_output, context.compose_error, context.compose_returncode = bdd_test_util.cli_call(
		["docker-compose"] + fileArgsToDockerCompose + ["up", "--force-recreate", "-d"], expect_success=True)
	assert context.compose_returncode == 0, "docker-compose failed to bring up {0}".format(composeYamlFile)
	bdd_compose_util.parseComposeOutput(context)
	timeoutSeconds = 15
	assert bdd_compose_util.allContainersAreReadyWithinTimeout(context, timeoutSeconds), "Containers did not come up within {} seconds aborting".format(timeoutSeconds)

@given(u'I wait "{seconds}" seconds')
def step_impl(context, seconds):
	time.sleep(float(seconds))

@given(u'I register with CA supplying username "{userName}" and secret "{secret}" on peers')
def step_impl(context, userName, secret):
	assert 'compose_containers' in context, "compose_containers not found in context"
	assert 'table' in context, "table (of peers) not found in context"
	aliases = context.table.headings
	containerDataList = bdd_test_util.getContainerDataValuesFromContext(context, aliases, lambda containerData: containerData)
	secretMsg = {"enrollId": userName, "enrollSecret": secret}
	for containerData in containerDataList:
		request_url = buildUrl(context, containerData.ipAddress, "/registrar")
		resp = requests.post(request_url, headers={'Content-type': 'application/json'}, data=json.dumps(secretMsg),verify=False)
		assert resp.status_code == 200, "Failed to POST to %s:  %s" % (request_url, resp.text)
		context.response = resp
		
		bdd_test_util.registerUser(context, secretMsg, containerData.composeService)
	context.userName = userName
	if 'chaincodeSpec' in context:
		context.chaincodeSpec["secureContext"] = context.userName

@given(u'I use the following credentials for querying peers')
def step_impl(context):
	assert 'compose_containers' in context, "compose_containers not found in context"
	assert 'table' in context, "table (of peers, username, secret) not found in context"
	peerToSecretMessage = {}
	for row in context.table.rows:
		peer, userName, secret = row['peer'], row['username'], row['secret']
		secretMsg = {"enrollId": userName, "enrollSecret" : secret}
		ipAddress = bdd_test_util.ipFromContainerNamePart(peer, context.compose_containers)
		request_url = buildUrl(context, ipAddress, "/registrar")
		
		resp = requests.post(request_url, headers={'Content-type': 'application/json'}, data=json.dumps(secretMsg), verify=False)
		assert resp.status_code == 200, "Failed to POST to %s:  %s" %(request_url, resp.text)
		context.response = resp
		
		peerToSecretMessage[peer] = secretMsg
	context.peerToSecretMessage = peerToSecretMessage

@when(u'requesting "{path}" from "{containerName}"')
def step_impl(context, path, containerName):
	ipAddress = bdd_test_util.ipFromContainerNamePart(containerName, context.compose_containers)
	request_url = buildUrl(context, ipAddress, path)
	resp = requests.get(request_url, headers={'Accept': 'application/json'}, verify=False)
	assert resp.status_code == 200, "Failed to GET url %s:  %s" % (request_url,resp.text)
	context.response = resp

@then(u'I should get a JSON response with "{attribute}" = "{expectedValue}"')
def step_impl(context, attribute, expectedValue):
	foundValue = getAttributeFromJSON(attribute, context.response.json(),
									  "Attribute not found in response (%s)" % (attribute))
	assert (formatStringToCompare(foundValue) == expectedValue), "For attribute %s, expected (%s), instead found (%s)" % (
	attribute, expectedValue, foundValue)

@when(u'user "{enrollId}" stores their last result as "{tagName}"')
def step_impl(context, enrollId, tagName):
	assert 'users' in context, "users not found in context. Did you register a user?"
	userRegistration = bdd_test_util.getUserRegistration(context, enrollId)
	userRegistration.tags[tagName] = userRegistration.lastResult

@then(u'I should have received a chaincode name')
def step_impl(context):
	if 'chaincodeSpec' in context:
		assert context.chaincodeSpec['chaincodeID']['name'] != ""
		context.transactionID = context.chaincodeSpec['chaincodeID']['name']
	elif 'grpcChaincodeSpec' in context:
		assert context.grpcChaincodeSpec.chaincodeID.name != ""
		context.transactionID = context.grpcChaincodeSpec.chaincodeID.name
	else:
		fail('chaincodeSpec not in context')

@then(u'I wait up to "{seconds}" seconds for transaction to be committed to peers')
def step_impl(context, seconds):
	assert 'transactionID' in context, "transactionID not found in context"
	assert 'compose_containers' in context, "compose_containers not found in context"
	assert 'table' in context, "table (of peers) not found in context"
	aliases =  context.table.headings
	containerDataList = bdd_test_util.getContainerDataValuesFromContext(context, aliases, lambda containerData: containerData)
	
	respMap = {container.containerName:0 for container in containerDataList}
	
	maxTime = datetime.now() + timedelta(seconds = int(seconds))
	for container in containerDataList:
		ipAddress = container.ipAddress
		request_url = buildUrl(context, ipAddress, "/transactions/{0}".format(context.transactionID))

		while (datetime.now() < maxTime):
			resp = requests.get(request_url, headers={'Accept': 'application/json'}, verify=False)
			if resp.status_code == 404:
				respMap[container.containerName] = 404
				time.sleep(1)
				continue
			elif resp.status_code == 200:
				respMap[container.containerName] = 200
				break
			else:
				raise Exception("Error requesting {0}, returned result code = {1}".format(request_url, resp.status_code))
		else:
			raise Exception("Max time exceeded waiting for transactions with current response map = {0}".format(respMap))

@when(u'user "{enrollId}" requests a new application TCert')
def step_impl(context, enrollId):
	assert 'users' in context, "users not found in context. Did you register a user?"
	(channel, userRegistration) = bdd_grpc_util.getGRPCChannelAndUser(context, enrollId)

	stub = devops_pb2.beta_create_Devops_stub(channel)

	secret = bdd_grpc_util.getSecretForUserRegistration(userRegistration)
	response = stub.EXP_GetApplicationTCert(secret, 2)
	assert response.status == fabric_pb2.Response.SUCCESS, 'Failure getting TCert from {0}, for user "{1}":  {2}'.format(userRegistration.composeService, enrollId, response.msg)
	tcert = response.msg

	userRegistration.lastResult = tcert

@when(
	u'"{enrollId}" uses application TCert "{assignerAppTCert}" to assign role "{role}" to application TCert "{assigneeAppTCert}"')
def step_impl(context, enrollId, assignerAppTCert, role, assigneeAppTCert):
	assert 'users' in context, "users not found in context. Did you register a user?"
	assert 'compose_containers' in context, "compose_containers not found in context"
	(channel, userRegistration) = bdd_grpc_util.getGRPCChannelAndUser(context, enrollId)
	stub = devops_pb2.beta_create_Devops_stub(channel)
	secret = bdd_grpc_util.getSecretForUserRegistration(userRegistration)
	response = stub.EXP_PrepareForTx(secret, 2)
	assert response.status == fabric_pb2.Response.SUCCESS, 'Failure getting Binding from {0}, for user "{1}":  {2}'.format(userRegistration.composeService, enrollId, response.msg)
	binding = response.msg

	chaincodeInput = chaincode_pb2.ChaincodeInput(function="addRole", args=(
	base64.b64encode(userRegistration.tags[assigneeAppTCert]), role))
	chaincodeInputRaw = chaincodeInput.SerializeToString()
	appTCert = userRegistration.tags[assignerAppTCert]
	sigmaInput = devops_pb2.SigmaInput(secret=secret, appTCert=appTCert, data=chaincodeInputRaw + binding)
	response = stub.EXP_ProduceSigma(sigmaInput, 2)
	assert response.status == fabric_pb2.Response.SUCCESS, 'Failure prducing sigma from {0}, for user "{1}":  {2}'.format(userRegistration.composeService, enrollId, response.msg)
	sigmaOutputBytes = response.msg
	
	sigmaOutput = devops_pb2.SigmaOutput()
	sigmaOutput.ParseFromString(sigmaOutputBytes)

	assert "grpcChaincodeSpec" in context, "grpcChaincodeSpec NOT found in context"
	newChaincodeSpec = chaincode_pb2.ChaincodeSpec()
	newChaincodeSpec.CopyFrom(context.grpcChaincodeSpec)
	newChaincodeSpec.metadata = sigmaOutput.asn1Encoding
	newChaincodeSpec.ctorMsg.CopyFrom(chaincodeInput)

	ccInvocationSpec = chaincode_pb2.ChaincodeInvocationSpec(chaincodeSpec=newChaincodeSpec)
	executeWithBinding = devops_pb2.ExecuteWithBinding(chaincodeInvocationSpec=ccInvocationSpec, binding=binding)
	response = stub.EXP_ExecuteWithBinding(executeWithBinding, 60)
	assert response.status == fabric_pb2.Response.SUCCESS, 'Failure executeWithBinding from {0}, for user "{1}":  {2}'.format(userRegistration.composeService, enrollId, response.msg)
	context.response = response
	context.transactionID = response.msg
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
	assert_equal(len(context.response), 0)
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
@given(u'I have a project with name "{}"')
def step_impl(context, project_name):
	context.execute_steps(u'When I create the project with name "{}"'.format(project_name))

@when(u'I destroy the project with the same id of the given project')
def step_impl(context):
	context.found_project = Project.find(context.project.id)
	context.found_project.delete()

@then(u'the project should no longer exist')
def step_impl(context):
	assert_true(not Project.exists(context.found_project.id))
```

id : seed_task_143
name : ko_143
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework : 
```gherkin
Scenario: add magic_comment patches_base when already_set
	Given a distgit at Version 1.1.1
	Then .spec file doesn't contain patches_base
	When I run rdopkg set-magic-comment patches_base foo
	Then .spec file contains patches_base=foo
	When I run rdopkg set-magic-comment patches_base v1.1.1
	Then .spec file contains patches_base=v1.1.1
```
input = ""
output:
```python
@given('a distgit at Version {version}')
def step_impl(context, version):
    step = u'Given a distgit at Version %s and Release 2' % version
	context.execute_steps(step)

@then('.spec file doesn\'t contain patches_base')
def step_impl(context):
	spec = specfile.Spec()
	assert spec.get_patches_base() == (None, 0)

@when('I run rdopkg {args}')
def step_impl(context, args):
	# proper argument parsing might be needed
	cmd = ['rdopkg'] + args.split(' ')
	context.command_output = run(*cmd, fatal=False, log_fail=False)

@then('.spec file contains {text}')
def step_impl(context, text):
	spec = specfile.Spec()
	assert text in spec.txt, "%s not found in .spec" % text

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
name : ko_145
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework : 
```gherkin
Scenario: add magic_comment patches_base empty when already set
	Given a distgit at Version 1.1.1
	Then .spec file doesn't contain patches_base
	When I run rdopkg set-magic-comment patches_base foo
	Then .spec file contains patches_base=foo
	When I run rdopkg set-magic-comment patches_base ''
	Then .spec file contains patches_base=
```
input = ""
output:
```python
@given('a distgit at Version {version}')
def step_impl(context, version):
    step = u'Given a distgit at Version %s and Release 2' % version
    context.execute_steps(step)

@then('.spec file doesn\'t contain patches_base')
def step_impl(context):
    spec = specfile.Spec()
    assert spec.get_patches_base() == (None, 0)

@when('I run rdopkg {args}')
def step_impl(context, args):
    # proper argument parsing might be needed
    cmd = ['rdopkg'] + args.split(' ')
    context.command_output = run(*cmd, fatal=False, log_fail=False)

@then('.spec file contains {text}')
def step_impl(context, text):
    spec = specfile.Spec()
    assert text in spec.txt, "%s not found in .spec" % text
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
name : ko_147
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework : 
```gherkin
Scenario: add magic_comment patches_base and patches_ignore when not present
	Given a distgit at Version 1.1.1
	When I run rdopkg set-magic-comment patches_base v1.1.1
	Then .spec file contains patches_base=v1.1.1
	When I run rdopkg set-magic-comment patches_ignore DROP-IN-RPM
	Then .spec file contains patches_ignore
```
input = ""
output:
```python
@given('a distgit at Version {version}')
def step_impl(context, version):
	step = u'Given a distgit at Version %s and Release 2' % version
	context.execute_steps(step)

@when('I run rdopkg {args}')
def step_impl(context, args):
	cmd = ['rdopkg'] + args.split(' ')
	context.command_output = run(*cmd, fatal=False, log_fail=False)

@then('.spec file contains {text}')
def step_impl(context, text):
	spec = specfile.Spec()
	assert text in spec.txt, "%s not found in .spec" % text
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
name : ko_149
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework : 
```gherkin
Scenario: add magic_comment only patches_ignore
	Given a distgit at Version 1.1.1
	Then .spec file doesn't contain patches_base
	Then .spec file doesn't contain patches_ignore
	When I run rdopkg set-magic-comment patches_ignore DROP-IN-RPM
	Then .spec file contains patches_ignore
```
input = ""
output:
```python
@given('a distgit at Version {version}')
def step_impl(context, version):
	step = u'Given a distgit at Version %s and Release 2' % version
	context.execute_steps(step)

@when('I run rdopkg {args}')
def step_impl(context, args):
	cmd = ['rdopkg'] + args.split(' ')
	context.command_output = run(*cmd, fatal=False, log_fail=False)

@then('.spec file contains {text}')
def step_impl(context, text):
	spec = specfile.Spec()
	assert text in spec.txt, "%s not found in .spec" % text

@then('.spec file doesn\'t contain patches_base')
def step_impl(context):
	spec = specfile.Spec()
	assert spec.get_patches_base() == (None, 0)


@then('.spec file doesn\'t contain patches_ignore')
def step_impl(context):
	spec = specfile.Spec()
	assert spec.get_patches_ignore_regex() is None
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
from behave import given, when, then
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
name : ko_155
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework : 
```gherkin
Scenario: set magic_comment to empty string
	Given a distgit at Version 1.1.1
	Then .spec file doesn't contain patches_base
	Then .spec file doesn't contain patches_ignore
	When I run rdopkg set-magic-comment patches_ignore  ''
	Then .spec file doesn't contain patches_ignore
```
input = ""
output:
```python
@given('a distgit at Version {version}')
def step_impl(context, version):
	step = u'Given a distgit at Version %s and Release 2' % version
	context.execute_steps(step)

@when('I run rdopkg {args}')
def step_impl(context, args):
	cmd = ['rdopkg'] + args.split(' ')
	context.command_output = run(*cmd, fatal=False, log_fail=False)

@then('.spec file doesn\'t contain patches_base')
def step_impl(context):
	spec = specfile.Spec()
	assert spec.get_patches_base() == (None, 0)

@then('.spec file doesn\'t contain patches_ignore')
def step_impl(context):
	spec = specfile.Spec()
	assert spec.get_patches_ignore_regex() is None
```

id : seed_task_156
name : ko_156
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework : 
```gherkin
Scenario: rdopkg fix - user reverted all changes
	Given a distgit
	When I run rdopkg fix
	When I undo all changes
	When I run rdopkg --continue
	Then command output contains 'No distgit changes found'
	Then no new commit was created
	Then rdopkg state file is present

```
input = ""
output:
```python
@given('a distgit')
def step_impl(context):
    context.execute_steps(u'Given a distgit at Version 1.2.3 and Release 2')

@when('I run rdopkg {args}')
def step_impl(context, args):
	cmd = ['rdopkg'] + args.split(' ')
	context.command_output = run(*cmd, fatal=False, log_fail=False)

@when(u'I undo all changes')
def step_impl(context):
	git("stash")
	assert git.is_clean()

@then("command output contains '{rex}'")
def step_impl(context, rex):
	assert re.search(rex, context.command_output), "Did not find [{0}] in command output [{1}]".format(rex, context.command_output.encode('ascii', 'replace'))

@then(u'no new commit was created')
def step_impl(context):
	new_commit = git.current_commit()
	assert new_commit == context.old_commit

@then(u'rdopkg state file is present')
def step_check_for_rdopkg_state_file_not_present(context):
	assert os.path.exists(os.path.join(context.distgitdir, STATE_FILE_FN))
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
name : ko_163
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework : 
```gherkin
Scenario: rdopkg new-version --bump-only --bug <id>
	Given a distgit at Version 2.0.0 and Release 3
	When I run rdopkg new-version --bump-only -n 2.1.0 --bug rhbz#12345
	Then command output contains 'Action finished'
	Then .spec file contains new changelog entry with rhbz#12345
	Then new commit was created
	Then git is clean
	Then last commit message contains rhbz#12345
	Then last commit message is:
	    """
	    foo-bar-2.1.0-1

	    Changelog:
	    - Update to 2.1.0 (rhbz#12345)

	    Resolves: rhbz#12345
	    """
```
input = ""
output:
```python
@given('a distgit at Version {version} and Release {release}')
def step_impl(context, version, release):
	_create_distgit(context, version, release)

@when('I run rdopkg {args}')
def step_impl(context, args):
	cmd = ['rdopkg'] + args.split(' ')
	context.command_output = run(*cmd, fatal=False, log_fail=False)

@then("command output contains '{rex}'")
def step_impl(context, rex):
	assert re.search(rex, context.command_output), "Did not find [{0}] in command output [{1}]".format(rex, context.command_output.encode('ascii', 'replace'))

@then('.spec file contains new changelog entry with {text}')
def step_impl(context, text):
	spec = specfile.Spec()
	entry = spec.get_last_changelog_entry()
	changelog_block = '\n'.join(entry[1])
	assert text in changelog_block, "[{0}] not found in [{1}]".format(text, changelog_block)
	assert entry != context.old_changelog_entry

@then(u'git is clean')
def step_impl(context):
	assert git.is_clean(), git('status').encode('ascii', 'replace')

@then(u'last commit message contains {simple_string}')
def step_impl(context, simple_string):
	msg = git.current_commit_message()
	assert simple_string in msg, (u"'{0}' not found in:\n{1}".format(simple_string, msg)).encode('ascii', 'replace')

@then(u'last commit message is')
def step_impl(context):
	msg = git.current_commit_message()
	assert context.text == msg, exdiff(context.text, msg, header="Commit message differs from expected format:")
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
name : ko_166
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework : 
```gherkin
Scenario: rdopkg new-version --bump-only with macro in Name
	Given a distgit at Version 2.0.0 and Release 3
	When I prepend .spec file with:
	    """
	    %global lib foo
	    """
	When I change .spec file tag Name to python-%lib-%{lib}
	When I run rdopkg new-version --bump-only -n 2.1.0
	Then command output contains 'Action finished'
	Then new commit was created
	Then git is clean
	Then last commit message contains python-foo-foo
	Then last commit message is:
	    """
	    python-foo-foo-2.1.0-1

	    Changelog:
	    - Update to 2.1.0
	    """
```
input = ""
output:
```python
@given('a distgit at Version {version} and Release {release}')
def step_impl(context, version, release):
	_create_distgit(context, version, release)

@when(u'I prepend .spec file with')
def step_impl(context):
	spec = specfile.Spec()
	spec._txt = context.text + spec.txt
	spec.save()

@when('I change .spec file tag {tag} to {value}')
def step_impl(context, tag, value):
	spec = specfile.Spec()
	spec.set_tag(tag, value)
	spec.save()

@when('I run rdopkg {args}')
def step_impl(context, args):
	cmd = ['rdopkg'] + args.split(' ')
	context.command_output = run(*cmd, fatal=False, log_fail=False)

@then('.spec file contains new changelog entry with {text}')
def step_impl(context, text):
	spec = specfile.Spec()
	entry = spec.get_last_changelog_entry()
	changelog_block = '\n'.join(entry[1])
	assert text in changelog_block, "[{0}] not found in [{1}]".format(text, changelog_block)
	assert entry != context.old_changelog_entry

@then(u'git is clean')
def step_impl(context):
	assert git.is_clean(), git('status').encode('ascii', 'replace')

@then(u'last commit message contains {simple_string}')
def step_impl(context, simple_string):
	msg = git.current_commit_message()
	assert simple_string in msg, (u"'{0}' not found in:\n{1}".format(simple_string, msg)).encode('ascii', 'replace')

@then(u'last commit message is')
def step_impl(context):
	msg = git.current_commit_message()
	assert context.text == msg, exdiff(context.text, msg, header="Commit message differs from expected format:")
```

id : seed_task_167
name : ko_167
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework : 
```gherkin
Scenario: rdopkg pkgenv with valid patches_base
	Given a distgit at Version 23 and Release 69
	Given a patches branch with 2 patches
	When I set .spec file patches_base to existing commit +42
	When I run rdopkg pkgenv
	Then command output contains 'Version:\s+23'
	Then command output contains 'VR:\s+1:23-69'
	Then command output contains 'Patches base:\s+\w+\+42'
	Then command output contains 'Patches base ref:\s+\w+ : existing git commit'
	Then command output contains 'Local patches branch:\s+master-patches : \w+'
```
input = ""
output:
```python
@given('a distgit at Version {version} and Release {release}')
def step_impl(context, version, release):
	_create_distgit(context, version, release)

@given('a patches branch with {n:n} patches')
def step_impl(context, n):
	distgitmagic.create_sample_patches_branch(n)

@when(u'I set .spec file patches_base to existing commit +{n:n}')
def step_impl(context, n):
	pb = git('show-ref', 'master-patches')[:8]
	if n:
		pb = '%s+%s' % (pb, n)
	context.execute_steps(u'When i set .spec file patches_base=%s' % pb)

@when('I run rdopkg {args}')
def step_impl(context, args):
	cmd = ['rdopkg'] + args.split(' ')
	context.command_output = run(*cmd, fatal=False, log_fail=False)

@then('.spec file contains {text}')
def step_impl(context, text):
	spec = specfile.Spec()
	assert text in spec.txt, "%s not found in .spec" % text

@then('.spec file contains /{rex}/')
def step_impl(context, rex):
	spec = specfile.Spec()
	assert re.search(rex, spec.txt), "/%s/ not found in .spec" % rex
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
name : ko_169
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework : 
```gherkin
Scenario: rdopkg pkgenv with invalid patches_base
	Given a distgit at Version 0 and Release 0
	Given a patches branch with 2 patches
	When I set .spec file patches_base=OVER+9000
	When I run rdopkg pkgenv
	Then command output contains 'Version:\s+0'
	Then command output contains 'VR:\s+1:0-0'
	Then command output contains 'Patches base:\s+OVER\+9000'
	Then command output contains 'Patches base ref:\s+OVER : invalid git reference'
```
input = ""
output:
```python
@given('a distgit at Version {version} and Release {release}')
def step_impl(context, version, release):
	_create_distgit(context, version, release)

@given('a patches branch with {n:n} patches')
def step_impl(context, n):
	distgitmagic.create_sample_patches_branch(n)

@when(u'I set .spec file patches_base={base}')
def step_impl(context, base):
	spec = specfile.Spec()
	spec.set_patches_base(base)
	spec.save()

@when('I run rdopkg {args}')
def step_impl(context, args):
	cmd = ['rdopkg'] + args.split(' ')
	context.command_output = run(*cmd, fatal=False, log_fail=False)

@then('.spec file contains {text}')
def step_impl(context, text):
	spec = specfile.Spec()
	assert text in spec.txt, "%s not found in .spec" % text

@then('.spec file contains /{rex}/')
def step_impl(context, rex):
	spec = specfile.Spec()
	assert re.search(rex, spec.txt), "/%s/ not found in .spec" % rex
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
from behave import given, when, then
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
name : ko_171
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework : 
```gherkin
Scenario: With TTY client sees response immediately even if program does not flush
	Given server started with '--workers=1 0 exec --tty python scripts/program.py'
	When client connects
	And program handles the request
	Then program recognizes that it runs in TTY
	When program writes 'hello'
	Then client receives 'hello'
```
input = ""
output:
```python
@given(u'server started with \'{cmd}\'')
def step_impl(context, cmd):
	context.server = subprocess.Popen(shlex.split('./malunas ' + cmd), stdout = subprocess.PIPE, stderr = subprocess.PIPE, bufsize = 1)
	poller = select.poll()
	poller.register(context.server.stderr, select.POLLIN)
	poll_result = poller.poll(TIMEOUT)
	if poll_result:
		line = context.server.stderr.readline()
		print(line)
		m = re.compile(r'^malunas: Listening on 0.0.0.0:(?P<port>\d+)').match(line) 
		context.port = int(m.group('port'))
	assert(context.server.poll() is None), 'server died: %s' % context.server.stderr.read(100) 

@when(u'client connects')
def step_impl(context):
	context.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server_address = ('localhost', context.port)
	context.client.connect(server_address)

@when(u'program handles the request')
def step_impl(context):
	connection, client_address = context.pm.accept()
	context.control_socket = connection

@then(u'program recognizes that it runs in TTY')
def step_impl(context):
	context.control_socket.send('ISTTY?\n')
	line = context.control_socket.recv(10) 
	assert("TTY=1" == line.strip()), 'program cannot confirm that it runs in a TTY'

@when(u'program writes \'hello\'')
def step_impl(context):
	context.control_socket.send('WRITE hello\n')

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

id : seed_task_172
name : ko_172
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework : 
```gherkin
Scenario: Without TTY client does not see any response if program does not flush
	Given server started with '--workers=1 0 exec python scripts/program.py' 
	When client connects
	And program handles the request
	Then program recognizes that it does not run in TTY
	When program writes 'hello'
	Then client does not receive anything
	When program exits 
	Then client receives 'hello'
```
input = ""
output:
```python
@given(u'server started with \'{cmd}\'')
def step_impl(context, cmd):
	context.server = subprocess.Popen(shlex.split('./malunas ' + cmd), stdout = subprocess.PIPE, stderr = subprocess.PIPE, bufsize = 1)
	poller = select.poll()
	poller.register(context.server.stderr, select.POLLIN)
	poll_result = poller.poll(TIMEOUT)
	if poll_result:
		line = context.server.stderr.readline()
		print(line)
		m = re.compile(r'^malunas: Listening on 0.0.0.0:(?P<port>\d+)').match(line) 
		context.port = int(m.group('port'))
	assert(context.server.poll() is None), 'server died: %s' % context.server.stderr.read(100) 

@when(u'client connects')
def step_impl(context):
	context.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server_address = ('localhost', context.port)
	context.client.connect(server_address)

@when(u'program handles the request')
def step_impl(context):
	connection, client_address = context.pm.accept()
	context.control_socket = connection

@then(u'program recognizes that it does not run in TTY')
def step_impl(context):
	context.control_socket.send('ISTTY?\n')
	line = context.control_socket.recv(10) 
	assert("TTY=0" == line.strip()), 'program cannot confirm that it does not run in a TTY'

@when(u'program writes \'hello\'')
def step_impl(context):
	context.control_socket.send('WRITE hello\n')

@then(u'client does not receive anything')
def step_impl(context):
	context.client.settimeout(TIMEOUT)
	try:
		line = context.client.recv(10) 
	except socket.timeout:
		return
	assert(None == line), 'Message some output was unexpectedly read from socket: %s' % line

@when(u'program exits')
def step_impl(context):
	context.control_socket.send('EXIT\n')

@then(u'client receives \'hello\'')
def step_impl(context):
	context.client.settimeout(TIMEOUT)
	line = context.client.recv(10)
	assert("hello" == line.strip()), "Message not received by client, but received: '%s'" % line
```

id : seed_task_173
name : ko_173
instruction :
Generate a Python implementation of the step functions for the following Gherkin scenario using the behave BDD testing framework : 
```gherkin
Scenario: Login Success
	Given the user has the correct credentials
	When the user enters username
	And the user enters password
	And clicks Login
	Then the user is presented with a welcome message
```
input = ""
output:
```python
@given(u'the user has the correct credentials')
def step_impl(context):
	context.browser.get('http://www.google.com')
	raise NotImplementedError(u'STEP: Given the user has the correct credentials')

@when(u'the enter username')
def step_impl(context):
	raise NotImplementedError(u'STEP: When the enter username')

@when(u'the user enters password')
def step_impl(context):
	raise NotImplementedError(u'STEP: When the user enters password')

@when(u'clicks Login')
def step_impl(context):
	raise NotImplementedError(u'STEP: When clicks Login')

@then(u'the user is presented with a welcome message')
def step_impl(context):
	raise NotImplementedError(u'STEP: Then the user is presented with a welcome message')
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
