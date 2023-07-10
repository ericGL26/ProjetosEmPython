 #calcular IMC

peso = float(input('degite seu peso'))
altura = float(input('degite sua altura'))

calculo = peso / altura**25
if calculo < 18.5:
    print('abaixo do peso')
elif calculo > 18.5 and calculo < 25:
    print('peso ideal')
elif calculo > 30 and calculo < 40:
    print('obesidade')
elif calculo > 40:
    print('obesidade morbida')
print(calculo)
