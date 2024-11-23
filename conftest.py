# -*- coding: UTF-8 -*-
"""
@ Date        : 2024/11/1 下午9:55
@ Author      : Poco Ray
@ File        : conftest.py
@ Description : Pytest配置文件
"""
import os
import pytest
import time
from airtest.core.api import connect_device, auto_setup
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from common import drivers_path
from utils import config


def get_driver_path(driver_name):
    """根据操作系统获取驱动路径"""
    if os.name == 'nt':  # Windows
        return os.path.join(drivers_path, f"{driver_name}.exe")
    else:  # Linux and others
        return os.path.join(drivers_path, driver_name)


@pytest.fixture(scope='session')
def setup_browser_driver():
    """根据配置文件中的浏览器类型安装相应的驱动"""
    browser = config.browser.lower()
    driver_name = None
    if browser == "chrome":
        driver_name = "chromedriver"
    elif browser == "firefox":
        driver_name = "geckodriver"
    elif browser == "edge":
        driver_name = "edgedriver"
    elif browser == "ie":
        driver_name = "iedriver"
    elif browser == "opera":
        driver_name = "operadriver"
    else:
        raise ValueError(f"不支持的浏览器类型: {browser}")

    if driver_name:
        driver_path = get_driver_path(driver_name)
        if not os.path.exists(driver_path):
            os.system(f"seleniumbase install {driver_name}")
        else:
            print(f"{driver_name} 已存在于 {driver_path}，无需下载.")


@pytest.fixture(scope='session')
def setup_airtest_poco():
    """配置 Airtest 和 Poco"""
    # 连接设备
    device = connect_device("android://127.0.0.1:5037/192.168.31.28:5555")
    auto_setup(__file__)
    poco = AndroidUiautomationPoco(device=device, use_airtest_input=True, screenshot_each_action=False)
    yield poco
    # 断开设备连接
    device.disconnect()