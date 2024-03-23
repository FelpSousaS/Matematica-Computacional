"""
Descrição do problema:
https://github.com/WladimirTavares/matcomp2023.1/blob/main/9/Readme.md
"""

# tabela com os dados
table = {
    25: {50: 2500, 60: 2850, 70: 3200, 80: 3550},
    45: {50: 2350, 60: 2700, 70: 3000, 80: 3350},
    65: {50: 1900, 60: 2250, 70: 2750, 80: 2850}
}

def interpolacao(x, x_values, y_values):
    n = len(x_values)
    resultado = 0.0
    for i in range(n):
        numerador = 1.0
        denominador = 1.0
        for j in range(n):
            if j != i:
                numerador *= (x - x_values[j])
                denominador *= (x_values[i] - x_values[j])
        resultado += y_values[i] * (numerador / denominador)
    return resultado

N, M = [int(x) for x in input().split()]

x_values = [25, 45, 65]
y_values = [[table[x][y] for y in [50, 60, 70, 80]] for x in x_values]

calorias = interpolacao(N, x_values, [interpolacao(M, [50, 60, 70], y) for y in y_values])

print('{:.5f}'.format(calorias))
