from playwright.sync_api import Page
from pytest_bdd import scenario, given, when, then
from pages import contact_page


contact_page = contact_page.ContactPage(Page)

@scenario('contactpage.feature', 'User types invalid email into email field')
def test_check_email_input_field_invalid_email_C42075(page: Page):
    pass


@given('User is on the STRV web contact page')
def navigate_to_contact_page(page: Page):
    contact_page.navigate(page)


@given('User filled in all mandatory input fields')
def add_valid_data(page: Page):
    contact_page.add_valid_contact_data(page)


@when('User types "<invalid email>" into email field')
def type_invalid_email(page: Page):
    contact_page.type_invalid_email(page)


@when('clicks SEND button')
def click_send_button(page: Page):
    contact_page.click_send_button(page)


@then('"<invalid email address error>" is displayed under the email input')
def check_invalid_email_error(page: Page):
    contact_page.check_invalid_email_error(page)
