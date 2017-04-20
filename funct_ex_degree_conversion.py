import matplotlib.pyplot as plot

temp = int(input("What's the temperature in Celcius?: "))

def f(x):
    return temp * 1.8 + 32

xs = [temp]
ys = []
for x in xs:
    ys.append(f(x))

plot.bar(xs, ys)
plot.show()
