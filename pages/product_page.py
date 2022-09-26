from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators

class ProductPage(BasePage):
	def click_add_product_to_basket(self):
		button=self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
		button.click()
		#self.should_be_message_added_to_basket()

	def should_be_message_added_to_basket(self):
		name=self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
		assert name in self.browser.find_element(*ProductPageLocators.MESSAGE_ADDED_TO_BASKET).text, "Incorrect name of product in basket"

	def amount_should_be_equal_to_price(self):
		price=self.browser.find_element(*ProductPageLocators.PRICE).text
		assert price in self.browser.find_element(*ProductPageLocators.AMOUNT).text, "Incorrect amount in basket"

		