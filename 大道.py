# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 11:44:53 2021

@author: USER
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()

x,y,z = mc.player.getTilePos()

for i in range(20):
    mc.setBlock(x,y-1,z+i,1)