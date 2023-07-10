lista = {}
escolhaprincipal = 0
mileum = False

def EditarUsuario():
    print('-'*40)
    escolhauser = str(input('Qual usuario voce deseja modificar os dados?: '))
    keys = lista.keys()
    users = list(keys)
    if not escolhauser in users:
        MostrarErroDigiteAlgoValido()
        EditarUsuario()
    escolhasec = input('Oque voce gostaria de modificar nele? ')
    while escolhasec != 'Endereco' and escolhasec != 'Numero':
        MostrarErroDigiteAlgoValido()
        escolhasec = input('Oque voce gostaria de modificar nele? ')

    if escolhasec == 'Endereco':
        modificacao = input('Digite o novo valor')
        while modificacao == '':
            MostrarErroDigiteAlgoValido()
            modificacao = input('Digite o novo valor')

    if escolhasec == 'Numero':
        modificacao = input('Digite o novo valor')
        while not modificacao.isnumeric():
            MostrarErroDigiteAlgoValido()
            modificacao = input('Digite o novo valor')

    meudic = lista
    lista[escolhauser][escolhasec] = modificacao
    with open('bancodedados.txt', 'r+') as lerb:
        for chave, valor in lista.items():
            nome = chave
            endereco = valor['Endereco']
            numero = valor['Numero']
            lerb.write(nome + ' '), lerb.write(endereco + ' '), lerb.write(numero + '\n')
def CarregarDados():
    try:
        with open('bancodedados.txt', 'r') as ler:
            listaarquivotxt = []
            for i in ler:
                listaarquivotxt.append(i)
            primeironome = [elemento.split()[0] for elemento in listaarquivotxt]
            primeiroendereco = [elemento.split()[1] for elemento in listaarquivotxt]
            primeironumero = [elemento.split()[2] for elemento in listaarquivotxt]
            # SEPARADOR
            c = 0
            for i in range(0, len(primeironome)):
                pessoatempadd = {}
                pessoatempadd["Endereco"] = primeiroendereco[c], pessoatempadd["Numero"] = primeironumero[c] ,lista[primeironome[c]] = pessoatempadd
                c += 1
    except:
        global mileum
        mileum = True

def ExcluirUsuario():
    if mileum == True:
        print("\033[31mErro, não foi encontrado uma base de dados, Tente novamente mais tarde\033[0m")
    else:
        escolhaexcluir = input('Qual pessoa deseja excluir? ')
        for i in lista:
            keys = lista.keys()
            users = list(keys)
            if not escolhaexcluir in users:
                MostrarErroDigiteAlgoValido()
                ExcluirUsuario()
            else:
                lista.pop(escolhaexcluir)
                print(f'{escolhaexcluir} foi excluido com sucesso')
                with open('bancodedados.txt', 'r+') as removerlista:
                    CarregarDados()
                    lista.pop(escolhaexcluir)
                    for chave, valor in lista.items():
                        nome = chave
                        endereco = valor['Endereco']
                        numero = valor['Numero']
                        removerlista.write(nome + ' ')
                        removerlista.write(endereco + ' ')
                        removerlista.write(numero + '\n')

def ListagemUsuarios():
    for i in lista:
        print(i, lista[i]['Endereco'], lista[i]['Numero'])

def PesquisarUsuario():
    try:
        escolhauser = input('Qual usuario voce deseja verificar os dados?: ')
        print(lista[escolhauser])
    except:
        MostrarErroDigiteAlgoValido()

def AdicionarUsuario():
    pessoatemp = {}
    numerotel = input('Digite seu numero de telefone: ').strip()
    while not numerotel.isnumeric() or numerotel == "":
        MostrarErroDigiteAlgoValido()
        numerotel = input('Digite seu numero de telefone: ').strip()

    endereco = str(input('Digite seu endereco')).strip()
    while endereco == '':
        MostrarErroDigiteAlgoValido()
        endereco = str(input('Digite seu endereco')).strip()

    nome = str(input('Digite seu nome:')).strip()
    while nome == '':
        MostrarErroDigiteAlgoValido()
        nome = str(input('Digite seu nome:')).strip()
    pessoatemp["Endereco"] = endereco
    pessoatemp["Numero"] = numerotel
    lista[nome] = pessoatemp

    with open('bancodedados.txt', 'a+') as arquivo:
        arquivo.write(nome + '  '), arquivo.write(numerotel + '  '), arquivo.write(endereco + '\n')

def ExibirMenu():
    print('-'*40)
    print('BEM VINDO!')
    print('-'*40)
    print('0- Listagem de usuarios')
    print('1- Pesquisar usuarios')
    print('2- Adicionar pessoa')
    print('3- Excluir pessoa')
    print('4- Editar pessoa')

def MostrarErroDigiteAlgoValido():
    print("\033[31mDigite algo valido!\033[0m")

opcoes = [
    ListagemUsuarios,
    PesquisarUsuario,
    AdicionarUsuario,
    ExcluirUsuario,
    EditarUsuario
]

while True:
    CarregarDados()
    ExibirMenu()

    try:
        escolhaprincipal = int(input('Oque deseja?: '))
        while escolhaprincipal > 4 or escolhaprincipal < 0:
            print("\033[31mDigite uma escolha valida!\033[0m")
            escolhaprincipal = int(input('Oque deseja?: '))
    except:
        MostrarErroDigiteAlgoValido()
        

    if len(lista) == 0:
        print('Nao há usuarios na lista cadastre algum antes')
        escolhaprincipal = 2

    opcoes[escolhaprincipal]()