# HQFS108
## Scenario
```gherkin
scenario: create a new hotspot metric configuration 
   given i am logged in to the admin panel 
   when i click on the 'create new hotspot metric configuration' button 
   then i should be redirected to the 'create new hotspot metric configuration' page
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: create a new hotspot metric configuration given i am logged in to the admin panel when i click on the 'create new hotspot metric configuration' button then i should be redirected to the 'create new hotspot metric configuration' page ```



from behave import given, when, then

@given("i am logged in to the admin panel")
def step_impl(context):
    context.browser.get("https://admin.example.com/login")
    context.browser.find_element_by_name("username").send_keys("admin")
    context.browser.find_element_by_name("password").send_keys("password")
    context.browser.find_element_by_xpath("//button[@type='submit']").click()

@when("i click on the 'create new hotspot metric configuration' button")
def step_impl(context):
    context.browser.find_element_by_link_text("Create New Hotspot Metric Configuration").click()

@then("i should be redirected to the 'create new hotspot metric configuration' page")
def step_impl(context):
    assert context.browser.current_url == "https://admin.example.com/hotspot-metric-configurations/new"
