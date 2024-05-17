from playwright.sync_api import Page
from pytest_bdd import scenario, given, then
import pages
from pages import homepage


@scenario('homepage.feature', 'User visits STRV homepage')
def test_check_homepage_title():
    pass


@given('User navigates to STRV web')
def navigate_to_homepage(page: Page):
    homepage = pages.homepage.HomePage(page)
    homepage.navigate()


@then('Title of the homepage equals STRV - Next-Level Design and Engineering Team')
def check_homepage_title(page: Page):
    homepage = pages.homepage.HomePage(page)
    homepage.check_homepage_title(page)
