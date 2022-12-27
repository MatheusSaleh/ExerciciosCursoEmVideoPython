larguraDaParede = float(input('Largura da parede: '))
alturaDaParede = float(input('Altura da parede: '))
areaDaParede = alturaDaParede * larguraDaParede
quantidadeDeTinta = areaDaParede / 2
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².'.format(larguraDaParede, alturaDaParede, areaDaParede))
print('Para pintar essa parede, você precisará de {}l de tinta.'.format(quantidadeDeTinta))
