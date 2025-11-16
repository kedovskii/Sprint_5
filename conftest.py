import pytest
from selenium import webdriver

BASE_URL = "https://qa-desk.stand.praktikum-services.ru/"


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def base_url():
    return BASE_URL


@pytest.fixture
def existing_user_credentials():
    return {"email": "existing_user@praktikum.ru", "password": "Qwerty123!"}
        
                  
    