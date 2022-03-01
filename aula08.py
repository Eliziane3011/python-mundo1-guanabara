import math #importa tudo
num = int(input('Digite um número: '))
raiz = math.sqrt(num) #sqrt=raiz
print('A raiz de {} é igual a {}'.format(num, math.ceil(raiz))) #math.ceil arredonda para cima, math.floor arredonda pra baixo

from math import sqrt, floor #importa só as funcionalidades sqrt e floor
num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz de {} é iual a {}'.format(num, floor(raiz)))






