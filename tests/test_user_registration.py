from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import MainPageLocators, AuthModalWindowLocators
from email_generator import generate_unique_email
from data import TestData


class TestUserRegistration:

    def test_user_can_register_successfully(self, driver):
        email = generate_unique_email()
        password = TestData.DEFAULT_PASSWORD
        expected_user_name = TestData.EXPECTED_USER_NAME

        # Шаг 1. Открыть главную страницу
        driver.get(TestData.BASE_URL)

        # Шаг 2. Нажать кнопку «Вход и регистрация»
        WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable(MainPageLocators.LOGIN_REGISTER_BUTTON)
        ).click()

        # Шаг 3. Нажать кнопку «Нет аккаунта»
        WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable(AuthModalWindowLocators.NO_ACCOUNT_BUTTON)
        ).click()

        # Шаг 4. Заполнить все поля формы регистрации
        email_input = WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(AuthModalWindowLocators.EMAIL_INPUT)
        )
        email_input.clear()
        email_input.send_keys(email)

        password_input = WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(AuthModalWindowLocators.PASSWORD_INPUT)
        )
        password_input.clear()
        password_input.send_keys(password)

        password_repeat_input = WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(AuthModalWindowLocators.PASSWORD_REPEAT_INPUT)
        )
        password_repeat_input.clear()
        password_repeat_input.send_keys(password)

        # Шаг 5. Нажать кнопку «Создать аккаунт»
        WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable(AuthModalWindowLocators.CREATE_ACCOUNT_BUTTON)
        ).click()

        # Ожидаем, что мы снова на главной и в шапке отображаются аватар и имя User
        assert WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.USER_AVATAR)
        )

        # Проверяем, что текст имени равен "User."
        assert WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.USER_NAME)
        ).text == expected_user_name

    def test_registration_with_invalid_email_shows_errors(self, driver):
        invalid_email = "haha-hoho-hehe"

        # Шаг 1. Открыть главную страницу
        driver.get(TestData.BASE_URL)

        # Шаг 2. Нажать кнопку «Вход и регистрация»
        WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable(MainPageLocators.LOGIN_REGISTER_BUTTON)
        ).click()

        # Шаг 3. Нажать кнопку «Нет аккаунта»
        WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable(AuthModalWindowLocators.NO_ACCOUNT_BUTTON)
        ).click()

        # Шаг 4. Заполнить поле Email некорректным значением
        email_input = WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(AuthModalWindowLocators.EMAIL_INPUT)
        )
        email_input.clear()
        email_input.send_keys(invalid_email)

        # Шаг 5. Нажать кнопку «Создать аккаунт»
        WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable(AuthModalWindowLocators.CREATE_ACCOUNT_BUTTON)
        ).click()

        # Проверка 1: под полем Email отображается сообщение «Ошибка»
        assert WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(AuthModalWindowLocators.EMAIL_ERROR_MESSAGE)
        ).text == "Ошибка"

        # Проверка 2: поле Email выделено красным
        assert WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(AuthModalWindowLocators.EMAIL_INPUT_ERROR)
        )

        # Проверка 3: поле «Пароль» выделено красным
        assert WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(AuthModalWindowLocators.PASSWORD_INPUT_ERROR)
        )

        # Проверка 4: поле «Повторите пароль» выделено красным
        assert WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(AuthModalWindowLocators.PASSWORD_REPEAT_INPUT_ERROR)
        )

    def test_registration_existing_user_shows_errors(self, driver):
        email = TestData.EXISTING_USER_EMAIL
        password = TestData.EXISTING_USER_PASSWORD

        # Шаг 1. Открыть главную страницу
        driver.get(TestData.BASE_URL)

        # Шаг 2. Нажать кнопку «Вход и регистрация»
        WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable(MainPageLocators.LOGIN_REGISTER_BUTTON)
        ).click()

        # Шаг 3. Нажать кнопку «Нет аккаунта»
        WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable(AuthModalWindowLocators.NO_ACCOUNT_BUTTON)
        ).click()

        # Шаг 4. Заполнить поле Email данными уже существующего пользователя
        email_input = WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(AuthModalWindowLocators.EMAIL_INPUT)
        )
        email_input.clear()
        email_input.send_keys(email)

        # Шаг 5. Заполнить поле «Пароль» данными уже существующего пользователя
        password_input = WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(AuthModalWindowLocators.PASSWORD_INPUT)
        )
        password_input.clear()
        password_input.send_keys(password)

        # Шаг 6. Заполнить поле «Повторите пароль» тем же паролем
        password_repeat_input = WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(AuthModalWindowLocators.PASSWORD_REPEAT_INPUT)
        )
        password_repeat_input.clear()
        password_repeat_input.send_keys(password)

        # Шаг 7. Нажать кнопку «Создать аккаунт»
        WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable(AuthModalWindowLocators.CREATE_ACCOUNT_BUTTON)
        ).click()

        # Проверка 1: под полем Email отображается сообщение «Ошибка»
        assert WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(AuthModalWindowLocators.EMAIL_ERROR_MESSAGE)
        ).text == "Ошибка"

        # Проверка 2: поле Email выделено красным
        assert WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(AuthModalWindowLocators.EMAIL_INPUT_ERROR)
        )

        # Проверка 3: поле «Пароль» выделено красным
        assert WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(AuthModalWindowLocators.PASSWORD_INPUT_ERROR)
        )

        # Проверка 4: поле «Повторите пароль» выделено красным
        assert WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(AuthModalWindowLocators.PASSWORD_REPEAT_INPUT_ERROR))
            