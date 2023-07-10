import random
adivinhamento = int(input('degite o numero que voce acha que o computador pensou'))
computador = random.randint(0, 5)
print(computador)
if adivinhamento == computador:
    print('voce venceu')
else:
    print('voce perdeu')