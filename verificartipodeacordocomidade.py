idade = int(input(('degite sua idade')))

if idade <= 9:
    print('mirim')
elif idade > 9 and idade < 18:
    print('infantil')
elif idade > 18 and idade < 20:
    print('senior')
elif idade > 19:
    print('master')