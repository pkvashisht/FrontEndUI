import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="class")
def setup(request):
    service_obj = Service("/Users/OEM/PycharmProjects/chromedriver.exe")
    driver = webdriver.Chrome(service=service_obj)
    driver.get("https://jupiter.cloud.planittesting.com/#/")
    driver.implicitly_wait(10)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()

