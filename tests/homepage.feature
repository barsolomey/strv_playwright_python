#noinspection CucumberUndefinedStep
Feature: STRV Homepage
  #C42050
  Scenario: User clicks Lets talk button
    Given User is on STRV web homepage
    When User clicks Lets talk button
    Then User is on the STRV web Contact page
  #C42051
  Scenario: User visits STRV homepage
    Given User is on STRV web homepage
    Then Title of the homepage equals STRV - Next-Level Design and Engineering Team