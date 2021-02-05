# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 16:38:29 2021

@author: USER
"""

from mcpi.minecraft import Minecraft

mc=Minecraft.create()

myID = mc.getPlayerEntityId("APE_27")
mc.postToTitle(myID, "Hello")