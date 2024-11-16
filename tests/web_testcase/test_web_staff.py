#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@ Date        : 2024/11/12 下午9:43
@ Author      : Poco Ray
@ File        : test_web_staff.py
@ Description : Web-员工管理测试用例
"""
import os
import allure
import pytest
from common import upload_path, download_path, screenshot_path
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
    @allure.title("部门查询功能正常")
    @pytest.mark.smoke
    @pytest.mark.run(order=23)
    def test_web_staff_list_query_department(self):
        self.login()
        self.click("span:contains('员工管理')")
        self.click("span:contains('员工列表')")
        staff_list_label = ["序号", "姓名", "邮箱", "入职时间", "所属部门", "状态", "操作"]
        for label in staff_list_label:
            self.assert_text(label, f"div:contains('{label}')")
        WebStaffPage.staff_list_query(self, "董事会")
        department_elements = self.find_elements("td:contains('董事会')")
        for element in department_elements:
            self.assert_equal("董事会", element.text)

    @allure.story("员工列表")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title("姓名查询功能正常")
    @pytest.mark.smoke
    @pytest.mark.run(order=24)
    def test_web_staff_list_query_name(self):
        self.login()
        self.click("span:contains('员工管理')")
        self.click("span:contains('员工列表')")
        WebStaffPage.staff_list_query(self, name="东东")
        name_elements = self.find_elements("td:contains('东东')")
        for element in name_elements:
            self.assert_equal("东东", element.text)

    @allure.story("员工列表")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title("下载失败(未勾选员工数据)")
    @pytest.mark.smoke
    @pytest.mark.run(order=25)
    def test_web_staff_list_download01(self):
        self.login()
        self.click("span:contains('员工管理')")
        self.click("span:contains('员工列表')")
        self.click("button:contains('下载')")
        self.assert_text("请选择要下载的员工信息", "p.el-message__content")

    @allure.story("员工列表")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title("下载成功(单个)")
    @pytest.mark.smoke
    @pytest.mark.run(order=26)
    def test_web_staff_list_download02(self):
        self.login()
        self.click("span:contains('员工管理')")
        self.click("span:contains('员工列表')")
        self.click(
            "/html/body/div[1]/section/section/main/div[2]/div[3]/div/div[1]/div/div[1]/div[3]/div/div[1]/div/table/tbody/tr[1]/td[1]/div/label/span")
        self.click("button:contains('下载')")
        screenshot_save_path = os.path.join(screenshot_path, "download.png")
        download_save_path = os.path.join(download_path, "员工信息.xlsx")
        self.save_screenshot(screenshot_save_path)
        self.assert_downloaded_file(download_save_path)

    @allure.story("员工列表")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title("下载成功(批量)")
    @pytest.mark.smoke
    @pytest.mark.run(order=27)
    def test_web_staff_list_download03(self):
        self.login()
        self.click("span:contains('员工管理')")
        self.click("span:contains('员工列表')")
        self.click(
            "/html/body/div[1]/section/section/main/div[2]/div[3]/div/div[1]/div/div[1]/div[2]/table/thead/tr/th[1]/div/label")
        self.click("button:contains('下载')")
        screenshot_save_path = os.path.join(screenshot_path, "download.png")
        download_save_path = os.path.join(download_path, "员工信息.xlsx")
        self.save_screenshot(screenshot_save_path)
        self.assert_downloaded_file(download_save_path)

    @allure.story("员工列表")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title("文件上传成功(合法文件合法数据+员工数据不存在)")
    @pytest.mark.smoke
    @pytest.mark.run(order=28)
    def test_web_staff_list_upload01(self):
        self.login()
        self.click("span:contains('员工管理')")
        self.click("span:contains('员工列表')")
        file_path = os.path.join(upload_path, "员工信息.xlsx")
        self.choose_file('input[type="file"]', file_path)
        self.assert_text('员工信息上传成功', 'p.el-message__content')
