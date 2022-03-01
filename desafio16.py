#DESAFIO 16: leia um número real inteiro e mostre sua porção inteira

num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, int(num)))
''' CORREÇÃO GUANABARA
from math import trunc
num = float(input('Digite um número real qualquer: '))
print('A porção inteira do número {} é {}'.format(num, trunc(num)))'''


#leia o comprimento do cat oposto e do cat adjacente de um triângulo retângulo, calcular e mostra a hipotenusa- EU FIZ
import math
nopo = float(input('Digite o valor do cateto oposto: '))
nadj = float(input('Digite o valor do cateto adjacente: '))
catopo = nopo**2
catadj = nadj**2
hip = catopo + catadj
hipotenusa = math.sqrt(hip)
print('O cateto oposto {} ao quadrado é igual a:{}'.format(nopo, catopo))
print('O cateto adjacente {} ao quadrado é igual a:{}'.format(nadj, catadj))
print('Com isso o comprimento da hipotenusa é igual a:{:.2f}'.format(hipotenusa))

'''CORREÇÃO GUANABARA sem importação
co = float(input('Comprimento do cateto oposto: '))
ca = flaot(input('Comprimento do cateto adjacente: '))
print('A hipotenusa vai medir {;.2f}'.foramt(hi))'''

import math # correçao com importação
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = math.hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))












