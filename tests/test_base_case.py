#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@ Date        : 2024/11/13 上午1:29
@ Author      : Poco Ray
@ File        : test_base_case.py
@ Description : 测试用例自定义基类
"""
import os
import pytest
from utils import config
from common import screenshot_path, download_path
from seleniumbase import BaseCase
from pages.base_page import locate_web_home
from pages.web_page.login_page import WebLoginPage

BaseCase.main(__name__, __file__)


@pytest.mark.usefixtures('setup_browser_driver')
class BaseTestCase(BaseCase):
    def setUp(self, **kwargs):
        super().setUp()
        # 设置浏览器打开最大化
        self.maximize_window()

        if not os.path.exists(screenshot_path):
            os.makedirs(screenshot_path)
        if not os.path.exists(download_path):
            os.makedirs(download_path)
        # 设置浏览器下载文件的路径, 下载路径变更后, 使用assert_downloaded_file方法断言时, 断言路径也需要变更.
        self.driver.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
        params = {'cmd': 'Page.setDownloadBehavior',
                  'params': {'behavior': 'allow', 'downloadPath': download_path}}
        self.driver.execute("send_command", params)

    def tearDown(self):
        self.save_teardown_screenshot()
        if self.has_exception():
            # <<< 如果测试失败，则运行自定义代码. >>>
            pass
        else:
            # <<< 如果测试通过，则运行自定义代码. >>>
            pass
        # (将不可靠的代码包装在 try/except 块中.)
        # <<< 在 super() 行之前运行自定义代码. >>>
        super().tearDown()

    def login(self, email: str = 'dongdong@qq.com', password: str = '111111'):
        """
        功能: 登录成功
        :param email:
        :param password:
        :return:
        """
        self.open(config.host)
        WebLoginPage.login(self, email, password)

    def check_permissions(self):
        """
        功能: 权限检查
        :return:
        """
        locate_auth = locate_web_home['auth_department']
        department = self.get_text(locate_auth).split('[')[1].split(']')[0].strip()
        WebLoginPage.check_permissions(self, department)
