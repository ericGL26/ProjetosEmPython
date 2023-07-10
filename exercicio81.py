sualista = []
escolha = input('Quer continuar? [s / n]')
while escolha == 's':
    if escolha == 's':
        escolhanum = int(input('Digite seu numero:'))
        sualista.append(escolhanum)
        escolha = input('Quer continuar? [s / n]')
    else:
        break
print('=-'*50)
if 5 in sualista:
    print('O valor 5 está presente na sua lista')
else:
    print('O valor 5 não está presente na sua lista')
print(f'Voce digitou {len(sualista)} elementos!')
sualista.sort(reverse=True)
print(f'Os valores em ordem decrescente são {sualista}')