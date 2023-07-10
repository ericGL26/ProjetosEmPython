idade = int(input('degite sua idade'))

if idade < 18:
    print('voce ainda vai se alistar')
elif idade >= 18 and idade < 40:
    print('já está na hora de se alistar')
elif idade > 40:
    print('já passou da hora')

if idade < 18:
    idadeav = idade - 18
    print('falta {} anos para voce se alistar'.format(idadeav))
elif idade > 18:
    idadeav = idade - 18
    print('voce está atrasado {} anos'.format(idadeav))