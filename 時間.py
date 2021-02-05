# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 11:20:15 2021

@author: USER
"""

from mcpi.minecraft import Minecraft
from time import sleep 

mc=Minecraft.create()

while True:
    mc.executeCommand("time add 50")
    sleep(0.2)