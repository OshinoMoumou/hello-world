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

sim_num = 5000

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
        if False:
            if inspectaser % 100 == 0:
                print(inspectaser)
        num_939 = 2
        num_113 = 6
        for i in range(0, dk - 1):
            grave = num_939 + num_113
            position = seven_random(grave)
            for n in position:
                if n < num_939:
                    num_939 = num_939 + 1
                    num_113 = num_113 + 3
                else:
                    num_113 = num_113 + 1
        grave = num_939 + num_113
        revive = sum(np.array(seven_random(grave)) < num_939)
        lp[revive] = lp[revive] + 1
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
    if False:#计算第n个dk的结果
        for dk in [1, 2, 3, 5, 10, 100, 1000]:
            draw(1000)
    if True:#计算各个DK数量的全针概率
        quanzhen = []
        X = []
        for dk in range(1,100):
            print(dk)
            quanzhen.append(simulate(dk)[0])
            X.append(dk)
        fig = plt.figure()
        plt.plot(X,quanzhen)
        plt.xlabel("Number of DK")
        plt.ylabel("Probability")
        plt.title("Distribution of All 113")
        #for a,b in zip(X,quanzhen):  
        #    plt.text(a, b, '%.3f' % b, ha='center', va= 'bottom',fontsize=11)
        plt.savefig("distribution%d.jpg"%dk)
        
