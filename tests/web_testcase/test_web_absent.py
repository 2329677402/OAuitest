#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@ Date        : 2024/11/12 下午9:41
@ Author      : Poco Ray
@ File        : test_web_absent.py
@ Description : Web-考勤管理测试用例
"""
import allure
import pytest
from pages.base_page import locate_web_common
from pages.web_page.absent_page import WebAbsentPage
from tests.test_base_case import BaseTestCase


@allure.feature("考勤管理")
@pytest.mark.web
@pytest.mark.absent
class TestAbsent(BaseTestCase):
    @allure.story("个人考勤")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title("个人考勤页面和功能正常")
    @pytest.mark.smoke
    @pytest.mark.run(order=9)
    def test_web_myabsent(self):
        self.login()
        self.click(locate_web_common["absent_model"])
        self.click(locate_web_common["myabsent_model"])
        self.assert_true(self.is_text_visible("发起考勤"))
        self.click("span:contains('发起考勤')")
        absent_form_label = ["标题", "请假类型", "审批人", "请假理由"]
        for label in absent_form_label:
            self.assert_text(label, f"label:contains('{label}')")
        self.assert_text("请假时间", "div:contains('请假时间')")
        WebAbsentPage.absent_form(self, "请假测试", "年假", ["2024-11-01", "2024-11-07"], "测试")
        self.sleep(1)
        # 默认模式下的自动化测试, 由于页面刷新速度较快, 可能会导致断言失败, 因此需要加入等待时间
        self.assert_text("发起成功", "p:contains('发起成功')")
        my_absent_label = ["标题", "类型", "原因", "发起时间", "开始日期", "结束日期", "审批人", "反馈意见", "审核状态"]
        for label in my_absent_label:
            self.assert_text(label, f"div:contains('{label}')")

    @allure.story("个人考勤")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("考勤发起失败(标题为空)")
    @pytest.mark.run(order=10)
    def test_web_myabsent_fail01(self):
        self.login()
        self.click("span:contains('考勤管理')")
        self.click("span:contains('个人考勤')")
        self.click("span:contains('发起考勤')")
        WebAbsentPage.absent_form(self, "", "年假", ["2024-11-01", "2024-11-07"], "测试")
        self.assert_text("请输入标题！", "div:contains('请输入标题')")

    @allure.story("个人考勤")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("考勤发起失败(请假类型为空)")
    @pytest.mark.run(order=11)
    def test_web_myabsent_fail02(self):
        self.login()
        self.click("span:contains('考勤管理')")
        self.click("span:contains('个人考勤')")
        self.click("span:contains('发起考勤')")
        WebAbsentPage.absent_form(self, "失败测试", "", ["2024-11-01", "2024-11-07"], "测试")
        self.assert_text("请选择请假类型！", "div:contains('请选择请假类型')")

    @allure.story("个人考勤")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("考勤发起失败(请假时间为空)")
    @pytest.mark.run(order=12)
    def test_web_myabsent_fail03(self):
        self.login()
        self.click("span:contains('考勤管理')")
        self.click("span:contains('个人考勤')")
        self.click("span:contains('发起考勤')")
        WebAbsentPage.absent_form(self, "失败测试", "事假", [], "测试")
        self.assert_text("请选择请假时间！", "div:contains('请选择请假时间')")

    @allure.story("个人考勤")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("考勤发起失败(请假理由为空)")
    @pytest.mark.run(order=13)
    def test_web_myabsent_fail04(self):
        self.login()
        self.click("span:contains('考勤管理')")
        self.click("span:contains('个人考勤')")
        self.click("span:contains('发起考勤')")
        WebAbsentPage.absent_form(self, "失败测试", "事假", ["2024-11-01", "2024-11-07"], "")
        self.assert_text("请输入请假事由", "div:contains('请输入请假事由')")

    @allure.story("个人考勤")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("考勤发起失败(全部为空)")
    @pytest.mark.run(order=14)
    def test_web_myabsent_fail05(self):
        self.login()
        self.click("span:contains('考勤管理')")
        self.click("span:contains('个人考勤')")
        self.click("span:contains('发起考勤')")
        WebAbsentPage.absent_form(self, "", "", [], "")
        self.assert_text("请输入标题！", "div:contains('请输入标题')")
        self.assert_text("请选择请假类型！", "div:contains('请选择请假类型')")
        self.assert_text("请选择请假时间！", "div:contains('请选择请假时间')")
        self.assert_text("请输入请假事由", "div:contains('请输入请假事由')")

    @allure.story("下属考勤")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title("下属考勤页面和功能正常")
    @pytest.mark.smoke
    @pytest.mark.run(order=15)
    def test_web_subabsent(self):
        self.login()
        self.click("span:contains('考勤管理')")
        self.click("span:contains('下属考勤')")
        sub_absent_label = ["标题", "发起人", "类型", "原因", "发起时间", "开始日期", "结束日期", "审批人", "反馈意见",
                            "审核状态", "处理"]
        for label in sub_absent_label:
            self.assert_text(label, f"th:contains('{label}')")
