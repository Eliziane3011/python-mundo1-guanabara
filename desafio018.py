#DESAFIO 18: leia um ângulo qualquer e mostra na tela o valor do seno, cosseno e tangente desse ângulo
import math # EU FIZ
x = float(input('Digite um ângulo qualquer: '))
seno = math.sin(math.radians(x)) #retorna em grau, para converter em radianos: math.radians
print('O ângulo {} tem o seno de {:.2f}'.format(x, seno))
cosseno = math.cos(math.radians(x))
print('O ângulo {} tem o cosseno de {:.2f}'.format(x, cosseno))
tangente = math.tan(math.radians(x))
print('O ângulo {}, a tangente de {:.2f}.'.format(x, tangente))

