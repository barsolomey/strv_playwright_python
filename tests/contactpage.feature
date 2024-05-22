#noinspection CucumberUndefinedStep
Feature: STRV Contact Page
  #C42077
  Scenario: User visits STRV contact page
    Given User is on the STRV web Contact page
    Then Title of the contact page equals Contact Us - Starting a Project With STRV

  #C42075
  Scenario: User types valid email into email field
    Given User is on the STRV web contact page
    And User filled in all mandatory input fields
    When User types "<valid email>" into email field
    And clicks SEND button
    Then Thank you message is displayed to user

  #C42076
  Scenario: User types invalid email into email field
    Given User is on the STRV web contact page
    And User filled in all mandatory input fields
    When User types "<invalid email>" into email field
    And clicks SEND button
    Then "<invalid email address error>" is displayed under the email input