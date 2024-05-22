from playwright.sync_api import Page
from pytest_bdd import scenario, given, when, then
from pages import contact_page


contact_page = contact_page.ContactPage(Page)

@scenario('contactpage.feature', 'User visits STRV contact page')
def test_check_contactpage_title_C42077(page: Page):
    pass

@given('User is on the STRV web Contact page')
def navigate_to_contact_page(page: Page):
    contact_page.navigate(page)


@then('Title of the contact page equals Contact Us - Starting a Project With STRV')
def check_contactpage_title(page: Page):
    contact_page.check_contactpage_title(page)
