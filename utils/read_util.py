#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@ Date        : 2024/11/2 下午6:00
@ Author      : Poco Ray
@ File        : read_util.py
@ Description : 读取各种文件工具类
"""
import os, yaml
import pandas as pd
import logging
from typing import Union
from faker import Faker

fake = Faker('zh_CN')  # 生成虚拟数据


class ExcelReader:
    """
    读取Excel文件中的内容。返回list。
    如：
    Excel中内容为：
    | A  | B  | C  | x |
    | A1 | B1 | C1 | . |
    | A2 | B2 | C2 | . |

    默认输出结果：
    [{A: A1, B: B1, C:C1}, {A:A2, B:B2, C:C2}]

    line=False输出结果：
    [[A,B,C], [A1,B1,C1], [A2,B2,C2]]

    可以指定sheet，通过index或者name：
    ExcelReader(excel, sheet=2)
    ExcelReader(excel, sheet='BaiDuTest')
    """

    def __init__(self, excel_path: str, sheet: int = 0 or str, header: bool = True):
        """
        :param excel_path: Excel文件路径
        :param sheet: sheet工作表名称(字符串)或者索引(整数, 0为第一个sheet)
        :param header: 表头行, True:包含, False:不包含
        """
        if os.path.exists(excel_path):
            self.excel_path = excel_path
        else:
            raise FileNotFoundError('文件不存在！')
        self.sheet = sheet
        self.header = header
        self._data = []

    @property
    def data(self):
        """
        功能: 读取excel数据
        :return: 将Excel数据转换为字典列表或者嵌套列表
        """
        if not self._data:
            df = pd.read_excel(self.excel_path, sheet_name=self.sheet)
            if self.header:
                self._data = df.to_dict(orient='records')  # 将数据转换为字典列表
            else:
                self._data = df.values.tolist()  # 将数据转换为嵌套列表
        return self._data


class YamlReader:
    """读取yaml文件数据"""

    def __init__(self, file_path: str):
        self.file_path = file_path

    def read_yaml(self, key: str = None) -> Union[dict, list, str]:
        """
        功能: 读取yaml文件
        :param key: yaml文件中的键, 可选
        :return: yaml文件数据
        """
        try:
            with open(self.file_path, encoding='utf-8') as f:
                data = yaml.load(f, Loader=yaml.FullLoader)  # yaml.FullLoader: 用于加载yaml文件内容
                if key:
                    for item in data:
                        if item.get(key) is not None:
                            return item.get(key)
                else:
                    return data
        except Exception as e:
            logging.error(f'读取Yaml文件失败: {e}')


class RandomDataGenerator:
    """基于 faker库 随机测试数据"""

    @property
    def random_name(self):
        """随机中文姓名, 格式: 蔡徐坤"""
        return fake.name()

    @property
    def random_phone(self):
        """随机手机号, 格式: 18766895523"""
        return fake.phone_number()

    @property
    def random_email(self):
        """随机邮箱, 格式: taopan@example.com"""
        return fake.email()

    @property
    def random_job(self):
        """随机职业, 格式: 质量管理/测试工程师(QA/QC工程师)"""
        return fake.job()

    @property
    def random_ssn(self):
        """随机中国居民证身份证号, 格式: 340406193710180483"""
        return fake.ssn()

    @property
    def random_company(self):
        """随机公司, 格式: 深圳市华为技术有限公司"""
        return fake.company()

    @property
    def random_city(self):
        """随机城市, 格式: 北京市"""
        return fake.city_name()

    @property
    def random_province(self):
        """随机省份, 格式: 浙江省"""
        return fake.province()

    @property
    def random_country(self):
        """随机国家, 格式: 中国"""
        return fake.country()

    @property
    def random_address(self):
        """随机地址+邮编, 格式: 江西省长沙市孝南罗路x座 806153"""
        return fake.address()

    @property
    def random_time(self):
        """随机时间, 格式: 18:00:00"""
        return fake.time()

    @property
    def random_year(self):
        """随机年份, 格式: 2024"""
        return fake.year()

    @property
    def random_month(self):
        """随机月份, 格式: 11"""
        return fake.month()

    @property
    def random_current_month(self):
        """随机生成当前月份内的日期, 格式: 2024-11-02 18:00:00"""
        return fake.date_time_this_month(before_now=True, after_now=False, tzinfo=None)

    @property
    def random_current_year(self):
        """随机生成当前年份内的日期, 格式: 2024-11-02 18:00:00"""
        return fake.date_time_this_year(before_now=True, after_now=False, tzinfo=None)

    @property
    def random_current_century(self):
        """随机生成当前世纪内的日期, 格式: 2000-04-12 18:34:11"""
        return fake.date_time_this_century(before_now=True, after_now=False, tzinfo=None)

    @property
    def random_week(self):
        """随机周, 格式: 星期一"""
        return fake.day_of_week()

    @staticmethod
    def random_birth(age):
        """
        功能: 随机生成生日, 格式: 2002-11-02
        :param age: 年份
        :return: 生日在 [当前年份-age, 当前日期] 之间, 如当前日期为2024-10-01,将age设置为1,则随机数据在 [2023-01-01, 2024-10-01] 之间
        """
        return fake.date_of_birth(tzinfo=None, minimum_age=0, maximum_age=age)


def replace_extend(file_path):
    """
    功能: 替换文件后缀名, 将py文件替换为yaml文件
    :param file_path: 文件路径
    :return: .py -> .yaml
    """
    return os.path.basename(file_path).replace('py', 'yaml')


# 测试功能是否正常
if __name__ == '__main__':
    # 读取faker库的测试数据
    generator = RandomDataGenerator()
    print(f"随机姓名: {generator.random_name}")
