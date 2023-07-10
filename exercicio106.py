import time
cor_vermelha = '\033[91m'
cor_verde = '\033[92m'
cor_amarela = '\033[93m'
cor_reset = '\033[0m'
while True:
    escolha = input(cor_amarela + 'Digite Funcao ou sistema: ')
    if escolha == 'Fim':
        break
    time.sleep(1)
    print(cor_vermelha + f'Acessando manual do {escolha}')
    time.sleep(1)
    print('-' * 30)
    help(escolha)