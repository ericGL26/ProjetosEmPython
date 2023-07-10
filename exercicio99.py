import time
listanum = []
totrodar = int(input('Quantos numeros quer colocar?'))
for r in range(0, totrodar):
    seunum = int(input('Digite seu numero:'))
    listanum.append(seunum)

def maior():
    maiornum = 0
    for i in listanum:
        if i > maiornum:
            maiornum = i
    return maiornum


print('-' * 30)
print(f'O maior numero foi {maior()}')
primeiravez = True
for p in listanum:
    if primeiravez == True:
        print('Foram digitados')
    primeiravez = False
    print(p, end=' ')
    time.sleep(1)

print(f',Ao todo foram digitados {len(listanum)} numeros')