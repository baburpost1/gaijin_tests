import pytest
from selene.support.shared import browser


@pytest.fixture(scope="session")
def load_env():
    load_env()


@pytest.fixture(autouse=True)
def setup_browser():
    # Установка параметров браузера
    browser.config.window_height = 14000
    browser.config.window_width = 16000

    yield
    browser.quit()