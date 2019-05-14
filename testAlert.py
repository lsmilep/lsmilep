#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time      :2019/1/15 23:44
# @Auth      :Administrator
# @Site      :
# @File      :testAlert.py
# @SoftWare  :PyCharm Community Edition

from selenium import webdriver
import time



driver=webdriver.Firefox()
driver.get('http://sahitest.com/demo/alertTest.htm')

time.sleep(5)

print "max"
driver.maximize_window()
time.sleep(5)
print "find'b1'"
driver.find_element_by_name('b1').click()
time.sleep(5)

print "switch"
alert=driver.switch_to_alert()
time.sleep(5)

print "text"

print alert.text
time.sleep(5)

print "accept"
alert.accept()
time.sleep(5)
driver.quit()