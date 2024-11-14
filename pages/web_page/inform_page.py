#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@ Date        : 2024/11/12 下午9:45
@ Author      : Poco Ray
@ File        : inform_page.py
@ Description : Web-通知管理页面操作封装
"""


class WebInformPage:
    @classmethod
    def publish_inform_form(cls, driver, title: str = None, departments: list = None, content: str = None):
        """
        功能: 封装发布通知表单操作
        :param driver: 浏览器驱动
        :param title: 通知标题
        :param departments: 通知部门(多选)
        :param content: 通知内容
        :return: 发布通知
        """
        department_list = ["所有部门", "董事会", "产品研发部", "运营部", "销售部", "人事部", "财务部"]
        if title:
            driver.type("input[placeholder='请输入通知标题']", title)
        if departments:
            driver.click("span:contains('请选择')")
            # 适用于多选下拉框的处理方式, 单选下拉框建议使用if-else处理
            for department in departments:
                if department not in department_list:
                    driver.fail(f"通知部门: {department}不存在!")
                else:
                    driver.click(f"li:contains('{department}')")
        if content:
            js_editor = f"""document.querySelector("div[contenteditable='true']").innerHTML = '{content}';"""
            driver.execute_script(js_editor)
        driver.sleep(1)
        driver.click("span:contains('提交')")
