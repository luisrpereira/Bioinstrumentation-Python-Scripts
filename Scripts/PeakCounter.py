import matplotlib.pyplot as plt



graph_data = open("ondaPulso.txt", "r")
values = graph_data.read().split(', ')
del values[-1]
pulse = map(float, values)
time = range(0, len(pulse))

plt.plot(time, pulse)


up = None
down = None
npeaks = 0
for x in range(0, len(values)):
    if x >= len(values)-1:
        break
    else:
        if float(values[x]) > 530:
            up = True

        if float(values[x]) < 530:
            down = True
        if up == down:

            if(values[x]>values[x-1]):
                plt.plot(x, float(values[x]), '-ko')
                npeaks = npeaks + 1
            up = None
            down = None

print("Picos:", npeaks)


plt.show(block=True)
