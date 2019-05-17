
from  selenium import webdriver
from time import sleep

url1="https://bidplus.gem.gov.in/bidlists"
browser=webdriver.Firefox(executable_path=r"D:/mozilla selenium/geckodriver.exe")
browser.get(url1)
sleep(5)
list1=[]
list2=[]
list3=[]
list4=[]
list5=[]
list6=[]
for i in range(1,11):
    list1.append(browser.find_element_by_xpath('/html/body/section[2]/div/div/div/div[1]/div/div/div/div[2]/div/div[1]/div[{}]/div[1]/p[1]/a'.format(i)).text)
    list2.append(browser.find_element_by_xpath('/html/body/section[2]/div/div/div/div[1]/div/div/div/div[2]/div/div[1]/div[{}]/div[2]/p[1]/span'.format(i)).text)
    list3.append(browser.find_element_by_xpath('/html/body/section[2]/div/div/div/div[1]/div/div/div/div[2]/div/div[1]/div[{}]/div[2]/p[2]/span'.format(i)).text)
    list4.append(browser.find_element_by_xpath('/html/body/section[2]/div/div/div/div[1]/div/div/div/div[2]/div/div[1]/div[{}]/div[3]/p[2]'.format(i)).text)
    list5.append(browser.find_element_by_xpath('/html/body/section[2]/div/div/div/div[1]/div/div/div/div[2]/div/div[1]/div[{}]/div[4]/p[1]/span'.format(i)).text)
    list6.append(browser.find_element_by_xpath('/html/body/section[2]/div/div/div/div[1]/div/div/div/div[2]/div/div[1]/div[{}]/div[4]/p[2]/span'.format(i)).text)
browser.quit()
import pandas as pd
from collections import OrderedDict
cal=['bid no',' items','Quantity Required','Department Name And Address','Start Date/Time(Enter date and time in different columns)','End Date/Time(Enter date and time in different columns)']
col_data = OrderedDict(zip(cal,[list1,list2,list3,list4,list5,list6]))
df = pd.DataFrame(col_data) 
df.to_csv("answer2.csv")