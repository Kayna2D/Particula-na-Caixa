from math import *
from  decimal import Decimal
from scipy.integrate import quad
import numpy as np

h = 6.626E-34
c = 3E8
h_ev = 4.136E-15
me = 9.11E-31
mp = 1.67E-27

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

def probabilidade(a, b, n, l): 
    integrand = lambda x: 2 / l * sin((n * pi * x) / l) ** 2
    result, _ = quad(integrand, a, b)
    return result

def funcaoOndaGraf(largura, n):
    return lambda x: sqrt(2 / largura) * np.sin((n * pi * x) / largura)

def probabilidadeGraf(n, l):
    return lambda x: sqrt(2 / l) * np.sin((n * pi * x) / l) ** 2

