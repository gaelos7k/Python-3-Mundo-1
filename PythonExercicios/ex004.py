from curses.ascii import isspace

conteudo = input('Digite algo: ')

print('O tipo primitivo desse valor é {}'.format(type(conteudo)))
print('Só tem espaços? {}'.format(conteudo.isspace()))
print('É um número? {}'.format(conteudo.isnumeric()))
print('É alfabético? {}'.format(conteudo.isalpha()))
print('É alfanumérico? {}'.format(conteudo.isalnum()))
print('Está em maiúsculo? {}'.format(conteudo.isupper()))
print('Está em minúsculo? {}'.format(conteudo.islower()))
print('Está capitalizado? {}'.format(conteudo.istitle()))