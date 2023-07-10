print('digite seu numero:')
listanumeros = []
seunumero = int(input(''))
listanumeros.append(seunumero)
c = 0
while seunumero != 999:
    seunumero = int(input('digite seu numero:'))
    listanumeros.append(seunumero)
    c += 1

valorbase = 0
for i in listanumeros:
   valorbase += i

print('Fora digitados {} numeros e a soma entre eles {}'.format(c, valorbase - 999))