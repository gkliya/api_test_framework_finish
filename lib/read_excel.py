import xlrd
import sys
sys.path.append('../..')
from config.config import *  # 从项目路径下导入
from lib.case_log import log_case_info  # 从项目路径下导入
from lib.db import *
from lib.run_method import *

rm=RunMethod()

def excel_to_list(data_file, sheet):
    data_list = []  # 新建个空列表，来乘装所有的数据
    wb = xlrd.open_workbook(os.path.join(data_path, data_file))  # 打开excel
    sh = wb.sheet_by_name(sheet)  # 获取工作簿
    header = sh.row_values(0)  # 获取标题行数据
    for i in range(1, sh.nrows):  # 跳过标题行，从第二行开始取数据
        d = dict(zip(header, sh.row_values(i)))  # 将标题和每行数据组装成字典
        data_list.append(d)
    return data_list  # 列表嵌套字典格式，每个元素是一个字典


def get_test_data(data_list, case_name):
    for case_data in data_list:
        if case_name == case_data['case_name']:  # 如果字典数据中case_name与参数一致
            return case_data
            # 如果查询不到会返回None


if __name__ == '__main__':
    data_list = excel_to_list("test_user_data.xlsx", "TestUserLogin")  # 读取excel，TestUserLogin工作簿的所有数据
    case_data = get_test_data(data_list, 'test_user_list')  # 查找用例'test_user_login_normal'的数据
    print(case_data)
    url = case_data.get('url')  # excel中的标题也必须是小写url
    method = case_data.get('method')
    expect_res = case_data.get('expect_res')  # 期望数据
    res = rm.run_main( method=method,url=url, headers=headers)  # 表单请求，数据转为字典格式
    count = query_db(expect_res)
    print(res.text)
