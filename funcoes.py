from math import *
from  decimal import Decimal

h = 6.626E-34
c = 3E8
h_ev = 4.136E-15

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

def ei(ni):
    return ni**2*h**2/(8*mp*largura**2)

def ei_ev(ni):
    return ei(ni)/1.602E-19

def ef(nf):
    return nf**2*h**2/(8*mp*largura**2)

def ef_ev(nf):
    return ef(nf)/1.602E-19

def efoton(ni, nf):
    efoton = ei_ev(ni) - ef_ev(nf)
    if efoton < 0:
        efoton = -efoton
    return efoton

print(funcOndaInicial(largura, ni))
print(funcOndaFinal(largura, nf))
print(f'Energia inicial: {Decimal(ei(ni)):.3E} J')
print(f'Energia inicial: {Decimal(ei_ev(ni)):.3E} eV')
print(f'Energia final: {Decimal(ef(nf)):.3E} J')
print(f'Energia final: {Decimal(ef_ev(nf)):.3E} eV')
print(f'Energia do foton: {Decimal(efoton(ni, nf)):.3E} eV')
