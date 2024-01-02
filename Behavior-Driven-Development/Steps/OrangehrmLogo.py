from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


@given('launch chrome browser')
def LaunchBrowser(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()

@when('open orange hrm homepage')
def OpenHomepage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(12)

@then('verify that the logo present on page')
def VerifyLogo(context):
    status = context.driver.find_element(By.XPATH, "//img[@alt='company-branding']")
    assert status.is_displayed() is True

@then('close browser')
def CloseBrowser(context):
    context.driver.close()


