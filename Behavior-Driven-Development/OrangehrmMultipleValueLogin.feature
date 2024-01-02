Feature: OrangeHRM Login

  Scenario Outline: Login to OrangeHRM with multiple parameters
    Given I launch Chrome browser
    When I open orange HRM Login page
    And Enter username "<Username>" and password "<Password>"
    And Click on login button
    Then User must successfully login to the Dashboard page


    Examples:
      | Username | Password |
      | admin    | admin123 |
      | admin123 | admin    |
      | adminxyz | admin123 |
      | admin    | adminxyz |


#Open the Terminal and locate the OrangehrmLogin.feature file and press enter.
#Here is the command - "behave Behavior-Driven-Development\OrangehrmMultipleValueLogin.feature"
# Allure Report Command - behave -f allure_behave.formatter:AllureFormatter -o Reports/ Behavior-Driven-Development\OrangehrmMultipleValueLogin.featur
# allure serve Results/