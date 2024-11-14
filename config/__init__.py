#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@ Date        : 2024/11/2 上午1:38
@ Author      : Poco Ray
@ File        : __init__.py
@ Description : 项目配置导出. 1. 对于固定的文件或路径, 通过os模块写死路径; 2. 对于可变的配置, 通过YamlReader工具类读取config.yaml文件中的配置.
"""

import os
from utils.read_util import YamlReader

__all__ = [
    'BASE_PATH',  # 项目根路径
    "data_path",  # 测试数据路径
    'LOG_PATH',  # 日志路径, BASE_PATH + "logs"
    'CASE_PATH',  # 测试用例集路径, BASE_PATH + "tests"
    'CASEYMAL_PATH',  # Yaml用例数据路径, BASE_PATH + "data/case_yaml"
    'LOCATORYMAL_PATH',  # Yaml定位数据路径, BASE_PATH + "data/locate_yaml"
    'DATA_FILE',  # 测试文件路径, BASE_PATH + "data/file"
    'DIFF_IMGPATH',  # 图片对比路径, BASE_PATH + "data/file/img"
    'screenshot_path',  # 截图路径
    'download_path',  # 截图路径
    'WIN_CHROMEDRIVER',  # 谷歌浏览器
    'WIN_FIREFOXDRIVER',  # 火狐浏览器
    'LINUX_CHROMEDRIVER',  # 谷歌浏览器
    'LINUX_FIREFOXDRIVER',  # 火狐浏览器
    'MAC_CHROMEDRIVER',  # 谷歌浏览器
    'MAC_FIREFOXDRIVER',  # 火狐浏览器
]


# Explain:
# 1. os.path.abspath(__file__): 返回当前文件的绝对路径
# 2. os.path.dirname(): 返回当前文件的上级目录路径
# 3. os.path.join(): 拼接路径
# 4. os.path.expanduser(): 将path中包含的"~"和"~user"转换成用户目录


BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 项目根路径
data_path = os.path.join(BASE_PATH, "data")  # 测试数据路径

LOG_PATH = os.path.join(BASE_PATH, "logs")  # 日志存放路径

CASE_PATH = os.path.join(BASE_PATH, "tests")  # 测试用例集路径

CASEYMAL_PATH = os.path.join(BASE_PATH, "data", "case_yaml")  # Yaml用例数据路径

LOCATORYMAL_PATH = os.path.join(BASE_PATH, "data", "locate_yaml")  # Yaml定位数据路径

DATA_FILE = os.path.join(BASE_PATH, "data", "file")  # 测试文件路径

DIFF_IMGPATH = os.path.join(BASE_PATH, "data", "file", "img")  # 图片对比路径

screenshot_path = os.path.join(BASE_PATH, "data", "screenshot")  # 截图路径
download_path = os.path.join(BASE_PATH, "data", "download")  # 截图路径

WIN_CHROMEDRIVER = os.path.join(BASE_PATH, "driver", "windows", "chromedriver.exe")  # 谷歌浏览器
WIN_FIREFOXDRIVER = os.path.join(BASE_PATH, "driver", "windows", "geckodriver.exe")  # 火狐浏览器
LINUX_CHROMEDRIVER = os.path.join(BASE_PATH, "driver", "linux", "chromedriver")  # 谷歌浏览器
LINUX_FIREFOXDRIVER = os.path.join(BASE_PATH, "driver", "linux", "geckodriver")  # 火狐浏览器
MAC_CHROMEDRIVER = os.path.join(BASE_PATH, "driver", "mac", "chromedriver")  # 谷歌浏览器
MAC_FIREFOXDRIVER = os.path.join(BASE_PATH, "driver", "mac", "geckodriver")  # 火狐浏览器
