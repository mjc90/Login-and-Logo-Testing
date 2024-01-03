
# Login and Logo Testing Project

This repository contains a list of three projects completed during my automation testing training. These projects were completed using a combination of selenium and behave framework.


## Authors

- [@mjc90](https://github.com/mjc90/Login-and-Logo-Testing.git)


## Project List

| Project Name                           | Description                                                                                             | Tools & Technologies Used     |
| -------------------------------------- | ------------------------------------------------------------------------------------------------------- | -------------- |
| OrangeHRM Logo Verification Automation                 | Verified the presence of a logo on the login page of a web application.                                 | Behave Framework, Selenium WebDriver, Chrome WebDriver, XPath Locators  |
| OrangeHRM Login Verification Automation                 | Verified successful login and redirection to the dashboard by providing the correct username and password on a web application. | Behave Framework, Selenium WebDriver, Chrome WebDriver, XPath Locators  |
| OrangeHRM Login Automation with Multiple Parameters                 | Automates the OrangeHRM login using BDD and Selenium, testing multiple username-password combinations for enhanced reliability and efficiency.                                                                                             | Behave Framework, Selenium WebDriver, Chrome WebDriver, XPath Locators, Allure Reporting  |



## Getting Started


# Project 1 - OrangeHRM Logo Verification Automation

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







# Project 2 - OrangeHRM Login Verification Automation

The primary objective of this project is to automate the verification of the presence of the OrangeHRM logo on the OrangeHRM homepage using the Behave framework with Selenium for web automation.


## OrangeHRM Login Automation

The primary objective of this project is to automate the login process to the OrangeHRM application using valid credentials. The automation ensures that users can successfully log in to the Dashboard page after entering the correct username and password.

## Feature: OrangeHRM Login
This feature outlines a scenario for automating the login process to the OrangeHRM application using valid parameters.

#### Scenario: Login to OrangeHRM with Valid Parameters

#### Steps:

#### 1. Given I launch Chrome browser
* Action: This step initializes the Chrome browser using Selenium's 'webdriver.Chrome()'.

* Expected Result: The Chrome browser window should launch successfully.

#### 2. When I open OrangeHRM Login page
* Action: This step navigates the initialized Chrome browser to the OrangeHRM Login page URL: https://opensource-demo.orangehrmlive.com/web/index.php/auth/login.

* Expected Result: The OrangeHRM Login page should load within 15 seconds, allowing users to enter their credentials.

#### 3. And Enter username "{user}" and password "{pwd}"
* Action: This step inputs the provided username ("admin") and password ("admin123") into the respective fields on the OrangeHRM Login page.

* Expected Result: The username and password fields should be populated with the provided credentials.

#### 4. And Click on login button
* Action:  This step clicks on the "Login" button on the OrangeHRM Login page to submit the entered credentials.

* Expected Result: The system should process the provided credentials and redirect the user to the Dashboard page within 8 seconds.

#### 5. Then User must successfully login to the Dashboard page
* Action:   This step verifies that the user has successfully logged in by confirming the presence of the "Dashboard" text on the Dashboard page.

* Expected Result: The "Dashboard" text should be displayed on the Dashboard page, confirming successful login. The Chrome browser window should then be closed, concluding the test scenario.

## Implementation:

#### * Behave Framework:
The Behave framework is utilized for Behavior-Driven Development (BDD) testing, enabling structured, human-readable test scenarios and step definitions.

#### * Selenium WebDriver: 
 Selenium WebDriver is employed to automate web browser actions, including launching the Chrome browser, navigating to specific URLs, entering credentials, clicking buttons, and verifying elements on web pages.

#### * XPath Locator:
 XPath locators are used to identify and interact with web elements such as input fields and buttons on the OrangeHRM Login page.

#### * Time Delay:
Time delays using time.sleep() are incorporated to ensure that web elements and pages have sufficient time to load, facilitating accurate interaction and verification.

##  Conclusion: 
By executing this project, you can automate the login process to the OrangeHRM application using valid credentials. This automation enhances testing efficiency by eliminating manual login efforts, ensuring consistent login results, and facilitating user authentication validation in the OrangeHRM system.





# Project 3 - OrangeHRM Login Automation with Multiple Parameters

The primary objective of this project is to automate the login process to the OrangeHRM web application using various combinations of usernames and passwords. By utilizing a Scenario Outline with Examples, the automation tests multiple parameter combinations to ensure that users can successfully log in to the Dashboard page with valid credentials.


## Feature: OrangeHRM Login

This feature outlines a scenario for automating the login process to the OrangeHRM application using multiple parameter combinations.

#### Scenario Outline: Login to OrangeHRM with Multiple Parameters

#### Steps:

#### 1. Given I launch Chrome browser

* Action: This step initializes the Chrome browser using Selenium's webdriver.Chrome().
* Expected Result: The Chrome browser window should launch successfully.

#### 2. When I open OrangeHRM Login page

* Action: This step navigates the initialized Chrome browser to the OrangeHRM Login page URL: https://opensource-demo.orangehrmlive.com/web/index.php/auth/login.
* Expected Result: The OrangeHRM Login page should load within 15 seconds, allowing users to enter their credentials.

#### 3. And Enter username "{user}" and password "{pwd}"

* Action: This step inputs the provided username and password combinations into the respective fields on the OrangeHRM Login page.
* Expected Result: The username and password fields should be populated with the provided credentials.

#### 4. And Click on login button

* Action: This step clicks on the "Login" button on the OrangeHRM Login page to submit the entered credentials.
* Expected Result: The system should process the provided credentials and redirect the user to the Dashboard page within 8 seconds.

#### 5. Then User must successfully login to the Dashboard page

* Action: This step verifies that the user has successfully logged in by confirming the presence of the "Dashboard" text on the Dashboard page.
* Expected Result: The "Dashboard" text should be displayed on the Dashboard page, confirming successful login. If the test fails, an assertion error message is displayed, and the Chrome browser window is closed.

### Examples:
The Scenario Outline is parameterized with multiple examples of username and password combinations, including:
* Username: admin, Password: admin123
* Username: admin123, Password: admin
* Username: adminxyz, Password: admin123
* Username: admin, Password: adminxyz

Each example represents a unique combination of usernames and passwords to test various scenarios and validate the login functionality across different credential inputs.

## Implementation:

#### * Behave Framework:
The Behave framework is utilized for Behavior-Driven Development (BDD) testing, enabling structured, human-readable test scenarios and step definitions.

#### * Selenium WebDriver: 
Selenium WebDriver is employed to automate web browser actions, including launching the Chrome browser, navigating to specific URLs, entering credentials, clicking buttons, and verifying elements on web pages.

#### * XPath Locator:
XPath locators are used to identify and interact with web elements such as input fields, buttons, and text on the OrangeHRM Login page and Dashboard page.

#### * Time Delay:
Time delays using time.sleep() are incorporated to ensure that web elements and pages have sufficient time to load, facilitating accurate interaction and verification.

##  Conclusion: 
By executing this project, i can automate the login process to the OrangeHRM application using multiple parameter combinations. This automation enhances testing efficiency by testing various credential scenarios, ensuring consistent login results, and facilitating user authentication validation in the OrangeHRM system.





## Contributing

Contributions are always welcome!

If you have any feedback or suggestions for improvements, please feel free to open an issue or pull request.

