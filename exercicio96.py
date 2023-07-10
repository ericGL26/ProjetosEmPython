largura = float(input('Digite a largura do seu terreno'))
comprimento = float(input('Digite o comprimento do seu terreno'))

def area(largura, comprimento):
    calculo = largura * comprimento
    return calculo

print(f'A area de seu terreno é de {area(largura, comprimento)} metros quadrados')