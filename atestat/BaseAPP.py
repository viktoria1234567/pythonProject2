"""методы для работы с webdriver"""
import logging
import yaml
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

with open('testdata.yaml', encoding='utf-8') as fy:
    testdata = yaml.safe_load(fy)

class BasePage:
    """методы для работы с webdriver"""

    def __init__(self, driver):
        self.driver = driver
        self.base_url = testdata['url_base'] #'https://test-stand.gb.ru'

    def find_element(self, locator, time=10):
        """поиск элемента"""
        try:
            element = WebDriverWait(self.driver, time).until(ec.presence_of_element_located(locator),
                                                             message=f'locator not found by {locator}')

        except:
            logging.exception('find element exeption')
            element = None

        return element

    def go_to_site(self):
        """открытие сайта """
        try:
            start_browser = self.driver.get(self.base_url)
        except:
            logging.exception('open start site exeption')
            start_browser = None
        return start_browser

    def get_element_property(self, locator, property_element):
        """возвращает значение св-ва поля/элемента"""
        element = self.find_element(locator)

        if not element:
            logging.error(f'Property {property_element} not found in element {locator}')
            return None

        return element.value_of_css_property(property_element)