#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
r = float(input('Quanto dinheiro você tem na carteira?R$'))
d = r / 5.22
print('Com R${:.2f} você Pode comprar US${:.2f}'.format(r, d))
