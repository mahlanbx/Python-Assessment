# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import random

import numpy

First_cluster = []
for i in range(16):
    First_clusterNumber = random.random()
    First_cluster.append(First_clusterNumber)
    
print(First_cluster)

import time
print(input('Enter data Reference to Generate new data file: '))
DateStamp=time.strftime("%Y-%b-%d__%H_%M_%S",time.localtime())
sensors = open('pipeline'+DateStamp+'.log','w')

randomList = [0,32]

i = 32
print("Random float numbers")






    
