#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@ Date        : 2024/11/4 下午10:54
@ Author      : Poco Ray
@ File        : login_page.py
@ Description : Web-登录页面操作封装
"""
from pages.base_page import locate_web_login


class WebLoginPage:
    @classmethod
    def login(cls, driver, email: str = None, password: str = None):
        """
        功能: 封装登录操作, 以及断言登录用户权限
        :param driver:
        :param email: 邮箱
        :param password: 密码
        :return: 进入首页
        """
        if email:
            driver.type(locate_web_login['email_input'], email)
        if password:
            driver.type(locate_web_login['password_input'], password)
        driver.click(locate_web_login['login_button'])

    @classmethod
    def check_permissions(cls, driver, department: str = "董事会"):
        """
        功能: 权限检查
        :param driver:
        :param department: 部门
        :return: None
        """
        # 基础权限-所有用户都有
        driver.assert_true(driver.is_text_visible("首页"))
        driver.assert_true(driver.is_text_visible("考勤管理"))
        driver.assert_true(driver.is_element_present("span:contains('个人考勤')"))
        driver.assert_true(driver.is_text_visible("通知管理"))
        driver.assert_true(driver.is_element_present("span:contains('通知列表')"))

        department_leader_list = ["董事会", "产品研发部", "运营部", "销售部", "人事部", "财务部"]
        # 特定权限
        if department in department_leader_list:
            driver.assert_true(driver.is_element_present("span:contains('下属考勤')"))
            driver.assert_true(driver.is_element_present("span:contains('发布通知')"))
            driver.assert_true(driver.is_text_visible("员工管理"))
            driver.assert_true(driver.is_element_present("span:contains('新增员工')"))
            if department == "董事会":
                driver.assert_true(driver.is_element_present("span:contains('员工列表')"))
            else:
                driver.assert_true(driver.is_element_present("span:contains('员工列表')"))
        else:
            # 普通员工权限
            driver.assert_false(driver.is_element_present("span:contains('下属考勤')"))
            driver.assert_false(driver.is_element_present("span:contains('发布通知')"))
            driver.assert_false(driver.is_element_present("span:contains('员工管理')"))
            driver.assert_false(driver.is_element_present("span:contains('新增员工')"))
            driver.assert_false(driver.is_element_present("span:contains('员工列表')"))
