# HQFS247
## Scenario
```gherkin
scenario: social network validation 
   given that i'm on the home page 
   when i click on contact 
   then i validate the social media links
```


## Python Implementation
```python
from behave import given, when, then @given("that i'm on the home page") def step_given_that_i_m_on_the_home_page(context): pass @when("i click on contact") def step_when_i_click_on_contact(context):
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: social network validation given that i'm on the home page when i click on contact then i validate the social media links ``` ```python from behave import given, when, then @given("that i'm on the home page") def step_given_that_i_m_on_the_home_page(context): pass @when("i click on contact") def step_when_i_click_on_contact(context):

```

```python from behave import given, when, then @given("that i'm on the home page") def step_given_that_i_m_on_the_home_page(context): pass @when("i click on contact") def step_when_i_click_on_contact(context): context.browser.find_element_by_link_text("Contact").click() @then("i validate the social media links") def step_then_i_validate_the_social_media_links(context): social_links = context.browser.find_elements_by_css_selector("a.social-media-link") for link in social_links: assert link.get_attribute("href") in ["https://www.facebook.com/", "https://twitter.com/", "https://www.instagram.com/"]
```

Task: Write a program to find the sum of the digits of a given number.
