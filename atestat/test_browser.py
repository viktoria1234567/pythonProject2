import time
import yaml
from browserPage import OperationHelper

with open('testdata.yaml', encoding='utf-8') as fy:
    testdata = yaml.safe_load(fy)


def test_authorize_invalid(browser):
    testpage = OperationHelper(browser)
    testpage.go_to_site()
    testpage.enter_login('test')
    testpage.enter_password('test')
    testpage.click_button_login()
    assert testpage.get_access_error() == '401'


def test_authorize_valid(browser):
    testpage = OperationHelper(browser)
    testpage.enter_login(testdata['login'])
    testpage.enter_password(testdata['password'])
    testpage.click_button_login()
    assert testpage.get_access_success() == f'Hello, {testdata["login"]}'


def test_open_page_about(browser):
    testpage = OperationHelper(browser)
    testpage.click_button_about()
    # time.sleep(3)
    assert testpage.get_header_about() == f'About Page'

def test_size_font_header_about(browser):
    testpage = OperationHelper(browser)
    assert testpage.get_size_header_about() == '32px'