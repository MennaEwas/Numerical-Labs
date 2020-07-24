def f(y):
    return y** 5 - 11 * y** 4 + 46 * y** 3 - 90 * y ** 2 + 81 * y - 27

def df(y):
    return 5 * y ** 4 - 11 * 4 * y ** 3 + 46 * 3 * y ** 2 - 90 * 2 * y + 81

def df2(y):
    return 5 * 4 * y ** 3 - 11 * 4 * 3 * y ** 2 + 46 * 3 * 2 * y - 90 * 2


def newton(f, df1 , df2 , p_old, tol):
    history = {}
    iterations = 0
    p_new = p_old - (f(p_old)* df1(p_old) / ((df1(p_old))**2 - f(p_old)*df2(p_old) ))
        
    while abs(p_new - p_old) > tol: 
            p_old = p_new
            p_new =  p_old -  (f(p_old)* df1(p_old) / ((df1(p_old))**2 - f(p_old)*df2(p_old) ))      
            iterations += 1
            history[iterations] = {
                'old': p_old,
                'new': p_new,
                'err': abs(p_new - p_old)}
    return p_new, history, iterations

def printTable(x):
    header = '{:6s}{:12s}{:12s}{:12s}'.format('itr','P[n-1]','P[n]',
              'abs(P[n-1]-P[n])')
    print('='*len(header) + '\n' + header + '\n' + '='*len(header))
    for i in x:
        print('{:<6d}{:<12.8f}{:<12.8f}{:<12.8f}'.format(i,
              x[i]['old'],
              x[i]['new'],
              x[i]['err']))


solution = newton(f,df,df2, 0.5, 1e-10)
print(printTable(solution[1]))
print('number of iteration = ', solution[2])


