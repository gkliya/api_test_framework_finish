import logging
import os

# 项目路径
prj_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 当前文件的上一级的上一级目录（增加一级）

data_path = os.path.join(prj_path, 'data')  # 数据目录
test_path = os.path.join(prj_path, 'test')   # 用例目录

log_file = os.path.join(prj_path, 'log', 'log.txt')  # 更改路径到log目录下
report_file = os.path.join(prj_path, 'report', 'report.html')  # 更改路径到report目录下

# log配置
logging.basicConfig(level=logging.DEBUG,  # log level
                    format='[%(asctime)s] %(levelname)s [%(funcName)s: %(filename)s, %(lineno)d] %(message)s',  # log格式,时间，日志级别名字、当前函数、当前执行程序名、日志的当前行号、日志信息
                    datefmt='%Y-%m-%d %H:%M:%S',  # 日期格式
                    filename=log_file,  # 日志输出文件
                    filemode='a')  # 追加模式


# 数据库配置
db_host = '192.168.20.240'
db_port = 3306
db_user = 'root'
db_passwd = 'Rc123#@!'
db = 'expertzz_dev'

# 邮件配置
smtp_server = 'smtp.sina.com'
smtp_user = 'test_results@sina.com'
smtp_password = 'hanzhichao123'

sender = smtp_user  # 发件人
receiver = '1345325190@qq.com'  # 收件人
subject = '接口测试报告'  # 邮件主题

headers = {
    "token": "eyJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE2MTA5NTAxMjMsImVudF9pZCI6bnVsbCwicm9sZUlkcyI6IjEwMDAiLCJ1c2VyX3R5cGUiOm51bGwsInVzZXJSZWFsbmFtZSI6InprM3JjYmEwMTMxIiwiaWQiOjE0NDgsInJvbGVOYW1lcyI6IuW5s-WPsOeuoeeQhuWRmCIsIm9yZ0lkIjoxMDAxLCJzdWIiOiJ3ZWIiLCJleHAiOjE2MTEwMzY1MjN9.ZffQIIp1jKZSvq6rLINAy4SUFiSpr50qgEJItqyN9Ss"}