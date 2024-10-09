from math import *
from  decimal import Decimal

me = 9.11E-31
mp = 1.67E-27
largura = float(input("Entre com a largura: "))
ni = float(input("Entre com ni: "))
nf = float(input("Entre com nf: "))
a = float(input("Entre com a: "))
b = float(input("Entre com b: "))

def funcOndaInicial(largura, ni):
    return f'Funcao de onda do nivel inicial: {Decimal(sqrt(2/largura)):.3E} . sen({Decimal(ni*pi/largura):.3E} . x)'

def funcOndaFinal(largura, nf): 
    return f'Funcao de onda do nivel final: {Decimal(sqrt(2/largura)):.3E} . sen({Decimal(nf*pi/largura):.3E} . x)'

#print(f'Funcao de onda do nivel inicial: {Decimal(sqrt(2/largura)):.3E} . sen({Decimal(ni*pi/largura):.3E} . x)')
#print(f'Funcao de onda do nivel final: {Decimal(sqrt(2/largura)):.3E} . sen({nf*pi/largura} . x)')

print(funcOndaInicial(largura, ni))
print(funcOndaFinal(largura, nf))
