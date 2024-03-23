"""
Descrição do problema:
https://github.com/WladimirTavares/matcomp2023.1/blob/main/1/Readme.md
"""

from fractions import Fraction

#leitura das variáveis
beta, p, m, M = [int(x) for x in input().split()]

# maior número representado
maximo = Fraction()
mul = Fraction(1, beta)
base = Fraction(beta-1, beta)
for i in range(p):
    maximo += base
    base *= mul
    
maximo *= Fraction(beta**M, 1)

# menor número representado
minimo = Fraction()
mul = Fraction(1, beta)
base = Fraction(1, beta)
for i in range(-m):
    base *= mul
    
minimo = base

print("{}/{}".format(Fraction(maximo).numerator, Fraction(maximo).denominator))
print("{}/{}".format(Fraction(minimo).numerator, Fraction(minimo).denominator))
