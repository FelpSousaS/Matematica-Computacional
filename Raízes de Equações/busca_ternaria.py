"""
Descrição do problema:
https://github.com/WladimirTavares/matcomp2023.1/blob/main/8/Readme.md
"""

import math

def f(n, a, x):
    ret = 0
    for i in range(n+1):
        ret = ret * x + a[i]
    return ret


def ternary_search(n, a, l, h, tol):
    iteracao = 1
    while True:
        if abs(h - l) < tol:
            return l, h, iteracao
        
        m1 = l + (h - l) / 3
        m2 = l + 2 * (h - l) / 3
        
        if f(n, a, l) * f(n, a, m1) < 0:
            h = m1
        
        elif f(n, a, m1) * f(n, a, m2) < 0:
            l = m1
            h = m2
        
        else:
            l = m2
        
        
        iteracao += 1


if __name__ == "__main__":
    n = int(input())
    a = [float(x) for x in input().split()]
    l, h = [float(x) for x in input().split()]
    tol = float(input())

    solution_l, solution_h, iterations = ternary_search(n, a, l, h, tol)
    solution_l = round(solution_l, 10)
    solution_h = round(solution_h, 10)
    
    print("busca ternaria realizou", iterations, "iteracoes")
    print("a solucao está no intervalo [{:.10f},{:.10f}]".format(solution_l, solution_h))