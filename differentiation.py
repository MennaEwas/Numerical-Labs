import matplotlib.pyplot as plt
from prettytable import PrettyTable

   
xl=[0,2,4,6,8,10,12,14,16,20]
yl= [8.23,9.66,10.95,12.68,14.20,15.5,16.27,18.78,22.27,24.56]
f = {}

def diff(x,h,f=f):
    xl=list(f.keys())
    if xl.index(x)==0: 
        return (-3* f[x] + 4* f[x+h] - f[x+2*h])/(2*h)

    elif (xl.index(x)-len(xl)) == -1:
        return (3* f[x] - 4* f[x-h] + f[x-2*h])/(2*h)
    else:
        return (f[x+h]-f[x-h]) / (2*h) 
    
for i in range(len(xl)):
    f[xl[i]]=yl[i] 
    
hl=[xl[1]-xl[0]]+[max([ xl[i+1]-xl[i] ,xl[i]-xl[i-1]]) for i in range(1,len(xl)-1)]+[xl[-1]-xl[-2]]
approx_f=[diff(xl[0],hl[0])]+[diff(xl[i],hl[i]) for i in range(1,len(xl)-1)]+[diff(xl[-1],hl[-1])]

methods=['forward']+['middle']*(len(xl)-2)+['backward']

t=PrettyTable()
t.add_column('h',hl)
t.add_column("X",xl)
t.add_column("Y",yl)
t.add_column('method',methods)
t.add_column("Y'",approx_f)
print(t)    

plt.figure()
plt.plot(xl,approx_f,label='Rates of growth')
plt.plot(xl,yl,label='height in inches')
plt.legend()
plt.axvline(color='b')
plt.axhline(color='b')
plt.show()



