from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import re

url = 'https://map.naver.com/v5/directions/-/-/-/transit?c=14149145.9847601,4484498.0384065,15,0,0,0,dh'

options = webdriver.ChromeOptions()
options.add_argument('window-size=1920,1080')
driver = webdriver.Chrome('chromedriver', options=options)
driver.get(url)
time.sleep(2)

start_place = input('출발지 입력 : ')
finish_place = input('도착지 입력 : ')

driver.find_element_by_xpath('//*[@id="directionStart0"]').send_keys(start_place)
time.sleep(2)
driver.find_element_by_xpath('//*[@id="directionStart0"]').send_keys(Keys.ENTER)
time.sleep(2)
driver.find_element_by_xpath('//*[@id="directionGoal1"]').send_keys(finish_place)
time.sleep(2)
driver.find_element_by_xpath('//*[@id="directionGoal1"]').send_keys(Keys.ENTER)
time.sleep(2)
driver.find_element_by_xpath('//*[@id="container"]/shrinkable-layout/div/directions-layout/'
'directions-result/div[1]/div/directions-search/div[2]/button[2]').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="container"]/shrinkable-layout/div/directions-layout/'
'directions-result/div[1]/directions-summary-list/directions-summary-list-tab/div/ul/li[2]/button').click()
time.sleep(2)
data_len = driver.find_element_by_xpath('//*[@id="container"]/shrinkable-layout/'
'div/directions-layout/directions-result/div[1]/directions-summary-list/directions-summary-list-tab/div/ul/li[2]/button')
string = data_len.text
num = re.findall(r'\d+', string)

for i in range(1, int(num[0]) + 1):
    data_time = driver.find_element_by_xpath('//*[@id="container"]/shrinkable-layout/div/directions-layout/'
    'directions-result/div[1]/directions-summary-list/'
    'directions-hover-scroll/div/ul/li[{}]/directions-summary-item-pubtransit/div[2]/ol/li[1]/div[2]/div[2]'.format(i))

    data_bus_num = driver.find_element_by_xpath('//*[@id="container"]/shrinkable-layout/div/directions-layout/'
    'directions-result/div[1]/directions-summary-list/'
    'directions-hover-scroll/div/ul/li[{}]/directions-summary-item-pubtransit/div[2]/ol/li[1]/div[1]/div[2]/em'.format(i))
    print('{}번 버스\n{}\n----------------------'.format(data_bus_num.text, data_time.text))