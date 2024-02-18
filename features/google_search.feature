@sanity
Feature: Search Feature
   Background:
     Given I navigate to google.com
   Scenario: Validating the search feature
     When I validate the page title
     Then I enter "Automation Step by Step" in search box
     And I click on the search button

   Scenario: Validating the search results with nex text
     When I validate the page title
     Then I enter "Hello Behave" in search box
     And I click on the search button