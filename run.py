#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@ Date        : 2024/11/1 下午9:08
@ Author      : Poco Ray
@ File        : run.py
@ Description : 入口文件，用于执行整个自动化测试生成Allure报告并发送通知.
实现以下功能:
    1. 打印项目启动信息.
    2. 执行 pytest 测试并生成临时报告.
    3. 生成 Allure 报告.
    4. 根据配置发送通知（如钉钉、微信、邮件、飞书）.
    5. 如果配置启用了 Excel 报告，则生成 Excel 报告.
    6. 自动启动 Allure 报告服务.
    7. 捕获并处理异常，发送错误邮件通知.
"""
import os
import traceback
import pyfiglet
import pytest
from utils.other_tool.models import NotificationType
from utils.other_tool.allure_data.allure_report_data import AllureFileClean
from utils.log_tool.log_control import INFO
from utils.notify_tool.send_wechat import WeChatSend
from utils.notify_tool.send_ding import DingTalkSendMsg
from utils.notify_tool.send_mail import SendEmail
from utils.notify_tool.send_lark import FeiShuTalkChatBot
from utils import config


def run():
    # 从配置文件中获取项目名称
    try:
        # INFO.logger.info(
        #     f"""
        #                      _    _         _      _____         _
        #       __ _ _ __ (_)  / \\  _   _| |_ __|_   _|__  ___| |_
        #      / _` | '_ \\| | / _ \\| | | | __/ _ \\| |/ _ \\/ __| __|
        #     | (_| | |_) | |/ ___ \\ |_| | || (_) | |  __/\\__ \\ |_
        #      \\__,_| .__/|_/_/   \\_\\__,_|\\__\\___/|_|\\___||___/\\__|
        #           |_|
        #           开始执行{config.project_name}项目...
        #         """
        # )
        ascii_banner = pyfiglet.figlet_format(config.project_name)
        print(ascii_banner)
        print(f"开始执行{config.project_name}项目...")
        # 如果性能足够, 可以使用auto参数, 会自动根据CPU核数来最大地分配线程数
        pytest.main(['-n', '4', '--alluredir', './report/tmp', "--clean-alluredir"])

        """
                   --reruns: 失败重跑次数
                   --count: 重复执行次数
                   -v: 显示错误位置以及错误的详细信息
                   -s: 等价于 pytest --capture=no 可以捕获print函数的输出
                   -q: 简化输出信息
                   -m: 运行指定标签的测试用例
                   -x: 一旦错误，则停止运行
                   --maxfail: 设置最大失败次数，当超出这个阈值时，则不会在执行测试用例
                    "--reruns=3", "--reruns-delay=2"
                   """

        # 自定义 Allure 报告生成路径
        allure_report_tmp = './report/tmp'
        allure_report_html = './report/html'

        os.system(f"allure generate {allure_report_tmp} -o {allure_report_html} --clean")

        allure_data = AllureFileClean().get_case_count()
        notification_mapping = {
            NotificationType.DING_TALK.value: DingTalkSendMsg(allure_data).send_ding_notification,
            NotificationType.WECHAT.value: WeChatSend(allure_data).send_wechat_notification,
            NotificationType.EMAIL.value: SendEmail(allure_data).send_main,
            NotificationType.FEI_SHU.value: FeiShuTalkChatBot(allure_data).post
        }

        if config.notification_type != NotificationType.DEFAULT.value:
            notification_mapping.get(config.notification_type)()

        # 程序运行之后，自动启动报告，如果不想启动报告，可注释这段代码
        # netstat -ano | findstr :53230 检查端口是否被占用
        os.system(f"allure serve {allure_report_tmp} -p 53230")


    except Exception:
        # 如有异常，相关异常发送邮件
        e = traceback.format_exc()
        send_email = SendEmail(AllureFileClean.get_case_count())
        send_email.error_mail(e)
        raise


if __name__ == '__main__':
    run()
