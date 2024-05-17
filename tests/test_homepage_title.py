from playwright.sync_api import Page, expect
from pytest_bdd import scenario, given, when, then
import pages.homepage
from locators import homepage_locators


@scenario('homepage.feature', 'User visits STRV homepage')
def test_homepage_title():
    pass


@given('User navigates to STRV web')
def navigate_to_homepage(page: Page):
    homepage = pages.homepage.HomePage(page)
    homepage.navigate()


@then('Title of the homepage equals STRV - Next-Level Design and Engineering Team')
def check_homepage_title(page: Page):
    homepage = pages.homepage.HomePage(page)
    homepage.check_homepage_title(page)
