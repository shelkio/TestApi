from selenium import webdriver
from PIL import Image
driver = webdriver.Chrome()
driver.maximize_window()
pric = ['100002107397','100004245563','1364451','100028310790','100006429059']
for i in pric:
    driver.get('https://item.jd.com/'+i+'.html')
    driver.save_screenshot(r'C:\Users\shelk\Desktop\img\price'+i+'.png')
    element = driver.find_element_by_xpath('/html/body/div[6]')
    left = element.location['x']
    top = element.location['y']
    right = element.location['x'] + element.size['width']
    bottom = element.location['y'] + element.size['height']
    im = Image.open(r'C:\Users\shelk\Desktop\img\price'+i+'.png')
    im = im.crop((left, top, right, bottom))
    im.save(r'C:\Users\shelk\Desktop\img\price_new'+i+'.png')
    print("价格为"+driver.find_element_by_class_name('price.J-p-'+i).text)