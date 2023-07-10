import random
computador = random.randint(0, 11)
t = 0
suaprevisao = int(input('O numero é:'))
while suaprevisao != computador:
    print('voce errou tente novamente')
    suaprevisao = int(input('O numero é:'))
    t += 1
print('parabens, voce tentou acertar {} vezes'.format(t))