suaexpressao = input('Digite sua expressao:')
quantidaderigth = 0
quantidadeleft = 0
for i in suaexpressao:
    if i == '(':
        quantidaderigth += 1
    else:
        if i == ')':
            quantidadeleft += 1

if quantidaderigth == quantidadeleft:
    print('Sua expressao está corrreta!')
else:
    print('Sua expressao está incorreta!')