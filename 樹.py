# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 13:54:08 2021

@author: USER
"""
from mcpi.minecraft import Minecraft
import time

mc=Minecraft.create()

x,y,z = mc.player.getTilePos()


def planttree(x,y,z):
    mc.setBlocks(x,y,z,x,y+3,z,17)
    mc.setBlocks(x-1,y+4,z-1,x+1,y+6,z+1,161)

for i in  range(0,50,5):
    for j in range(0, 50, 5):
        planttree(x+i, y, z+j)