armazemnumero = []
rodadas = 0
seunumero = int(input('digite seu numero'))
armazemnumero.append(seunumero)
rodadas += 1
while seunumero != 999:
    seunumero = int(input('digite seu numero'))
    if seunumero != 999:
       armazemnumero.append(seunumero)
       rodadas += 1
t = 0
for i in armazemnumero:
    t += i
print(f'Foram digitados {rodadas} numeros e a soma de todos eles resulta em {t}')