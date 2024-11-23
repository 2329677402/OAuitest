#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@ Date        : 2024/11/18 下午10:42
@ Author      : Poco Ray
@ File        : test_business.py
@ Description : 功能描述
"""
import allure
import pytest

from tests.test_base_case import BaseTestCase
from tests.web_testcase.test_web_absent import TestAbsent
from tests.web_testcase.test_web_inform import TestInform
from tests.web_testcase.test_web_staff import TestStaff


class TestBusiness(BaseTestCase):
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("业务场景测试")
    @pytest.mark.smoke
    @pytest.mark.run(order=30)
    def test_business(self):
        """
        功能: 业务场景测试
        :return:
        """
        self.login()
        TestAbsent().test_web_myabsent()
        TestAbsent().test_web_subabsent()
        TestInform().test_web_publish_inform()
        TestStaff().test_web_staff_list_query_department()

