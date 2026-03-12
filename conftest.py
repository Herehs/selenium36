import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: ru, en, fr, es, etc...")


@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    if user_language is None:
        raise pytest.UsageError("--language should be set (e.g. --language=es)")

    options = Options()
    options.set_preference("intl.accept_languages", user_language)

    service = Service(GeckoDriverManager().install())
    browser = webdriver.Firefox(service=service, options=options)

    yield browser
    browser.quit()