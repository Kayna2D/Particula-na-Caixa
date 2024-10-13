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

def en(n, m, largura):
    return n**2*h**2/(8*m*largura**2)

def en_ev(n, m, largura):
    return en(n, m, largura)/1.602E-19

def efoton(ni, nf, m, largura):
    efoton = en_ev(ni, m, largura) - en_ev(nf, m, largura)
    if efoton < 0:
        efoton = -efoton
    return efoton

def comprimento(efoton):  
    return h*c/efoton/1.602E-19  

def frequencia(efoton):
    return efoton/h*1.602E-19

def velocidade(n, m, largura):
    return sqrt(2*en(n, m, largura)/m)


def deBroglie(m, v):
    return h/(m*v)

print(funcOndaInicial(largura, ni))
print(funcOndaFinal(largura, nf))
print(f'Energia inicial: {Decimal(en(ni, mp, largura)):.3E} J')
print(f'Energia inicial: {Decimal(en_ev(ni, mp, largura)):.3E} eV')
print(f'Energia final: {Decimal(en(nf, mp, largura)):.3E} J')
print(f'Energia final: {Decimal(en_ev(nf, mp, largura)):.3E} eV')
print(f'Energia do foton: {Decimal(efoton(ni, nf, mp, largura)):.3E} eV')
print(f'Comprimento do foton: {Decimal(comprimento(efoton(ni, nf, mp, largura))):.3E} m')
print(f'Frequencia do foton: {Decimal(frequencia(efoton(ni, nf, mp, largura))):.3E} Hz')
print(f'Velocidade inicial: {Decimal(velocidade(ni, mp, largura)):.3E} m/s')
print(f'Velocidade final: {Decimal(velocidade(nf, mp, largura)):.3E} m/s')
print(f'Comprimento  de onda de De Broglie inicial: {Decimal(deBroglie(mp, velocidade(ni, mp, largura))):.3E} m')
print(f'Comprimento  de onda de De Broglie final: {Decimal(deBroglie(mp, velocidade(nf, mp, largura))):.3E} m')
