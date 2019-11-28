from selenium.webdriver.common.by import By
import time

class LoginPage():

    def __init__(self, driver):
        self.driver = driver

    # Locators

    _email_or_phone = "//input[@type='email']"
    _passw = "//input[@type='password']"
    _login_button = "//button[contains(text(), 'login')]"
    _email_account = "//div[@class='container-fluid']//div[@class='row']//a[contains(text(),'Email accounts')]"
    _search = "//input[@id='search']"
    _search_result = "//div[@id='result']//tr[1]/th"
    _copy_option = "//a[contains(text(),' incoming emails to other email(s)')]"
    _add_recipient = "//form[@name='copy_filter']//div[@class='form-group']//input"
    _add_other_recipient = "//button[@id='add-another-email']"
    _submit_button = "//button[@type='submit']"
    _active_filter = "//td[contains(text(),'Send copy of incoming emails to')]"
    _clear_icon = "//span[@id='clear-icon']/i"
    _remove_filter = "//td[contains(text(),'Send copy of incoming emails to')]//a[2]"

    def get_username(self):
        return self.driver.find_element(By.XPATH, self._email_or_phone)

    def get_password_field(self):
        return self.driver.find_element(By.XPATH, self._passw)

    def get_login_button(self):
        return self.driver.find_element(By.XPATH, self._login_button)

    def get_email_account_tab(self):
        return self.driver.find_element(By.XPATH, self._email_account)

    def get_search_bar(self):
        return self.driver.find_element(By.XPATH, self._search)

    def get_search_result(self):
        return self.driver.find_element(By.XPATH, self._search_result)

    def get_copy_option(self):
        return self.driver.find_element(By.XPATH, self._copy_option)

    def get_add_recipient(self):
        return self.driver.find_elements(By.XPATH, self._add_recipient)

    def get_add_other_recipient(self):
        return self.driver.find_element(By.XPATH, self._add_other_recipient)

    def get_submit_button(self):
        return self.driver.find_element(By.XPATH, self._submit_button)

    def get_active_filter(self):
        return self.driver.find_element(By.XPATH, self._active_filter)

    def get_clear_icon(self):
        return self.driver.find_element(By.XPATH, self._clear_icon)

    def get_remove_filter(self):
        return self.driver.find_element(By.XPATH, self._remove_filter)

    def click_on_add_recipient(self):
        self.get_add_other_recipient().click()

    def click_on_remove_filter(self):
        try:
            self.get_remove_filter().click()
            confirm = self.driver.switch_to.alert
            confirm.accept()
        except Exception as e:
            print(e)

    def click_on_clear_icon(self):
        self.get_clear_icon().click()

    def click_on_login_button(self):
        self.get_login_button().click()

    def enter_email(self, email):
        self.get_username().send_keys(email)

    def enter_password(self, password):
        self.get_password_field().send_keys(password)

    def select_email_account(self):
        self.get_email_account_tab().click()

    def input_search_key(self, email1):
        self.get_search_bar().send_keys(email1)

    def select_search_result(self, email1):
        try:
            print(self.get_search_result().text)
            if self.get_search_result().text == email1:
                self.get_search_result().click()
        except Exception as e:
            print(e)

    def select_copy_option(self):
        self.get_copy_option().click()

    def input_recipient(self, email2):
        recipient_list = []
        for i in self.get_add_recipient():
            recipient_list.append(i.get_attribute("value"))
        try:
            if recipient_list == ['']:
                i.send_keys(email2)
            else:
                if email2 in recipient_list:
                    print("{} already added".format(email2))
                else:
                    self.click_on_add_recipient()
                    for i in self.get_add_recipient():
                        if not i.get_attribute("value"):
                            i.send_keys(email2)
                            break
        except Exception as e:
            print(e)

    def click_submit(self):
        self.get_submit_button().click()

    def is_recipient_added(self, email2):
        try:
            if email2 in self.get_active_filter().text:
                print("{} has been added".format(email2))
                return True
        except Exception as e:
            print(e)
            return False

    def remove_recipient(self, email1, email2):
        self.select_email_account()
        try:
            self.click_on_clear_icon()
        except Exception as e:
            print(e)
        self.input_search_key(email1)
        time.sleep(2)
        self.select_search_result(email1)
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0, -1000);")  # scroll page down
        self.click_on_remove_filter()
        try:
            if not self.is_recipient_added(email2):
                print("{} has been deleted".format(email2))
        except Exception as e:
            print(e)





