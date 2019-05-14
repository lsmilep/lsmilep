#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time      :2019/4/24 23:32
# @Auth      :Administrator
# @Site      :
# @File      :test.py
# @SoftWare  :PyCharm Community Edition


#!/usr/bin/python
import json

data = [ { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 } ,{'f':8,'g':9,'h':10}]

json = json.dumps(data, sort_keys=True, indent=2, separators=(',', ': '))
print json

class test():
    def __init__(self):
        print 'in __init__'
        pass

    def testo(self):
        print 'test'

    def __del__(self):
        print 'in __del__'
        pass


class test1():
    def testo(self):
        print "testo"

if __name__ ==  "__main__":
    # # testClass = test()
    # # testClass.test()
    # testClass = test1()
    # testClass.testo()

    def create_a_list(x, y=2, z=3):  # 默认参数项必须放后面
        return [x, y, z]


    b = create_a_list(1)  # [1, 2, 3]
    c = create_a_list(3,z=3)  # [3, 2, 3]
    d = create_a_list(6, 7, 8)  # [6, 7, 8]
    e = "hello"

    print b,c,d,e
