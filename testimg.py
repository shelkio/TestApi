import threading

from selenium import webdriver
from PIL import Image

pric = ['100002107397','100004245563','1364451']
pric2 = ['100028310790','100006429059']
def test1():
    driver = webdriver.Chrome()
    driver.maximize_window()
    for i in pric:
        driver.get('https://item.jd.com/'+i+'.html')
        element = driver.find_element_by_class_name('product-intro.clearfix')
        element.screenshot(r'C:\Users\shelkio\Desktop\img\price'+i+'.png')
        print("价格为"+driver.find_element_by_class_name('price.J-p-'+i).text)
def test2():
    driver = webdriver.Chrome()
    driver.maximize_window()
    for i in pric2:
        driver.get('https://item.jd.com/'+i+'.html')
        element = driver.find_element_by_class_name('product-intro.clearfix')
        element.screenshot(r'C:\Users\shelkio\Desktop\img\price' + i + '.png')
        print("价格为"+driver.find_element_by_class_name('price.J-p-'+i).text)

threading.Thread(target=test1).start()
threading.Thread(target=test2).start()