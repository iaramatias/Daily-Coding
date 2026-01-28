#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros
m = int(input('Digite o valor do metro:'))
c = m*100
ml = m*1000
print('O valor em metro informado é {}, em centimetros é {} e em milímetros é {}'.format(m,c,ml))
