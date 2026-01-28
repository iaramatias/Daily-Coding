#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta pinta uma área de 2 metros quadrados
larg = float(input('Digite a largura da parede: '))
a = float(input('Digite a altura da parede: '))
area = larg * a
p = area / 2
print('Sua parede tem a dimensão de {:.2f} por {:.2f} e sua área é de {:.2f}m².\nPara pintar essa parede,você precisará '
      'de {:.2f} litros de tinta'.format(larg, a, area, p))





