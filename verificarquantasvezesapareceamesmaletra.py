#verificar quantas vezes a letra A aparece qual a posicao que ela aparece pela primeira vez e qual posicao ela aparece po ultimo

minhafrase = input('degite uma frase')
contarletra = minhafrase.count('a')

if contarletra > 0:
    encontrarposicao = minhafrase.find('a')
    ultimaposicao = minhafrase.rfind('a')
    print('a letra A parece {} vezes, a posicao que ela parerece da primeira vez é {} e a ultima posicao é {}'.format(contarletra, encontrarposicao, ultimaposicao))
else:
    encontrarposicao = 'nao tem a letra A na sua frase'
    print(encontrarposicao)