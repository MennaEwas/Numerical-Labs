#import math

def horner(x,a):
    result = 0 
    for i in range(len(a)-1, 1, -1):
        result = a[i] + (x* result)
        return result
    
    
solution = horner(3, [1,2,3,4,5])    
print(solution)