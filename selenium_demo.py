from selenium import webdriver
import requests
from selenium.webdriver.common.by import By
# import sys
# print(sys.executable)
import os 
print(os.environ['PATH'])
import ddddocr
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.firefox.options import Options


from datetime import datetime, timedelta


# 创建一个Chrome浏览器实例
firefox_options = Options()
firefox_options.add_argument("--headless")

gecko_path = '/usr/local/bin/geckodriver'

browser = webdriver.Firefox(executable_path=gecko_path,options=firefox_options)

test_times=0


while test_times<3:

    # 打开网页
    url_link = "https://www.baidu.com"

    browser.get(url_link)
    
    # 在这里可以进行更多操作，比如查找元素、执行搜索等
    browser.find_element(By.ID,'loginform-username').send_keys("username")
    browser.find_element(By.ID,'loginform-password').send_keys("password")

    captcha_element  = browser.find_element(By.ID,'loginform-verifycode-image')

    image_data = captcha_element.screenshot_as_png
    with open('captcha.png', 'wb') as f:
        f.write(image_data)

    ocr = ddddocr.DdddOcr()

    with open("captcha.png", 'rb') as f:
        image = f.read()

    res = ocr.classification(image)

    print(res)
    browser.find_element(By.ID,'loginform-verifycode').send_keys(res)
    browser.find_element(By.NAME,'login-button').click()
    # 等待跳转或其他条件的发生
    try:
        
        WebDriverWait(browser, 10).until(EC.presence_of_all_elements_located((By.XPATH,'//*[@id="w3-container"]/table/tbody/tr[1]/td[2]')))
        # WebDriverWait(browser, 10).until(EC.presence_of_all_elements_located((By.XPATH,'//*[@id="w1-container"]//td[@data-col-seq="1"]')))
                                         
        # WebDriverWait(browser, 10).until(EC.url_changes(browser.current_url))
        # WebDriverWait(browser, 10).until(ip_elements)
        print("页面已跳转或条件已满足")
        test_times=100
    except TimeoutException:
        print("等待超时，页面可能没有跳转或条件未满足")
        test_times = test_times + 1
    print(test_times)

    
ip_elements = browser.find_elements(By.XPATH, '//*[@id="w1-container"]//td[@data-col-seq="1"]')


# 输出结果
ip_addresses = [element.text for element in ip_elements]
print(ip_addresses)


import pytz
target_timezone = pytz.timezone('Asia/Shanghai')

# 获取当前时间
current_time = datetime.now()
localized_time = current_time.astimezone(target_timezone)


# 格式化时间
formatted_time = localized_time.strftime("%Y-%m-%d %H:%M:%S")
print(formatted_time)

if len(ip_addresses)==0:
    #不在
    log_line = formatted_time + " 0.5"
elif ip_addresses[0].split(".")[0]=="10" and (ip_addresses[0].split(".")[1]=="134" or ip_addresses[0].split(".")[1]=="192"):
    #xue
    log_line = formatted_time + " 0"
elif ip_addresses[0].split(".")[0]=="172" or (ip_addresses[0].split(".")[0]=="10" and ip_addresses[0].split(".")[1]=="29"):
    #sha
    log_line = formatted_time + " 1"
else:
    log_line = formatted_time + " 0.25"

print(log_line)

with open('temp_v2.log', 'a+') as file:
    file.write(log_line + '\n')


# 关闭浏览器窗口
browser.quit()

