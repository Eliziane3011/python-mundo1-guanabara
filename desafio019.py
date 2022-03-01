#DESAFIO 19: professor quer sortear um dos seus 4 alunos para apagar o quadro, fazer um programa que ajude lendo o nome deles e escrevendo o escolhido
import random #EU FIZ
alunos = ['Kaio', 'Eliziane', 'Bethoven', 'Védio']
print('Sorteio do aluno para apagar o quadro negro')
print('O sorteado foi: ' + alunos[random.randrange(len(alunos))]) #len do 0, 1, 2 e 3
print('O sorteado foi: ' + alunos[random.randint(0, 3)]) #random.randint(inicio, final)

'''CORREÇÃO GUANABARA 
from random import choice #from especifica o uso de somente uma funcionalidade
1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4] #lista sempre entre colchetes
escolhido = random.choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))'''


#DESAFIO 20: sortear a ordem de apresentação para trabalhos EU FIZ
from random import shuffle
aluno1 = str(input('Digite o primeiro nome: '))
aluno2 = str(input('Digite o segundo nome: '))
aluno3 = str(input('Digite o terceiro nome: '))
aluno4 = str(input('Digite o quarto nome: '))
lista = [aluno1, aluno2, aluno3, aluno4]
print('A ordem de apresentação do trabalho será: ')
shuffle(lista) #shuffle significa embaralhar, quanto coloca o from não precisa colocar random.shuffle
print(lista)









