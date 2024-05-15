from playwright.sync_api import Page, expect

import pages.homepage
from locators import homepage_locators


def test_check_title(page: Page):
    # Go to STRV homepage and check that homepage url matches
    homepage = pages.homepage.HomePage(page)
    homepage.navigate()
    # Expect a title "to contain" a substring.
    expect(page).to_have_title(homepage_locators.HomePageLocators.homepage_title)


def test_check_links(page: Page):

    homepage = pages.homepage.HomePage(page)
    homepage.navigate()
    # expect links "let's talk" have contact page url
    locator = homepage_locators.HomePageLocators.letstalk_button_menu
    expect(locator).to_have_attribute("href", "https://strv.com/contacts")