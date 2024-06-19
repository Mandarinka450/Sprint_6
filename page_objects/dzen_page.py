import time
from locators.dzen_page_locators import DzenPageLocators
from page_objects.base_page import BasePage


class DzenPage(BasePage):
    def switch_to_dzen_page(self):
        self.click_to_element(DzenPageLocators.LOGO_DZEN)
        self.switch_to_new_window()
        self.wait_visibility_element(DzenPageLocators.NEWS)
        current_url = self.get_current_url()
        return current_url
