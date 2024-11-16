#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@ Date        : 2024/11/16 下午9:46
@ Author      : Poco Ray
@ File        : __init__.py
@ Description : 封装常用项目路径
"""
__all__ = [
    'logs_path',
    'data_path',
    'screenshot_path',
    'upload_path',
    'download_path',
    'drivers_path'
]

from common.setting import ensure_path_sep

class Paths:
    """ 封装常用项目路径 """
    logs_path = ensure_path_sep("\\logs")
    data_path = ensure_path_sep("\\data")
    screenshot_path = ensure_path_sep("\\data\\screenshot")
    upload_path = ensure_path_sep("\\data\\upload")
    download_path = ensure_path_sep("\\data\\download")


logs_path = Paths.logs_path
data_path = Paths.data_path
screenshot_path = Paths.screenshot_path
upload_path = Paths.upload_path
download_path = Paths.download_path
drivers_path = "D:\\Develop\\Env\\miniconda3\\envs\\test_env\\Lib\\site-packages\\seleniumbase\\drivers"

# 测试
if __name__ == '__main__':
    print(logs_path)
    print(data_path)
    print(screenshot_path)
    print(upload_path)
    print(download_path)
    print(drivers_path)
