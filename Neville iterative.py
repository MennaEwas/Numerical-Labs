import numpy as np
#from prettytable import PrettyTable

def nev(a, x, m, n):
    if n == 0:
        #base
        return a[m][1]
    
    else:
        #recursive formula
        answer = (nev(a, x, m, n - 1) * (x - a[m - n][0]) - nev(a, x, m - 1, n - 1) * (x - a[m][0])) / (a[m][0] - a[m - n][0])
        a[m][n + 1] = answer
        return answer

u = [1.0, 1.3, 1.6, 1.9, 2.2]
y = [0.7651977, 0.6200860, 0.4554022, 0.2818186, 0.1103623]
l = len(u)

solution = np.zeros((len(u), len(u) + 1))
for i in range(l):
    solution[i][0] = u[i]
    solution[i][1] = y[i]
        
nev(solution, 1.5, len(u) - 1, len(u) - 1)
solution2 = (solution[len(u) - 1][len(u)]) 
print("Final Solution =  ", solution2)
print(solution)

'''   
# you need to install prettytable first     
t= PrettyTable()
t.header = False
for i in range(l):
    t.add_row(solution[i])
    
print(t)
'''