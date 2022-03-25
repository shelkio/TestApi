#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'test'


import os,sys
from datetime import datetime

import threadpool

sys.path.append(os.path.dirname(__file__))
from config import setting
import unittest,time
from lib.sendmail import send_mail
from lib.newReport import new_report
# from db_fixture import test_data
from package.HTMLTestRunner import HTMLTestRunner, MergeResult

import threading


def add_case(test_path=setting.TEST_CASE):
    """加载所有的测试用例"""
    discover = unittest.defaultTestLoader.discover(test_path, pattern='*API.py')
    return discover


# 所有case 结果result，存入list
all_result = []


def run_case(all_case,result_path=setting.TEST_REPORT,nth=0):
    """执行所有的测试用例"""

    # # 初始化接口测试数据
    # test_data.init_data()

    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = result_path + '/' + now + 'result.html'
    fp = open(result_path,'wb')
    runner = HTMLTestRunner(stream=fp,title='接口自动化测试报告',
                            description='环境：windows 10 浏览器：chrome',
                            tester='Test')
    res = runner.runthread(all_case)
    all_result.append(res)
    fp.close()
    # report = new_report(setting.TEST_REPORT) #调用模块生成最新的报告
    # send_mail(report) #调用发送邮件模块


if __name__ == "__main__":
    # 按目录获取到的cases
    allcasenames = add_case()
    # 保存的.html 结果目录
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    time_stamp = int(time.time())
    count = 0
    start_time = datetime.now()
    # 3线程数
    task_pool = threadpool.ThreadPool(2)

    lst = []
    pathlist = []
    for i, j in zip(allcasenames, range(len(list(allcasenames)))):
        file_path = setting.TEST_REPORT + '/rp2/' + str(now) + str(count) + ".html"
        count += 1
        # 禁止文件路转义
        file_path = file_path.replace("\r", r"\r").replace('\n', r'\n')
        # thread_pool 多参数写法
        lst.append(([i, file_path, j], None))
        pathlist.append(file_path)
    rqs = threadpool.makeRequests(run_case, lst)
    #  等待运行结束
    [task_pool.putRequest(req) for req in rqs]
    task_pool.wait()

    end_time = datetime.now()
    # 批量删除单独生成的报告
    for i in pathlist:
        os.remove(i)
    file_path_main = setting.TEST_REPORT + '/rp2/' + str(now) + "_result" + ".html"
    fp = open(file_path_main, "wb")

    # 自定义生成html的class，目前是集合在HTMLTestRunner ，好像不能独立出来，用了很多HTMLTestRunner的自带方法
    merge_html = MergeResult(fp=fp, result_list=all_result, start_time=start_time, end_time=end_time)
    merge_html.make_html()
    fp.close()


