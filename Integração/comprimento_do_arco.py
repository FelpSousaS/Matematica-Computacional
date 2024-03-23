"""
Descrição do problema:
https://github.com/WladimirTavares/matcomp2023.1/blob/main/13/Readme.md
"""

import math

def f(x, coeficientes):
    n = len(coeficientes)
    return sum(coeficientes[i] * x ** (n - i - 1) for i in range(n))

def calcular_tamanho_curva(n, coeficientes, a, b):
    dx = (b - a) / n
    tamanho = 0
    for i in range(n):
        x = a + i * dx
        w = a + (i + 1) * dx
        y = f(x, coeficientes)
        z = f(w, coeficientes)
        delta_x = w - x
        delta_y = z - y
        tam_segmento = math.sqrt(delta_x ** 2 + delta_y ** 2)
        tamanho += tam_segmento
    return tamanho

def calcular_comprimento_curva(n, coeficientes, a, b):
    if n < 1:
        return 0.0

    tamanho_anterior = calcular_tamanho_curva(1, coeficientes, a, b)
    tamanho_atual = 0.0
    iteracoes = 1

    while abs(tamanho_atual - tamanho_anterior) >= 0.000001:
        tamanho_anterior = tamanho_atual
        n *= 2
        tamanho_atual = calcular_tamanho_curva(n, coeficientes, a, b)
        iteracoes += 1

    return tamanho_atual

n = int(input())
coeficientes = [int(x) for x in input().split()]
a, b = [int(x) for x in input().split()]

comprimento = calcular_comprimento_curva(n, coeficientes, a, b)

print('{:.5f}'.format(comprimento))
