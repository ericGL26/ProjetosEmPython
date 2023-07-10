lista = {}
nome = input('Digite seu nome:')
media = float(input(f'Qual foi a media de {nome}?'))
if media >= 5:
    situacao = 'Aprovado'
    print(f'Parabens {nome}')
else:
    situacao = 'Reprovado'
    print(f'Precisa estudar mais em {nome}')
print('-' * 40)
lista["nome"] = nome
lista["media"] = media
lista["situacao"] = situacao
print(f'Media de {lista["nome"]} é {lista["media"]}')
print(f'Nome é igual á {lista["nome"]}')
print(f'Situacao é igual á {lista["situacao"]}')