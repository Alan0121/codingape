# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 10:46:38 2021

@author: USER
"""

from mcpi.minecraft import Minecraft
import time
import random

mc=Minecraft.create()

x,y,z=mc.player.getTilePos()

l=10
w=10
h=20
block=4
air=0
mc.setBlocks(x,y,z,x+w,y+h,z+l,block)
mc.setBlocks(x+1,y+1,z+1,x+w-1,y+h-1,z+l-1,air)