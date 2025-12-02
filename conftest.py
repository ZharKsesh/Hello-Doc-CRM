import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

#Пишу фикстуру, которая будет инициализировать драйвер для наших тестов
@pytest.fixture(scope="function",autouse=True)
def driver(request):
    options = Options()
    #options.add_argument("--headless") #нам нужен "безголовый режим" если мы хотим запускать тесты в CI, Докере и т.д.
    options.add_argument("--no-sandbox") #что это не песочница, а реальный проект
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Firefox(options=options)
    request.cls.driver = driver #создает объект Драйвер внутри тестовых классов
    yield driver
    driver.quit()
