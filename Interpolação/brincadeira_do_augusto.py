"""
Descrição do problema:
https://github.com/WladimirTavares/matcomp2023.1/blob/main/10/Readme.md
"""

#Recursivo
def menor_grau(tam, seq):
    grau = 0
    if len(set(seq)) == 1:
        return grau
    nova_seq = [seq[i+1] - seq[i] for i in range(tam-1)]
    grau = 1 + menor_grau(tam-1, nova_seq)
    return grau

tamanho = int(input())
seq = [int(x) for x in input().split()]
print(menor_grau(tamanho,seq))

"""
Iterativo

def menor_grau(tamanho, seq):
    grau = 0
    while len(set(seq)) != 1:
        nova_seq = [seq[i+1] - seq[i] for i in range(tamanho-1)]
        seq = nova_seq
        tamanho = tamanho - 1
        grau = grau + 1
    return grau

tamanho = int(input())
seq = [int(x) for x in input().split()]
print(menor_grau(tamanho, seq))

"""