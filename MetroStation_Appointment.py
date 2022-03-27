import time
import datetime

import requests
import schedule
import threading


tomorrow = (datetime.datetime.now()+datetime.timedelta(days=+1)).strftime("%Y%m%d")
cook = ["NzNlZmMzNmQtOWEzZC00YmQ2LTk4ZjYtYmVmYzZlOGQ1MmEyLDE2NDg4MDU4NTY4MjcsWDFxeVE4WEsyd3hBanI2b2FKakR2eEsva3BJPQ==",
        'YWY2OGI0NTEtY2NjNy00OTdiLThmMjYtZjJlMzdiNDc3MGFmLDE2NDg5NjU3NjI3MDQsVmdFOExNWjhHSHZwL1lqTlJHTGNJVW5jajJVPQ==']
header = {
    'Host': 'webapi.mybti.cn',
    'Origin': 'https://webui.mybti.cn',
    'Content-Type': 'application/json;charset=utf-8',
    'Accept-Language': 'zh-cn',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Accept': 'application/json, text/plain, */*',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) '
                  'Mobile/15E148 /sa-sdk-ios/sensors-verify/dg.ruubypay.com?production  YiTongXing/5.0.9',
    'Authorization': cook[0],
    'Referer': 'https://webui.mybti.cn/',
    'Content-Length': '148',
}
header1 = {
    'Host': 'webapi.mybti.cn',
    'Origin': 'https://webui.mybti.cn',
    'Content-Type': 'application/json;charset=utf-8',
    'Accept-Language': 'zh-cn',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Accept': 'application/json, text/plain, */*',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) '
                  'Mobile/15E148 /sa-sdk-ios/sensors-verify/dg.ruubypay.com?production  YiTongXing/5.0.9',
    'Authorization': cook[1],
    "Referer": 'https://webui.mybti.cn/',
    'Content-Length': '148',
}


def get_balance():
    url = 'https://webapi.mybti.cn/Appointment/GetBalance'
    parm = {
        "enterDates": [
            tomorrow
        ],
        "timeSlot": "0750-0800",
        "stationName": "沙河站"
    }
    re = requests.post(url=url, headers=header, json=parm)
    a = re.json()
    for i in a:
        str1 = i['timeSlotQueryString']
        str2 = str1.split('-')
        stationName = str2[0]
        enterDates = str2[1] + str2[2] + str2[3]
        print('预约站名:' + stationName + '     预约日期时间:' + enterDates + '     剩余可预约数量:' + str(i['balance']) + "     当前时间:"
              + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))


def create_appointment():
    for i in range(10):
        try:
            get_balance()
            url = 'https://webapi.mybti.cn/Appointment/CreateAppointment'
            parm = {
                "stationName": "沙河站",
                "snapshotTimeSlot": "0630-0930",
                "lineName": "昌平线",
                "enterDate": tomorrow,
                "timeSlot": "0750-0800",
                "snapshotWeekOffset": 0
            }
            re = requests.post(url=url, headers=header, json=parm)
            a = re.json()
            print(a)
            if a['stationEntrance'] is None:
                print('预约1号失败'+'     当前时间:' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
            else:
                print('预约1号成功'+'     预约站名:' + parm['stationName'] + '     预约日期:' + parm['enterDate'] + '     预约时间段' + parm[
                    'timeSlot'] + '     当前时间:' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
                break
        except Exception as e:
            print("Error %s:" % e)
        time.sleep(1)


def create_appointment1():
    for i in range(10):
        try:
            get_balance()
            url = 'https://webapi.mybti.cn/Appointment/CreateAppointment'
            parm = {
                "stationName": "沙河站",
                "snapshotTimeSlot": "0630-0930",
                "lineName": "昌平线",
                "enterDate": tomorrow,
                "timeSlot": "0750-0800",
                "snapshotWeekOffset": 0
            }
            re = requests.post(url=url, headers=header1, json=parm)
            a = re.json()
            print(a)
            if a['stationEntrance'] is None:
                print('预约2号失败'+'     当前时间:' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
            else:
                print('预约2号成功'+'     预约站名:' + parm['stationName'] + '     预约日期:' + parm['enterDate'] + '     预约时间段' + parm[
                    'timeSlot'] + '     当前时间:' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
                break
        except Exception as e:
            print("Error %s:" % e)
        time.sleep(1)

def sch_test1():
    threading.Thread(target=create_appointment).start()

def sch_test2():
    threading.Thread(target=create_appointment1).start()


schedule.every().day.at('11:59:58').do(sch_test1)  # 每天晚上八点执行
schedule.every().day.at('11:59:58').do(sch_test2)  # 每天晚上八点执行

while True:
    schedule.run_pending()  # 运行所有可运行的任


# get_balance()
