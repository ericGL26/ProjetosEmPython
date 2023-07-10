
nota1 = float(input('degite sua nota'))
nota2 = float(input('degite sua outra nota'))
media = (nota1 + nota2) / 2
if media < 5:
    print('reprovado')
elif media > 5 and media < 6.9:
    print('recuperacao')
elif media >= 7:
    print('aprovado')