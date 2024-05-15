from locators import homepage_locators
from urls import urls
from playwright.sync_api import Page, expect


class HomePage:
    def __init__(self, page):
        self.page = page
        self.header_text_nextlevel = homepage_locators.HomePageLocators.header_text_nextlevel

    def navigate(self):
        self.page.goto(urls.Urls.homepage_url)

    def check_lets_talk_links(self):
        self.page.get_by_text("Let's talk")
