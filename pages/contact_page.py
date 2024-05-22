from locators import contactpage_locators
from urls import urls
from playwright.sync_api import Page, expect


class ContactPage:
    def __init__(self, page):
        self.page = page
        self.contactpage_title = contactpage_locators.ContactPageLocators.contactpage_title

    def navigate(self, page):
        self.page = page
        self.page.goto(urls.Urls.contactpage_url)

    def check_contactpage_title(self, page):
        self.page = page
        expect(page).to_have_title(contactpage_locators.ContactPageLocators.contactpage_title)

    def add_valid_contact_data(self, page):
        self.page = page
        page.locator(contactpage_locators.ContactPageLocators.contactpage_firstname).type('Test')
        page.locator(contactpage_locators.ContactPageLocators.contactpage_lasttname).type('Test')
        page.locator(contactpage_locators.ContactPageLocators.contactpage_company).type('STRV')
        page.locator(contactpage_locators.ContactPageLocators.contactpage_jobTitle).type('QA')
        page.locator(contactpage_locators.ContactPageLocators.contactpage_location).type('Prague')
        page.locator(contactpage_locators.ContactPageLocators.contactpage_source).type('work')
        page.locator(contactpage_locators.ContactPageLocators.contactpage_message).type('Test')

    def type_invalid_email(self, page):
        self.page = page
        page.locator(contactpage_locators.ContactPageLocators.contactpage_email).type(
            contactpage_locators.ContactPageLocators.contactpage_invalid_email)

    def type_valid_email(self, page):
        self.page = page
        page.locator(contactpage_locators.ContactPageLocators.contactpage_email).type(
            contactpage_locators.ContactPageLocators.contactpage_valid_email)

    def click_send_button(self, page):
        self.page = page
        page.locator(contactpage_locators.ContactPageLocators.contactpage_sendbutton).click()

    def check_invalid_email_error(self, page):
        self.page = page
        expect(page.locator(contactpage_locators.ContactPageLocators.contactpage_email_input_error))\
            .to_be_visible()

    def check_success_message(self, page):
        self.page = page
        expect(page.locator(contactpage_locators.ContactPageLocators.contactpage_success_message)).to_be_visible()