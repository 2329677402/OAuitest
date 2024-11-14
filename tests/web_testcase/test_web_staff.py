#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@ Date        : 2024/11/12 下午9:43
@ Author      : Poco Ray
@ File        : test_web_staff.py
@ Description : Web-员工管理测试用例
"""
import allure
import pytest
from pages.web_page.staff_page import WebStaffPage
from tests.test_base_case import BaseTestCase


@allure.feature("员工管理")
@pytest.mark.web
@pytest.mark.staff
class TestStaff(BaseTestCase):
    @allure.story("新增员工")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title("新增员工页面和功能正常")
    @pytest.mark.smoke
    @pytest.mark.run(order=22)
    def test_web_add_staff(self):
        self.login()
        self.click("span:contains('员工管理')")
        self.click("span:contains('新增员工')")
        add_staff_label = ["姓名", "邮箱", "密码", "部门", "领导"]
        for label in add_staff_label:
            self.assert_text(label, f"label:contains('{label}')")

    @allure.story("员工列表")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title("员工列表页面和功能正常")
    @pytest.mark.smoke
    @pytest.mark.run(order=23)
    def test_web_staff_list(self):
        self.login()
        self.click("span:contains('员工管理')")
        self.click("span:contains('员工列表')")
        staff_list_label = ["序号", "姓名", "邮箱", "入职时间", "所属部门", "状态", "操作"]
        for label in staff_list_label:
            self.assert_text(label, f"div:contains('{label}')")
        WebStaffPage.staff_list_query(self, "董事会", "东东")
        department_elements = self.find_elements("td:contains('董事会')")
        for element in department_elements:
            self.assert_equal("董事会", element.text)