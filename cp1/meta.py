import numpy as np
import matplotlib.pyplot as plt


temperatures = np.array(())
mag = np.array(())
sus = np.array(())
en = np.array(())
hc = np.array(())
hce = np.array(())


f = open('result.txt', 'r')



for i in f:
    if i[0]==' ':
        continue
    elif i[0]=='t':
        count = 0
        num = ''
        for j in i:
            count+=1
            if count>13:
                num+=j
        num = float(num)
        temperatures = np.append(temperatures, [num])
    elif i[0]=='M':
        count = 0
        num = ''
        for j in i:
            count+=1
            if count>15:
                num+=j
        num = float(num)
        mag = np.append(mag, [num])
    elif i[0]=='S':
        count = 0
        num = ''
        for j in i:
            count+=1
            if count>16:
                num+=j
        num = float(num)
        sus = np.append(sus, [num])
    elif i[0]=='T':
        count = 0
        num = ''
        for j in i:
            count+=1
            if count>14:
                num+=j
        num = float(num)
        en = np.append(en, [num])
    elif i[0]=='A':
        count = 0
        num = ''
        for j in i:
            count+=1
            if count>16:
                num+=j
        num = float(num)
        hc = np.append(hc, [num])
    elif i[0]=='H':
        count = 0
        num = ''
        for j in i:
            count+=1
            if count>21:
                num+=j
        num = float(num)
        hce = np.append(hce, [num])


sus = sus/float(50)
hc=hc/float(50)
hce=hce/float(50)



plt.plot(temperatures,mag)
plt.title('magnetization')
plt.show()

plt.plot(temperatures,sus)
plt.title('Susceptebility')
plt.show()

plt.plot(temperatures,en)
plt.title('Energy')
plt.show()

plt.plot(temperatures,hc)
plt.title('Heat Capacity')
plt.errorbar(temperatures,hc, yerr = hce, fmt = 'o')
plt.show()
