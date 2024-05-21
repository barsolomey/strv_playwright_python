from playwright.sync_api import Page
from pytest_bdd import scenario, given, when, then
import pages
from pages import homepage, contact_page


@scenario('homepage.feature', 'User clicks Lets talk button')
def test_check_letstalk_link(page: Page):
    pass


@given('User navigates to STRV web')
def navigate_to_homepage(page: Page):
    homepage = pages.homepage.HomePage(page)
    homepage.navigate(page)


@when('User clicks Lets talk button')
def click_lets_talk_button(page: Page):
    homepage = pages.homepage.HomePage(page)
    homepage.click_lets_talk_button(page)


@then('User navigates to Contact page')
def check_contact_page_url(page: Page):
    contactpage = pages.contact_page.ContactPage(page)
    contactpage.check_contactpage_title(page)
