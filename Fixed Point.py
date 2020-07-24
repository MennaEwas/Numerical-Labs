import numpy as np
import matplotlib.pyplot as plt

def g(x): 
    return np.sqrt((10 - x**3)/4)
#
#def f(x):
#    return (10 - 4*x**2)**(1/3)
#
#def l(x):
#    return (10/x**2) - 4

def fixedpoint (a, b, t, g):
    x1 = a 
    x2 = g(x1)
    while abs(x2 - x1) >= t: 
        plt.axvline(x= x2)
        x1 = x2
        x2 = g(x1)
    return x2

def plotfun(a,b,g):
    x=np.arange(a,b,0.1)
    y= g(x)
    plt.plot(x,y)
    plt.plot(x,x)
    
    
plt.figure()
s1 = fixedpoint(1, 2, 1e-5, g)
#s2 = fixedpoint(1,2, 1e-5, f)
#s3 = fixedpoint(1,2,1e-5,l)
print(s1)
#print(s2)
#print(s3)
plotfun(1,2,g)
plt.axvline(x = s1)
plt.show()