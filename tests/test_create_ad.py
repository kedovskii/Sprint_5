import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from email_generator import generate_unique_email
from locators import MainPageLocators, CreateAdLocators, AuthModalWindowLocators, ProfileLocators

class TestCreateAd:

    def test_unauthorized_user_sees_auth_modal(self, driver, base_url):
        # Шаг 1. Открыть главную страницу
        driver.get(base_url)

        # Шаг 2. Нажать кнопку «Разместить объявление»
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(MainPageLocators.PLACE_AD_BUTTON)).click()

        # Шаг 3. Проверка: отображается модальное окно с заголовком «Чтобы разместить объявление, авторизуйтесь»
        assert WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(CreateAdLocators.AUTH_REQUIRED_TITLE)).text == "Чтобы разместить объявление, авторизуйтесь"

    def test_authorized_user_can_create_ad(self, driver, base_url):
        email = generate_unique_email()
        password = "Qwerty123!"

        unique_suffix = int(time.time())
        title = f"Тестовое объявление {unique_suffix}"
        description = "Описание тестового товара"
        price = "1234"

        # Шаг 1. Открыть главную страницу
        driver.get(base_url)

        # Шаг 2. Нажать кнопку «Вход и регистрация»
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(MainPageLocators.LOGIN_REGISTER_BUTTON)).click()

        # Шаг 3. Нажать кнопку «Нет аккаунта»
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(AuthModalWindowLocators.NO_ACCOUNT_BUTTON)).click()

        # Шаг 4. Заполнить поле Email новым адресом
        email_input = WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(AuthModalWindowLocators.EMAIL_INPUT))
        email_input.clear()
        email_input.send_keys(email)

        # Шаг 5. Заполнить поле «Пароль»
        password_input = WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(AuthModalWindowLocators.PASSWORD_INPUT))
        password_input.clear()
        password_input.send_keys(password)

        # Шаг 6. Заполнить поле «Повторите пароль»
        password_repeat_input = WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(AuthModalWindowLocators.PASSWORD_REPEAT_INPUT))
        password_repeat_input.clear()
        password_repeat_input.send_keys(password)

        # Шаг 7. Нажать кнопку «Создать аккаунт»
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(AuthModalWindowLocators.CREATE_ACCOUNT_BUTTON)).click()

        # Шаг 8. Дождаться, что пользователь авторизован (есть аватар)
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(MainPageLocators.USER_AVATAR))

        # Шаг 9. Нажать кнопку «Разместить объявление»
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(MainPageLocators.PLACE_AD_BUTTON)).click()

        # Шаг 10. Заполнить поле «Название»
        title_input = WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(CreateAdLocators.TITLE_INPUT))
        title_input.clear()
        title_input.send_keys(title)

        # Шаг 11. Заполнить поле «Описание товара»
        description_input = WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(CreateAdLocators.DESCRIPTION_INPUT))
        description_input.clear()
        description_input.send_keys(description)

        # Шаг 12. Заполнить поле «Стоимость»
        price_input = WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(CreateAdLocators.PRICE_INPUT))
        price_input.clear()
        price_input.send_keys(price)

        # Шаг 13. Выбрать категорию «Книги»
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(CreateAdLocators.CATEGORY_DROPDOWN)).click()
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(CreateAdLocators.CATEGORY_BOOKS_OPTION)).click()

        # Шаг 14. Выбрать город «Санкт-Петербург»
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(CreateAdLocators.CITY_DROPDOWN)).click()
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(CreateAdLocators.CITY_SPB_OPTION)).click()

        # Шаг 15. Выбрать RadioButton «Новый»
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(CreateAdLocators.CONDITION_NEW_RADIO)).click()

        # Шаг 16. Нажать кнопку «Опубликовать»
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(CreateAdLocators.PUBLISH_BUTTON)).click()

        # Шаг 17. Перейти в профиль пользователя по URL
        # Я так и не смог найти Xpath для перехода в профиль по нажатию на элемент, поэтому перехожу напрямую по URL
        expected_profile_url = base_url + "profile"
        driver.get(expected_profile_url)

        # Шаг 18. Проверить, что URL страницы профиля корректный
        WebDriverWait(driver, 5).until(expected_conditions.url_to_be(expected_profile_url))
        assert driver.current_url == expected_profile_url

        # Шаг 19. Проверка: в «Мои объявления» есть объявление с нашим уникальным заголовком
        my_ads = WebDriverWait(driver, 5).until(expected_conditions.visibility_of_all_elements_located(ProfileLocators.MY_AD))
        alt_values = [picture.get_attribute("alt") for picture in my_ads]
        assert title in alt_values