#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@ Date        : 2024/11/4 下午10:54
@ Author      : Poco Ray
@ File        : base_page.py
@ Description : 基础页面类
"""
from config import LOCATORYMAL_PATH
from utils.read_util import YamlReader

locate_web_yaml_path = YamlReader(LOCATORYMAL_PATH + "/locate_web.yaml")

locate_web_common = locate_web_yaml_path.read_yaml('common_page') # 公共页面元素定位
locate_web_login = locate_web_yaml_path.read_yaml('login_page') # 登录页面元素定位
locate_web_home = locate_web_yaml_path.read_yaml('home_page') # 首页页面元素定位
locate_web_absent = locate_web_yaml_path.read_yaml('absent_page') # 考勤管理页面元素定位
locate_web_inform = locate_web_yaml_path.read_yaml('inform_page') # 考勤管理页面元素定位
locate_web_staff = locate_web_yaml_path.read_yaml('staff_page') # 员工管理页面元素定位

class BasePage:
    def __init__(self, driver):
        self.driver = driver

