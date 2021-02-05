# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 11:15:12 2021

@author: USER
"""

from mcpi.minecraft import Minecraft
import time
import random

mc=Minecraft.create()
x,y,z=mc.player.getTilePos()

flower=38

while True:
    
    mc.setBlock(x,y,z,57)
    
