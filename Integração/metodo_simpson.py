"""
Descrição do problema:
https://github.com/WladimirTavares/matcomp2023.1/blob/main/11/Readme.md
"""
def metodo_simpson(f, a, b, n):
    h = (b - a) / n
    x = [a + i * h for i in range(n+1)]

    integral = 0
    for i in range(n):
        xi = x[i]
        xi1 = x[i+1]
        xm = (xi + xi1) / 2

        integral += h / 6 * (f(xi) + 4*f(xm) + f(xi1))

    return integral


grau = int(input())
coeficientes = [int(x) for x in input().split()]
A, B, N = [int(x) for x in input().split()]

f = lambda x: sum(coeficientes[i] * x**(grau-i) for i in range(grau+1))

resultado = metodo_simpson(f, A, B, N)

print('{:.5f}'.format(resultado))



