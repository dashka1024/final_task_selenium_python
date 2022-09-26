from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK=(By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM=(By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM=(By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON=(By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME=(By.CSS_SELECTOR, ".product_main h1")
    MESSAGE_ADDED_TO_BASKET=(By.CSS_SELECTOR, ".alert:nth-child(1) .alertinner")
    PRICE=(By.CSS_SELECTOR,".product_main .price_color")
    AMOUNT=(By.CSS_SELECTOR,".alert:nth-child(3) .alertinner p")
    


  