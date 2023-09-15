from selene import browser, have
import allure


# class Page:
#
#     def open_page(self, page_name):
#         base_part_url = f'https://{page_name}.gaijin.net'
#         browser.open(base_part_url)
#         return self

class RegistrationPage():
    def __init__(self):
        self.open_page(page_name='login')

    def open_page(self, page_name):
        browser.open(f'https://{page_name}.gaijin.net/ru/profile/register')
        return self
    with allure.step('Заполнение email'):
        def fill_login(self, value):
            browser.element('[id="login"]').send_keys(value)

    with allure.step('Заполнение имени профиля'):
        def fill_nick(self, value):
            browser.element('[id="nick"]').send_keys(value)

    with allure.step('Заполнение пароля'):
        def fill_password(self, value):
            browser.element('[id="password"]').send_keys(value)

    with allure.step('Заполнение пароля повторно'):
        def fill_password_repeat(self, value):
            browser.element('[id="password-repeat"]').send_keys(value)

    with allure.step('Нажатие на кнопку подтвердить'):
        def press_accept_button(self):
            browser.element('[id="REGISTER_OK"]').click()

    with allure.step('Проверка сообщения о необходимости согласиться с правилами'):
        def assert_eula(self):
            browser.element('[id="eula_empty"]').should(
                have.text('Вы должны прочитать и согласиться с условиями пользовательского соглашения'))
