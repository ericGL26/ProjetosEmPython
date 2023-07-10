nomes = ['ana', 'pedro', 'maria', 'lucas', 'sara', 'carlos', 'laura', 'tiago', 'julia', 'ricardo']
vogais = ['a', 'e', 'i', 'o', 'u']
indice = 0
for r in range(0, 10):
    armazemvogais = []
    for letra in nomes[indice]:
        if letra in vogais:
            armazemvogais.append(letra)
    print(f'As vogais da palavra {nomes[indice]} sao {armazemvogais}')
    indice += 1