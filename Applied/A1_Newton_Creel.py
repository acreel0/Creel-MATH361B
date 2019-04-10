import numpy as np
import math as m

# input variables
N = 100
TOL= 1e-4
z0=1.4

# define the functions

# part 1:
# f = lambda x: 1/100 * ( x**4 + (np.exp(1)-2-np.sqrt(2))*x**3 + (2*np.sqrt(2)-np.sqrt(2)*np.exp(1)-3-2*np.exp(1))*x**2 + (2*np.sqrt(2)*np.exp(1)+3*np.sqrt(2)-3*np.exp(1))*x + 3*np.sqrt(2)*np.exp(1) )
# fprime = lambda x: 1/100 * ( 4*x**3 + 3*(np.exp(1)-2-np.sqrt(2))*x**2 + 2*(2*np.sqrt(2)-np.sqrt(2)*np.exp(1)-3-2*np.exp(1))*x + (2*np.sqrt(2)*np.exp(1)+3*np.sqrt(2)-3*np.exp(1)))

# part 2:
f = lambda x: m.tan(x) - x - 2
fprime = lambda x: (1/m.cos(x))**2 - 1

# create the array and add z0 to the array
appx = np.zeros([0,2])
appx = np.vstack([appx, np.array([z0, 0])])

# implement Newton's method
while np.size(appx,1) < N-1:
    zn = z0 - f(z0)/fprime(z0)
    diff = abs(zn-z0)
    appx = np.vstack([appx, np.array([zn, diff])])
    if diff < TOL:
        print('Iterations have stopped due to reaching tolerance.')
        break
    z0 = zn

if np.size(appx,1) == N:
    print('Iterations have stopped due to reaching the max number of iterations.')

print('The iterations and difference between consecutive iterations are:')
print(appx)
