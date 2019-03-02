import numpy as np

N = 400
x = np.zeros([0,4])

for aa in range(1,N):
    
    for bb in range (aa,N):
        c = aa**2 + bb**2
        cc = np.sqrt(c)
        s = aa + bb + cc
        
        if (cc.is_integer()==True):
            x = np.vstack([x, np.array([aa,bb,cc,s])])
        
        if (s==1026):
            triple = [aa,bb,cc]
            print("The pythagorean triple whose sum is 1026 is", triple)
