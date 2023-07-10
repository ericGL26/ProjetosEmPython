armazempeso = []
maior_peso = 0
menor_peso = 0

for r in range(0, 5):
    peso = float(input('digite o peso dos seus 5 amigos'))
    armazempeso.append(peso)
    menor_peso = peso



for i in armazempeso:
    if i > maior_peso:
        maior_peso = i
    if i < menor_peso:
        menor_peso = i

print('maior peso é {}'.format(maior_peso))
print('menor peso é {}'.format(menor_peso))
#podemos ir tirando 1 de cada peso ai o que ficar com numero por mais tempo é o maior peso

#melhor codigo