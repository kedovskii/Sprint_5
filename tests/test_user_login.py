from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import MainPageLocators, AuthModalWindowLocators


class TestUserLogin:

    def test_user_can_login_successfully(self, driver, base_url, existing_user_credentials):
        email = existing_user_credentials["email"]
        password = existing_user_credentials["password"]
        expected_user_name = "User."

        # Шаг 1. Открыть главную страницу
        driver.get(base_url)

        # Шаг 2. Нажать кнопку «Вход и регистрация»
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(MainPageLocators.LOGIN_REGISTER_BUTTON)).click()

        # Шаг 3. Заполнить поле Email
        email_input = WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(AuthModalWindowLocators.EMAIL_INPUT))
        email_input.clear()
        email_input.send_keys(email)

        # Шаг 4. Заполнить поле «Пароль»
        password_input = WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(AuthModalWindowLocators.PASSWORD_INPUT))
        password_input.clear()
        password_input.send_keys(password)

        # Шаг 5. Нажать кнопку «Войти»
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(AuthModalWindowLocators.LOGIN_SUBMIT_BUTTON)).click()

        # Проверка: на главной в шапке отображаются аватар и имя пользователя User.
        assert WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(MainPageLocators.USER_AVATAR))
        assert WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(MainPageLocators.USER_NAME)).text == expected_user_name