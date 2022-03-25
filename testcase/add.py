import codecs
import sys
sys.path.append(r"C:\Users\shelk\PycharmProjects\TestApi")
from config import setting
from lib.readexcel import ReadExcel
import requests
import time,datetime
import random
import json


import _md5

testData = ReadExcel(r"C:\Users\shelk\Desktop\行业.xls", "Sheet1").read_data()

rejectReason = testData[0]["发动单位（支队）"]
getname = testData[0]["姓名"]
getphone = testData[0]["手机号"]
getnum = testData[0]["身份证号"]
now = time.time()
timenow = int(round(now * 1000))
a="111"
b = {1,2,3}
c={
  "business_id" : "91",
  "longitude" : 116.46608734130859,
  "appId" : "101000001193",
  "cgs_token" : "db62a5029e9f4a8bbe7ccc494eed7289",
  "latitude" : 40.020961761474609,
  "timestamp" : 1635314957089,
  "nonce" : "5568963314805448"
}

qbc = {"business_id" : "91", "longitude" : 116.46608734130859,"latitude" : 40.020961761474609}
qbc["appid"] = "101000001193"
qbc["cgs_token"] = "db62a5029e9f4a8bbe7ccc494eed7289"
qbc["nonce"] = "5568963314805448"
qbc["timestamp"] = "1635314957089"

print("几何和阿大撒"+str(qbc))


import collections
#按key排序
kd = collections.OrderedDict(sorted(c.items(), key=lambda t: t[0]))
print (kd.items())
#定义一个空集合
dic=[]
#循环把key=value拼接到集合里
for key,value in kd.items():
 dic.append(str(key)+"="+str(value))
print(dic)
#把集合拆分以&拼接成字符串
newstr = '&'.join(dic)+"&secretKey=5A1F85D141DA5B60B48B8EE7B2712343"
sign = _md5.md5(newstr.encode(encoding="utf-8")).hexdigest().upper()
print(sign)
later = datetime.datetime.now()+datetime.timedelta(hours=24)
print(later)
print(datetime.datetime.now())
print(time.mktime(later.timetuple()))
import re
a = '******* 正在执行用例 ->event_query_001 *********\n ******* 正在执行用例 ->cgs_query_002 *'
b = re.findall("正在执行用例 ->(.+?) ",a)
print(b[-1])
import threading
import time



a =["aaa","nn",123,456,330,7]
b = []
for i in a:
    b.append(i)
print(b)


def triangles():
    print(123)
    ret = [1]
    while True:
        yield ret
        for i in range(1, len(ret)):
            ret[i] = pre[i] + pre[i - 1]
        ret.append(1)
        pre = ret[:]
print(123123)
triangles()

d = {"a": r"\asdf"}
q = str(d)
f = json.dumps(d)
c = str(f).replace(r"\\", "\\")
e = c
print(codecs.getdecoder("unicode_escape")(str(d))[0])
print(d)
print(q)
a = ['', '2', '', '2', '3']
for i in range(len(a)):
    if len(a[i]) == 0:
        print(i)

a = "(0, <package.HTMLTestRunner._TestResult run=1 errors=0 failures=0>)"
q = a.split(',')[0].strip("(")
print(q)










n = int(input("输入:"))


for i in range(2,n+1):
    for j in range(2,i):
        print(str(i) +"%"+ str(j)+"值是" + str(i % j))
        if i % j ==0:
            print("j的值是"+str(j))
            break
        else:
            print("i的值是"+str(i))


















# url = 'https://suishoupai.zhongchebaolian.com:9002/suishoupai/ssp_platform/industry/queryByCondition'
#
# headers = {
#     "Content-Type": "application/json;charset=UTF-8",
#     "Cookie": "Admin-Phone=17600352198; sidebarStatus=1; Admin-Token=c6cbc3bf22f746b0808a6707e5c69171"
# }
#
#
# for i in range(1):
#     num = random.randint(100, 999)
#     print(i)
#     date = {
# 		"appId": "100100006211",
# 		"departmentId": "10021038",
# 		"groupId": "19",
# 		"idNumber": "33262419630719572X",
# 		"name": "潘和仙",
# 		"nonce": "0154057177894023",
# 		"phoneNumber": "15625898526",
# 		"status": "1",
# 		"timestamp": "1633675789912",
# 		"token": "c6cbc3bf22f746b0808a6707e5c69171",
# 		"sign": "0D23CB3DFDCF648C49C9536C6459A587"
# }
#     req = requests.post(url=url, headers=headers, json=date)
#     print(req.json())

