precoDoProduto = float(input('Qual é o preço do produto? '))
descontoDoProduto = precoDoProduto * 0.05
precoDoProdutoComDesconto = precoDoProduto - descontoDoProduto
print('O produto que custava R${}, '
      'na promoção com desconto de 5% vai passar a custar R${}'.format(precoDoProduto,
                                                                       round(precoDoProdutoComDesconto, 2)))
