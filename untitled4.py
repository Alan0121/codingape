# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 15:37:45 2021

@author: USER
"""

from mcpi.minecraft import Minecraft
import time
import random

mc=Minecraft.create()

x,y,z=mc.player.getTilePos 
while True 

  color=random.randrange(0,16)
  mc.setBlocks(x-5,y-1,z-5,x+5,y-1,z+5,95,color)
  time.sleep(0.5)

