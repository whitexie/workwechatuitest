import allure
from allure import severity_level
from interface_po_test.api.contacts import Contacts
from interface_po_test.api.department import Department
from interface_po_test.common.utils import Utils


class TestContacts:
    depart = Department()
    contact = Contacts()

    @allure.feature('员工管理')
    @allure.title('创建员工成功')
    @allure.severity(severity_level.BLOCKER)
    def test_create(self):
        """
        验证输入正确的入参，创建员工成功
        :return:
        """
        user_id = Utils.build_user()
        phone_number = Utils.build_phone_number()
        assert self.contact.create(user_id, user_id, [1], mobile=phone_number)['errcode'] == 0
