import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft

def loadData(filePath):
    fr = open(filePath, 'r+')
    lines = fr.readlines()
    length = len(lines)
    print(length)
    # 这里可以记录一下挨个数值分别是啥意思
    ep_0 = []
    ep_1 = []
    ep_2 = []
    ep_3 = []
    for line in lines:
        items = line.split(' ')
        # print(items)
        ep_0.append(float(items[-4]))#timestamp
        ep_1.append(float(items[-3]))# x
        ep_2.append(float(items[-2]))# y
        ep_3.append(float(items[-1]))# z
    return ep_0, ep_1, ep_2,ep_3, length

if __name__ == '__main__':
    ep_0, ep_1, ep_2, ep_3, length = loadData('/home/zty/workspace/LARVIO/results/imu.txt')
    x = ep_0
    length=length-1
    outx=np.abs(np.fft.rfft(ep_1))/length #fft变换后的振幅x
    outy=np.abs(np.fft.rfft(ep_2))/length
    outz=np.abs(np.fft.rfft(ep_3))/length
    #f=n*fs/N           #频率序列
    #print(t.shape)
    #freqs = np.linspace(0, 95631, 95631+1)
    freqs = np.linspace(0, int(length/2), int(length/2)+2)
    plt.figure(figsize=(10, 3))
    plt.subplot(131)
    plt.plot(freqs, outx)
    plt.subplot(132)
    plt.plot(freqs,outy)
    plt.subplot(133)
    plt.plot(freqs,outz)

    plt.savefig('/home/zty/workspace/LARVIO/results/imufft.png')