#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@ Date        : 2024/11/5 上午12:08
@ Author      : Poco Ray
@ File        : login_page.py
@ Description : APP-登录页
"""
from airtest.core.api import *


class AppLoginPage:

    @classmethod
    def app_login(cls, poco, username, password):
        """登录操作"""
        poco(text="请输入账号").click()
        text(username)
        poco(text="请输入密码").click()
        text(password)
        poco(text="登录").click()
