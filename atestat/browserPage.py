"""класс для работы со страницей"""
import logging

import yaml
from selenium.webdriver.common.by import By

from BaseAPP import BasePage


class TestSearchLocators:
    ids = dict()
    with open('locators.yaml', encoding='utf-8') as fy:
        locators = yaml.safe_load(fy)

        for item in locators['css'].keys():
            ids[item] = (By.CSS_SELECTOR, locators['css'][item])

        for item in locators['xpath'].keys():
            ids[item] = (By.XPATH, locators['xpath'][item])


class OperationHelper(BasePage):
    """методы для работы с элементами вэб-страницы"""

    def enter_text_into_field(self, locator, text, description=None):
        """общий метод для ввода текста в поле по заданному локатору"""
        name_element = locator if description is None else description
        logging.debug(f'send work {text} in element {name_element}')
        field = self.find_element(locator)
        if not field:
            logging.error(f'element "{name_element}" with locator: "{locator}" - not found')
            return False
        try:
            field.clear()
            field.send_keys(text)
            return True
        except:
            logging.exception(f'exception with work locator {locator}')
            return False

        return True

    def enter_login(self, login):
        """ввод текста в поле логин"""
        self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_FIELD_LOGIN'], login,
                                   description='UserName')

    def enter_password(self, password):
        """ввод текста в поле пароля"""
        self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_FIELD_PASS'], password,
                                   description='password')

    def click_button(self, locator, time=10, description=None):
        """общий метод для нажатие на кнопку по локатору"""
        name_element = locator if description is None else description
        logging.debug(f'send work in button {name_element}')
        button = self.find_element(locator)
        if not button:
            logging.error(f'not find button "{name_element}')
            return False
        else:
            try:
                button.click()
            except:
                logging.exception(f'exception with click button {name_element}')
                return False
        logging.debug(f'clicked button "{name_element}"')
        return True

    def click_button_login(self):
        """нажатие на кнопку LOGIN"""
        self.click_button(TestSearchLocators.ids['LOCATOR_BUTTON_LOGIN'], description='LOGIN')

    def click_button_about(self):
        """нажатие на кнопку About"""
        self.click_button(TestSearchLocators.ids['LOCATOR_BUTTON_ABOUT'], description='ABOUT')

    def get_text(self, locator, time=10, description=None):
        """получение текста поля"""
        name_element = locator if description is None else description
        logging.debug(f'send text in field {name_element}')
        field = self.find_element(locator, time)
        if not field:
            logging.error(f'error sent field {name_element}')
            return None
        else:
            try:
                text_field = field.text
            except:
                logging.exception(f'exception send text in field {name_element}')
                return None
        return text_field

    def get_access_success(self):
        """получение текста при успешной авторизации"""
        return self.get_text(TestSearchLocators.ids['LOCATOR_ACCESS_SUCCESS'], description='success login')

    def get_access_error(self):
        """получение сообщения об ошибке в доступе"""
        return self.get_text(TestSearchLocators.ids['LOCATOR_ACCESS_ERROR'], description='error login')

    def get_header_about(self):
        """получение заголовка страницы About"""
        return self.get_text(TestSearchLocators.ids['LOCATOR_HEADER_ABOUT'], description='error login')

    def get_size_header_about(self):
        """получение размера заголовка страницы About"""
        return self.get_element_property(TestSearchLocators.ids['LOCATOR_HEADER_ABOUT'], 'font-size')