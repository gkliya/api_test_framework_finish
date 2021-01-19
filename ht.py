# -*- coding:utf-8 -*-
# @Time     :2021/1/14 15:23
# @Author     :liyuan
# @File      :ht.py
# @Software  :PyCharm

import time
from selenium import webdriver
driver=''

def zhuzhou_test_login(user_id,role_id):
   global driver #全局定义driver字段，否则调用完该函数后浏览器会自动关闭
   zhiku = 'zhiku:' + str(role_id) + ':' + user_id + ':' + time.strftime(format('%Y%m%d')) #组装输入的内容
   driver = webdriver.Chrome()  #打开浏览器
   url = 'https://tool.chinaz.com/tools/md5.aspx' #MD5在线加密网站
   driver.get(url) #访问加密网站
   driver.find_element_by_id('q').send_keys(zhiku) #定位到输入框，并且输入需要加密的内容
   driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/form/div/div[2]/div/input[1]').click() #点击加密按钮
   result = driver.find_element_by_id('MD5Result') #获取加密后的内容
   #组装最后访问天元区网站的链接
   test_url = 'http://192.168.20.116:818/checkLogin?' + 'userAccount=' + user_id + '&roleId=' + str(role_id) + '&token=' + result.text + '&backUrl=http%3A%2F%2Frencai.zzgxxc.cn%2F'
   online_url='http://rencaiguanli.zzgxxc.cn/checkLogin?' + 'userAccount=' + user_id + '&roleId=' + str(role_id) + '&token=' + result.text + '&backUrl=http%3A%2F%2Frencai.zzgxxc.cn%2F'
   # driver.get(online_url) #访问天元区线上环境链接

   driver.get(test_url) #访问天元区测试环境链接
   print(online_url)


#输入用户名，用户角色
# zhuzhou_test_login('zk2adminc21',1)  #线上账号

zhuzhou_test_login('zk3rcba0131',1)  #测试账号