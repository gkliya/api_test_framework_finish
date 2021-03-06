import unittest
from lib.read_excel import *  # 从项目路径下导入
from lib.case_log import log_case_info  # 从项目路径下导入
from lib.db import *
from lib.run_method import *

rm=RunMethod()
global entId

class TestUserLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):   # 整个测试类只执行一次
        cls.data_list = excel_to_list(os.path.join( data_path,"test_user_data.xlsx"), "TestUserLogin")# 读取TestUserReg工作簿的所有数据
        # cls.data_list 同 self.data_list 都是该类的公共属性



    def test_user_login_normal(self):
        case_data = get_test_data(self.data_list, 'test_user_login_normal')   # 从数据列表中查找到该用例数据
        url = case_data.get('url')   # excel中的标题也必须是小写url
        data = json.loads(case_data.get('data')) # 注意字符串格式，需要用json.loads()转化为字典格式
        expect_res = case_data.get('expect_res')  # 期望数据
        res = requests.post(url=url, data=(data),headers=headers)  # 表单请求，数据转为字典格式
        log_case_info('test_user_login_normal', url, data, expect_res, res.text)
        self.assertEqual(res.json()['msg'], expect_res)  # 断言
        entId= res.json()['data']['entId']
        return entId


    def test_user_login_delete(self):
        case_data = get_test_data(self.data_list, 'test_user_login_password_wrong')  # 从数据列表中查找到该用例数据
        url = case_data.get('url')  # excel中的标题也必须是小写url
        data = {"id":entId}
        expect_res = case_data.get('expect_res')  # 期望数据
        res = requests.delete(url=url, data=data,headers=headers)
        log_case_info('test_user_login_password_wrong', url, data, expect_res, res.text)
        self.assertEqual(res.json()['msg'], expect_res)  # 断言

    def test_user_list(self):
        case_data=get_test_data(self.data_list,'test_user_list')
        url = case_data.get('url')  # excel中的标题也必须是小写url
        method=case_data.get('method')
        expect_res = case_data.get('expect_res')  # 期望数据
        res = rm.run_main( method=method,url=url, headers=headers)  # 表单请求，数据转为字典格式
        count=query_db(expect_res)
        self.assertEqual(res.json()['data']['total'], count)


if __name__ == '__main__':
    unittest.main(verbosity=2)
