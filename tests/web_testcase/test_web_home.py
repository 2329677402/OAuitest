#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@ Date        : 2024/11/7 上午12:06
@ Author      : Poco Ray
@ File        : test_web_home.py
@ Description : Web-首页测试用例
"""
import allure
import pytest
from pages.base_page import locate_web_home
from tests.test_base_case import BaseTestCase


@allure.feature("首页模块")
@pytest.mark.web
@pytest.mark.home
class TestHome(BaseTestCase):
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title("首页数据展示正确")
    @pytest.mark.smoke
    @pytest.mark.run(order=8)
    def test_web_home(self):
        self.login()
        self.assert_element(locate_web_home['staff_chart'])
        self.assert_exact_text('部门员工统计', locate_web_home['staff_title'])
        self.assert_element(locate_web_home['inform_card'])
        self.assert_exact_text('最新通知', locate_web_home['inform_title'])
        self.assert_element(locate_web_home['absent_card'])
        self.assert_exact_text('最新请假', locate_web_home['absent_title'])
