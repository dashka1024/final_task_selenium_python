from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK=(By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM=(By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM=(By.CSS_SELECTOR, "#register_form")
    EMAIL_FIELD=(By.CSS_SELECTOR,"#id_registration-email")
    PASSWORD_FIELD=(By.CSS_SELECTOR,"#id_registration-password1")
    CONFIRM_PASSWORD_FIELD=(By.CSS_SELECTOR,"#id_registration-password2")
    REGISTER_BUTTON=(By.CSS_SELECTOR,"[name='registration_submit']")

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON=(By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME=(By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_IN_BASKET=(By.CSS_SELECTOR, ".alert:nth-child(1) .alertinner strong")
    MESSAGE_ADDED_TO_BASKET=(By.CSS_SELECTOR, ".alert:nth-child(1) .alertinner")
    PRICE=(By.CSS_SELECTOR,".product_main .price_color")
    AMOUNT=(By.CSS_SELECTOR,".alert:nth-child(3) .alertinner p strong")
    MESSAGE_AMOUNT_IN_BASKET=(By.CSS_SELECTOR,".alert:nth-child(3) .alertinner p:nth-child(1)")
    SUCCESS_MESSAGE=(By.CSS_SELECTOR,".alert-success:nth-child(1) .alertinner")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    GO_TO_BASKET_FROM_HEADER_BUTTON = (By.CSS_SELECTOR, ".btn[href*='basket']")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    PRODUCT_IN_BASKET_ON_BASKET_PAGE = (By.CSS_SELECTOR, ".basket-items")
    MESSAGE_BASKET_IS_EMPTY = (By.CSS_SELECTOR, "#content_inner > p")
    


  