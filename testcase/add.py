from config import setting
from lib.readexcel import ReadExcel
import requests
import time
import random

testData = ReadExcel(r"C:\Users\shelk\Desktop\新建 XLS 工作表.xls", "Sheet1").read_data()
print(testData)
rejectReason = testData[0]["发动单位（支队）"]
print(rejectReason)
now = time.time()
timenow = int(round(now * 1000))


url = 'https://suishoupai.zhongchebaolian.com:9002/suishoupai/ssp_platform/repairConfig/RejectReasonAdd'
headers = {
    "Content-Type": "application/json;charset=UTF-8",
    "Cookie": "Admin-Phone=17600352198; name=value; Admin-Token=615a7943b4624ff1b83021c43706497c"
}


for i in range(2):
    num = random.randint(100, 999)
    print(i)
    date = {
        "appId": "100100006211",
        "nonce": "2471068996874"+str(num),
        "rejectReason": testData[i]["rejectReason"],
        "status": "true",
        "supFacilityType": '100',
        "timestamp": 1629276407129,
        "token": "615a7943b4624ff1b83021c43706497c",
        "sign": "CCD9386892BEABC8CBEB7484E4B1458F"
    }
    req = requests.post(url=url, headers=headers, json=date)
    print(req.json())

