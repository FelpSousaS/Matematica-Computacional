"""
Descrição do problema:
https://github.com/WladimirTavares/matcomp2023.1/blob/main/6/Readme.md
"""

def f(ca, cb, cc, x):
    return (cc + x) / ((ca - 2*x)**2 * (cb - x))

def bissection_method(K, ca, cb, cc, xl, xu, epsilon):
    n = epsilon  # Determinando o número de casas decimais
    a = xl
    b = xu

    while abs(b - a) > 0.5 * 10**(-n):
        c = (a + b) / 2.0
        fc = f(ca, cb, cc, c)
        

        if fc > K:
            b = c
        else:
            a = c
            
     
    return c

def truncate(f, n):
    '''Truncates/pads a float f to n decimal places without rounding'''
    s = '%.12f' % f
    i, p, d = s.partition('.')
    return '.'.join([i, (d+'0'*n)[:n]])


K, ca, cb, cc, xl, xu, epsilon = [float(x) for x in input().split()]


resultado = bissection_method(K, ca, cb, cc, xl, xu, int(epsilon))


print(truncate(resultado, int(epsilon)))
