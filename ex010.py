dinheiroNaCarteira = float(input('Quanto dinheiro você tem na carteira? R$'))
dinheiroNaCarteiraEmDolares = dinheiroNaCarteira / 5.28
print('Com R${} você pode comprar US${}'.format(dinheiroNaCarteira, round(dinheiroNaCarteiraEmDolares, 2)))
