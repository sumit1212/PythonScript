from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import xlwt

wb = xlwt.Workbook()
ws = wb.add_sheet('Sheet1')

ws.write(0,0,'Insure')
ws.write(0,1,'Cashless')
ws.write(0,2,'IDV') 
ws.write(0,3,'Zero Depreciation Addon')
ws.write(0,4,'Premium') 

# Specifying incognito mode as you launch your option[OPTIONAL]
option = webdriver.Firefox()
#option.add_argument("--incognito")

# Go to desired website
option.get("http://ci.policybazaar.com/#/quotes?enquiryId=NTk3NzAyNjI=&leadid=MTYzMjMxMzk%3D&frame=true&flag=true&ref=p&_k=qgn178")

row = 1
name = option.find_elements_by_class_name('quote-tile')
flag = 0
#print(name)
for i in name:
    #print(i)
    img = (i.find_elements_by_tag_name('img'))
    insure = img[0].get_attribute('src')
    #print(insure)
    ws.write(row,0,insure)
    #inn = (i.find_elements_by_class_name('inner'))
    #print(inn)
    buy = (i.find_elements_by_class_name('buy-plan'))
    #print(buy)
   #if (flag % 2 == 0): 
    sp = (buy[0].find_elements_by_tag_name('span'))

    #print(sp[0].text)

    #flag +=1
    ws.write(row,4,sp[0].text) 
    row+=1

'''
row =1
name = option.find_elements_by_class_name('img_logo')
for i in name:
    img = (i.find_elements_by_tag_name('img'))
    insure = img[0].get_attribute('src')
    print(insure)
    ws.write(row,0,insure)
    row+=1

name = option.find_elements_by_class_name('inner')
for i in name:
    print(i.text)

row =1
flag = 1
name = option.find_elements_by_class_name('buy-plan')
for i in name:
    flag +=1
    if (flag % 2 == 0): 
        sp = (i.find_elements_by_tag_name('span'))
        sp = (sp[0].text)
        print(sp)
        ws.write(row,4,sp)   
        row+=1
'''


wb.save('examp2.xls') 