Feature: Search Feature
   Scenario: Validating the search feature
     Given I navigate to google.com
     When I validate the page title
     Then I enter "Automation Step by Step" in search box
     And I click on the search button
     Then I validate the search results