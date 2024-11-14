#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@ Date        : 2024/11/12 下午9:45
@ Author      : Poco Ray
@ File        : staff_page.py
@ Description : Web-员工管理页面操作封装
"""
class WebStaffPage:
    @classmethod
    def staff_list_query(cls, driver, department: str = None, name: str = None, date_range: list = None):
        """
        功能: 封装员工列表查询操作
        :param driver: 浏览器驱动
        :param department: 查询部门(单选)
        :param name: 查询姓名
        :param date_range: 查询日期范围
        :return: 查询结果
        """
        driver.click("span:contains('请选择部门')")
        department_list = ["董事会", "产品研发部", "运营部", "销售部", "人事部", "财务部"]
        # 适用于单选下拉框的处理方式, 多选下拉框建议使用循环处理
        if department:
            if department not in department_list:
                driver.fail(f"查询部门: {department}不存在!")
            else:
                driver.click(f"li:contains('{department}')")
        if name:
            driver.type("input[placeholder='请输入姓名']", name)
        try:
            if date_range:
                start_date, end_date = date_range
                driver.type("input[placeholder='开始日期']", start_date)
                driver.type("input[placeholder='结束日期']", end_date)
        except ValueError:
            driver.fail("日期范围格式错误, 请输入['1970-01-01', '2099-12-31']的格式!")
        driver.click("button:contains('查询')")