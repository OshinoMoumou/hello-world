#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 20:29:28 2019

@author: jacob.caulfield
"""

import random
import numpy as np
import matplotlib.pyplot as plt
import math

ordinal = lambda n: "%d%s" % (n,"tsnrhtdd"[(math.floor(n/10)%10!=1)*(n%10<4)*n%10::4])

sim_num = 50000

def seven_random(n):
    num = 0
    a = []
    while num < 7:
        while True:
            r = random.randrange(n)
            if not r in a:
                a.append(r)
                break
        num = num + 1
    return a

def simulate(dk):
    lp = [0, 0, 0, 0, 0, 0, 0, 0]
    for inspectaser in range(0, sim_num):
        a = [0,0,0,1,0,0,0,1]
        for i in range(0, dk):
            grave = len(a)
            position = seven_random(grave)
            for n in position:
                a.append(a[n])
        lanpang = sum(a[(len(a) - 7):(len(a))])
        lp[lanpang] = lp[lanpang] + 1
    return np.array(lp) / sim_num

def draw(dk):
    Y = simulate(dk)
    X = [0, 1, 2, 3, 4, 5, 6, 7]
    fig = plt.figure()
    plt.bar(X,Y,0.9,color="black")
    plt.xlabel("Number of 939")
    plt.ylabel("Probability")
    plt.title("%s DK"%ordinal(dk))
    for a,b in zip(X,Y):  
        plt.text(a, b, '%.3f' % b, ha='center', va= 'bottom',fontsize=11)
    plt.savefig("quanzhen%d.jpg"%dk)

if __name__ == '__main__':
    for dk in [1, 2, 3, 5, 10, 100, 1000]:
        draw(dk)