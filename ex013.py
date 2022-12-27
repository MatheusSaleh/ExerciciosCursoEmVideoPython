salarioSemAumento = float(input('Digite o salário do funcionário:'))
aumentoDoSalario = salarioSemAumento * 0.15
salarioComAumento = salarioSemAumento + aumentoDoSalario
print('Um funcionário que ganhava R${}, com 15% de aumento passa a ganhar R${}'.format(salarioSemAumento, round(salarioComAumento, 2)))
