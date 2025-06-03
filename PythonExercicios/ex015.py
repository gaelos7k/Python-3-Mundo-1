km_percorrido = float(input('Informe a quantidade de quilômetros percorridos: '))
dias_alugados = int(input('Informe a quantidade de dias que ficou em posso do carro: '))

preco = (dias_alugados * 60) + (km_percorrido * 0.15)
print('O preço a pagar pelo serviço é R${}'.format(preco))