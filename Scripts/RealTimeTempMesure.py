import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import math
import numpy as np

style.use('fivethirtyeight')

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

file = open( 'outputTemperatura.txt', 'w+')

def animate(i):
    dados = open('output.txt','r').read()
    valores = dados.split('\n')
    xs = []
    ys = []
    vo_graph = []
    b = 3932
    r0 = 10000
    t0 = 298.15

    #R infinito
    rinf = float(r0) * (float(math.exp(float(-b) / float(t0))))

    del valores[-1]

    x = 0
    for val in valores:
        x=x+1

        #Valores Bitalino para volt
        v0 = (((float(val) / float(1023)) - 0.5) * 3.3) / 10.09

        #Valores termistor
        R3 = (float(-16500) - float(20000 * v0)) / (float(2 * v0) - 1.65)

        #Calculo Temperatura
        t = (b / (np.log(R3 / rinf))) - 273.15
        print(t)

        t.tofile(file, sep='\n', format='%f')
        file.write("\n")

        xs.append(float(x))
        ys.append(float(t))


    ax1.clear()
    ax1.set_ylim(15, 40)
    ax1.plot(xs, ys)


ani = animation.FuncAnimation(fig, animate, interval=1000)

plt.show()



