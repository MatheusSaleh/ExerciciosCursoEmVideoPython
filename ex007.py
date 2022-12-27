primeiraNota = float(input('Primeira nota do aluno: '))
segundaNota = float(input('Segunda nota do aluno: '))
media = (primeiraNota + segundaNota)/2
print('A média entre {} e {} é igual a {}'.format(primeiraNota, segundaNota, round(media, 1)))
