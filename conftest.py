#!/usr/bin/env python
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
from common import drivers_path
from utils import config
from appium import webdriver as appium_driver
from appium.options.common.base import AppiumOptions


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
def app_driver():
    options = AppiumOptions()
    options.load_capabilities({
        "platformName": "Android",  # 平台名称, adb shell getprop ro.product.brand
        "platformVersion": "12",  # Android版本, adb shell getprop ro.build.version.release
        "deviceName": "127.0.0.1:16384",  # MuMu模拟器固定ADB调试端口, adb devices
        "appPackage": "com.android.browser",  # 包名, adb shell dumpsys window | findstr mCurrentFocus
        "appActivity": ".BrowserActivity",  # 应用名, adb shell dumpsys window | findstr mCurrentFocus
        "automationName": "uiautomator2",  # 自动化引擎
        "autoGrantPermissions": True,  # 自动授予权限
        "noReset": False,  # 是否重置app状态
        "fullReset": False,  # 是否清理app缓存数据
        "newCommandTimeout": 3600,  # 会话超时时间
        "connectHardwareKeyboard": True,  # 是否连接硬件键盘
    })
    ad = appium_driver.Remote("http://localhost:4723", options=options)  # 创建driver并启动app
    time.sleep(3)
    yield ad
    ad.quit()
