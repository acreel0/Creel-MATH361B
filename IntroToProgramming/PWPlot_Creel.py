import numpy as np
import matplotlib.pyplot as plt

# Input variables
N = 1000

def my_func(x):
    if(x<-2):
        return -3*(x+2)**2 + 1
    elif(x<-1):
        return 1
    elif(x<=1):
        return (x-1)**3 + 3
    elif(x<2):
        return np.sin(np.pi*x) + 3
    else:
        return 3*np.sqrt(x-2) + 4

x = np.linspace(-3,3,N)
y = [0]*N # or y = np.zeros(N)

for ii in range(len(x)):
    y[ii] = my_func(x[ii])

plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('f(x)')

plt.show()