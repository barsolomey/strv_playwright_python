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