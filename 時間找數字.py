# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 15:25:17 2021

@author: USER
"""

from random import randrange
from time import time
def linearSearch():
    sTime = time()
    for i in range(1,10000001):
        if i ==number:
            print("找到答案了!是" + str(i))
            print("線性搜尋法:花了" + str(time()-sTime) + "秒")
            break
        
number = randrange(1,10000001)
linearSearch()
        