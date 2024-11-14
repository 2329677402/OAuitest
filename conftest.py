#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@ Date        : 2024/11/1 下午9:55
@ Author      : Poco Ray
@ File        : conftest.py
@ Description :
"""
import os
import shutil
import pytest
import time
from seleniumbase import BaseCase
from appium import webdriver as appium_driver
from appium.options.common.base import AppiumOptions
from pkg_resources import resource_filename

BASE_PATH = os.path.dirname(os.path.abspath(__file__))  # 项目根路径
DRIVER_DIR = os.path.join(BASE_PATH, 'drivers')  # 自定义驱动目录
DRIVER_PATH = os.path.join(DRIVER_DIR, 'chromedriver.exe')  # 目标ChromeDriver路径
SELENIUMBASE_DRIVER_PATH = resource_filename('seleniumbase', 'drivers/chromedriver.exe')  # SeleniumBase默认驱动路径


@pytest.fixture(scope='session', autouse=True)
def web_driver():
    # 检查自定义驱动目录是否存在，不存在则创建
    if not os.path.exists(DRIVER_DIR):
        os.makedirs(DRIVER_DIR)

    # 检查chromedriver.exe是否存在，不存在则从seleniumbase复制
    if not os.path.exists(DRIVER_PATH):
        if os.path.exists(SELENIUMBASE_DRIVER_PATH):
            shutil.copy(SELENIUMBASE_DRIVER_PATH, DRIVER_PATH)
            print(f"已将chromedriver.exe复制到指定路径：{DRIVER_PATH}")
        else:
            print("错误：在 SeleniumBase 的默认驱动程序路径中未找到 chromedriver.exe！")
            return
    yield


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
