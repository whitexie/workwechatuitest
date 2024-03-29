from selenium.webdriver.common.by import By
from selenium_project.pages import BasePage
from selenium_project.pages.search_result_page import SearchResultPage
from selenium_project.pages import UserAddPage


class ContactPage(BasePage):

    _add_user = (By.XPATH, '(//a[@class="qui_btn ww_btn js_add_member"])[2]')
    _search_user = (By.ID, 'memberSearchInput')
    _save_status = (By.ID, 'js_tips')

    def go_to_add_user(self):
        self.click(self._add_user, by_js=True)
        return UserAddPage(self._driver)

    def search_user_by_name(self, name):
        self.send_content(self._search_user, name)
        return SearchResultPage(self._driver)

    @property
    def save_status(self):
        return self.find(self._save_status).is_displayed()
