armazenaridade = []
menoresidade = []
maioresidade = []

for r in range(0, 7):
    idade = int(input('degite a idade dos seus 7 amigos'))
    armazenaridade.append(idade)

for i in armazenaridade:
    if i < 18:
        maioresidade.append(i)
#parte que tira menores de idade e so printa os maiores
    else:
        if i >= 18:
            menoresidade.append(i)
#parte que tira os maiores e printa os menores

print(menoresidade, 'maiores de idade')
print(maioresidade, 'menores de idade')