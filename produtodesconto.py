
produto = input('degite o nome do produto')
precosemdesconto = int(input('degite o valor do produto'))
porcentagem = 5
desconto = (porcentagem / 100) * precosemdesconto
precofinal = precosemdesconto - desconto
print('o preço do {} com desconto é {}'.format(produto, precofinal))