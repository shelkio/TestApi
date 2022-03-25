#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'test'

import os,sys,json
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from lib.signparms import SignParms

class SendRequests():
    """发送请求数据"""
    def sendRequests(self,s,apiData):

            #从读取的表格中获取响应的参数作为传递
            method = apiData["method"]
            url = apiData["url"]
            if apiData["params"] == "":
                par = None
            else:
                par = eval(apiData["params"])
            if apiData["headers"] == "":
                h = None
            else:
                h = eval(apiData["headers"])
            if apiData["body"] == "":
                body_data = None
            else:
                 # body_data = eval(apiData["body"])
                 body_data = SignParms.sign(eval(apiData["body"]),"101000001192","C7717A19F0615B0BBE07286253B9E823")
            type = apiData["type"]
            v = False
            if type == "data":
                body = body_data
            elif type == "json":
                body = json.dumps(body_data)
            else:
                body = body_data
            #发送请求
            re = s.request(method=method,url=url,headers=h,params=par,data=body)
            return re
