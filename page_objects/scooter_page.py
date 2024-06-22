from locators.base_page_locators import BasePageLocators
from locators.scooter_page_locators import ScooterPageLocators
from page_objects.base_page import BasePage


class ScooterPage(BasePage):
    def switch_to_scooter_page(self):
        self.click_to_element(ScooterPageLocators.LOGO_SCOOTER)
        self.switch_to_new_window()
        self.wait_visibility_element(BasePageLocators.TEXT_SCOOTER)
        current_url = self.get_current_url()
        return current_url
