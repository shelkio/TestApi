import time

import requests
import schedule

header = {
'Host': 'webapi.mybti.cn',
'Origin': 'https://webui.mybti.cn',
'Content-Type': 'application/json;charset=utf-8',
'Accept-Language': 'zh-cn',
'Accept-Encoding': 'gzip, deflate, br',
'Connection': 'keep-alive',
'Accept': 'application/json, text/plain, */*',
'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 /sa-sdk-ios/sensors-verify/dg.ruubypay.com?production  YiTongXing/5.0.9',
'Authorization': 'NzNlZmMzNmQtOWEzZC00YmQ2LTk4ZjYtYmVmYzZlOGQ1MmEyLDE2NDg4MDU4NTY4MjcsWDFxeVE4WEsyd3hBanI2b2FKakR2eEsva3BJPQ==',
'Referer': 'https://webui.mybti.cn/',
'Content-Length': '148',
}
def GetBalance():
    url  = 'https://webapi.mybti.cn/Appointment/GetBalance'
    parms = {
        "enterDates": [
            "20220324",
            "20220325"
        ],
        "timeSlot": "0740-0810",
        "stationName": "沙河站"
    }
    respn = requests.post(url=url,headers=header,json=parms)
    a = respn.json()
    for i in a:
        str1 = i['timeSlotQueryString']
        str2 = str1.split('-')
        stationName = str2[0]
        enterDates = str2[1]+str2[2]+str2[3]
        print('预约站名:'+stationName+'           预约日期时间:'+enterDates+'             剩余可预约数量:'+str(i['balance']))


def CreateAppointment():
    url = 'https://webapi.mybti.cn/Appointment/CreateAppointment'
    parms = {
        "stationName": "沙河站",
        "snapshotTimeSlot": "0700-0900",
        "lineName": "昌平线线",
        "enterDate": "20220325",
        "timeSlot": "0750-0800",
        "snapshotWeekOffset": 0
    }
    respn = requests.post(url=url, headers=header, json=parms)
    print("当前时间:"+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    a = respn.json()
    print(a)
    if a['stationEntrance'] is None:
        print('预约失败')
    else:
        print('预约站名:'+parms['stationName']+'预约日期:'+parms['enterDate']+'     预约时间段'+parms['timeSlot']+'   预约成功')

# schedule.every().day.at("11:00:01").do(CreateAppointment)  # 每天晚上八点执行
#
# while True:
#     schedule.run_pending() # 运行所有可运行的任务


GetBalance()
print("当前时间:"+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
# CreateAppointment()
