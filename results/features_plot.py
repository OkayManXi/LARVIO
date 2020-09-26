#!/usr/bin/env python
# -*- coding:utf-8   -*-

# import re
import numpy as np
import matplotlib.pyplot as plt


def loadData(filePath):
    fr = open(filePath, 'r+')
    lines = fr.readlines()
    length = len(lines)
    # 这里可以记录一下挨个数值分别是啥意思
    ep_0 = []
    ep_1 = []
    #ep_2 = []
    for line in lines:
        items = line.split(' ')
        # print(items)
        ep_0.append(float(items[-2]))
        ep_1.append(float(items[-1]))
        #ep_2.append(float(items[-1]))
    return ep_0, ep_1, length


if __name__ == '__main__':
    ep_0, ep_1, length = loadData('/home/zty/workspace/LARVIO/results/cameraimu.txt')
    x = list(range(1, length+1))

    plt.xlabel('Time')
    plt.ylabel('Features Num')
    plt.title('Camera Imu')

    #plt.plot(x, ep_0)
    plt.plot(x, ep_1)
    #plt.plot(x, ep_2, linestyle=':')

    plt.legend(('ep_1'), loc='upper right')
    plt.savefig('/home/zty/workspace/LARVIO/results/cameraimu_features.png')
    #plt.show()