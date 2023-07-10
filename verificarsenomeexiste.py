

# codigo que vai verificar se a cidade tem algum nome especifico

nome = input('degite o nome da sua cidade')
verificar = nome.find('santo')
if verificar == 1:
    print('existe o nome santo na sua cidade')
else:
    print('nao existe o nome santo na sua cidade')