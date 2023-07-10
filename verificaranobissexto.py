# verificar se o ano é bissexto

ano = int(input('degite o ano'))

if ano % 4 == 0:
    if ano % 100 == 0:
        if ano % 400 == 0:
            print('o ano é bissexto')
        else:
            print('o ano nao é bissexto')
    else:
        print('o é bissexto')
else:
    print('o ano nao é bissexto')