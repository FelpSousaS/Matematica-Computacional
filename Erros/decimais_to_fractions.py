"""
Descrição do problema:
https://github.com/WladimirTavares/matcomp2023.1/blob/main/3/Readme.md
"""

from fractions import Fraction

def decimal_to_binario(base, p, num):
    is_negative = False
    digitos = []
    
    for _ in range(p):
        num *= base
        if num >= 1:
            digitos.append("1")
            num -= 1
        else:
            digitos.append("0")

    cont = 0
    while digitos[0] == "0":
        digitos.pop(0)
        cont += 1
        if len(digitos) == 0:
            if num * base >= 0:
                is_negative = True
            break

    for _ in range(cont):
        num *= base
        if num >= 1:
            digitos.append("1")
            num -= 1
        else:
            digitos.append("0")

    binario = "0."
    for d in digitos:
        binario += d

    return binario, cont * -1, is_negative


def binario_to_frac(binario, p, b, exp):
    fracs = []
    aux = 1

    for x in binario[2:]:
        if x == '1':
            fracs.append(Fraction(1, int(pow(b, aux) * pow(b, exp * (-1)))))
        aux += 1

    return fracs

def resultado(exp):
    if exp < m:
        print('underflow')
    elif exp > M:
        print('overflow')
    else:
        print(frac)
        print(Fraction(str(num)) - frac)


num = float(input())
b, p, m, M = [int(x) for x in input().split()]

binario = decimal_to_binario(b, p, num)
exp = binario[1]
is_negative = binario[2]
fracs = binario_to_frac(binario[0], p, b, exp)
frac = sum(fracs)

if is_negative:
    exp -= 1

resultado(exp)

