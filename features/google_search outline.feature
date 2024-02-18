@smoke
Feature: Search Feature
   Scenario Outline: Validating the search feature
     Given I navigate to google.com
     When I validate the page title
     Then I enter "<searchTitle>" in search box
     And I click on the search button
     Examples:
         | searchTitle |
         | Hello BDD   |
         | Hello TDD   |