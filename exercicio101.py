nacimento = int(input('Digite seu ano de nacimento:'))
idade = 2023 - nacimento
def voto():
    if idade > 17:
        print(f'Com {idade} o voto é Obrigatorio')
    else:
        if idade < 18:
            print(f'Com {idade} não vota')
        else:
            if idade > 64:
                print(f'Com {idade} o  voto é opcional')
voto()