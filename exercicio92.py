lista = {}
salario = 0
nome = input('Digite seu nome:')
nacimento = int(input('Digite o ano de nacimento:'))
carteira = int(input('Digite a carteira de trabalho: (0 não tem)'))
idade = 2023 - nacimento
idade = 2023 - nacimento
aposentadoria = 65 - idade
lista["nome"] = nome
lista["nacimento"] = nacimento
lista["carteira"] = carteira

if carteira == 0:
    print(f'Nome tem valor de {nome}')
    print(f'Idade tem valor de {idade}')
    print(f'ctps tem valor de {carteira}')
else:
    contratacao = int(input('Ano de contratação:'))
    salario = float(input('Digite seu salario'))
    lista["contratacao"] = contratacao
    lista["salario"] = salario
    print(f'Nome tem valor de {nome}')
    print(f'Idade tem valor de {idade}')
    print(f'ctps tem valor de {carteira}')
    print(f'Salario tem valor de {salario}')
    print(f'Aposentadoria tem valor de {aposentadoria}')