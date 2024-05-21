from locators import homepage_locators
from urls import urls
from playwright.sync_api import Page, expect


class HomePage:
    def __init__(self, page):
        self.page = page
        self.header_text_nextlevel = homepage_locators.HomePageLocators.header_text_nextlevel

    def navigate(self, page):
        self.page = page
        self.page.goto(urls.Urls.homepage_url)

    def click_lets_talk_button(self, page):
        self.page = page
        self.page.get_by_role("link", name=homepage_locators.HomePageLocators.letstalk_button_wave).click()

    def check_homepage_title(self, page):
        self.page = page
        expect(page).to_have_title(homepage_locators.HomePageLocators.homepage_title)
