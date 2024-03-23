"""
Descrição do problema:
https://github.com/WladimirTavares/matcomp2023.1/blob/main/7/Readme.md
"""

def f(c, v, t, m):
    return (9.8 * m / c) * (1 - pow(2.71828, (-c * t / m))) - v
    
    
def bissection_method(c, v , t):
    a = 50 
    b = 100
    n = 0.001
    
    while abs(b-a) > n:
        x = (a + b) / 2.0
        fm = f(c, v, t, x)
        
        if fm == 0:
            break
        if (fm * f(c, v, t, a)) < 0:
            b = x
        else:
            a = x
            
    return round(x, 2)
    
    
c, v , t = [float(x) for x in input().split()]

resultado = bissection_method(c, v, t)

print("{:.2f}".format(resultado))