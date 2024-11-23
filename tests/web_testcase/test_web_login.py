#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@ Date        : 2024/11/5 上午12:55
@ Author      : Poco Ray
@ File        : test_web_login.py
@ Description : Web-登录测试用例
"""
import allure
import pytest
from tests.test_base_case import BaseTestCase
from pages.base_page import locate_web_home, locate_web_login


@allure.feature("登录模块")
@pytest.mark.web
@pytest.mark.login
class TestWebLogin(BaseTestCase):
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title("登录成功(邮箱存在+密码正确)")
    @pytest.mark.smoke
    @pytest.mark.run(order=1)
    def test_web_login_success(self):
        self.login(email="dongdong@qq.com", password="111111")
        self.assert_element(locate_web_home['sidebar'])  # 首页侧边栏
        self.check_permissions()

    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("登录失败(邮箱存在+密码错误)")
    @pytest.mark.run(order=2)
    def test_web_login_fail01(self):
        self.login(email="dongdong@qq.com", password="1234567")
        self.assert_text("请输入正确的密码", locate_web_login['error_message'])

    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("登录失败(邮箱不存在+密码任意)")
    @pytest.mark.run(order=3)
    def test_web_login_fail02(self):
        self.login(email="dong@qq.com", password="123")
        self.assert_text("请输入正确的邮箱", locate_web_login['error_message'])

    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("登录失败(邮箱不合法+密码任意)")
    @pytest.mark.run(order=4)
    def test_web_login_fail03(self):
        self.login(email="dongdong@qqcom", password="111111")
        self.assert_text("邮箱格式错误", locate_web_login['error_message'])

    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("登录失败(邮箱为空+密码任意)")
    @pytest.mark.run(order=5)
    def test_web_login_fail04(self):
        self.login(email="", password="111111")
        self.assert_text("邮箱格式错误", locate_web_login['error_message'])

    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("登录失败(邮箱存在+密码不合法)")
    @pytest.mark.run(order=6)
    def test_web_login_fail05(self):
        self.login(email="dongdong@qq.com", password="111")
        self.assert_text("密码格式错误", locate_web_login['error_message'])

    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("登录失败(邮箱存在+密码为空)")
    @pytest.mark.run(order=7)
    def test_web_login_fail06(self):
        self.login(email="dongdong@qq.com", password="")
        self.assert_text("密码格式错误", locate_web_login['error_message'])
