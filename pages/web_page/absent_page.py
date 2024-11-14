#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@ Date        : 2024/11/12 下午9:43
@ Author      : Poco Ray
@ File        : absent_page.py
@ Description : Web-考勤管理页面操作封装
"""


class WebAbsentPage:
    @classmethod
    def absent_form(cls, driver, title: str = None, absent_type: str = None, date_range: list = None,
                    reason: str = None):
        """
        功能: 封装提交考勤表单操作
        :param driver:
        :param title: 请假标题
        :param absent_type: 请假类型
        :param date_range: 请假时间
        :param reason: 请假原因
        :return: None
        """
        if title:
            driver.type("input[placeholder='请输入请假标题']", title)
        if absent_type:
            driver.click("span:contains('请选择请假类型')")
            absent_type_list = ["事假", "病假", "年假", "婚假", "产假", "陪产假", "丧假", "调休", "其他"]
            if absent_type not in absent_type_list:
                driver.fail(f"请假类型: {absent_type}不存在!")
            else:
                driver.click(f"li:contains('{absent_type}')")
        try:
            if date_range:
                start_date, end_date = date_range
                driver.type("input[placeholder='开始日期']", start_date)
                driver.type("input[placeholder='结束日期']", end_date)
        except ValueError:
            driver.fail("日期范围格式错误, 请输入['0000-00-00', '9999-99-99']的格式!")
        if reason:
            driver.type("textarea.el-textarea__inner", reason)
        driver.click("span:contains('确认')")
