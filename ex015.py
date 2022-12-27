diasAlugados = int(input('Quantos dias alugados? '))
quilometrosRodados = int(input('Quantos Km rodados? '))
totalaPagar = (diasAlugados * 60) + (0.15 * quilometrosRodados)
print('O total a pagar é de R${}'.format(totalaPagar))
