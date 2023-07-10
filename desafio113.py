lista = {}
vermelho = "\033[91m"
branco = "\033[97m"

def verificarint():
    teste = False
    while teste == False:
        try:
            numerointeiro = int(input(branco + 'Digite um numero inteiro: '))
            if type(numerointeiro) == int:
                lista["int"] = numerointeiro
                teste = True

        except:
            print(vermelho + 'ERRO, Digite um numero inteiro valido!')

def verificarfloat():
    teste = False
    while teste == False:
        numerofloat = str(input(branco + 'Digite seu numero real:'))
        if '.' in numerofloat:
            lista["flo"] = numerofloat
            teste = True
        else:
            print(vermelho + 'Digite um numero real valido!')

verificarint()
verificarfloat()
print(f'O numero real é {lista["flo"]} o inteiro é {lista["int"]}')