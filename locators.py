from selenium.webdriver.common.by import By

class MainPageLocators:
    LOGIN_REGISTER_BUTTON = (By.XPATH, '//button[contains(normalize-space(), "Вход и регистрация")]')
    PLACE_AD_BUTTON = (By.XPATH, '//*[self::button or self::a][contains(normalize-space(), "Разместить объявление")]')
    USER_AVATAR = (By.XPATH, '//button[contains(@class, "circleSmall")]')
    USER_NAME = (By.XPATH, '//h3[contains(@class, "profileText") and contains(@class, "name")]')
    LOGOUT_BUTTON = (By.XPATH, '//button[contains(normalize-space(), "Выйти")]')
    AD_CARD = (By.XPATH, '//div[contains(@class,"homePage")]//div[@class="card"][1]')

class AuthModalWindowLocators:
    # Кнопка/ссылка «Нет аккаунта»
    NO_ACCOUNT_BUTTON = (By.XPATH, '//*[self::button or self::a][contains(normalize-space(), "Нет аккаунта")]')

    # Кнопка «Создать аккаунт»
    CREATE_ACCOUNT_BUTTON = (By.XPATH, '//button[contains(normalize-space(), "Создать аккаунт")]')

    # Кнопка «Войти» (для логина)
    LOGIN_SUBMIT_BUTTON = (By.XPATH, '//button[normalize-space()="Войти"]')

    # Поля формы
    EMAIL_INPUT = (By.XPATH, '//input[@type="email" or @name="email"]')
    PASSWORD_INPUT = (By.XPATH, '(//input[@type="password"])[1]')
    PASSWORD_REPEAT_INPUT = (By.XPATH, '(//input[@type="password"])[2]')

    # Сообщение «Ошибка» под полем Email
    EMAIL_ERROR_MESSAGE = (By.XPATH, '//*[text()="Ошибка" and ancestor::*[.//input[@type="email" or @name="email"]]]')

    # Поля, подсвеченные как ошибочные (красная рамка / класс ошибки)
    EMAIL_INPUT_ERROR = (By.XPATH, '//input[@name="email"]/parent::div[contains(@class,"input_inputError")]')
    PASSWORD_INPUT_ERROR = (By.XPATH, '//input[@name="password"]/parent::div[contains(@class,"input_inputError")]')
    PASSWORD_REPEAT_INPUT_ERROR = (By.XPATH, '//input[@name="submitPassword"]/parent::div[contains(@class,"input_inputError")]')

class CreateAdLocators:
    AUTH_REQUIRED_TITLE = (By.XPATH, '//h1[normalize-space()="Чтобы разместить объявление, авторизуйтесь"]')
    TITLE_INPUT = (By.XPATH, '//input[@name="name" and @placeholder="Название"]')
    DESCRIPTION_INPUT = (By.XPATH, '//textarea[@name="description" and @placeholder="Описание товара"]')
    PRICE_INPUT = (By.XPATH, '//input[@name="price" and @placeholder="Стоимость"]')

    CATEGORY_DROPDOWN = (By.XPATH, '//input[@name="category"]/following-sibling::button[contains(@class,"dropDownMenu_arrowDown")]')
    CATEGORY_BOOKS_OPTION = (By.XPATH, '//div[contains(@class,"dropDownMenu_options")]//button[.//span[normalize-space()="Книги"]]')

    CITY_DROPDOWN = (By.XPATH, '//input[@name="city"]/following-sibling::button[contains(@class,"dropDownMenu_arrowDown")]')
    CITY_SPB_OPTION = (By.XPATH, '//div[contains(@class,"dropDownMenu_options")]//button[.//span[normalize-space()="Санкт-Петербург"]]')

    # Радио «Новый» для состояния товара
    CONDITION_NEW_RADIO = (By.XPATH, '//*[self::label or self::span][normalize-space()="Новый"]')

    # Кнопка «Опубликовать»
    PUBLISH_BUTTON = (By.XPATH, '//button[contains(normalize-space(),"Опубликовать")]')
    
class ProfileLocators:
    PROFILE_BUTTON = (By.XPATH, '//button[contains(@class, "circleSmall")]')
    MY_AD = (By.XPATH, '//div[contains(@class, "profilePage")]//div[contains(@class, "card")]//img[contains(@class, "picture")]')
