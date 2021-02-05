# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 11:33:41 2021

@author: USER
"""
from mcpi.minecraft import Minecraft
import time
import random

mc=Minecraft.create()
count=0
flower=38

while count<50:
    x,y,z=mc.player.getTilePos()
    color=random.randint(0,9)
    mc.setBlock(x,y,z,flower,color)
    time.sleep(0.1)
    count=count+1
