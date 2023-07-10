import random
listanumero = []
l = 0
while l < 5:
    l += 1
    numeroale = random.randint(0, 5)
    listanumero.append(numeroale)
tupla = (listanumero)

m = tupla[0]
for i in tupla:
    if i < m:
        m = i
print(f'O menor numero é {m}')
n = tupla[0]
for r in tupla:
    if r > n:
        n = r
print(f'O maior numero é {n}')
print(tupla)