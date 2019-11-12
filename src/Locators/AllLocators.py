from selenium.webdriver.common.by import By

class HomePageLocators():
    SIGN_UP_FOR_TRIAL_BUTTON=(By.LINK_TEXT,"USE AUTH0 FOR FREE")

class SignUpPageLocators():
    EMAIL_TEXT_BOX=(By.NAME,"email")
    PASSWORD_TEXT_BOX=(By.NAME,"password")
    SIGN_UP_BUTTON=(By.LINK_TEXT,"SIGN UP")
    ERROR_MESSAGE_DIV=(By.CLASS_NAME,"text-error-utils")