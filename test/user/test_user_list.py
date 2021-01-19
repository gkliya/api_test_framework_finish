# -*- coding:utf-8 -*-
# @Time     :2021/1/15 13:58
# @Author     :liyuan
# @File      :test_user_list.py
# @Software  :PyCharm

import unittest
import requests
import json
from lib.read_excel import *
from lib.case_log import *

class Test_user_list(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.data_list=excel_to_list("test_user_data.xlsx","TestUserList")

