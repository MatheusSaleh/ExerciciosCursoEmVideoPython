distanciaMetros = float(input('A distância em metros: '))
distanciaKm = distanciaMetros/1000
distanciaHm = distanciaMetros/100
distanciaDam = distanciaMetros/10
distanciaDm = distanciaMetros * 10
distanciaCm = distanciaMetros * 100
distanciaMm = distanciaMetros *  1000
print('A medida de {}m corresponde a'.format(distanciaMetros))
print(distanciaKm, 'km')
print(distanciaHm, 'Hm')
print(distanciaDam, 'Dam')
print(distanciaDm, 'Dm')
print(distanciaCm, 'Cm')
print(distanciaMm, 'Mm')