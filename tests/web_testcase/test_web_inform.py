#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@ Date        : 2024/11/12 下午9:42
@ Author      : Poco Ray
@ File        : test_web_inform.py
@ Description : Web-通知管理测试用例
"""
import allure
import pytest
from pages.web_page.inform_page import WebInformPage
from tests.test_base_case import BaseTestCase


@allure.feature("通知管理")
@pytest.mark.web
@pytest.mark.inform
class TestInform(BaseTestCase):
    @allure.story("发布通知")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title("发布通知页面和功能正常")
    @pytest.mark.smoke
    @pytest.mark.run(order=16)
    def test_web_publish_inform(self):
        self.login()
        self.click("span:contains('通知管理')")
        self.click("span:contains('发布通知')")
        publish_inform_label = ["通知标题", "通知部门"]
        for label in publish_inform_label:
            self.assert_text(label, f"label:contains('{label}')")
        self.assert_text("通知内容", "div:contains('通知内容')")
        WebInformPage.publish_inform_form(self, "通知测试", ["董事会", "财务部"], "通知内容")
        self.sleep(1)
        self.assert_true(self.is_element_visible("p:contains('发布成功')"))

    @allure.story("发布通知")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("发布通知失败(通知标题为空)")
    @pytest.mark.run(order=17)
    def test_web_publish_inform_fail01(self):
        self.login()
        self.click("span:contains('通知管理')")
        self.click("span:contains('发布通知')")
        WebInformPage.publish_inform_form(self, "", ["董事会", "财务部"], "通知内容")
        self.assert_text("请输入通知标题", "div:contains('请输入通知标题')")

    @allure.story("发布通知")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("发布通知失败(通知部门为空)")
    @pytest.mark.run(order=18)
    def test_web_publish_inform_fail02(self):
        self.login()
        self.click("span:contains('通知管理')")
        self.click("span:contains('发布通知')")
        WebInformPage.publish_inform_form(self, "测试", [], "通知内容")
        self.assert_text("请选择通知部门", "div:contains('请选择通知部门')")

    @allure.story("发布通知")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("发布通知失败(通知内容为空)")
    @pytest.mark.xfail(reason="Bug: 通知内容为空时, 仍然可以发布通知")
    @pytest.mark.run(order=19)
    def test_web_publish_inform_fail03(self):
        self.login()
        self.click("span:contains('通知管理')")
        self.click("span:contains('发布通知')")
        WebInformPage.publish_inform_form(self, "测试", ["董事会", "财务部"], "")
        self.assert_text("请输入通知内容", "div:contains('请输入通知内容')")

    @allure.story("发布通知")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("发布通知失败(全部为空)")
    @pytest.mark.xfail(reason="Bug: 通知内容为空时, 提交不会提示")
    @pytest.mark.run(order=20)
    def test_web_publish_inform_fail04(self):
        self.login()
        self.click("span:contains('通知管理')")
        self.click("span:contains('发布通知')")
        WebInformPage.publish_inform_form(self, "", [], "")
        self.assert_text("请输入通知标题", "div:contains('请输入通知标题')")
        self.assert_text("请选择通知部门", "div:contains('请选择通知部门')")
        self.assert_text("请输入通知内容", "div:contains('请输入通知内容')")

    @allure.story("通知列表")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title("通知列表页面和功能正常")
    @pytest.mark.smoke
    @pytest.mark.run(order=21)
    def test_web_inform_list(self):
        self.login()
        self.click("span:contains('通知管理')")
        self.click("span:contains('通知列表')")
        inform_list_label = ["通知标题", "发布者", "发布时间", "通知部门", "操作"]
        for label in inform_list_label:
            self.assert_text(label, f"div:contains('{label}')")
