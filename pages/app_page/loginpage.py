#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@ Date        : 2024/11/5 上午12:08
@ Author      : Poco Ray
@ File        : login_page.py
@ Description : APP-登录页
"""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from time import sleep


class AppLoginPage(BasePage):
    def __init__(self, driver):
        """
        功能: 获取当前Activity
        :param driver: WebDriver对象
        """
        super(AppLoginPage, self).__init__(driver)
        self.activity = self.driver.current_activity

    def login(self, username, password):
        """
        功能: 登录操作
        :param username: 用户名
        :param password: 密码
        :return:
        """
        self.driver.find_element(By.ID, 'com.android.browser:id/share_button').click()  # 点击允许
        sleep(1)
        self.driver.find_element(By.XPATH,
                                 '//android.view.View[@resource-id="personal-center"]/android.view.View/android.widget.TextView').click()  # 点击用户头像
        sleep(1)
        self.driver.find_element(By.XPATH, '//*[@text="登录"]').click()  # 点击登录按钮
        sleep(1)
        self.driver.find_element(By.CLASS_NAME, 'android.widget.EditText').send_keys(username)  # 输入用户名/手机号/邮箱
        sleep(1)
        self.driver.find_element(By.XPATH, '//*[@text="请勾选协议"]').click()  # 点击勾选协议
        sleep(1)
        self.driver.find_element(By.XPATH, '//*[@text="下一步"]').click()  # 点击下一步
        sleep(1)
        self.driver.find_element(By.XPATH, '//*[@text="账号密码登录"]').click()  # 点击账号密码登录
        sleep(1)
        (self.driver.find_element(By.XPATH,
                                  '//android.view.View[@resource-id="naPassWrapper"]/android.view.View/android.view.View[2]/android.view.View[1]/android.view.View[2]/android.widget.EditText')
         .send_keys(password))  # 输入密码
        sleep(1)
        self.driver.find_element(By.XPATH, '//*[@text="登 录"]').click()  # 点击登录
        sleep(1)
