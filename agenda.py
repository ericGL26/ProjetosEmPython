lista = {}
escolhaprincipal = 0
mileum = False
import json


def EditarUsuario():
    if len(lista) == 0:
        print("\033[31mERRO, Lista vazia cadastre um usuario antes de comecar\033[0m")
    else:
        l()
        escolhauser = str(input('Qual usuario voce deseja modificar os dados?: '))
        keys = lista.keys()
        users = list(keys)
        if not escolhauser in users:
            print("\033[31mERRO, Digite um usuario valido\033[0m")
            EditarUsuario()

        escolhasec = input('Oque voce gostaria de modificar nele? ')
        while escolhasec != 'Endereco' and escolhasec != 'Numero':
            print("\033[31mERRO, Digite uma propriedade valida!\033[0m")
            escolhasec = input('Oque voce gostaria de modificar nele? ')

        if escolhasec == 'Endereco':
            modificacao = input('Digite o novo valor')
            while modificacao == '':
                print("\033[31mERRO, Digite um valor valido\033[0m")
                modificacao = input('Digite o novo valor')

        if escolhasec == 'Numero':
            modificacao = input('Digite o novo valor')
            while not modificacao.isnumeric():
                print("\033[31mERRO, Digite um valor valido\033[0m")
                modificacao = input('Digite o novo valor')

        meudic = lista
        lista[escolhauser][escolhasec] = modificacao
        with open('bancodedados.txt', 'r+') as lerb:
            lerb.truncate()
            for chave, valor in lista.items():
                nome = chave
                endereco = valor['Endereco']
                numero = valor['Numero']
                lerb.write(nome + ' ')
                lerb.write(endereco + ' ')
                lerb.write(numero + '\n')

def escolhaseis():
    try:
        with open('bancodedados.txt', 'r') as ler:
            listaarquivotxt = []
            for i in ler:
                listaarquivotxt.append(i)
            # PARTE DE FILTRAR PARA ADICIONAR NA LISTA
            # PRIMEIROS NOMES NUMERO E ENDERECO
            primeironome = [elemento.split()[0] for elemento in listaarquivotxt]
            primeiroendereco = [elemento.split()[1] for elemento in listaarquivotxt]
            primeironumero = [elemento.split()[2] for elemento in listaarquivotxt]
            # SEPARADOR
            c = 0
            for i in range(0, len(primeironome)):
                pessoatempadd = {}
                pessoatempadd["Endereco"] = primeiroendereco[c]
                pessoatempadd["Numero"] = primeironumero[c]
                lista[primeironome[c]] = pessoatempadd
                c += 1
    except:
        global mileum
        mileum = True


def escolhaquatro():
    if len(lista) == 0:
        print("\033[31mErro 210, lista vazia\033[0m")
    else:
        if mileum == True:
            print("\033[31mErro 1001, Não foi encontrado uma base de dados tente novamente mais tarde\033[0m")
        else:
            # PARTE DA LISTA
            escolhaexcluir = input('Qual pessoa deseja excluir? ')
            for i in lista:
                keys = lista.keys()
                users = list(keys)
                if not escolhaexcluir in users:
                    print("\033[31mErro 401, Usuario nao identificado\033[0m")
                    escolhaquatro()
                else:
                    lista.pop(escolhaexcluir)
                    print(f'{escolhaexcluir} foi excluido com sucesso')
                    # PARTE DO ARQUIVO TXT
                    with open('bancodedados.txt', 'r+') as removerlista:
                        escolhaseis()
                        removerlista.truncate()
                        lista.pop(escolhaexcluir)
                        for chave, valor in lista.items():
                            nome = chave
                            endereco = valor['Endereco']
                            numero = valor['Numero']
                            removerlista.write(nome + ' ')
                            removerlista.write(endereco + ' ')
                            removerlista.write(numero + '\n')
                break


def l():
    print('-'*40)

while True:
    escolhaseis()
    l()
    print('BEM VINDO!')
    l()
    # escolhas
    print('1- Listagem de usuarios')
    print('2- Pesquisar usuarios')
    print('3- Adicionar pessoa')
    print('4- Excluir pessoa')
    print('5- Editar pessoa')
    try:
        escolhaprincipal = int(input('Oque deseja?: '))
        while escolhaprincipal > 5 or escolhaprincipal < 1:
            print("\033[31mDigite uma escolha valida!\033[0m")
            escolhaprincipal = int(input('Oque deseja?: '))
    except:
        print("\033[31mDigite uma escolha valida!\033[0m")
    if escolhaprincipal == 1:
        if len(lista) == 0:
            print("\033[31mERRO, Lista vazia\033[0m")
        else:
            for i in lista:
                print(i, lista[i]['Endereco'], lista[i]['Numero'])

    if escolhaprincipal == 2:
        if len(lista) == 0:
            print("\033[31mERRO, Lista vazia\033[0m")
        else:
            try:
                escolhauser = input('Qual usuario voce deseja verificar os dados?: ')
                print(lista[escolhauser])
            except:
                print("\033[31mERRO, Usuario nao encontrado\033[0m")

    if escolhaprincipal == 3:
        pessoatemp = {}
        numerotel = input('Digite seu numero de telefone: ').strip()
        while not numerotel.isnumeric() or numerotel == "":
            print("\033[31mERRO, Digite um numero valido\033[0m")
            numerotel = input('Digite seu numero de telefone: ').strip()

        endereco = str(input('Digite seu endereco')).strip()
        while endereco == '':
            print("\033[31mERRO, Digite um endereco valido\033[0m")
            endereco = str(input('Digite seu endereco')).strip()

        nome = str(input('Digite seu nome:')).strip()
        while nome == '':
            print("\033[31mERRO, Digite um nome valido\033[0m")
            nome = str(input('Digite seu nome:')).strip()

        pessoatemp["Endereco"] = endereco
        pessoatemp["Numero"] = numerotel
        lista[nome] = pessoatemp

        with open('bancodedados.txt', 'a+') as arquivo:
            arquivo.write(nome + '  ')
            arquivo.write(numerotel + '  ')
            arquivo.write(endereco + '\n')


    if escolhaprincipal == 4:
        escolhaquatro()

    if escolhaprincipal == 5:
        EditarUsuario()

    # PARTE DE LER O ARQUIVO TXT
    if escolhaprincipal == 6:
        escolhaseis()