from selenium.webdriver.common.by import By
from pages.basepage import BasePage
from pages import contact_page


class UserAddPage(BasePage):
    _username = (By.NAME, 'username')
    _account_id = (By.ID, 'memberAdd_acctid')
    _email = (By.ID, 'memberAdd_mail')
    _save_btn = (By.CSS_SELECTOR, 'a.qui_btn.ww_btn.js_btn_save')

    def add_user(self, name, account, email):
        self.send_content(self._username, name)
        self.send_content(self._account_id, account)
        self.send_content(self._email, email)
        self.click(self._save_btn)
        return contact_page.ContactPage(self._driver)
