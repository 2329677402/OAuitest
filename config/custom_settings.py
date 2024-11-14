#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@ Date        : 2024/11/14 下午8:20
@ Author      : Poco Ray
@ File        : custom_settings.py
@ Description : 自定义设置文件，用于覆盖Seleniumbase的默认设置
要覆盖 seleniumbase/config/settings.py 中存储的默认设置，请更改此处的值并在运行时添加“--settings_file=./config/settings.py”
"""

# 超时设置: 定义等待页面元素出现的默认超时时间
MINI_TIMEOUT = 2  # 最小超时时间，通常用于等待时间较短的操作
SMALL_TIMEOUT = 7  # 较小超时时间，适用于等待时间稍长的操作
LARGE_TIMEOUT = 10  # 较大超时时间，适用于等待时间较长的操作
EXTREME_TIMEOUT = 30  # 极限超时时间，适用于等待时间非常长的操作

# 页面加载超时：设置页面加载的超时时间
PAGE_LOAD_TIMEOUT = 120

# 页面加载策略: 定义页面加载策略
PAGE_LOAD_STRATEGY = "normal"  # 页面加载策略，"normal"、"eager" 或 "none"

# 日志和下载管理: 控制是否保存现有日志和下载文件
ARCHIVE_EXISTING_LOGS = False  # 是否保存现有日志
ARCHIVE_EXISTING_DOWNLOADS = False  # 是否保存现有下载文件

# 截图设置: 控制最后页面截图是否包含背景
SCREENSHOT_WITH_BACKGROUND = False  # 是否包含背景

# 标签页切换: 控制点击打开新标签页时是否自动切换
SWITCH_TO_NEW_TABS_ON_CLICK = True  # 是否自动切换到新标签页

# JavaScript等待: 控制在页面加载和点击后是否等待 JavaScript 完成
WAIT_FOR_RSC_ON_PAGE_LOADS = True  # 页面加载后等待 JavaScript 完成
WAIT_FOR_RSC_ON_CLICKS = False  # 点击后等待 JavaScript 完成
WAIT_FOR_ANGULARJS = True  # 等待 AngularJS 完成
SKIP_JS_WAITS = False  # 跳过所有 JavaScript 等待

# 演示模式: 设置演示模式的默认行为
DEFAULT_DEMO_MODE_TIMEOUT = 0.5  # 演示模式超时时间
HIGHLIGHTS = 4  # 高亮次数
DEFAULT_MESSAGE_DURATION = 2.55  # 消息显示时长

# 内容安全策略: 控制是否禁用浏览器的内容安全策略
DISABLE_CSP_ON_FIREFOX = True  # 禁用 Firefox 的内容安全策略
DISABLE_CSP_ON_CHROME = False  # 禁用 Chrome 的内容安全策略

# 代理设置: 控制无效代理字符串时是否立即报错
RAISE_INVALID_PROXY_STRING_EXCEPTION = True  # 无效代理字符串时立即报错

# 浏览器分辨率: 设置新窗口的默认浏览器分辨率
CHROME_START_WIDTH = 1250  # Chrome 浏览器宽度
CHROME_START_HEIGHT = 840  # Chrome 浏览器高度
HEADLESS_START_WIDTH = 1440  # 无头模式宽度
HEADLESS_START_HEIGHT = 1880  # 无头模式高度

# 驱动下载消息: 控制是否隐藏与下载驱动相关的消息
HIDE_DRIVER_DOWNLOADS = False  # 是否隐藏驱动下载消息

# MasterQA模式: 设置 MasterQA 模式的默认行为
MASTERQA_DEFAULT_VALIDATION_MESSAGE = "页面看起来是否正常？"  # 默认验证消息
MASTERQA_WAIT_TIME_BEFORE_VERIFY = 0.5  # 验证前等待时间
MASTERQA_START_IN_FULL_SCREEN_MODE = False  # 是否全屏模式启动
MASTERQA_MAX_IDLE_TIME_BEFORE_QUIT = 600  # 最大空闲时间

# Google身份验证器: 设置用于双因素身份验证的密钥
TOTP_KEY = "base32secretABCD"  # Google 身份验证器密钥

# MySQL数据库凭证: 设置用于将测试数据保存到 MySQL 数据库的凭证
DB_HOST = "127.0.0.1"  # 数据库主机
DB_PORT = 3306  # 数据库端口
DB_USERNAME = "root"  # 数据库用户名
DB_PASSWORD = "test"  # 数据库密码
DB_SCHEMA = "test_db"  # 数据库模式

# Amazon S3存储桶凭证: 设置用于将截图和其他日志文件保存到 Amazon S3 的凭证
S3_LOG_BUCKET = "[S3 BUCKET NAME]"  # S3 存储桶名称
S3_BUCKET_URL = "https://s3.amazonaws.com/[S3 BUCKET NAME]/"  # S3 存储桶 URL
S3_SELENIUM_ACCESS_KEY = "[S3 ACCESS KEY]"  # S3 访问密钥
S3_SELENIUM_SECRET_KEY = "[S3 SECRET KEY]"  # S3 秘密密钥

# 加密设置: 设置用于字符串/密码混淆的加密密钥和标记
ENCRYPTION_KEY = "Pg^.l!8UdJ+Y7dMIe&fl*%!p9@ej]/#tL~3E4%6?"  # 加密密钥
OBFUSCATION_START_TOKEN = "$^*ENCRYPT="  # 混淆开始标记
OBFUSCATION_END_TOKEN = "?&#$"  # 混淆结束标记
