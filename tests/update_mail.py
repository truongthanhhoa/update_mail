from pages.login_page.login_pages_mail_server import LoginPage
from utilities.start_browser import start_browser
from utilities.read_data import get_excel_data
from ddt import ddt, data, unpack
from utilities.read_data import get_csv_data
import pandas as pd
from pandas import ExcelFile
from pandas import ExcelWriter
import time
import unittest
import pytest


@pytest.mark.usefixtures("start_browser")
@ddt
class NewCalendar(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self, start_browser):
        self.driver = start_browser
        self.login = LoginPage(start_browser)

    @data(*get_csv_data("C:/Users/hoa.truongthanh/PycharmProjects/google_calendar/test_data.csv"))
    @unpack
    def test_update_mail(self, username, password):
        # Input credential
        self.login.enter_email(username)
        self.login.enter_password(password)
        self.login.click_on_login_button()
        self.driver.implicitly_wait(5)

        # get execl data
        exel_data = get_excel_data("C:/Users/hoa.truongthanh/PycharmProjects/google_calendar/progros-forwarding.xlsx")

        # # update email
        for i in exel_data:
            self.login.select_email_account()
            try:
                self.login.click_on_clear_icon()
            except Exception as e:
                print(e)
            self.login.input_search_key(i[0])
            time.sleep(2)
            self.login.select_search_result(i[0])
            time.sleep(2)
            self.driver.execute_script("window.scrollBy(0, -1000);")    # scroll page down
            self.login.select_copy_option()
            self.login.input_recipient(i[1])
            self.login.click_submit()
            self.login.is_recipient_added(i[1])

            # remove recipient
            # self.login.remove_recipient(key, value)


