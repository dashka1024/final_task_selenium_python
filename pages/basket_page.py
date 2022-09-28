from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):

	def should_not_be_products_in_basket(self):
		assert self.is_not_element_present(*BasketPageLocators.PRODUCT_IN_BASKET_ON_BASKET_PAGE), "There are products in basket"

	def should_be_message_basket_is_empty(self):
		assert self.is_element_present(*BasketPageLocators.MESSAGE_BASKET_IS_EMPTY), "There is no message 'Basket is empty'"