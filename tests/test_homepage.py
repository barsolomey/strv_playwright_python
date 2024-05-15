import re
from playwright.sync_api import Page, expect

import pages.homepage
from pages import homepage
from locators import homepage_locators
from pages.homepage import HomePage
from urls import urls


def test_has_title(page: Page):
    # Go to STRV homepage and check that homepage url matches
    homepage = pages.homepage.HomePage(page)
    homepage.navigate()
    # Expect a title "to contain" a substring.
    expect(page).to_have_title(homepage_locators.HomePageLocators.homepage_title)
