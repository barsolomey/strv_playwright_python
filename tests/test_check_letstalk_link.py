from playwright.sync_api import Page, expect
from pytest_bdd import scenario, given, when, then
import pages.homepage
import pages.contact_page
from locators import contactpage_locators

@scenario('homepage.feature', 'User clicks Lets talk button')
def test_check_lets_talk_link(page: Page):
    pass

@given('User navigates to STRV web')
def navigate_to_homepage(page: Page):
    homepage = pages.homepage.HomePage(page)
    homepage.navigate()


@when('User clicks Lets talk button')
def click_lets_talk_button(page: Page):
    homepage = pages.homepage.HomePage(page)
    homepage.click_lets_talk_button()


@then('User navigates to Contact page')
def check_contact_page_url(page: Page):
    contactpage = pages.contact_page.ContactPage(page)
    contactpage.check_contactpage_title(page)