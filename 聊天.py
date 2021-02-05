# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 15:09:35 2021

@author: USER
"""

from mcpi.minecraft import Minecraft
import time
import random

mc=Minecraft.create()

x,y,z = mc.player.getTilePos()

try:
    blockType = int(input("請輸入想放的方塊ID:"))
    mc.setBlock(x,y,z,blockType)
except:
    print("只能輸入數字!")
    
