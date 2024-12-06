import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

driver = None
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )

@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        service_obj = Service("/Users/OEM/PycharmProjects/chromedriver.exe")
        driver = webdriver.Chrome(service=service_obj)

    elif browser_name == "firefox":
        service_obj = Service("/Users/OEM/PycharmProjects/geckodriver.exe")
        driver = webdriver.Firefox(service=service_obj)


    driver.get("https://jupiter.cloud.planittesting.com/#/")
    driver.maximize_window()
    driver.implicitly_wait(5)
    request.cls.driver = driver
    yield
    driver.close()

