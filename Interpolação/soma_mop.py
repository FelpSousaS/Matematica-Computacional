"""
Descrição do problema:
https://github.com/WladimirTavares/matcomp2023.1/blob/main/12/Readme.md
"""

import numpy as np

def f(coeficientes, n):
    D = len(coeficientes) - 1
    return sum(coeficientes[i] * n**(D-i) for i in range(D+1))

def calcular_soma_mop(D, coeficientes):
    soma = 0
    for i in range(1, D+1):
        a = np.zeros((i, i), float)
        b = np.zeros(i, float)
        for j in range(i):
            for k in range(i):
                a[j][k] = (1+j) ** k
            b[j] = f(coeficientes, 1+j)
        poly = np.linalg.solve(a, b)
        for j in range(1, 15):
            op = sum(int(poly[m]-0.5 + (poly[m] > 0)) * j ** m for m in range(i))
            if abs(op - f(coeficientes, j)) > 1e-7:
                soma += op
                break
    return int(soma)

D = int(input())
coeficientes = [int(x) for x in input().split()]
soma_mop = calcular_soma_mop(D, coeficientes)
print(soma_mop) 


