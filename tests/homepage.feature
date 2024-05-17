#noinspection CucumberUndefinedStep
Feature: STRV Homepage
  #C42050
  Scenario: User clicks Lets talk button
    Given User navigates to STRV web
    When User clicks Lets talk button
    Then User navigates to Contact page
  #C42051
  Scenario: User visits STRV homepage
    Given User navigates to STRV web
    Then Title of the homepage equals STRV - Next-Level Design and Engineering Team