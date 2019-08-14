from selenium.webdriver.common.by import By

from pages.basepage import BasePage


class SearchResultPage(BasePage):

    _search_result_user_list = (By.ID, 'search_member_list')
    _edit_user = (By.CSS_SELECTOR, 'a.qui_btn.ww_btn.js_edit')
    _move_top = (By.CSS_SELECTOR, 'a.qui_btn.ww_btn.js_move_top')
    _disable = (By.CSS_SELECTOR, 'a.qui_btn.ww_btn.js_disable')
    _disable_status = (By.CSS_SELECTOR, 'span.member_display_cover_detail_forbidden.js_disable_tip')
    _edit_status = (By.ID, 'js_tips')

    def __init__(self, driver):
        BasePage.__init__(self, driver)

    @property
    def get_disable_status(self):
        self.find(self._disable_status).is_displayed()

    def disable_user(self):
        if self.get_disable_status:
            self.click(self._disable)

    def enable_user(self):
        if not self.get_disable_status:
            self.click(self._disable)

    def go_to_edit_user(self):
        self.click(self._edit_user)
        return UserEditPage(self._driver)


class UserEditPage(BasePage):

    _username = (By.ID, 'username')
    _english_name = (By.ID, 'memberEdit_english_name')
    _phone = (By.ID, 'memberEdit_phone')
    _telephone = (By.ID, 'memberEdit_telephone')
    _email = (By.ID, 'memberEdit_mail')
    _address = (By.ID, 'memberEdit_address')
    _title = (By.ID, 'memberEdit_title')

    _save = (By.XPATH, '(//a[@class="qui_btn ww_btn ww_btn_Blue js_save"])[1]')
    _cancel = (By.XPATH, '(//a[@class="qui_btn ww_btn js_cancel"])[1]')

    def __init__(self, driver):
        BasePage.__init__(self, driver)

    def edit_name(self, name):
        self.send_content(self._username, name)
        return self

    def edit_en_name(self, en_name):
        self.send_content(self._english_name, en_name)
        return self

    def edit_phone(self, phone):
        self.send_content(self._phone, phone)
        return self

    def edit_telephone(self, telephone):
        self.send_content(self._telephone, telephone)
        return self

    def edit_email(self, email):
        self.send_content(self._email, email)
        return self

    def edit_address(self, address):
        self.send_content(self._address, address)
        return self

    def edit_title(self, title):
        self.send_content(self._title, title)
        return self

    _EDIT_DICT = {
        'name': edit_name,
        'en_name': edit_en_name,
        'phone': edit_phone,
        'telephone': edit_telephone,
        'email': edit_email,
        'address': edit_address,
        'title': edit_title
    }

    def edit_user_info(self, name=None, en_name=None, phone=None,
                       telephone=None, email=None, address=None, title=None):
        # todo 是否可以优化
        """

        :param name:
        :param en_name:
        :param phone:
        :param telephone:
        :param email:
        :param address:
        :param title:
        :return:
        """
        edit_dict = {
            'name': name,
            'en_name': en_name,
            'phone': phone,
            'telephone': telephone,
            'email': email,
            'address': address,
            'title': title
        }

        for key, value in edit_dict.items():
            if value:
                self._EDIT_DICT[key](self, value)

        # if name:
        #     self.edit_name(name)
        # if en_name:
        #     self.edit_en_name(en_name)
        # if phone:
        #     self.edit_phone(phone)
        # if telephone:
        #     self.edit_telephone(telephone)
        # if email:
        #     self.edit_email(email)
        # if address:
        #     self.edit_address(address)
        # if title:
        #     self.edit_title(title)

        self.click(self._save)

        return SearchResultPage(self._driver)
