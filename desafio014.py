tc = float(input('Digite a temperatura agora em graus celsius? °C'))
tf = (tc*1.8)+32
print('A temperatura {0}°C é igual a {1} °F!'.format(tc, tf))

kmper = float(input('Quantos kilometros você percorreu com o carro?'))
dias = int(input('Por quantos dias você alugou o carro?'))
prepag = (60 * dias) + (0.15 * kmper)
print('O valor dos {}km percorridos e pelos {} dias de aluguel será R${:.2f}'. format(kmper, dias, prepag))







