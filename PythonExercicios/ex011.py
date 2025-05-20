largura = float(input('Informa a largura da parede: '))
altura = float(input('Informe a altura da parede: '))

area = altura * largura

tinta = area / 2

print('A área da parede é {}'.format(area))
print('É preciso {} litros de tinta para pinta-la'.format(tinta))