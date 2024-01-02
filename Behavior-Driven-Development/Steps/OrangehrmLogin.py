from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


@given('I launch Chrome browser')
def browser_launch(context):
    context.driver = webdriver.Chrome()


@when('I open orange HRM Login page')
def login_page(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(15)


@when('Enter username "{user}" and password "{pwd}"')
def pass_parameters(context, user, pwd):
    context.driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys(user)
    context.driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys(pwd)


@when('Click on login button')
def button_click(context):
    context.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
    time.sleep(8)


@then('User must successfully login to the Dashboard page')
def dash(context):
    text = context.driver.find_element(By.XPATH, "//h6[normalize-space()='Dashboard']").text
    assert text == "Dashboard"
    context.driver.close()
