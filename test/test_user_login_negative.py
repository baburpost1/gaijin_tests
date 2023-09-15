from selene import browser, support
from pages.registration_page import RegistrationPage

def test_login_user_negaive(setup_browser):
    registration_page = RegistrationPage()
    registration_page.fill_login(value='test@test.com')
    registration_page.fill_nick('BaburTest')
    registration_page.fill_password('123456')
    registration_page.fill_password_repeat('123456')
    registration_page.press_accept_button()
    registration_page.assert_eula()


