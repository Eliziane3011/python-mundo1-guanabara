numesc = int(input('Você quer o resultado de qual tabuada?'))
tab1 = 1 * numesc
tab2 = 2 * numesc
tab3 = 3 * numesc
tab4 = 4 * numesc
tab5 = 5 * numesc
tab6 = 6 * numesc
tab7 = 7 * numesc
tab8 = 8 * numesc
tab9 = 9 * numesc
tab10 = 10 * numesc
print(f'A tabuada desse número é: \n '
      f'1x{numesc} = {tab1}, 2x{numesc}={tab2}\n'
      f' 3x{numesc}={tab3}, 4x{numesc}={tab4}\n'
      f' 5x{numesc}={tab5}, 6x{numesc}={tab6}, \n '
      f' 7x{numesc}={tab7}, 8x{numesc}={tab8}, \n '
      f' 9x{numesc}={tab9}, 10x{numesc}={tab10}')

dincart = float(input('Quantos reais você tem em sua carteira?'))
conv = dincart / 3.27
print('O valor do seu dinheiro em dólares é igual a {:.2f}US$'.format(conv))

altura = float(input('Quantos metros tem a altura dessa parede?'))
largura = float(input('Quantos metros tem a largura dessa parede?'))
area = altura * largura
qtinta = area / 2
print('A quantidade de tinta em litros para pintar a parede de {}x{}m, com {}m² será preciso de {}L'.format(altura, largura, area, qtinta))

num = int(input('Digite um número: '))
print('{} x {:2} = {}'.format(num, 1, num*1))
print('{} x {:2} = {}'.format(num, 2, num*2))
print('{} x {:2} = {}'.format(num, 3, num*3))
print('{} x {:2} = {}'.format(num, 4, num*4))
print('{} x {:2} = {}'.format(num, 5, num*5))
print('{} x {:2} = {}'.format(num, 6, num*6))
print('{} x {:2} = {}'.format(num, 7, num*7))
print('{} x {:2} = {}'.format(num, 8, num*8))
print('{} x {:2} = {}'.format(num, 9, num*9))
print('{} x {} = {}'.format(num, 10, num*10))
print('-'*12)

