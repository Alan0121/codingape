# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 10:22:57 2021

@author: USER
"""

from mcpi.minecraft import Minecraft
import time
import random

mc=Minecraft.create()

while True:
    x,y,z = mc.player.getPos()
    x = x + random.uniform(-20, 20)
    z = z + random.uniform(-20, 20)
    y = y + 