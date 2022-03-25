import random
import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://bjjj.zhongchebaolian.com/cgsadm/')
time.sleep(1)
driver.find_element_by_id('username').send_keys('17600352198')
driver.find_element_by_id('password').send_keys('a12345678')
time.sleep(5)
driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[1]/div/ul/div[8]/li/div').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[1]/div/ul/div[8]/li/ul/div/a/li').click()
time.sleep(3)
i=0

while True:
    i=i+1
    tt = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[4]/div[3]/table/tbody/tr['+str(i)+']').text
    print(i)
    if 'FQ20220128000030' in tt:
        print("找到了")

        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[4]/div[4]/div[2]/table/tbody/tr['+str(i)+']/td[18]/div/button').click()
        break

