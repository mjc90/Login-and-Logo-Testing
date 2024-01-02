
# Login and Logo Testing Project

This repository contains a list of three projects completed during my automation testing training. These projects were completed using a combination of selenium and behave framework.


## Authors

- [@mjc90](https://github.com/mjc90/Login-and-Logo-Testing.git)


## Project List

| Project Name                           | Description                                                                                             | Tools Used     |
| -------------------------------------- | ------------------------------------------------------------------------------------------------------- | -------------- |
| Login and Logo Testing                 | Verified the presence of a logo on the login page of a web application.                                 | Selenium with Python Behave (BDD)  |
| Login and Logo Testing                 | Verified successful login and redirection to the dashboard by providing the correct username and password on a web application. | Selenium with Python Behave (BDD)  |
| Login and Logo Testing                 | newfnwenfuwenfuwe                                                                                                | Selenium with Python Behave (BDD)  |



## Getting Started


# OrangeHRM Logo Verification Automation

The primary objective of this project is to automate the verification of the presence of the OrangeHRM logo on the OrangeHRM homepage using the Behave framework with Selenium for web automation.


## Feature: OrangeHRM Logo Verification

This feature specifies a scenario where the presence of the OrangeHRM logo on the homepage is verified.

#### Scenario: Logo Presence on OrangeHRM Home Page

#### Steps:

#### 1. Given launch chrome browser

* Action: This step initializes the Chrome browser using Selenium's webdriver.Chrome().
* Expected Result: The Chrome browser window should launch and be maximized.

#### 2. When open orange hrm homepage

* Action: This step navigates the initialized Chrome browser to the OrangeHRM homepage URL: https://opensource-demo.orangehrmlive.com/web/index.php/auth/login.
* Expected Result: The OrangeHRM homepage should load within 12 seconds (as indicated by the time.sleep(12) statement).

#### 3. Then verify that the logo present on page

* Action: This step verifies the presence of the OrangeHRM logo on the homepage using an XPath locator (//img[@alt='company-branding']).
* Expected Result: The OrangeHRM logo should be displayed on the homepage. If the logo is present and displayed, the assertion will pass; otherwise, it will fail.

#### 4. And close browser

* Action: This step closes the Chrome browser that was initialized at the beginning of the test scenario.
* Expected Result: The Chrome browser window should be closed, ending the test scenario.

## Implementation:

#### * Behave Framework:
The Behave framework is utilized for BDD (Behavior-Driven Development) testing, allowing for structured, human-readable test scenarios and step definitions.

#### * Selenium WebDriver: 
Selenium WebDriver is employed to automate the web browser actions, such as launching the browser, navigating to URLs, and verifying elements on web pages.

#### * XPath Locator:
An XPath locator (//img[@alt='company-branding']) is used to locate and verify the presence of the OrangeHRM logo on the homepage.

#### * Time Delay:
A time delay of 12 seconds (time.sleep(12)) is added before verifying the logo's presence. This delay provides the webpage with sufficient time to load the logo, ensuring accurate verification.

##  Conclusion: 
By executing this scenario, the process of verifying the OrangeHRM logo's presence on its homepage is automated, ensuring consistent and efficient logo verification.




## Contributing

Contributions are always welcome!

If you have any feedback or suggestions for improvements, please feel free to open an issue or pull request.

