import time
from behave import given, when, then
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

@given(u'I navigate to google.com')
def step_impl(context):
    context.driver.get("https://www.google.com")

@when(u'I validate the page title')
def step_impl(context):
    title = context.driver.title
    print("Title of the page is: " + title)
    assert "Googles" in title


@then(u'I enter "{searchText}" in search box')
def step_impl(context, searchText):
    context.driver.find_element("name", "q").send_keys(searchText)
    time.sleep(2)

@then(u'I click on the search button')
def step_impl(context):
    context.driver.find_element("name", "btnK").click()
    time.sleep(2)
