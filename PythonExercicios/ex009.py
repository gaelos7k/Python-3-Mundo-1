numero = int(input('Informe um número para ver sua tabuada: '))

for i in range(11):
    print('{} x {} = {}'.format(numero, i, numero * i))
