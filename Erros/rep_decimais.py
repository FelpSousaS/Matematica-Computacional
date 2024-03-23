"""
Descrição do problema:
https://github.com/WladimirTavares/matcomp2023.1/blob/main/2/Readme.md
"""

def convert_decimal_to_float(decimal, beta, p, m, M):
    resultado = ""
    
    if decimal < 0:
        resultado += "-"
    
    decimal = abs(decimal)
    
    parte_inteira = int(decimal)
    resultado += str(parte_inteira)
    
    parte_frac = decimal - parte_inteira

    
    
    if p > 0:
        resultado += "."
        
        while parte_frac > 0 and len(resultado) - resultado.index('.') - 1 < p:
            parte_frac *= beta
            digito = int(parte_frac)
            resultado += str(digito)
            parte_frac -= digito
    
    exp = 0
    
    if parte_inteira > 0:
        exp = len(str(parte_inteira)) - 1
    
    exp = max(m, exp)
    exp = min(M, exp)
    
    # Remove os dígitos 0 iniciais e calcula mais dígitos finais de acordo com a quantidade de zeros removidos
    if '.' in resultado:
        digits = resultado[resultado.index('.') + 1:]
        zeros_removed = 0
        
        for digito in digits:
            if digito == '0':
                zeros_removed += 1
            else:
                break
            
        
        expt = zeros_removed    
        
        if zeros_removed > 0:
            resultado = resultado[:resultado.index('.') + 1] + digits[zeros_removed:]
            
            while zeros_removed > 0 and len(resultado) - resultado.index('.') - 1 < p:
                parte_frac *= beta
                digito = int(parte_frac)
                resultado += str(digito)
                parte_frac -= digito
                zeros_removed -= 1
    
    # Imprime o contador de dígitos iniciais 0 removidos
    if expt > 0:
        resultado += " -" + str(expt)
    
    return resultado, exp

x = float(input())
beta, p, m, M = [int(x) for x in input().split()]

float_num, exp = convert_decimal_to_float(x, beta, p, m, M)

print(float_num)




