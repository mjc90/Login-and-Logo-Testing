from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
@given('launch chrome browser')
def LaunchBrowser(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()

@when('open orange hrm homepage')
def OpenHomepage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

@then('verify that the logo present on page')
def VerifyLogo(context):
    status = context.driver.find_element(By.XPATH, "//img[@alt='company-branding']").is_displayed
    assert status is True

@then('close browser')
def CloseBrowser(context):
    context.driver.close()